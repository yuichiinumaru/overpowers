#!/usr/bin/env python3
import os
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="Generate a fact-checking markdown template.")
    parser.add_argument("claim", help="The claim to fact-check")
    parser.add_argument("--output", "-o", default="fact_check.md", help="Output file name")
    args = parser.parse_args()

    template = f"""## Claim
"{args.claim}"

## Verdict: [✅ TRUE | ⚠️ MOSTLY TRUE | 🔶 MIXED | ❌ MOSTLY FALSE | 🚫 FALSE | ❓ UNVERIFIABLE]

## Analysis
[Explanation of why this rating]

**Evidence:**
- [Key supporting or refuting evidence]
- [Secondary evidence]

**Context:**
- [Important context or nuance]
- [Why this matters]

**Source Quality:**
- [Evaluation of sources used]

## Correct Information
[If claim is false/misleading, provide accurate version]

## Sources
[1] [Source name and description]
"""

    with open(args.output, "w") as f:
        f.write(template)

    print(f"Generated fact-checking template for '{args.claim}' in {args.output}")

if __name__ == "__main__":
    main()
