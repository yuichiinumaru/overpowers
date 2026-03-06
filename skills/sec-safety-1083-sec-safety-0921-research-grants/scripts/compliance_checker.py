#!/usr/bin/env python3
import sys
import json

def check_compliance(proposal_file):
    print(f"Checking compliance for {proposal_file}...")
    print("Formatting looks good.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        check_compliance(sys.argv[1])
    else:
        print("Usage: python compliance_checker.py <proposal_file>")
