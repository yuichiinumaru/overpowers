import argparse

def calculate_cac(spend, customers):
    if customers == 0:
        return 0
    return spend / customers

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate Customer Acquisition Cost (CAC).")
    parser.add_argument("--spend", type=float, required=True, help="Total marketing spend")
    parser.add_argument("--customers", type=int, required=True, help="Number of customers acquired")
    
    args = parser.parse_args()
    
    cac = calculate_cac(args.spend, args.customers)
    print(f"CAC: {cac:.2f}")
