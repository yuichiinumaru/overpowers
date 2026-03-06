#!/usr/bin/env python3
import sys

def analyze_cost(region):
    print(f"Analyzing AWS Cost Operations in region: {region}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        analyze_cost(sys.argv[1])
    else:
        print("Usage: ./aws_cost_helper.py <region>")
