#!/usr/bin/env python3
"""
NSFC Justification Writer Script
"""
import sys

def main():
    if len(sys.argv) > 1:
        command = sys.argv[1]
        print(f"Executing command: {command}")
    else:
        print("No command provided")

if __name__ == "__main__":
    main()
