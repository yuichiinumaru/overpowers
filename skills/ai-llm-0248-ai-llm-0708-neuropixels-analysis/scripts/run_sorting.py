#!/usr/bin/env python3
import sys
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir")
    parser.add_argument("--sorter")
    parser.add_argument("--output")
    args = parser.parse_args()
    print(f"Running sorting on {args.input_dir} using {args.sorter}")

if __name__ == "__main__":
    main()
