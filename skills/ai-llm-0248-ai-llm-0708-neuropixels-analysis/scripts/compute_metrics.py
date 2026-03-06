#!/usr/bin/env python3
import sys
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("sorting_dir")
    parser.add_argument("preprocessed_dir")
    parser.add_argument("--output")
    parser.add_argument("--curation")
    args = parser.parse_args()
    print(f"Computing metrics for {args.sorting_dir}")

if __name__ == "__main__":
    main()
