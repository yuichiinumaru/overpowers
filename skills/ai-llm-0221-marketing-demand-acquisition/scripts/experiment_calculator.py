import argparse
import math

def calculate_sample_size(baseline_conv_rate, min_detectable_effect, confidence_level=0.95, power=0.8):
    # Simplified sample size calculation for A/B testing
    # z-scores for confidence level
    z_alpha = 1.96  # 95% confidence
    z_beta = 0.84   # 80% power
    
    p = baseline_conv_rate
    delta = min_detectable_effect
    
    n = (z_alpha + z_beta)**2 * (p * (1 - p)) / (delta**2)
    return math.ceil(n)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate A/B test sample size.")
    parser.add_argument("--baseline", type=float, required=True, help="Baseline conversion rate (e.g., 0.05)")
    parser.add_argument("--mde", type=float, required=True, help="Minimum detectable effect (absolute, e.g., 0.01)")
    
    args = parser.parse_args()
    
    sample_size = calculate_sample_size(args.baseline, args.mde)
    print(f"Required sample size per variant: {sample_size}")
