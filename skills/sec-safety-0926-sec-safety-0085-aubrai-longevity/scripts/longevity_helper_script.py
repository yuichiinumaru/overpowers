#!/usr/bin/env python3
import sys

def analyze_longevity(target):
    print(f"Analyzing longevity data for: {target}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        analyze_longevity(sys.argv[1])
    else:
        print("Usage: ./longevity_helper.py <target>")
