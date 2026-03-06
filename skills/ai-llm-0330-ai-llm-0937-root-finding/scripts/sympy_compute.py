#!/usr/bin/env python3
import sys

def compute(*args):
    print(f"Computing with Sympy: {args}")

if __name__ == "__main__":
    compute(sys.argv[1:])
