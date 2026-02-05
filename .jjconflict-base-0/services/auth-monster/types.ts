import { z } from 'zod';

export enum AuthProvider {
  Gemini = 'gemini',
  Windsurf = 'windsurf',
  Anthropic = 'anthropic',
  Cursor = 'cursor',
  Qwen = 'qwen',
  IFlow = 'iflow',
  OpenAI = 'openai',
  Copilot = 'copilot',
  Kiro = 'kiro',
  Zhipu = 'zhipu',
  Minimax = 'minimax',
  Azure = 'azure',
  Grok = 'grok',
  DeepSeek = 'deepseek',
  Generic = 'generic'
}

export type AuthMethod = 'sticky' | 'round-robin' | 'hybrid' | 'quota-optimized';

export interface OAuthTokens {
  accessToken: string;
  refreshToken?: string;
  expiryDate?: number;
  tokenType?: string;
}

export interface ManagedAccount {
  id: string;
  email: string;
  provider: AuthProvider;
  tokens: OAuthTokens;
  apiKey?: string;
  metadata?: Record<string, any>;
  lastUsed?: number;
  isHealthy: boolean;
  
  // Rotation & Health fields
  healthScore?: number;
  rateLimitResetTime?: number;
  consecutiveFailures?: number;
  cooldownUntil?: number;
  lastSwitchReason?: string;

  // Usage Stats (Phase 3)
  usage?: {
    totalInputTokens: number;
    totalOutputTokens: number;
    totalCost: number; // USD
  };

  // Quota Management
  quota?: {
    limit: number;
    remaining: number;
    resetTime?: number;
    modelSpecific?: Record<string, {
      limit: number;
      remaining: number;
      resetTime?: number;
    }>;
  };
}

export const AuthMonsterConfigSchema = z.object({
  active: z.nativeEnum(AuthProvider).default(AuthProvider.Gemini),
  fallback: z.array(z.nativeEnum(AuthProvider)).default([]),
  method: z.enum(['sticky', 'round-robin', 'hybrid', 'quota-optimized']).default('sticky'),
  proxy: z.string().optional(),
  modelPriorities: z.record(z.string(), z.array(z.string())).default({
    'gemini-3-pro-preview': ['claude-4.5-opus-thinking', 'gpt-5.2-codex'],
    'claude-4.5-opus-thinking': ['gpt-5.2-codex', 'gemini-3-pro-preview'],
    'gpt-5.2-codex': ['claude-4.5-opus-thinking', 'gemini-3-pro-preview']
  }),
  fallbackDirection: z.enum(['up', 'down']).default('down'),
  thinking: z.object({
    enabled: z.boolean().default(true),
    defaultBudget: z.number().default(1024),
    defaultLevel: z.string().default('low')
  }).optional(),
  quota: z.object({
    enabled: z.boolean().default(true),
    cooldownMinutes: z.number().default(5),
    preflightCheck: z.boolean().default(true)
  }).optional(),
  providers: z.record(z.string(), z.object({
    enabled: z.boolean().default(true),
    profile: z.string().optional(),
    port: z.number().optional(),
    options: z.record(z.string(), z.any()).optional()
  })).default({})
});

export type AuthMonsterConfig = z.infer<typeof AuthMonsterConfigSchema>;

export interface AuthDetails {
  provider: AuthProvider;
  account: ManagedAccount;
  headers: Record<string, string>;
  modelInProvider?: string;
}

export interface PluginContext {
  config: AuthMonsterConfig;
  storagePath: string;
}
