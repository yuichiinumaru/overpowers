#!/usr/bin/env python3
import argparse

def calculate_metrics(mrr, cac, ltv, churn_rate):
    metrics = {}
    metrics["Annual Recurring Revenue (ARR)"] = mrr * 12

    if cac > 0:
        metrics["LTV:CAC Ratio"] = ltv / cac
    else:
        metrics["LTV:CAC Ratio"] = float('inf')

    if churn_rate > 0:
        metrics["Months to Recover CAC"] = cac / (mrr / (1/churn_rate)) if ltv > 0 else 0

    return metrics

def main():
    parser = argparse.ArgumentParser(description="Calculate basic startup unit economics.")
    parser.add_argument("--mrr", type=float, required=True, help="Monthly Recurring Revenue")
    parser.add_argument("--cac", type=float, required=True, help="Customer Acquisition Cost")
    parser.add_argument("--ltv", type=float, required=True, help="Customer Lifetime Value")
    parser.add_argument("--churn", type=float, required=True, help="Monthly Churn Rate (decimal, e.g., 0.05 for 5%)")

    args = parser.parse_args()

    metrics = calculate_metrics(args.mrr, args.cac, args.ltv, args.churn)

    print("--- Startup Health Metrics ---")
    for k, v in metrics.items():
        if isinstance(v, float):
            print(f"{k}: {v:.2f}")
        else:
            print(f"{k}: {v}")

    # Basic analysis
    print("\nAnalysis:")
    if metrics.get("LTV:CAC Ratio", 0) >= 3:
        print("✅ LTV:CAC is healthy (>= 3.0)")
    else:
        print("⚠️ LTV:CAC is low (< 3.0). Focus on decreasing CAC or increasing LTV.")

if __name__ == "__main__":
    main()
