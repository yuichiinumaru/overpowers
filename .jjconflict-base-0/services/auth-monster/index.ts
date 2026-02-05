/**
 * Auth Monster Service - Core Re-exports
 * 
 * This is the unified entry point for the auth-monster engine when used
 * as a service within Overpowers.
 */

export { UnifiedModelHub, ModelHubEntry } from './hub';
export {
    AuthProvider,
    AuthMethod,
    ManagedAccount,
    AuthMonsterConfig,
    AuthMonsterConfigSchema,
    AuthDetails,
    PluginContext,
    OAuthTokens
} from './types';
export {
    getCachedQuota,
    setCachedQuota,
    isOnCooldown,
    getCooldownStatus,
    applyCooldown,
    extractQuota,
    findHealthyAccount,
    preflightCheck
} from './quota-manager';
export { AccountRotator } from './rotation';
export { StorageManager } from './storage';
export { SecretStorage } from './secret-storage';
export { CostEstimator } from './cost-estimator';
export { validateThinking, ThinkingValidationResult } from './thinking-validator';
export { TokenExtractor, autoDiscoverAccounts } from './extractors/extractor';
