#!/usr/bin/env python3
import argparse
import itertools
import random
import json

def main():
    parser = argparse.ArgumentParser(description="Generate synthetic tuple combinations from dimensions")
    parser.add_argument("dimensions_file", help="JSON file containing dimensions and their values")
    parser.add_argument("--num", type=int, default=20, help="Number of tuples to generate")
    args = parser.parse_args()

    with open(args.dimensions_file, 'r') as f:
        dims = json.load(f)

    # dims should be like: {"Feature": ["Search", "Schedule"], "Persona": ["Buyer", "Seller"]}
    keys = list(dims.keys())
    values_lists = [dims[k] for k in keys]

    all_combinations = list(itertools.product(*values_lists))

    if args.num > len(all_combinations):
        print(f"Requested {args.num} tuples, but only {len(all_combinations)} combinations exist. Returning all.")
        sampled = all_combinations
    else:
        sampled = random.sample(all_combinations, args.num)

    print("Generated Tuples:")
    for i, t in enumerate(sampled, 1):
        tuple_str = ", ".join([f"{keys[j]}: {t[j]}" for j in range(len(keys))])
        print(f"{i}. ({tuple_str})")

if __name__ == "__main__":
    main()
