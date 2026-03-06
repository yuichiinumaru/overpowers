#!/usr/bin/env python3
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Compute metrics for Neuropixels analysis")
    parser.add_argument("input", help="Input sorting results")
    parser.add_argument("output", help="Output metrics file")
    args = parser.parse_args()

    print(f"Computing metrics for {args.input}, outputting to {args.output}", file=sys.stderr)
    print("Done")

if __name__ == "__main__":
    main()
