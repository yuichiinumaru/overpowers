import json
import csv
import random
import argparse
import sys
from pathlib import Path

def load_data(filepath):
    path = Path(filepath)
    if path.suffix == '.json':
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    elif path.suffix == '.csv':
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)
    else:
        print(f"Unsupported file format: {path.suffix}", file=sys.stderr)
        sys.exit(1)

def save_data(data, filepath):
    path = Path(filepath)
    if path.suffix == '.json':
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
    elif path.suffix == '.csv':
        if not data:
            return
        keys = data[0].keys()
        with open(path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
    print(f"Saved {len(data)} traces to {filepath}")

def main():
    parser = argparse.ArgumentParser(description="Sample traces for the review interface")
    parser.add_argument("input_file", help="Path to the input JSON or CSV file")
    parser.add_argument("output_file", help="Path to save the sampled data (JSON or CSV)")
    parser.add_argument("-n", "--number", type=int, default=100, help="Number of traces to sample")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for reproducibility")

    args = parser.parse_args()

    data = load_data(args.input_file)

    if len(data) <= args.number:
        print(f"Input data has {len(data)} items, which is less than or equal to requested sample size {args.number}. Returning all items.")
        sampled_data = data
    else:
        random.seed(args.seed)
        sampled_data = random.sample(data, args.number)

    save_data(sampled_data, args.output_file)

if __name__ == "__main__":
    main()
