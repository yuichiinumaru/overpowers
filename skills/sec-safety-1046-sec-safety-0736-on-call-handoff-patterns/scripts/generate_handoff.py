#!/usr/bin/env python3
"""
Generate an on-call handoff template based on the patterns described in SKILL.md.
"""
import argparse
import datetime
import os

TEMPLATE = """# On-Call Handoff: {date}

## Shift Summary
*   **Shift:** [e.g., Morning, Swing, Night]
*   **Primary:** {primary}
*   **Secondary:** [Secondary Name]

## Active Incidents
*   [List any ongoing Sev 1/2/3 incidents, links to tracking, and current status]

## Ongoing Investigations
*   [List non-incident investigations, PRs to review, or follow-ups]

## Recent Changes & Deployments
*   [List major config changes, deployments, or feature flags toggled during the shift]

## Notes for Next Shift
*   [Any specific things the next shift needs to keep an eye on, follow up with, or be aware of]
"""

def main():
    parser = argparse.ArgumentParser(description="Generate an on-call handoff template")
    parser.add_argument("--primary", type=str, required=True, help="Name of the primary on-call")
    args = parser.parse_args()

    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    handoff_content = TEMPLATE.format(date=date_str, primary=args.primary)

    output_filename = f"handoff_{date_str}.md"
    with open(output_filename, "w") as f:
        f.write(handoff_content)

    print(f"Handoff template generated: {output_filename}")

if __name__ == "__main__":
    main()
