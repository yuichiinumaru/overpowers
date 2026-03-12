#!/usr/bin/env python3
"""
Helper script for Amazon Product API Skill.
Usage: python3 amazon-product-api.py --keywords <keywords> [--brand <brand>] [--pages <pages>] [--lang <lang>]
Requires BROWSERACT_API_KEY environment variable.
"""
import os
import sys
import argparse

def main():
    if 'BROWSERACT_API_KEY' not in os.environ:
        print("Error: BROWSERACT_API_KEY environment variable is not set.", file=sys.stderr)
        print("Please go to https://www.browseract.com/reception/integrations to get your Key.", file=sys.stderr)
        sys.exit(1)

    # Find the actual script path
    script_path = os.path.join(os.path.dirname(__file__), 'amazon_product_api.py')

    if not os.path.exists(script_path):
        print(f"Error: Could not find actual script at {script_path}", file=sys.stderr)
        sys.exit(1)

    # Forward all arguments to the actual script
    args = ["python3", "-u", script_path] + sys.argv[1:]
    os.execvp("python3", args)

if __name__ == "__main__":
    main()
