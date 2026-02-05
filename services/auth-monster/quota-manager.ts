import { AuthProvider, ManagedAccount } from './types';

// ============================================================================
// TYPES
// ============================================================================

export interface ModelQuota {
  name: string;
  percentage: number;
  resetTime: number | null;
}

export interface QuotaResult {
  success: boolean;
  models: ModelQuota[];
  lastUpdated: number;
  remaining: number; // overall remaining
}

interface CacheEntry {
  result: QuotaResult;
  timestamp: number;
}

interface CooldownEntry {
  until: number;
}

export interface PreflightResult {
  proceed: boolean;
  accountId: string;
  switchedFrom?: string;
  reason?: string;
  quotaPercent?: number | null;
}

// ============================================================================
// QUOTA MANAGER
// ============================================================================

const CACHE_TTL_MS = 30_000;
const quotaCache = new Map<string, CacheEntry>();
const cooldownMap = new Map<string, CooldownEntry>();

function getCacheKey(provider: AuthProvider, accountId: string): string {
  return `${provider}:${accountId}`;
}

/**
 * Get cached quota result if still valid
 */
export function getCachedQuota(provider: AuthProvider, accountId: string): QuotaResult | null {
  const key = getCacheKey(provider, accountId);
  const entry = quotaCache.get(key);

  if (!entry) return null;

  if (Date.now() - entry.timestamp > CACHE_TTL_MS) {
    quotaCache.delete(key);
    return null;
  }

  return entry.result;
}

/**
 * Cache quota result
 */
export function setCachedQuota(
  provider: AuthProvider,
  accountId: string,
  result: QuotaResult
): void {
  const key = getCacheKey(provider, accountId);
  quotaCache.set(key, { result, timestamp: Date.now() });
}

/**
 * Check if account is on cooldown
 */
export function isOnCooldown(provider: AuthProvider, accountId: string): boolean {
  const key = getCacheKey(provider, accountId);
  const entry = cooldownMap.get(key);

  if (!entry) return false;

  if (Date.now() > entry.until) {
    cooldownMap.delete(key);
    return false;
  }

  return true;
}

export function getCooldownStatus(provider: AuthProvider, accountId: string): { active: boolean, until?: number } {
  const key = getCacheKey(provider, accountId);
  const entry = cooldownMap.get(key);

  if (!entry) return { active: false };

  if (Date.now() > entry.until) {
    cooldownMap.delete(key);
    return { active: false };
  }

  return { active: true, until: entry.until };
}

/**
 * Apply cooldown to an exhausted account
 */
export function applyCooldown(
  provider: AuthProvider,
  accountId: string,
  minutes: number
): void {
  const key = getCacheKey(provider, accountId);
  cooldownMap.set(key, { until: Date.now() + minutes * 60 * 1000 });
}

/**
 * Extract quota from ManagedAccount object.
 * This effectively replaces "fetchAccountQuota" by using the state we already have.
 */
export function extractQuota(account: ManagedAccount): QuotaResult {
  if (!account.quota) {
    // If no quota tracking, assume healthy/unlimited
    return {
      success: true,
      remaining: 1000,
      models: [],
      lastUpdated: Date.now()
    };
  }

  const models: ModelQuota[] = [];
  if (account.quota.modelSpecific) {
    for (const [name, info] of Object.entries(account.quota.modelSpecific)) {
      models.push({
        name,
        percentage: info.limit > 0 ? (info.remaining / info.limit) * 100 : 100,
        resetTime: info.resetTime || null
      });
    }
  }

  return {
    success: true,
    remaining: account.quota.remaining,
    models,
    lastUpdated: Date.now()
  };
}

/**
 * Find healthy account with remaining quota
 */
export function findHealthyAccount(
  provider: AuthProvider,
  allAccounts: ManagedAccount[],
  excludeIds: string[] = []
): ManagedAccount | null {
  // Filter available accounts
  const available = allAccounts.filter(
    (a) =>
      a.provider === provider &&
      !excludeIds.includes(a.id) &&
      !isOnCooldown(provider, a.id) &&
      a.isHealthy !== false
  );

  if (available.length === 0) return null;

  // Sort by health score + quota
  available.sort((a, b) => {
    // Health Score
    const scoreA = a.healthScore ?? 70;
    const scoreB = b.healthScore ?? 70;
    if (Math.abs(scoreA - scoreB) > 5) {
        return scoreB - scoreA;
    }

    // Quota
    const quotaA = a.quota?.remaining ?? 1000;
    const quotaB = b.quota?.remaining ?? 1000;
    return quotaB - quotaA;
  });

  return available[0];
}

/**
 * Perform pre-flight quota check before session start
 */
export function preflightCheck(
  provider: AuthProvider,
  currentAccount: ManagedAccount,
  allAccounts: ManagedAccount[]
): PreflightResult {
  // Check cooldown
  if (isOnCooldown(provider, currentAccount.id)) {
    const alt = findHealthyAccount(provider, allAccounts, [currentAccount.id]);
    if (alt) {
        return {
            proceed: true,
            accountId: alt.id,
            switchedFrom: currentAccount.id,
            reason: 'Current account on cooldown'
        };
    }
    return { proceed: false, accountId: currentAccount.id, reason: 'Account on cooldown and no alternatives' };
  }

  // Check quota
  const quota = extractQuota(currentAccount);
  if (quota.remaining <= 0) {
      applyCooldown(provider, currentAccount.id, 5); // 5 min cooldown
      const alt = findHealthyAccount(provider, allAccounts, [currentAccount.id]);
      if (alt) {
        return {
            proceed: true,
            accountId: alt.id,
            switchedFrom: currentAccount.id,
            reason: 'Quota exhausted'
        };
      }
  }

  return {
    proceed: true,
    accountId: currentAccount.id,
    quotaPercent: quota.remaining // simplified
  };
}
