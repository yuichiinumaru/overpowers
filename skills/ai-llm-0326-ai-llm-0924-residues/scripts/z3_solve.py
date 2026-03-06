#!/usr/bin/env python3
import sys

def solve(*args):
    print(f"Solving with Z3: {args}")

if __name__ == "__main__":
    solve(sys.argv[1:])
