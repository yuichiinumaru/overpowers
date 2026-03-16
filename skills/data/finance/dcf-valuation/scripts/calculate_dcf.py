#!/usr/bin/env python3
"""
DCF Model Calculator
Calculates a basic Discounted Cash Flow valuation.
"""
import sys
import argparse

def calculate_dcf(initial_fcf, growth_rate, discount_rate, terminal_growth_rate, shares_outstanding, debt, cash, years=5):
    """
    Calculate simple DCF valuation.
    """
    fcf_projections = []
    pv_of_fcf = []

    current_fcf = initial_fcf
    for year in range(1, years + 1):
        current_fcf = current_fcf * (1 + growth_rate)
        fcf_projections.append(current_fcf)
        pv = current_fcf / ((1 + discount_rate) ** year)
        pv_of_fcf.append(pv)

    sum_pv_fcf = sum(pv_of_fcf)

    # Calculate Terminal Value using Gordon Growth Model
    terminal_value = (fcf_projections[-1] * (1 + terminal_growth_rate)) / (discount_rate - terminal_growth_rate)
    pv_terminal_value = terminal_value / ((1 + discount_rate) ** years)

    # Calculate Enterprise Value and Equity Value
    enterprise_value = sum_pv_fcf + pv_terminal_value
    equity_value = enterprise_value + cash - debt
    fair_value_per_share = equity_value / shares_outstanding

    print("\n--- DCF Valuation Summary ---")
    print(f"Projected FCFs (Years 1-{years}): {[round(f, 2) for f in fcf_projections]}")
    print(f"Present Value of FCFs: ${sum_pv_fcf:,.2f}")
    print(f"Terminal Value (Year {years}): ${terminal_value:,.2f}")
    print(f"Present Value of Terminal Value: ${pv_terminal_value:,.2f}")
    print(f"Implied Enterprise Value: ${enterprise_value:,.2f}")
    print(f"Implied Equity Value: ${equity_value:,.2f}")
    print(f"\nFair Value Per Share: ${fair_value_per_share:,.2f}")

def main():
    parser = argparse.ArgumentParser(description="DCF Valuation Calculator")
    parser.add_argument("--fcf", type=float, required=True, help="Initial Free Cash Flow")
    parser.add_argument("--growth", type=float, required=True, help="Expected FCF Growth Rate (e.g. 0.10 for 10%)")
    parser.add_argument("--wacc", type=float, required=True, help="Discount Rate/WACC (e.g. 0.08 for 8%)")
    parser.add_argument("--tgr", type=float, required=True, help="Terminal Growth Rate (e.g. 0.02 for 2%)")
    parser.add_argument("--shares", type=float, required=True, help="Shares Outstanding")
    parser.add_argument("--debt", type=float, default=0, help="Total Debt (default: 0)")
    parser.add_argument("--cash", type=float, default=0, help="Total Cash (default: 0)")
    parser.add_argument("--years", type=int, default=5, help="Projection Years (default: 5)")

    args = parser.parse_args()

    try:
        calculate_dcf(args.fcf, args.growth, args.wacc, args.tgr, args.shares, args.debt, args.cash, args.years)
    except Exception as e:
        print(f"Error calculating DCF: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
