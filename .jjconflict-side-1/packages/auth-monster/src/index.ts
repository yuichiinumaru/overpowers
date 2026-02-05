import {
  AuthProvider,
  AuthMonsterConfig,
  ManagedAccount,
  AuthDetails,
  PluginContext
} from './core/types';
import { StorageManager } from './core/storage';
import { AccountRotator, RateLimitReason } from './core/rotation';
import { UnifiedModelHub } from './core/hub';
import { sanitizeCrossModelRequest } from './utils/sanitizer';
import { proxyFetch } from './core/proxy';
import { CostEstimator } from './core/cost-estimator';
import { HistoryManager } from './core/history';
import { enforceReasoning } from './core/reasoning';

// Import Providers
import { GeminiProvider } from './providers/gemini';
import { AnthropicProvider, transformRequest as anthropicTransformRequest, transformResponseText as anthropicTransformResponse } from './providers/anthropic';
import { cursorProvider } from './providers/cursor';
import { WindsurfProvider, streamChat } from './providers/windsurf';
import { QwenProvider } from './providers/qwen';
import { IFlowProvider } from './providers/iflow';
import { KiroProvider } from './providers/kiro';
import { ZhipuProvider } from './providers/zhipu';
import { MinimaxProvider } from './providers/minimax';
import { AzureProvider } from './providers/azure';
import { GrokProvider } from './providers/grok';
import { DeepSeekProvider } from './providers/deepseek';
import { GenericProvider } from './providers/generic';

export { RateLimitReason };

export class AuthMonster {
  private storage: StorageManager;
  private accounts: ManagedAccount[] = [];
  private config: AuthMonsterConfig;
  private rotator: AccountRotator;
  private hub: UnifiedModelHub;
  private history: HistoryManager;
  private lastUsedAccountId: string | null = null;
  private lastWarmupTime: Map<string, number> = new Map();

  constructor(context: PluginContext) {
    this.config = context.config;
    this.storage = new StorageManager(context.storagePath);
    this.rotator = new AccountRotator();
    this.hub = new UnifiedModelHub();
    this.history = new HistoryManager(context.storagePath);
  }

  async init() {
    this.accounts = await this.storage.loadAccounts();
  }

  async getAuthDetails(modelOrProvider?: string | AuthProvider): Promise<AuthDetails | null> {
    // 1. Try routing via Unified Model Hub if it looks like a model name
    if (modelOrProvider && typeof modelOrProvider === 'string' &&
      !Object.values(AuthProvider).includes(modelOrProvider as AuthProvider)) {

      const modelChain = this.hub.resolveModelChain(modelOrProvider, this.config);

      for (const modelName of modelChain) {
        const hubChoice = this.hub.selectModelAccount(modelName, this.accounts);
        if (hubChoice) {
          const details = await this.selectAccount(hubChoice.provider, [hubChoice.account], hubChoice.modelInProvider);
          if (details) return details;
        }
      }
    }

    // 2. Default provider-based selection
    const targetProvider = (modelOrProvider as AuthProvider) || this.config.active;
    const providerAccounts = this.accounts.filter(a => a.provider === targetProvider);

    if (providerAccounts.length === 0) {
      // Try fallback
      for (const fallbackProvider of this.config.fallback) {
        const fallbackAccounts = this.accounts.filter(a => a.provider === fallbackProvider);
        if (fallbackAccounts.length > 0) {
          return await this.selectAccount(fallbackProvider, fallbackAccounts);
        }
      }
      return null;
    }

    return await this.selectAccount(targetProvider, providerAccounts);
  }

  private async selectAccount(provider: AuthProvider, accounts: ManagedAccount[], modelInProvider?: string): Promise<AuthDetails | null> {
    const account = this.rotator.selectAccount(accounts, this.config.method);

    if (!account) {
      return null;
    }

    // Thinking Warmup: Triggered when switching to a new account
    if (this.lastUsedAccountId !== account.id) {
      this.runThinkingWarmup(account.id).catch(err =>
        console.error(`[AuthMonster] Warmup background task failed for ${account.email}:`, err)
      );
      this.lastUsedAccountId = account.id;
    }

    const headers = await this.getHeadersForAccount(provider, account);

    return {
      provider,
      account,
      headers,
      modelInProvider
    };
  }

  /**
   * Performs a request with transparent model fallback and retries.
   * If a model in the chain fails with a quota error, it automatically 
   * reports the error and moves to the next model in the chain.
   */
  async request(model: string, url: string, options: any): Promise<Response> {
    const modelChain = this.hub.resolveModelChain(model, this.config);
    let lastError: any = new Error(`No available accounts for model chain: ${modelChain.join(', ')}`);

    for (const currentModel of modelChain) {
      let auth = await this.getAuthDetails(currentModel);

      // --- Rate Limit Parking (Phase 3) ---
      if (!auth) {
        // If no usable accounts found, check if any are just rate-limited and wait
        const accountsWithReset = this.accounts.filter(a => a.rateLimitResetTime && a.rateLimitResetTime > Date.now());
        if (accountsWithReset.length > 0) {
          const earliestReset = Math.min(...accountsWithReset.map(a => a.rateLimitResetTime!));
          const waitTime = earliestReset - Date.now();

          // Only park if the wait is reasonable (< 60s)
          if (waitTime > 0 && waitTime < 60000) {
            console.log(`[AuthMonster] All accounts busy. Parking request for ${Math.ceil(waitTime / 1000)}s...`);
            await new Promise(resolve => setTimeout(resolve, waitTime + 100)); // Wait + buffer
            auth = await this.getAuthDetails(currentModel);
          }
        }
      }

      if (!auth) continue;

      const startTime = Date.now();
      let requestBody = options.body;

      try {
        const headers = { ...options.headers, ...auth.headers };

        // Transform body if it's an object (AI request)
        if (requestBody && typeof requestBody === 'object' && !(requestBody instanceof FormData) && !(requestBody instanceof Blob)) {
          requestBody = JSON.stringify(this.transformRequest(auth.provider, requestBody, auth.modelInProvider));
        }

        const targetUrl = this.getRequestUrl(auth.provider, auth.modelInProvider || model, auth.account) || url;

        let response: Response;

        if (auth.provider === AuthProvider.Windsurf) {
          response = await this.handleWindsurfRequest(auth, options);
        } else {
          response = await proxyFetch(targetUrl, {
            ...options,
            headers,
            body: requestBody
          });
        }

        // --- Stats & History Collection (Phase 3) ---
        const collectStats = async () => {
          // console.log("[AuthMonster] Collecting stats...");
          const durationMs = Date.now() - startTime;
          const responseClone = response.clone();
          let responseBody: any;
          let inputTokens = 0;
          let outputTokens = 0;

          try {
            const text = await responseClone.text();
            try { responseBody = JSON.parse(text); } catch { responseBody = text; }
          } catch { }

          // Extract tokens
          if (responseBody && typeof responseBody === 'object' && responseBody.usage) {
            inputTokens = responseBody.usage.prompt_tokens || responseBody.usage.input_tokens || 0;
            outputTokens = responseBody.usage.completion_tokens || responseBody.usage.output_tokens || 0;
          }

          // Estimate tokens if missing
          if (inputTokens === 0 && typeof requestBody === 'string') inputTokens = CostEstimator.estimateTokens(requestBody);
          if (outputTokens === 0) {
            if (typeof responseBody === 'string') outputTokens = CostEstimator.estimateTokens(responseBody);
            else if (responseBody?.choices?.[0]?.message?.content) outputTokens = CostEstimator.estimateTokens(responseBody.choices[0].message.content);
          }

          const cost = CostEstimator.calculateCost(auth!.modelInProvider || currentModel, inputTokens, outputTokens);

          // Update Usage
          if (!auth!.account.usage) auth!.account.usage = { totalInputTokens: 0, totalOutputTokens: 0, totalCost: 0 };
          auth!.account.usage.totalInputTokens += inputTokens;
          auth!.account.usage.totalOutputTokens += outputTokens;
          auth!.account.usage.totalCost += cost;

          // Log to History
          let parsedRequest = requestBody;
          if (typeof requestBody === 'string') {
            try { parsedRequest = JSON.parse(requestBody); } catch { }
          }

          await this.history.addEntry({
            model: currentModel,
            provider: auth!.provider,
            accountId: auth!.account.id,
            tokens: { input: inputTokens, output: outputTokens },
            cost,
            request: parsedRequest,
            response: responseBody,
            durationMs,
            success: response.ok,
            error: !response.ok ? `Status ${response.status}` : undefined
          });
        };

        // Don't await stats collection to avoid blocking the response return (fire and forget)
        collectStats().catch(err => console.error('[AuthMonster] Stats collection failed:', err));

        if (response.status === 429 || response.status === 403) {
          const text = await response.clone().text().catch(() => '');
          if (text.toLowerCase().includes('quota') || text.toLowerCase().includes('rate limit')) {
            console.warn(`[AuthMonster] Quota exceeded for ${auth.account.email} (${auth.provider}). Falling back...`);
            await this.reportRateLimit(auth.account.id, 60000, 'QUOTA_EXHAUSTED');
            continue; // Try next in chain
          }
        }

        if (!response.ok) {
          const errorText = await response.clone().text().catch(() => 'Unknown error');
          console.warn(`[AuthMonster] Request failed for ${auth.account.email} (${auth.provider}): ${response.status} ${errorText}`);
          await this.reportFailure(auth.account.id);
          if (response.status >= 500) continue;
        } else {
          await this.reportSuccess(auth.account.id);
        }

        return response;
      } catch (error) {
        console.error(`[AuthMonster] Error during request with ${auth.account.email}:`, error);

        // Log failure to history
        this.history.addEntry({
          model: currentModel,
          provider: auth.provider,
          accountId: auth.account.id,
          request: requestBody,
          response: null,
          durationMs: Date.now() - startTime,
          success: false,
          error: String(error)
        }).catch(() => { });

        await this.reportFailure(auth.account.id);
        lastError = error;
        continue; // Try next in chain
      }
    }

    throw lastError;
  }

  /**
   * Sends a lightweight request to 'wake up' reasoning models
   */
  async runThinkingWarmup(accountId: string) {
    const account = this.accounts.find(a => a.id === accountId);
    if (!account) return;

    // Only warmup reasoning models (Anthropic Claude 4.5 Opus / Thinking)
    if (account.provider !== AuthProvider.Anthropic) return;

    // Throttle warmups to once every 5 minutes per account
    const lastWarmup = this.lastWarmupTime.get(accountId) ?? 0;
    if (Date.now() - lastWarmup < 5 * 60 * 1000) return;

    const isReasoningModel = account.metadata?.model?.includes('opus') ||
      account.metadata?.model?.includes('thinking') ||
      !account.metadata?.model; // Assume reasoning if model unknown for Anthropic

    if (!isReasoningModel) return;

    try {
      const headers = await this.getHeadersForAccount(account.provider, account);
      const url = account.apiKey
        ? "https://api.anthropic.com/v1/messages"
        : "https://console.anthropic.com/api/v1/messages";

      const body: any = {
        model: account.metadata?.model || "claude-4.5-opus-thinking",
        max_tokens: 1,
        messages: [{ role: "user", content: "Hello" }]
      };

      // Enable thinking if supported
      if (body.model.includes('thinking') || body.model.includes('opus')) {
        body.thinking = { type: "enabled", budget_tokens: 1024 };
      }

      await proxyFetch(url, {
        method: "POST",
        headers,
        body: JSON.stringify(body),
        signal: AbortSignal.timeout(5000) // Don't hang on warmup
      });

      this.lastWarmupTime.set(accountId, Date.now());
    } catch (error) {
      // Warmup failures are non-critical, but log them
      console.warn(`[AuthMonster] Thinking warmup failed for ${account.email}:`, error);
    }
  }

  /**
   * Generates headers using provider-specific logic
   */
  private async getHeadersForAccount(provider: AuthProvider, account: ManagedAccount): Promise<Record<string, string>> {
    switch (provider) {
      case AuthProvider.Gemini:
        return GeminiProvider.getHeaders(account);
      case AuthProvider.Anthropic:
        return AnthropicProvider.getHeaders(account);
      case AuthProvider.Cursor:
        return cursorProvider.getHeaders(account);
      case AuthProvider.Windsurf:
        return WindsurfProvider.getHeaders(account);
      case AuthProvider.Qwen:
        return QwenProvider.getHeaders(account);
      case AuthProvider.IFlow:
        return IFlowProvider.getHeaders(account);
      case AuthProvider.Kiro:
        return KiroProvider.getHeaders(account);
      case AuthProvider.Zhipu:
        return ZhipuProvider.getHeaders(account);
      case AuthProvider.Minimax:
        return MinimaxProvider.getHeaders(account);
      case AuthProvider.Azure:
        return AzureProvider.getHeaders(account);
      case AuthProvider.Grok:
        return GrokProvider.getHeaders(account);
      case AuthProvider.DeepSeek:
        return DeepSeekProvider.getHeaders(account);
      case AuthProvider.Generic:
        return await GenericProvider.getHeaders(account);
      default:
        // Default header generation fallback
        const headers: Record<string, string> = {};
        if (account.apiKey) {
          headers['Authorization'] = `Bearer ${account.apiKey}`;
        } else if (account.tokens.accessToken) {
          headers['Authorization'] = `Bearer ${account.tokens.accessToken}`;
        }
        return headers;
    }
  }

  /**
   * Provider-specific request transformations
   */
  transformRequest(provider: AuthProvider, body: any, modelInProvider?: string): any {
    // 1. Cross-model signature sanitization (Gemini <-> Claude conflicts)
    let sanitizedBody = sanitizeCrossModelRequest(body);

    // 1.5. Reasoning Enforcer
    if (this.config.thinking?.enabled) {
      sanitizedBody = enforceReasoning(sanitizedBody, modelInProvider);
    }

    // 2. Inject hub-selected model if present
    if (modelInProvider) {
      sanitizedBody.model = modelInProvider;
    }

    // 3. Provider-specific transformations
    switch (provider) {
      case AuthProvider.Anthropic:
        return anthropicTransformRequest(sanitizedBody);
      case AuthProvider.Gemini:
        return GeminiProvider.transformRequest(sanitizedBody);
      default:
        return sanitizedBody;
    }
  }

  /**
   * Provider-specific response transformations
   */
  transformResponse(provider: AuthProvider, text: string): string {
    switch (provider) {
      case AuthProvider.Anthropic:
        return anthropicTransformResponse(text);
      default:
        return text;
    }
  }

  private getRequestUrl(provider: AuthProvider, model: string, account: ManagedAccount): string | null {
    if (provider === AuthProvider.Generic ||
      (this.config.providers && this.config.providers[provider]?.options?.baseUrl)) {
      const baseUrl = this.config.providers[provider]?.options?.baseUrl;
      if (baseUrl) {
        return `${baseUrl.replace(/\/$/, '')}/chat/completions`;
      }
    }

    switch (provider) {
      case AuthProvider.Gemini: return GeminiProvider.getUrl(model, account);
      case AuthProvider.Anthropic: return AnthropicProvider.getUrl(model, account);
      case AuthProvider.Cursor: return cursorProvider.getUrl(model, account);
      case AuthProvider.Windsurf: return WindsurfProvider.getUrl(model, account);
      case AuthProvider.Qwen: return QwenProvider.getUrl(model, account);
      case AuthProvider.Azure: return AzureProvider.getUrl(model, account);
      case AuthProvider.Grok: return GrokProvider.getUrl(model, account);
      case AuthProvider.DeepSeek: return DeepSeekProvider.getUrl(model, account);
      case AuthProvider.Generic: return GenericProvider.getUrl(model, account);
      default: return null;
    }
  }

  private async handleWindsurfRequest(auth: AuthDetails, options: any): Promise<Response> {
    let messages: any[] = [];
    let model = auth.modelInProvider || 'default';
    try {
      const bodyObj = typeof options.body === 'string' ? JSON.parse(options.body) : options.body;
      if (bodyObj) {
        messages = bodyObj.messages || [];
        if (bodyObj.model) model = bodyObj.model;
      }
    } catch (e) { }

    const credentials = {
      apiKey: auth.account.apiKey || auth.account.tokens.accessToken,
      port: auth.account.metadata?.port,
      csrfToken: auth.account.metadata?.csrfToken,
      version: auth.account.metadata?.version
    };

    if (!credentials.apiKey || !credentials.port || !credentials.csrfToken) {
      throw new Error("Missing Windsurf credentials (port, csrfToken, or apiKey)");
    }

    const text = await streamChat(credentials as any, { model, messages });

    return new Response(JSON.stringify({
      id: 'chatcmpl-' + Date.now(),
      object: 'chat.completion',
      created: Math.floor(Date.now() / 1000),
      model: model,
      choices: [{
        index: 0,
        message: { role: 'assistant', content: text },
        finish_reason: 'stop'
      }],
      usage: { prompt_tokens: 0, completion_tokens: 0, total_tokens: 0 }
    }), { status: 200, headers: { 'Content-Type': 'application/json' } });
  }

  /**
   * Returns all managed accounts (including tokens)
   */
  getAccounts(): ManagedAccount[] {
    return this.accounts;
  }

  /**
   * Returns health info for all accounts
   */
  getAllAccountsStatus() {
    return this.accounts.map(acc => ({
      id: acc.id,
      email: acc.email,
      provider: acc.provider,
      isHealthy: acc.isHealthy,
      healthScore: acc.healthScore ?? 70, // Default initial score if not set
      consecutiveFailures: acc.consecutiveFailures ?? 0,
      lastUsed: acc.lastUsed,
      cooldownUntil: acc.cooldownUntil,
      rateLimitResetTime: acc.rateLimitResetTime,
      lastSwitchReason: acc.lastSwitchReason
    }));
  }

  async addAccount(account: ManagedAccount) {
    await this.storage.addAccount(account);
    await this.init(); // Refresh local cache
  }

  async deleteAccount(id: string) {
    await this.storage.deleteAccount(id);
    await this.init(); // Refresh local cache
  }

  async reportSuccess(accountId: string) {
    const account = this.accounts.find(a => a.id === accountId);
    if (account) {
      this.rotator.recordSuccess(account);
      await this.storage.saveAccounts(this.accounts);
    }
  }

  async reportFailure(accountId: string) {
    const account = this.accounts.find(a => a.id === accountId);
    if (account) {
      this.rotator.recordFailure(account);
      await this.storage.saveAccounts(this.accounts);
    }
  }

  async reportRateLimit(accountId: string, retryAfterMs?: number, reason: RateLimitReason = 'UNKNOWN') {
    const account = this.accounts.find(a => a.id === accountId);
    if (account) {
      this.rotator.recordRateLimit(account, retryAfterMs, reason);
      await this.storage.saveAccounts(this.accounts);
    }
  }
}

// Example usage/factory
export function createAuthMonster(context: PluginContext) {
  return new AuthMonster(context);
}
