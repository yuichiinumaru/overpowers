#!/usr/bin/env python3
import sys
import argparse

def generate_disclaimer():
    return """
================================================================================
LEGAL ADVISOR DISCLAIMER
================================================================================

This document or template is provided for informational purposes only.
Consult with a qualified attorney for legal advice specific to your situation.
It does not constitute a formal legal opinion or create an attorney-client
relationship.

================================================================================
"""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate the standard legal advisor disclaimer.")
    parser.add_argument("--out", help="Output file (optional)")

    args = parser.parse_args()

    disclaimer = generate_disclaimer()

    if args.out:
        with open(args.out, 'w') as f:
            f.write(disclaimer)
        print(f"Generated legal disclaimer at {args.out}")
    else:
        print(disclaimer)
