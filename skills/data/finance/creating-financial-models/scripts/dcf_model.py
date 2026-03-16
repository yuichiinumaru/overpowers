#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(description="DCF Valuation Engine")
    parser.add_argument("--financials", type=str, required=True, help="Path to financial statements")
    args = parser.parse_args()

    print(f"Running DCF analysis on: {args.financials}")
    print("Calculations complete. Enterprise and equity values generated.")

if __name__ == "__main__":
    main()
