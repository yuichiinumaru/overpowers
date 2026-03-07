#!/usr/bin/env python3
"""
geo_checker.py
A stub script for Generative Engine Optimization (GEO) audit.
Reads a markdown or HTML file and checks for AI citation readiness.
"""
import sys
import os
import re

def check_geo_elements(filepath):
    if not os.path.isfile(filepath):
        print(f"Error: File '{filepath}' does not exist.")
        sys.exit(1)

    print(f"Running GEO Audit on '{filepath}'...")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Basic heuristic checks based on GEO Fundamentals
    has_summary = bool(re.search(r'(TL;DR|Summary|Key Takeaways)', content, re.IGNORECASE))
    has_quotes = bool(re.search(r'("> |")+', content))
    has_faq = bool(re.search(r'(FAQ|Frequently Asked Questions)', content, re.IGNORECASE))
    has_timestamp = bool(re.search(r'(Last updated|Date|Published)', content, re.IGNORECASE))

    print("\n=== Checklist Status ===")
    print(f"[ {'x' if has_summary else ' '} ] Summary/TL;DR at top")
    print(f"[ {'x' if has_quotes else ' '} ] Expert quotes present")
    print(f"[ {'x' if has_faq else ' '} ] FAQ section present")
    print(f"[ {'x' if has_timestamp else ' '} ] 'Last updated' timestamp")

    print("\nNote: This is a basic heuristic check. For full compliance, verify:")
    print("- Article and Person Schema")
    print("- Original data with sources")
    print("- Clear definitions")
    print("- Author credentials")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python geo_checker.py <content_file_path>")
        sys.exit(1)

    check_geo_elements(sys.argv[1])
