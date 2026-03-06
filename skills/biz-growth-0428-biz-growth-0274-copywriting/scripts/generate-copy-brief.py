#!/usr/bin/env python3
import sys
import argparse

def generate_brief_template():
    template = """# Copy Brief Summary

## 1. Page Goal
- [Insert primary purpose: e.g., Lead generation, Sales, Sign-up]

## 2. Target Audience
- [Insert target customer profile and their main problem]

## 3. Core Value Proposition
- [Insert the main benefit or transformation offered]

## 4. Primary CTA
- [Insert the exact action you want them to take]

## 5. Traffic / Awareness Context
- [Insert traffic source and awareness level (unaware, problem-aware, etc.)]

## 6. Assumptions
- [List any assumptions made about the audience or offer]

---
**Status**: Please review and confirm this brief before proceeding to the copy drafting phase.
"""
    return template

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a Copy Brief Summary template.")
    parser.add_argument("--out", default="copy-brief.md", help="Output file name")
    args = parser.parse_args()

    with open(args.out, 'w') as f:
        f.write(generate_brief_template())

    print(f"Generated copy brief template at {args.out}")
