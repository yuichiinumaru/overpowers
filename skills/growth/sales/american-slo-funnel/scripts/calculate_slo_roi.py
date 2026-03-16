#!/usr/bin/env python3
"""
SLO ROI Calculator
Calculates the Return on Ad Spend (ROAS) and Break-Even Point for a Self-Liquidating Offer funnel.
"""
import sys
import argparse

def calculate_roas(cpa, aov):
    """
    Calculate Return on Ad Spend (ROAS)
    """
    if cpa == 0:
        return float('inf')
    return (aov / cpa) * 100

def main():
    parser = argparse.ArgumentParser(description="SLO Funnel Metrics Calculator")
    parser.add_argument("--traffic-cost", type=float, required=True, help="Total ad spend for the funnel.")
    parser.add_argument("--leads", type=int, required=True, help="Total number of leads acquired.")
    parser.add_argument("--front-end-sales", type=int, required=True, help="Total number of front-end product sales.")
    parser.add_argument("--front-end-price", type=float, required=True, help="Price of the front-end product.")

    args = parser.parse_args()

    # Calculate Costs
    cpl = args.traffic_cost / args.leads if args.leads > 0 else 0
    cpa = args.traffic_cost / args.front-end-sales if args.front-end-sales > 0 else 0

    # Calculate Revenue
    total_revenue = args.front-end-sales * args.front-end-price
    aov = args.front-end-price # In a pure front-end SLO, AOV is just the product price

    # Calculate ROI metrics
    profit = total_revenue - args.traffic_cost
    roas = calculate_roas(args.traffic_cost, total_revenue) if args.traffic_cost > 0 else float('inf')

    print(f"--- SLO Funnel Performance ---")
    print(f"Total Ad Spend: ${args.traffic_cost:.2f}")
    print(f"Total Revenue: ${total_revenue:.2f}")
    print(f"Net Profit/Loss: ${profit:.2f}")
    print(f"Cost Per Lead (CPL): ${cpl:.2f}")
    print(f"Cost Per Acquisition (CPA): ${cpa:.2f}")
    print(f"Average Order Value (AOV): ${aov:.2f}")
    print(f"Return on Ad Spend (ROAS): {roas:.2f}%")

    if profit >= 0:
        print("\nResult: BREAK-EVEN OR PROFITABLE! The SLO is working.")
    else:
        print("\nResult: LOSS-MAKING. You need to improve conversion rates or reduce CPA.")

if __name__ == "__main__":
    main()
