#!/usr/bin/env python3
import sys
import argparse

def calculate_slo_metrics(ad_spend, cpc, conversion_rate, front_end_price, bump_take_rate, bump_price, oto_take_rate, oto_price):
    """
    Calculates SLO funnel metrics and profitability.
    """
    clicks = ad_spend / cpc
    buyers = clicks * conversion_rate
    cpa = ad_spend / buyers if buyers > 0 else float('inf')

    front_end_revenue = buyers * front_end_price

    bump_buyers = buyers * bump_take_rate
    bump_revenue = bump_buyers * bump_price

    oto_buyers = buyers * oto_take_rate
    oto_revenue = oto_buyers * oto_price

    total_revenue = front_end_revenue + bump_revenue + oto_revenue
    aov = total_revenue / buyers if buyers > 0 else 0
    roas = total_revenue / ad_spend if ad_spend > 0 else 0
    profit = total_revenue - ad_spend

    return {
        "clicks": clicks,
        "buyers": buyers,
        "cpa": cpa,
        "aov": aov,
        "roas": roas,
        "profit": profit,
        "total_revenue": total_revenue
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate SLO Funnel Metrics")
    parser.add_argument("--spend", type=float, required=True, help="Total Ad Spend ($)")
    parser.add_argument("--cpc", type=float, required=True, help="Cost Per Click ($)")
    parser.add_argument("--cr", type=float, required=True, help="Front-End Conversion Rate (e.g., 0.03 for 3%)")
    parser.add_argument("--fe_price", type=float, required=True, help="Front-End Product Price ($)")
    parser.add_argument("--bump_rate", type=float, default=0.0, help="Order Bump Take Rate (e.g., 0.20 for 20%)")
    parser.add_argument("--bump_price", type=float, default=0.0, help="Order Bump Price ($)")
    parser.add_argument("--oto_rate", type=float, default=0.0, help="Upsell (OTO) Take Rate (e.g., 0.10 for 10%)")
    parser.add_argument("--oto_price", type=float, default=0.0, help="Upsell (OTO) Price ($)")

    args = parser.parse_args()

    results = calculate_slo_metrics(
        args.spend, args.cpc, args.cr, args.fe_price,
        args.bump_rate, args.bump_price, args.oto_rate, args.oto_price
    )

    print("\n=== SLO Funnel Projection ===")
    print(f"Ad Spend: ${args.spend:.2f}")
    print(f"Traffic (Clicks): {int(results['clicks'])}")
    print(f"Customers (Buyers): {int(results['buyers'])}")
    print(f"Cost Per Acquisition (CPA): ${results['cpa']:.2f}")
    print(f"Average Order Value (AOV): ${results['aov']:.2f}")
    print("-----------------------------")
    print(f"Total Revenue: ${results['total_revenue']:.2f}")
    print(f"Net Profit/Loss (Day 0): ${results['profit']:.2f}")
    print(f"ROAS: {results['roas']:.2f}x")

    if results['profit'] >= 0:
        print("\n✅ Status: Profitable (Self-Liquidating Day 0)")
    else:
        print("\n❌ Status: Unprofitable (Losing money on front-end)")
