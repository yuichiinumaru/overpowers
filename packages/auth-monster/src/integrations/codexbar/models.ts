export interface CostUsageTokenSnapshot {
  sessionTokens: number | null;
  sessionCostUSD: number | null;
  last30DaysTokens: number | null;
  last30DaysCostUSD: number | null;
  daily: CostUsageDailyReportEntry[];
  updatedAt: Date;
}

export interface CostUsageDailyReportEntry {
  date: string;
  inputTokens: number | null;
  cacheReadTokens: number | null;
  cacheCreationTokens: number | null;
  outputTokens: number | null;
  totalTokens: number | null;
  costUSD: number | null;
  modelsUsed: string[] | null;
  modelBreakdowns: CostUsageModelBreakdown[] | null;
}

export interface CostUsageModelBreakdown {
  modelName: string;
  costUSD: number | null;
}

export interface CostUsageDailyReport {
  data: CostUsageDailyReportEntry[];
  summary: CostUsageSummary | null;
}

export interface CostUsageSummary {
  totalInputTokens: number | null;
  totalOutputTokens: number | null;
  cacheReadTokens: number | null;
  cacheCreationTokens: number | null;
  totalTokens: number | null;
  totalCostUSD: number | null;
}

export interface CostUsageSessionReportEntry {
  session: string;
  inputTokens: number | null;
  outputTokens: number | null;
  totalTokens: number | null;
  costUSD: number | null;
  lastActivity: string | null;
}

export interface CostUsageSessionReport {
  data: CostUsageSessionReportEntry[];
  summary: CostUsageSessionSummary | null;
}

export interface CostUsageSessionSummary {
  totalCostUSD: number | null;
}

export interface CostUsageMonthlyReportEntry {
  month: string;
  totalTokens: number | null;
  costUSD: number | null;
}

export interface CostUsageMonthlyReport {
  data: CostUsageMonthlyReportEntry[];
  summary: CostUsageMonthlySummary | null;
}

export interface CostUsageMonthlySummary {
  totalTokens: number | null;
  totalCostUSD: number | null;
}
