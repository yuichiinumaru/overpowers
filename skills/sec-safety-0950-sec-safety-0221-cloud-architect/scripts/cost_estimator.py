import sys

def estimate_aws_costs(resources):
    # Very rough placeholder for estimation logic
    prices = {
        "t3.medium": 0.0416, # per hour
        "m5.large": 0.096,
        "lambda_1m_invocations": 0.20,
        "s3_gb_month": 0.023
    }
    
    total_monthly = 0
    for res, qty in resources.items():
        if res in prices:
            if "t3" in res or "m5" in res:
                total_monthly += prices[res] * 24 * 30 * qty
            else:
                total_monthly += prices[res] * qty
                
    return total_monthly

if __name__ == "__main__":
    # Example usage: python cost_estimator.py t3.medium:2 m5.large:1
    resources = {}
    for arg in sys.argv[1:]:
        name, qty = arg.split(':')
        resources[name] = int(qty)
        
    cost = estimate_aws_costs(resources)
    print(f"Estimated Monthly AWS Cost: ${cost:.2f}")
