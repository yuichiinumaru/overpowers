#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(description="Sensitivity Testing Framework")
    parser.add_argument("--base-model", type=str, required=True, help="Path to base case model")
    args = parser.parse_args()

    print(f"Running sensitivity analysis on: {args.base_model}")
    print("Generating tornado charts and value ranges.")

if __name__ == "__main__":
    main()
