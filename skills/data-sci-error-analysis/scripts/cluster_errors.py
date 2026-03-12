#!/usr/bin/env python3
import json
import argparse
import sys
from collections import defaultdict

def main():
    parser = argparse.ArgumentParser(description="A simple script to group error notes for error-analysis")
    parser.add_argument("input_file", help="Path to input JSON file containing error annotations")
    parser.add_argument("--output", help="Path to output JSON file for grouped categories")
    args = parser.parse_args()

    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading input file: {e}", file=sys.stderr)
        sys.exit(1)

    # Expecting data format: [{"trace_id": "1", "note": "...", "fail": true}]
    failures = [item for item in data if item.get('fail') or item.get('status') == 'fail']

    print(f"Found {len(failures)} failed traces.")
    print("Instructions: Please review these annotations and group them into 5-10 distinct categories.")
    print("You can use an LLM for initial clustering by passing this list.\n")

    for i, item in enumerate(failures, 1):
        note = item.get('note') or item.get('what_went_wrong') or 'No note provided'
        print(f"[{item.get('trace_id', i)}] {note}")

    print("\nNext steps:")
    print("1. Group similar notes.")
    print("2. Assign a clear name and one-sentence definition to each category.")

if __name__ == "__main__":
    main()
