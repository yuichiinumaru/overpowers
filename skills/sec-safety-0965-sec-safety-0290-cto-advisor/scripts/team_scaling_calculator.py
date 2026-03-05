import sys

def calculate_ratios(engineers):
    return {
        "Managers": round(engineers / 8, 1),
        "Seniors": round(engineers * 0.3),
        "Mids": round(engineers * 0.4),
        "Juniors": round(engineers * 0.2),
        "Product Managers": round(engineers / 10, 1),
        "QA Engineers": round(engineers * 0.15, 1)
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python team_scaling_calculator.py <number_of_engineers>")
        sys.exit(1)
        
    try:
        num = int(sys.argv[1])
        ratios = calculate_ratios(num)
        print(f"--- Recommended Structure for {num} Engineers ---")
        for role, count in ratios.items():
            print(f"{role}: {count}")
    except ValueError:
        print("Please provide a valid number.")
