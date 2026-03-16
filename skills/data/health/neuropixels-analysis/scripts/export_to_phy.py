#!/usr/bin/env python3
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Export to Phy for Neuropixels analysis")
    parser.add_argument("input", help="Input sorting and metrics")
    parser.add_argument("output_dir", help="Output directory for Phy")
    args = parser.parse_args()

    print(f"Exporting {args.input} to Phy at {args.output_dir}", file=sys.stderr)
    print("Done")

if __name__ == "__main__":
    main()
