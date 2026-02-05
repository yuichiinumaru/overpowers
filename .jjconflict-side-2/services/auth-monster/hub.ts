import { AuthProvider, ManagedAccount, AuthMonsterConfig } from './types';
import { AccountRotator } from './rotation';
import { validateThinking, ThinkingValidationResult } from './thinking-validator';
import { isOnCooldown } from './quota-manager';

/**
 * Entry in the Model Hub mapping a generic model name 
 * to a specific provider's model identifier.
 */
export interface ModelHubEntry {
  provider: AuthProvider;
  modelInProvider: string;
}

/**
 * UnifiedModelHub manages the mapping between generic model names 
 * and the pool of providers/accounts that can serve them.
 * 
 * It implements global load balancing across different providers
 * based on health, quota, and PID-based offsets.
 */
export class UnifiedModelHub {
  private modelMap: Map<string, ModelHubEntry[]> = new Map();

  constructor() {
    this.initializeDefaultMappings();
  }

  /**
   * Set up default mappings for common models.
   * In a real-world scenario, this could be loaded from a config file.
   */
  private initializeDefaultMappings() {
    // Gemini 3 Flash & Pro
    this.addMapping('gemini-3-flash-preview', [
      { provider: AuthProvider.Gemini, modelInProvider: 'gemini-3-flash' },
      { provider: AuthProvider.Windsurf, modelInProvider: 'gemini-3-flash' },
      { provider: AuthProvider.Kiro, modelInProvider: 'gemini-3-flash' }
    ]);

    this.addMapping('gemini-3-pro-preview', [
      { provider: AuthProvider.Gemini, modelInProvider: 'gemini-3-pro' },
      { provider: AuthProvider.Windsurf, modelInProvider: 'gemini-3-pro' }
    ]);

    // Claude 4.5 Opus (Thinking)
    this.addMapping('claude-4.5-opus-thinking', [
      { provider: AuthProvider.Anthropic, modelInProvider: 'claude-4.5-opus-thinking' },
      { provider: AuthProvider.Windsurf, modelInProvider: 'claude-4.5-opus' },
      { provider: AuthProvider.Cursor, modelInProvider: 'claude-4.5-opus' }
    ]);

    // GPT-5.2 Codex
    this.addMapping('gpt-5.2-codex', [
      { provider: AuthProvider.OpenAI, modelInProvider: 'gpt-5.2-codex' },
      { provider: AuthProvider.Windsurf, modelInProvider: 'gpt-5.2-codex' },
      { provider: AuthProvider.Copilot, modelInProvider: 'gpt-5.2-codex' }
    ]);

    // NEW HARVESTED MODELS (Mark III)

    // Claude 3.7 Sonnet (Latest)
    this.addMapping('claude-3-7-sonnet-20250219', [
        { provider: AuthProvider.Anthropic, modelInProvider: 'claude-3-7-sonnet-20250219' },
        { provider: AuthProvider.Windsurf, modelInProvider: 'claude-3-7-sonnet' },
        { provider: AuthProvider.Cursor, modelInProvider: 'claude-3.7-sonnet' }
    ]);

    // Claude 4.5 Sonnet (Internal ID -> Provider ID)
    this.addMapping('claude-sonnet-4-5', [
        { provider: AuthProvider.Anthropic, modelInProvider: 'CLAUDE_SONNET_4_5_20250929_V1_0' },
        { provider: AuthProvider.Cursor, modelInProvider: 'claude-4.5-sonnet' }
    ]);

    // DeepSeek R1 (Reasoning)
    this.addMapping('deepseek-r1', [
        { provider: AuthProvider.Qwen, modelInProvider: 'deepseek-r1' }, // Qwen provider often proxies DeepSeek
        { provider: AuthProvider.Windsurf, modelInProvider: 'deepseek-reasoner' },
        { provider: AuthProvider.Generic, modelInProvider: 'deepseek-r1' } // Local Ollama fallback
    ]);

    // Qwen 3 Coder Plus
    this.addMapping('qwen3-coder-plus', [
        { provider: AuthProvider.Qwen, modelInProvider: 'qwen3-coder-plus' }
    ]);

    // --- MARK VI: EXPANSION (Protocol: NET_CRAWLER) ---

    // Anthropic: Claude 4.5 Haiku
    this.addMapping('claude-haiku-4-5', [
        { provider: AuthProvider.Anthropic, modelInProvider: 'claude-haiku-4-5-20251001' },
        { provider: AuthProvider.Windsurf, modelInProvider: 'claude-haiku-4.5' }
    ]);

    // Gemini: 2.5 Family (The "Workhorse" Suite)
    this.addMapping('gemini-2.5-pro', [
        { provider: AuthProvider.Gemini, modelInProvider: 'gemini-2.5-pro' },
        { provider: AuthProvider.Windsurf, modelInProvider: 'gemini-2.5-pro' }
    ]);
    this.addMapping('gemini-2.5-flash', [
        { provider: AuthProvider.Gemini, modelInProvider: 'gemini-2.5-flash' },
        { provider: AuthProvider.Windsurf, modelInProvider: 'gemini-2.5-flash' }
    ]);
    this.addMapping('gemini-2.5-flash-lite', [
        { provider: AuthProvider.Gemini, modelInProvider: 'gemini-2.5-flash-lite' }
    ]);
    this.addMapping('gemini-2.5-flash-image', [
        { provider: AuthProvider.Gemini, modelInProvider: 'gemini-2.5-flash-image' }
    ]);

    // OpenAI: GPT-5 Family
    this.addMapping('gpt-5.2-pro', [
        { provider: AuthProvider.OpenAI, modelInProvider: 'gpt-5.2-pro' },
        { provider: AuthProvider.Copilot, modelInProvider: 'gpt-5.2-pro' }
    ]);
    this.addMapping('gpt-5-mini', [
        { provider: AuthProvider.OpenAI, modelInProvider: 'gpt-5-mini' }
    ]);
    this.addMapping('gpt-5-nano', [
        { provider: AuthProvider.OpenAI, modelInProvider: 'gpt-5-nano' }
    ]);

    // OpenAI: Deep Research (Reasoning)
    this.addMapping('o3-deep-research', [
        { provider: AuthProvider.OpenAI, modelInProvider: 'o3-deep-research' }
    ]);
    this.addMapping('o4-mini-deep-research', [
        { provider: AuthProvider.OpenAI, modelInProvider: 'o4-mini-deep-research' }
    ]);

    // OpenAI: Sora (Video)
    this.addMapping('sora-2', [
        { provider: AuthProvider.OpenAI, modelInProvider: 'sora-2' }
    ]);
    this.addMapping('sora-2-pro', [
        { provider: AuthProvider.OpenAI, modelInProvider: 'sora-2-pro' }
    ]);

    // DeepSeek: V3.2 Exp
    this.addMapping('deepseek-v3.2-exp', [
        { provider: AuthProvider.Qwen, modelInProvider: 'deepseek-v3.2-exp' }, // Via Qwen Proxy
        { provider: AuthProvider.Generic, modelInProvider: 'deepseek-v3.2-exp' } // Via Generic/Local
    ]);

    // Qwen Models
    this.addMapping('qwen-max', [
        { provider: AuthProvider.Qwen, modelInProvider: 'qwen-max' }
    ]);
    this.addMapping('qwen-plus', [
        { provider: AuthProvider.Qwen, modelInProvider: 'qwen-plus' }
    ]);
    this.addMapping('qwen-turbo', [
        { provider: AuthProvider.Qwen, modelInProvider: 'qwen-turbo' }
    ]);

    // iFlow Models
    this.addMapping('iflow-chat', [
        { provider: AuthProvider.IFlow, modelInProvider: 'iflow-chat' }
    ]);

    // Kiro (AWS) Models
    this.addMapping('codewhisperer', [
        { provider: AuthProvider.Kiro, modelInProvider: 'codewhisperer-analysis' }
    ]);
    this.addMapping('amazon-q-dev', [
        { provider: AuthProvider.Kiro, modelInProvider: 'amazon-q-developer' }
    ]);

    // Generic / Llama Models (Default placeholders)
    this.addMapping('llama-3-8b', [
        { provider: AuthProvider.Generic, modelInProvider: 'llama3:8b' }
    ]);
    this.addMapping('mistral', [
        { provider: AuthProvider.Generic, modelInProvider: 'mistral' }
    ]);
  }

  /**
   * Resolves the chain of models to try for a request, based on fallback configuration.
   * 
   * @param requestedModel The initial model requested
   * @param config The current AuthMonster configuration
   * @returns Ordered array of models to attempt
   */
  public resolveModelChain(requestedModel: string, config: AuthMonsterConfig): string[] {
    const modelName = requestedModel.toLowerCase();
    const fallbacks = config.modelPriorities[modelName] || [];
    
    // The chain starts with the requested model
    const chain = [modelName, ...fallbacks];
    
    // Handle directionality if requested (though usually fallbacks are already ordered)
    // If 'up', we might want to prioritize smarter models in the fallbacks.
    // However, the prompt says "ordered array of fallback models" in config, 
    // so we'll respect that order mostly.
    
    if (config.fallbackDirection === 'up') {
      // In a real implementation, we might have a 'smarts' score for each model.
      // For now, we'll assume the user-provided order is what they want, 
      // but let's just make sure we don't have duplicates.
      return Array.from(new Set(chain));
    }

    return Array.from(new Set(chain));
  }

  /**
   * Adds or updates a mapping for a generic model name.
   */
  public addMapping(modelName: string, entries: ModelHubEntry[]) {
    this.modelMap.set(modelName.toLowerCase(), entries);
  }

  /**
   * Validates and normalizes request parameters, particularly thinking budget.
   */
  public validateRequest(
    provider: AuthProvider,
    modelId: string,
    thinking?: string | number
  ): { valid: boolean; value?: string | number; warning?: string } {
      if (thinking === undefined) return { valid: true };
      return validateThinking(provider, modelId, thinking);
  }

  /**
   * Selects the best (Provider, Account) combination to serve a request for a model.
   * Uses fallback chain if primary model has no available accounts.
   * 
   * @param modelName Generic model name (e.g., 'gemini-3-flash-preview')
   * @param allAccounts List of all managed accounts across all providers
   * @param config Optional config to resolve fallbacks
   * @returns The selected provider, account, and provider-specific model name
   */
  public selectModelAccount(
    modelName: string, 
    allAccounts: ManagedAccount[],
    config?: AuthMonsterConfig
  ): { provider: AuthProvider, account: ManagedAccount, modelInProvider: string } | null {

    let modelsToTry = [modelName];

    // If config is provided, resolve the full fallback chain
    if (config) {
        modelsToTry = this.resolveModelChain(modelName, config);
    }

    for (const model of modelsToTry) {
        const selection = this.attemptSelectModelAccount(model, allAccounts);
        if (selection) {
            return selection;
        }
    }

    return null;
  }

  private attemptSelectModelAccount(
    modelName: string,
    allAccounts: ManagedAccount[]
  ): { provider: AuthProvider, account: ManagedAccount, modelInProvider: string } | null {
    const hubEntries = this.modelMap.get(modelName.toLowerCase());
    
    // If no explicit mapping, we can't route via Hub
    if (!hubEntries) return null;

    // 1. Gather all candidates (Account + Provider Model Info)
    const candidates: Array<{ 
      provider: AuthProvider, 
      account: ManagedAccount, 
      modelInProvider: string,
      score: number,
      remainingQuota: number
    }> = [];

    for (const entry of hubEntries) {
      const providerAccounts = allAccounts.filter(a => a.provider === entry.provider);
      
      for (const account of providerAccounts) {
        // Filter out unhealthy or rate-limited accounts
        if (!this.isAccountUsable(account)) continue;

        const remainingQuota = this.getRemainingQuota(account, entry.modelInProvider);
        const healthScore = account.healthScore ?? 70;

        candidates.push({
          provider: entry.provider,
          account,
          modelInProvider: entry.modelInProvider,
          score: healthScore,
          remainingQuota
        });
      }
    }

    if (candidates.length === 0) return null;

    // 2. Global Load Balancing Logic
    candidates.sort((a, b) => {
      // 0. Quota availability (Binary check: Does it have any quota left?)
      const hasQuotaA = a.remainingQuota > 0 ? 1 : 0;
      const hasQuotaB = b.remainingQuota > 0 ? 1 : 0;
      if (hasQuotaA !== hasQuotaB) {
        return hasQuotaB - hasQuotaA;
      }

      // Primary: Health Score (with 5-point buffer to allow secondary sorting)
      if (Math.abs(a.score - b.score) > 5) {
        return b.score - a.score;
      }

      // Secondary: Quota availability (fine-grained)
      if (a.remainingQuota !== b.remainingQuota) {
        return b.remainingQuota - a.remainingQuota;
      }

      // Tertiary: PID-based offset to prevent parallel collisions
      // We use a combination of account ID hash and PID
      const hashA = this.simpleHash(a.account.id) + process.pid;
      const hashB = this.simpleHash(b.account.id) + process.pid;
      return (hashA % 100) - (hashB % 100);
    });

    const choice = candidates[0];
    return {
      provider: choice.provider,
      account: choice.account,
      modelInProvider: choice.modelInProvider
    };
  }

  /**
   * Basic usability check for an account
   */
  private isAccountUsable(account: ManagedAccount): boolean {
    const now = Date.now();
    if (account.rateLimitResetTime && now < account.rateLimitResetTime) return false;
    if (account.cooldownUntil && now < account.cooldownUntil) return false;
    if (isOnCooldown(account.provider, account.id)) return false;
    if (account.healthScore !== undefined && account.healthScore < 50) return false; // MIN_USABLE
    return account.isHealthy !== false;
  }

  /**
   * Retrieves remaining quota for a specific model on an account
   */
  private getRemainingQuota(account: ManagedAccount, model: string): number {
    if (!account.quota) return 1000; // Default high value if untracked
    
    if (account.quota.modelSpecific?.[model]) {
      return account.quota.modelSpecific[model].remaining;
    }
    
    return account.quota.remaining;
  }

  /**
   * Simple string hash for tie-breaking
   */
  private simpleHash(s: string): number {
    let hash = 0;
    for (let i = 0; i < s.length; i++) {
      hash = ((hash << 5) - hash) + s.charCodeAt(i);
      hash |= 0; // Convert to 32bit integer
    }
    return Math.abs(hash);
  }
}
