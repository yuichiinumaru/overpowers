import { AuthProvider } from './types';

export interface ThinkingSupport {
  type: 'none' | 'budget' | 'levels';
  min?: number;
  max?: number;
  levels?: string[]; // ordered low to high
  maxLevel?: string;
  default?: number | string;
  zeroAllowed?: boolean;
  dynamicAllowed?: boolean;
}

/**
 * Thinking budget bounds
 */
export const THINKING_BUDGET_MIN = 0;
export const THINKING_BUDGET_MAX = 100000;
export const THINKING_BUDGET_DEFAULT_MIN = 512;

export interface ThinkingValidationResult {
  valid: boolean;
  value: string | number;
  warning?: string;
}

export const THINKING_LEVEL_BUDGETS: Record<string, number> = {
  minimal: 512,
  low: 1024,
  medium: 8192,
  high: 24576,
  xhigh: 32768,
};

export const THINKING_LEVEL_RANK: Record<string, number> = {
  minimal: 1,
  low: 2,
  medium: 3,
  high: 4,
  xhigh: 5,
};

export const VALID_THINKING_LEVELS = ['minimal', 'low', 'medium', 'high', 'xhigh', 'auto'] as const;
export type ThinkingLevel = (typeof VALID_THINKING_LEVELS)[number];

export const THINKING_OFF_VALUES = ['off', 'none', 'disabled', '0'] as const;
export const THINKING_AUTO_VALUE = 'auto';

/**
 * Get thinking support for a specific model/provider combo.
 * This acts as a mini-catalog.
 */
export function getModelThinkingSupport(provider: AuthProvider, modelId: string): ThinkingSupport | null {
  const model = modelId.toLowerCase();

  // Anthropic / Claude
  if (provider === AuthProvider.Anthropic || model.includes('claude')) {
    if (model.includes('3-7-sonnet') || model.includes('3.7-sonnet')) {
      return {
        type: 'budget',
        min: 1024,
        max: 32000, // 3.7 supports up to 64k extended, typically
        zeroAllowed: true,
        dynamicAllowed: true
      };
    }
    if (model.includes('4-5-opus') || model.includes('4.5-opus')) {
        // Hypothetical 4.5 Opus support
        return {
            type: 'budget',
            min: 2048,
            max: 64000,
            zeroAllowed: false,
            dynamicAllowed: true
        };
    }
  }

  // OpenAI / Codex / O-series
  if (provider === AuthProvider.OpenAI || model.includes('o1') || model.includes('o3') || model.includes('codex')) {
      // O1/O3 use levels (low/medium/high) usually, but sometimes budget
      return {
          type: 'levels',
          levels: ['low', 'medium', 'high'],
          default: 'medium',
          dynamicAllowed: false
      };
  }

  // Default: check if it's a known reasoning model
  if (model.includes('reasoning') || model.includes('thinking')) {
      return {
          type: 'budget',
          min: 1024,
          max: 16000,
          dynamicAllowed: true
      };
  }

  // No thinking support by default
  return { type: 'none' };
}

export function capLevelAtMax(
  level: string,
  maxLevel: string | undefined
): { level: string; capped: boolean } {
  if (!maxLevel) return { level, capped: false };
  const levelRank = THINKING_LEVEL_RANK[level] ?? 0;
  const maxRank = THINKING_LEVEL_RANK[maxLevel] ?? 5;
  if (levelRank > maxRank) {
    return { level: maxLevel, capped: true };
  }
  return { level, capped: false };
}

function findClosestLevel(input: string, validLevels: string[]): string | undefined {
  const normalized = input.toLowerCase().trim();
  if (validLevels.includes(normalized)) {
    return normalized;
  }
  for (const level of validLevels) {
    if (level.startsWith(normalized)) {
      return level;
    }
  }
  return undefined;
}

export function validateThinking(
  provider: AuthProvider,
  modelId: string,
  value: string | number
): ThinkingValidationResult {
  const thinking = getModelThinkingSupport(provider, modelId);

  if (typeof value === 'string' && value.length > 100) {
    return { valid: false, value: 'off', warning: 'Thinking value too long.' };
  }
  if (typeof value === 'string' && value.trim() === '') {
    return { valid: false, value: 'off', warning: 'Empty thinking value.' };
  }
  if (typeof value === 'string') {
    const normalizedValue = value.toLowerCase().trim();
    if (THINKING_OFF_VALUES.includes(normalizedValue as any)) {
      return { valid: true, value: 'off' };
    }
  }

  if (!thinking) {
    return { valid: true, value, warning: `Unknown thinking support for ${modelId}.` };
  }
  if (thinking.type === 'none') {
    return { valid: false, value: 'off', warning: `Model ${modelId} does not support thinking.` };
  }

  if (typeof value === 'string' && value.toLowerCase().trim() === THINKING_AUTO_VALUE) {
    if (!thinking.dynamicAllowed) {
       const fallback = thinking.type === 'budget' ? (thinking.min ?? 1024) : (thinking.levels?.[0] ?? 'low');
       return { valid: false, value: fallback, warning: 'Dynamic thinking not supported. Using minimum.' };
    }
    return { valid: true, value: 'auto' };
  }

  if (thinking.type === 'budget') {
    return validateBudgetThinking(thinking, value, modelId);
  }
  if (thinking.type === 'levels') {
    return validateLevelThinking(thinking, value, modelId);
  }

  return { valid: true, value };
}

function validateBudgetThinking(
  thinking: ThinkingSupport,
  value: string | number,
  modelId: string
): ThinkingValidationResult {
  const min = thinking.min ?? THINKING_BUDGET_MIN;
  const max = thinking.max ?? THINKING_BUDGET_MAX;

  let budget: number;
  if (typeof value === 'string') {
    const normalizedLevel = value.toLowerCase().trim();
    if (normalizedLevel in THINKING_LEVEL_BUDGETS) {
      budget = THINKING_LEVEL_BUDGETS[normalizedLevel];
    } else {
      const parsed = Number(value);
      if (isNaN(parsed) || !Number.isFinite(parsed)) {
        return { valid: false, value: min, warning: `Invalid budget "${value}".` };
      }
      budget = parsed;
    }
  } else {
    budget = value;
  }

  if (budget < min) {
    return { valid: true, value: min, warning: `Budget ${budget} below min. Clamped to ${min}.` };
  }
  if (budget > max) {
    return { valid: true, value: max, warning: `Budget ${budget} exceeds max. Clamped to ${max}.` };
  }

  return { valid: true, value: budget };
}

function validateLevelThinking(
  thinking: ThinkingSupport,
  value: string | number,
  modelId: string
): ThinkingValidationResult {
  const validLevels = thinking.levels ?? [];

  if (typeof value === 'number') {
    // Map number to level
    let closestLevel = validLevels[0] ?? 'low';
    let closestDiff = Infinity;
    for (const level of validLevels) {
      const budget = THINKING_LEVEL_BUDGETS[level] ?? 8192;
      const diff = Math.abs(budget - value);
      if (diff < closestDiff) {
        closestDiff = diff;
        closestLevel = level;
      }
    }
    return { valid: true, value: closestLevel, warning: `Mapped budget ${value} to level ${closestLevel}.` };
  }

  const normalized = value.toLowerCase().trim();
  if (validLevels.includes(normalized)) {
    return { valid: true, value: normalized };
  }

  const closest = findClosestLevel(normalized, validLevels);
  if (closest) {
    return { valid: true, value: closest, warning: `Mapped ${value} to ${closest}.` };
  }

  return { valid: false, value: validLevels[0] ?? 'low', warning: `Invalid level ${value}.` };
}
