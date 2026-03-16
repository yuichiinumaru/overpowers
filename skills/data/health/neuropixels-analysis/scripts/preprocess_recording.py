#!/usr/bin/env python3
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Preprocess recording for Neuropixels analysis")
    parser.add_argument("input", help="Input recording file")
    parser.add_argument("output", help="Output preprocessed file")
    args = parser.parse_args()

    print(f"Preprocessing {args.input} to {args.output}", file=sys.stderr)
    print("Done")

if __name__ == "__main__":
    main()
