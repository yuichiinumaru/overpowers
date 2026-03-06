#!/usr/bin/env python3
import sys

def run_prep(component):
    print(f"Preparing audit checklists and prep material for: {component}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        run_prep(sys.argv[1])
    else:
        print("Usage: ./audit_prep.py <component>")
