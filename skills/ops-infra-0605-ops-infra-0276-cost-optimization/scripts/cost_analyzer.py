#!/usr/bin/env python3
"""
Cloud Cost Analyzer

This script parses infrastructure files (e.g. Terraform) to look for missing
cost allocation tags.

Usage:
  python3 cost_analyzer.py --path ./terraform
"""

import os
import re
import argparse
import sys

# Simplified logic for demonstration
def scan_terraform(path):
    print(f"Scanning Terraform files in {path} for cost tags...")

    cost_tags = ['Environment', 'Project', 'CostCenter', 'Owner']
    missing_tags = []

    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith('.tf'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r') as f:
                        content = f.read()

                        # Very simple check for resource definitions
                        if 'resource ' in content:
                            if 'tags =' not in content and 'tags {' not in content:
                                print(f"[WARNING] No tags found in {filepath}")
                            else:
                                for tag in cost_tags:
                                    if tag not in content:
                                        missing_tags.append(tag)
                                if missing_tags:
                                    print(f"[WARNING] Missing specific cost tags in {filepath}: {missing_tags}")
                                    missing_tags = []
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Cloud Cost Tagging Analyzer")
    parser.add_argument("--path", required=True, help="Path to infrastructure code")
    args = parser.parse_args()

    if not os.path.exists(args.path):
        print(f"Error: Path {args.path} does not exist.")
        sys.exit(1)

    scan_terraform(args.path)

if __name__ == "__main__":
    main()
