import { ManagedAccount, AuthMethod } from './types';
import { isOnCooldown } from './quota-manager';

// ============================================================================
// CONSTANTS & TYPES
// ============================================================================

export type RateLimitReason = 
  | "QUOTA_EXHAUSTED"
  | "RATE_LIMIT_EXCEEDED" 
  | "MODEL_CAPACITY_EXHAUSTED"
  | "SERVER_ERROR"
  | "UNKNOWN";

const QUOTA_EXHAUSTED_BACKOFFS = [60_000, 300_000, 1_800_000, 7_200_000] as const;
const RATE_LIMIT_EXCEEDED_BACKOFF = 30_000;
const MODEL_CAPACITY_EXHAUSTED_BACKOFF = 15_000;
const SERVER_ERROR_BACKOFF = 20_000;
const UNKNOWN_BACKOFF = 60_000;
const MIN_BACKOFF_MS = 2_000;
const RATE_LIMIT_DEDUP_WINDOW_MS = 2_000;

export interface HealthScoreConfig {
  initial: number;
  successReward: number;
  rateLimitPenalty: number;
  failurePenalty: number;
  recoveryRatePerHour: number;
  minUsable: number;
  maxScore: number;
}

export const DEFAULT_HEALTH_SCORE_CONFIG: HealthScoreConfig = {
  initial: 70,
  successReward: 1,
  rateLimitPenalty: -10,
  failurePenalty: -20,
  recoveryRatePerHour: 2,
  minUsable: 50,
  maxScore: 100,
};

// ============================================================================
// HEALTH SCORE TRACKER
// ============================================================================

export class HealthScoreTracker {
  private config: HealthScoreConfig;
  // Map account ID to last update timestamp for passive recovery calculation
  private lastUpdateTimes: Map<string, number> = new Map();

  constructor(config: Partial<HealthScoreConfig> = {}) {
    this.config = { ...DEFAULT_HEALTH_SCORE_CONFIG, ...config };
  }

  getScore(account: ManagedAccount): number {
    const currentScore = account.healthScore ?? this.config.initial;
    const lastUpdate = this.lastUpdateTimes.get(account.id) ?? Date.now();
    
    // Apply passive recovery
    const now = Date.now();
    const hoursSinceUpdate = (now - lastUpdate) / (1000 * 60 * 60);
    
    if (hoursSinceUpdate > 0) {
      const recoveredPoints = Math.floor(hoursSinceUpdate * this.config.recoveryRatePerHour);
      return Math.min(this.config.maxScore, currentScore + recoveredPoints);
    }
    
    return currentScore;
  }

  recordSuccess(account: ManagedAccount): void {
    const current = this.getScore(account);
    account.healthScore = Math.min(this.config.maxScore, current + this.config.successReward);
    account.consecutiveFailures = 0;
    account.isHealthy = account.healthScore >= this.config.minUsable;
    this.lastUpdateTimes.set(account.id, Date.now());
  }

  recordRateLimit(account: ManagedAccount): void {
    const current = this.getScore(account);
    account.healthScore = Math.max(0, current + this.config.rateLimitPenalty);
    account.consecutiveFailures = (account.consecutiveFailures ?? 0) + 1;
    account.isHealthy = account.healthScore >= this.config.minUsable;
    this.lastUpdateTimes.set(account.id, Date.now());
  }

  recordFailure(account: ManagedAccount): void {
    const current = this.getScore(account);
    account.healthScore = Math.max(0, current + this.config.failurePenalty);
    account.consecutiveFailures = (account.consecutiveFailures ?? 0) + 1;
    account.isHealthy = account.healthScore >= this.config.minUsable;
    this.lastUpdateTimes.set(account.id, Date.now());
  }

  isUsable(account: ManagedAccount): boolean {
    return this.getScore(account) >= this.config.minUsable;
  }
}

// ============================================================================
// ACCOUNT ROTATOR
// ============================================================================

export class AccountRotator {
  private healthTracker: HealthScoreTracker;
  private cursor: number = 0;
  private lastRateLimitTimes: Map<string, number> = new Map();

  constructor(healthConfig?: Partial<HealthScoreConfig>) {
    this.healthTracker = new HealthScoreTracker(healthConfig);
    // PID-based initial offset for round-robin to maximize throughput across parallel instances
    this.cursor = process.pid;
  }

  selectAccount(accounts: ManagedAccount[], strategy: AuthMethod = 'sticky'): ManagedAccount | null {
    if (!accounts.length) return null;

    // Filter out accounts that are cooling down or rate limited OR unhealthy
    const availableAccounts = accounts.filter(acc => {
      const now = Date.now();
      if (acc.rateLimitResetTime && now < acc.rateLimitResetTime) return false;
      if (acc.cooldownUntil && now < acc.cooldownUntil) return false;
      
      // Check global cooldown manager
      if (isOnCooldown(acc.provider, acc.id)) return false;

      // Check explicit quota if available (Proactive check)
      if (acc.quota && acc.quota.remaining <= 0) return false;

      // Check health
      if (!this.healthTracker.isUsable(acc)) return false;

      return true;
    });

    if (availableAccounts.length === 0) return null;

    switch (strategy) {
      case 'round-robin':
        return this.selectRoundRobin(availableAccounts);
      case 'hybrid':
        return this.selectHybrid(availableAccounts);
      case 'quota-optimized':
        return this.selectQuotaOptimized(availableAccounts);
      case 'sticky':
      default:
        return this.selectSticky(availableAccounts);
    }
  }

  private selectQuotaOptimized(accounts: ManagedAccount[]): ManagedAccount {
    // Sort by remaining quota (descending)
    const sorted = [...accounts].sort((a, b) => {
      const quotaA = a.quota?.remaining ?? 1000;
      const quotaB = b.quota?.remaining ?? 1000;
      return quotaB - quotaA;
    });
    return sorted[0];
  }

  private selectRoundRobin(accounts: ManagedAccount[]): ManagedAccount {
    const account = accounts[this.cursor % accounts.length];
    this.cursor++;
    return account;
  }

  private selectSticky(accounts: ManagedAccount[]): ManagedAccount {
    // Incorporate a process-based offset to ensure different IDE instances 
    // or subagents pick different starting accounts.
    const offset = process.pid % accounts.length;
    return accounts[offset];
  }

  private selectHybrid(accounts: ManagedAccount[]): ManagedAccount {
    // Sort by health score (descending) and then by last used (ascending - LRU)
    // We want the healthiest account that hasn't been used recently.
    
    const scored = accounts.map(acc => ({
      account: acc,
      score: this.healthTracker.getScore(acc),
      lastUsed: acc.lastUsed ?? 0
    }));

    // Apply PID-based rotation to the base list to break ties in a way that
    // maximizes throughput across parallel instances.
    const pidOffset = process.pid % scored.length;
    const rotatedScored = [
      ...scored.slice(pidOffset),
      ...scored.slice(0, pidOffset)
    ];

    rotatedScored.sort((a, b) => {
      // Primary: Health Score
      if (Math.abs(a.score - b.score) > 5) { // 5 point buffer
        return b.score - a.score;
      }
      // Secondary: LRU (Least Recently Used)
      return a.lastUsed - b.lastUsed;
    });

    return rotatedScored[0].account;
  }

  recordSuccess(account: ManagedAccount): void {
    this.healthTracker.recordSuccess(account);
    account.lastUsed = Date.now();
  }

  recordFailure(account: ManagedAccount): void {
    this.healthTracker.recordFailure(account);
  }

  recordRateLimit(account: ManagedAccount, retryAfterMs?: number, reason: RateLimitReason = 'UNKNOWN'): void {
    const now = Date.now();
    const lastAt = this.lastRateLimitTimes.get(account.id) ?? 0;

    // Deduplicate concurrent 429s within 2000ms window
    if (now - lastAt < RATE_LIMIT_DEDUP_WINDOW_MS) {
      if (retryAfterMs) {
        account.rateLimitResetTime = now + retryAfterMs;
      }
      return;
    }

    this.lastRateLimitTimes.set(account.id, now);
    this.healthTracker.recordRateLimit(account);
    
    const backoff = retryAfterMs ?? this.calculateBackoff(reason, account.consecutiveFailures ?? 1);
    account.rateLimitResetTime = now + backoff;
    account.lastSwitchReason = 'rate-limit';
  }

  private calculateBackoff(reason: RateLimitReason, consecutiveFailures: number): number {
    switch (reason) {
      case "QUOTA_EXHAUSTED": {
        const index = Math.min(consecutiveFailures, QUOTA_EXHAUSTED_BACKOFFS.length - 1);
        return QUOTA_EXHAUSTED_BACKOFFS[index];
      }
      case "RATE_LIMIT_EXCEEDED":
        return RATE_LIMIT_EXCEEDED_BACKOFF;
      case "MODEL_CAPACITY_EXHAUSTED":
        return MODEL_CAPACITY_EXHAUSTED_BACKOFF;
      case "SERVER_ERROR":
        return SERVER_ERROR_BACKOFF;
      case "UNKNOWN":
      default:
        return UNKNOWN_BACKOFF;
    }
  }
}
