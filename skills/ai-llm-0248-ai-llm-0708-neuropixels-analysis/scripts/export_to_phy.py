#!/usr/bin/env python3
import sys
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("analyzer")
    parser.add_argument("--output")
    args = parser.parse_args()
    print(f"Exporting to phy: {args.analyzer}")

if __name__ == "__main__":
    main()
