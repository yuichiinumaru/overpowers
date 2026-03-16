#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(description="Generate a business case markdown template.")
    parser.add_argument("--project", required=True, help="Name of the project/product")
    parser.add_argument("--sponsor", required=True, help="Executive Sponsor")
    parser.add_argument("--output", help="Output file path (default: stdout)")

    args = parser.parse_args()

    markdown = f"# Business Case: {args.project}\n\n"
    markdown += f"**Sponsor:** {args.sponsor}\n"
    markdown += "**Date:** (YYYY-MM-DD)\n\n"

    markdown += "## 1. Executive Summary\n"
    markdown += "*Brief overview of the problem, proposed solution, and expected ROI.*\n\n"

    markdown += "## 2. Problem Statement\n"
    markdown += "*What specific customer or business problem does this solve?*\n\n"

    markdown += "## 3. Market Opportunity\n"
    markdown += "*TAM, SAM, SOM estimates. Competitor analysis.*\n\n"

    markdown += "## 4. Proposed Solution\n"
    markdown += "*High-level description of the product/feature.*\n\n"

    markdown += "## 5. Financial Projections\n"
    markdown += "*Estimated costs (Capex/Opex) vs Projected Revenue/Savings over 3-5 years.*\n\n"

    markdown += "## 6. Risks & Mitigations\n"
    markdown += "*What could go wrong and how will we prevent it?*\n\n"

    markdown += "## 7. Timeline & Milestones\n"
    markdown += "*Key deliverables and estimated dates.*\n\n"

    if args.output:
        with open(args.output, "w") as f:
            f.write(markdown)
        print(f"Business case template generated at {args.output}")
    else:
        print(markdown)

if __name__ == "__main__":
    main()
