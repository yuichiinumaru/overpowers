#!/usr/bin/env python3
"""
Sample Size Calculator for A/B Testing
Calculates the required sample size based on baseline conversion rate and minimum detectable effect (MDE).
"""
import sys
import argparse
import math

def calculate_sample_size(baseline_rate, mde, power=0.8, alpha=0.05):
    """
    Calculate required sample size for an A/B test.
    Using standard normal distribution approximation.
    """
    if not (0 < baseline_rate < 1):
        raise ValueError("Baseline rate must be between 0 and 1.")
    if not (0 < mde < 1):
        raise ValueError("MDE must be between 0 and 1.")

    # Standard normal deviates (approximate)
    # Z_alpha/2 for 95% confidence = 1.96
    z_alpha = 1.96 if alpha == 0.05 else 1.645 # default to 95% or 90%
    # Z_beta for 80% power = 0.84
    z_beta = 0.84 if power == 0.8 else 1.28 # default to 80% or 90%

    p1 = baseline_rate
    p2 = baseline_rate * (1 + mde)

    if p2 >= 1:
        raise ValueError("MDE is too large, resulting rate exceeds 1.")

    p_pooled = (p1 + p2) / 2

    numerator = (z_alpha * math.sqrt(2 * p_pooled * (1 - p_pooled)) +
                 z_beta * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2)))**2
    denominator = (p1 - p2)**2

    n_per_variant = math.ceil(numerator / denominator)
    return n_per_variant

def main():
    parser = argparse.ArgumentParser(description="A/B Test Sample Size Calculator")
    parser.add_argument("--baseline", type=float, required=True, help="Baseline conversion rate (e.g. 0.05 for 5%)")
    parser.add_argument("--mde", type=float, required=True, help="Minimum Detectable Effect as a relative percentage (e.g. 0.10 for 10% lift)")
    parser.add_argument("--power", type=float, default=0.8, help="Statistical power (default: 0.8)")
    parser.add_argument("--alpha", type=float, default=0.05, help="Significance level (default: 0.05)")

    args = parser.parse_args()

    try:
        sample_size = calculate_sample_size(args.baseline, args.mde, args.power, args.alpha)
        print(f"Required sample size per variant: {sample_size:,}")
        print(f"Total required sample size (2 variants): {sample_size * 2:,}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
