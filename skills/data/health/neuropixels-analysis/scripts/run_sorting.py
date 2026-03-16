#!/usr/bin/env python3
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Run spike sorting for Neuropixels analysis")
    parser.add_argument("input", help="Input preprocessed file")
    parser.add_argument("output", help="Output sorting results")
    args = parser.parse_args()

    print(f"Running sorting on {args.input}, outputting to {args.output}", file=sys.stderr)
    print("Done")

if __name__ == "__main__":
    main()
