#!/usr/bin/env python3
"""
Helper script for Amazon ASIN Lookup Skill.
Usage: python3 amazon-asin-lookup.py <ASIN>
Requires BROWSERACT_API_KEY environment variable.
"""
import os
import sys

def main():
    if 'BROWSERACT_API_KEY' not in os.environ:
        print("Error: BROWSERACT_API_KEY environment variable is not set.", file=sys.stderr)
        print("Please go to https://www.browseract.com/reception/integrations to get your Key.", file=sys.stderr)
        sys.exit(1)

    if len(sys.argv) != 2:
        print("Usage: python3 amazon-asin-lookup.py <ASIN>", file=sys.stderr)
        sys.exit(1)

    asin = sys.argv[1]
    print(f"Executing Amazon ASIN Lookup for ASIN: {asin}")

    # Path to the actual script relative to this skill's root
    # SKILL.md says: python -u ./.cursor/skills/amazon-asin-lookup-api-skill/scripts/amazon_asin_lookup_api.py "ASIN_VALUE"

    script_path = os.path.join(os.path.dirname(__file__), 'amazon_asin_lookup_api.py')

    if not os.path.exists(script_path):
        print(f"Error: Could not find actual script at {script_path}", file=sys.stderr)
        sys.exit(1)

    os.execvp("python3", ["python3", "-u", script_path, asin])

if __name__ == "__main__":
    main()
