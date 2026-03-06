#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        print(f"z3_solve executing: {cmd}")
    else:
        print("z3_solve: No command provided")

if __name__ == "__main__":
    main()
