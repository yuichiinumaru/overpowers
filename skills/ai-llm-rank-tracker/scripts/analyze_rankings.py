import json
import argparse
import sys

def analyze_rankings(data_file):
    try:
        with open(data_file, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading data: {e}")
        return

    # Assuming data is a list of dicts with 'keyword', 'old_rank', 'new_rank'
    if not isinstance(data, list):
        print("Data format should be a list of keyword ranking dicts.")
        return

    improvements = []
    declines = []
    stable = []

    for item in data:
        kw = item.get('keyword', 'unknown')
        old_r = item.get('old_rank')
        new_r = item.get('new_rank')

        if old_r is None or new_r is None:
            continue

        change = old_r - new_r

        if change > 3:
            improvements.append((kw, old_r, new_r, change))
        elif change < -3:
            declines.append((kw, old_r, new_r, change))
        else:
            stable.append((kw, old_r, new_r, change))

    print("### Biggest Improvements 📈")
    for kw, o, n, c in sorted(improvements, key=lambda x: x[3], reverse=True):
        print(f"| {kw} | {o} | {n} | +{c} |")

    print("\n### Biggest Declines 📉")
    for kw, o, n, c in sorted(declines, key=lambda x: x[3]):
        print(f"| {kw} | {o} | {n} | {c} |")

    print(f"\n### Stable Keywords")
    print(f"{len(stable)} keywords remained within ±3 positions (stable)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze keyword ranking changes")
    parser.add_argument("data_file", help="Path to JSON file containing ranking data")
    args = parser.parse_args()

    analyze_rankings(args.data_file)
