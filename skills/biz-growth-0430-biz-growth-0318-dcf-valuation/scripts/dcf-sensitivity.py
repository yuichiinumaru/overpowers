#!/usr/bin/env python3
import sys
import argparse
import itertools

def generate_sensitivity_matrix(base_wacc, base_tg):
    """
    Generates a 3x3 sensitivity matrix for DCF valuation.
    Varies WACC by +/- 1% and Terminal Growth by 2.0%, 2.5%, 3.0%.
    (Values inside matrix are placeholders for actual calculated Fair Value per Share)
    """
    waccs = [base_wacc - 0.01, base_wacc, base_wacc + 0.01]
    tgs = [0.020, 0.025, 0.030]

    print("\n### Sensitivity Matrix (Placeholder Values)")
    print("| Terminal Growth / WACC | {:.1f}% | {:.1f}% (Base) | {:.1f}% |".format(waccs[0]*100, waccs[1]*100, waccs[2]*100))
    print("|---|---|---|---|")

    for tg in tgs:
        row = f"| **{tg*100:.1f}%** | "
        for wacc in waccs:
            # Placeholder calculation: just an inverse relationship for demonstration
            # In a real script, this would run the full DCF model for these parameters
            factor = (tg / wacc) * 100
            row += f"${factor:.2f} | "
        print(row)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a DCF Sensitivity Matrix")
    parser.add_argument("--wacc", type=float, required=True, help="Base WACC (e.g., 0.08 for 8%)")
    parser.add_argument("--tg", type=float, default=0.025, help="Base Terminal Growth (e.g., 0.025 for 2.5%)")

    args = parser.parse_args()
    generate_sensitivity_matrix(args.wacc, args.tg)
