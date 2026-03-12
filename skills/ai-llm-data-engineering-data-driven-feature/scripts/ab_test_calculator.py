import math
from scipy import stats
import argparse

def calculate_sample_size(baseline_conv_rate, mde, confidence_level=0.95, power=0.8):
    """
    Calculate sample size per group for an A/B test.
    
    baseline_conv_rate: current conversion rate (e.g., 0.1 for 10%)
    mde: minimum detectable effect (e.g., 0.02 for 2% absolute increase)
    confidence_level: significance level (default 0.95)
    power: statistical power (default 0.8)
    """
    alpha = 1 - confidence_level
    beta = 1 - power
    
    z_alpha = stats.norm.ppf(1 - alpha/2)
    z_beta = stats.norm.ppf(1 - beta)
    
    p1 = baseline_conv_rate
    p2 = baseline_conv_rate + mde
    p_avg = (p1 + p2) / 2
    
    n = (z_alpha * math.sqrt(2 * p_avg * (1 - p_avg)) + z_beta * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2)))**2 / (mde**2)
    
    return math.ceil(n)

def calculate_statistical_significance(control_conversions, control_size, treatment_conversions, treatment_size):
    """
    Calculate p-value for A/B test results.
    """
    p1 = control_conversions / control_size
    p2 = treatment_conversions / treatment_size
    p_pool = (control_conversions + treatment_conversions) / (control_size + treatment_size)
    
    z_score = (p2 - p1) / math.sqrt(p_pool * (1 - p_pool) * (1/control_size + 1/treatment_size))
    p_value = 1 - stats.norm.cdf(abs(z_score))
    
    return p_value, z_score

def main():
    parser = argparse.ArgumentParser(description="A/B Testing Helper Calculator")
    subparsers = parser.add_subparsers(dest="command")
    
    # Sample Size Parser
    sample_parser = subparsers.add_parser("sample_size", help="Calculate required sample size")
    sample_parser.add_argument("--baseline", type=float, required=True, help="Baseline conversion rate (0.0 to 1.0)")
    sample_parser.add_argument("--mde", type=float, required=True, help="Minimum Detectable Effect (absolute)")
    sample_parser.add_argument("--confidence", type=float, default=0.95, help="Confidence level (default: 0.95)")
    sample_parser.add_argument("--power", type=float, default=0.8, help="Statistical power (default: 0.8)")
    
    # Significance Parser
    sig_parser = subparsers.add_parser("significance", help="Calculate statistical significance")
    sig_parser.add_argument("--c_conv", type=int, required=True, help="Control conversions")
    sig_parser.add_argument("--c_size", type=int, required=True, help="Control total size")
    sig_parser.add_argument("--t_conv", type=int, required=True, help="Treatment conversions")
    sig_parser.add_argument("--t_size", type=int, required=True, help="Treatment total size")
    
    args = parser.parse_args()
    
    if args.command == "sample_size":
        n = calculate_sample_size(args.baseline, args.mde, args.confidence, args.power)
        print(f"Required sample size per group: {n}")
        print(f"Total sample size needed: {n * 2}")
    elif args.command == "significance":
        p_val, z = calculate_statistical_significance(args.c_conv, args.c_size, args.t_conv, args.t_size)
        print(f"P-value: {p_val:.4f}")
        print(f"Z-score: {z:.4f}")
        if p_val < 0.05:
            print("Status: STATISTICALLY SIGNIFICANT (p < 0.05)")
        else:
            print("Status: NOT STATISTICALLY SIGNIFICANT")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
