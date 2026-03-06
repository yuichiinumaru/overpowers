#!/usr/bin/env python3
import sys
import argparse

def calculate_sample_size(baseline_conversion_rate, mde, power=0.8, significance=0.05):
    """
    Calculates the required sample size for an A/B test.
    This is a simplified estimation script.
    """
    import math
    from scipy.stats import norm

    # Z-scores
    z_alpha = norm.ppf(1 - significance / 2)
    z_beta = norm.ppf(power)

    # Rates
    p1 = baseline_conversion_rate
    p2 = baseline_conversion_rate * (1 + mde)

    # Pooled variance
    p_pooled = (p1 + p2) / 2

    # Sample size per group
    n = ((z_alpha * math.sqrt(2 * p_pooled * (1 - p_pooled)) +
          z_beta * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2) / ((p2 - p1) ** 2)

    return math.ceil(n)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Estimate A/B test sample size.")
    parser.add_argument("--baseline", type=float, required=True, help="Baseline conversion rate (e.g., 0.05 for 5%)")
    parser.add_argument("--mde", type=float, required=True, help="Minimum Detectable Effect (relative, e.g., 0.10 for 10% lift)")
    parser.add_argument("--power", type=float, default=0.8, help="Statistical power (default: 0.8)")
    parser.add_argument("--significance", type=float, default=0.05, help="Significance level (default: 0.05)")

    args = parser.parse_args()

    try:
        # Check if scipy is installed, if not provide a simpler approximation or instruction
        import scipy
        n_per_variant = calculate_sample_size(args.baseline, args.mde, args.power, args.significance)
        print(f"Estimated sample size per variant: {n_per_variant}")
        print(f"Total estimated sample size (A/B): {n_per_variant * 2}")
    except ImportError:
        print("Error: The 'scipy' library is required for accurate calculation.")
        print("Please install it using: pip install scipy")
        print("\nAlternatively, here is a rough approximation rule of thumb:")
        print("n = 16 * p * (1-p) / (delta^2)")
        p = args.baseline
        delta = args.baseline * args.mde
        rough_n = int(16 * p * (1 - p) / (delta ** 2))
        print(f"Rough estimated sample size per variant: {rough_n}")
        print(f"Total rough estimated sample size (A/B): {rough_n * 2}")
