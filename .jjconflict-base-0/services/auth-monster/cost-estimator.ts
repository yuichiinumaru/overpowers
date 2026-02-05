export interface ModelPricing {
  inputCostPer1M: number;
  outputCostPer1M: number;
}

const DEFAULT_PRICING: ModelPricing = { inputCostPer1M: 0, outputCostPer1M: 0 };

const PRICING_TABLE: Record<string, ModelPricing> = {
  // Gemini
  'gemini-1.5-flash': { inputCostPer1M: 0.075, outputCostPer1M: 0.30 },
  'gemini-1.5-pro': { inputCostPer1M: 3.50, outputCostPer1M: 10.50 },
  'gemini-2.0-flash': { inputCostPer1M: 0.10, outputCostPer1M: 0.40 }, // Estimated

  // Anthropic
  'claude-3-5-sonnet': { inputCostPer1M: 3.00, outputCostPer1M: 15.00 },
  'claude-3-haiku': { inputCostPer1M: 0.25, outputCostPer1M: 1.25 },
  'claude-3-opus': { inputCostPer1M: 15.00, outputCostPer1M: 75.00 },
  'claude-4.5-opus-thinking': { inputCostPer1M: 20.00, outputCostPer1M: 100.00 }, // Estimated

  // OpenAI
  'gpt-4o': { inputCostPer1M: 5.00, outputCostPer1M: 15.00 },
  'gpt-4o-mini': { inputCostPer1M: 0.15, outputCostPer1M: 0.60 },
  'o1-preview': { inputCostPer1M: 15.00, outputCostPer1M: 60.00 },
  'o1-mini': { inputCostPer1M: 3.00, outputCostPer1M: 12.00 },

  // Generic Fallbacks
  'gpt-4': { inputCostPer1M: 30.00, outputCostPer1M: 60.00 },
  'gpt-3.5-turbo': { inputCostPer1M: 0.50, outputCostPer1M: 1.50 },
  'gpt-5.2-pro': { inputCostPer1M: 10.00, outputCostPer1M: 30.00 },
};

export class CostEstimator {
  /**
   * Calculates the cost in USD for a given model and token usage.
   */
  static calculateCost(model: string, inputTokens: number, outputTokens: number): number {
    const pricing = this.getPricing(model);
    const inputCost = (inputTokens / 1_000_000) * pricing.inputCostPer1M;
    const outputCost = (outputTokens / 1_000_000) * pricing.outputCostPer1M;
    return inputCost + outputCost;
  }

  /**
   * Estimates token count based on character count (heuristic: ~4 chars per token).
   */
  static estimateTokens(text: string): number {
    if (!text) return 0;
    return Math.ceil(text.length / 4);
  }

  private static getPricing(model: string): ModelPricing {
    // Exact match
    if (PRICING_TABLE[model]) return PRICING_TABLE[model];

    // Fuzzy match / Substring match
    // e.g. "claude-3-5-sonnet-20241022" should match "claude-3-5-sonnet"
    const key = Object.keys(PRICING_TABLE).find(k => model.includes(k));
    if (key) return PRICING_TABLE[key];

    return DEFAULT_PRICING;
  }
}
