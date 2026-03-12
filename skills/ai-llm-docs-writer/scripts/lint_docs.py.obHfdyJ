#!/usr/bin/env python3
"""
Basic style linter for Gemini CLI documentation.
"""
import sys
import re
import argparse

PROHIBITED_WORDS = ["please", "foo", "bar"]
LATIN_ABBREVS = {"e.g.": "for example", "i.e.": "that is"}

def check_file(file_path):
    issues = []
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
    except Exception as e:
        return [f"Error reading file: {e}"]

    for i, line in enumerate(lines):
        line_num = i + 1
        
        # Check text wrap (80 chars)
        if len(line) > 81 and not ("http" in line or "|" in line):
            issues.append(f"L{line_num}: Line exceeds 80 characters.")

        # Check prohibited words
        for word in PROHIBITED_WORDS:
            if re.search(r'\b' + word + r'\b', line, re.IGNORECASE):
                issues.append(f"L{line_num}: Prohibited word found: '{word}'")

        # Check Latin abbreviations
        for abbrev in LATIN_ABBREVS:
            if abbrev in line:
                issues.append(f"L{line_num}: Use '{LATIN_ABBREVS[abbrev]}' instead of '{abbrev}'")

        # Check naming
        if "the Gemini CLI" in line:
            issues.append(f"L{line_num}: Use 'Gemini CLI' instead of 'the Gemini CLI'")

    return issues

def main():
    parser = argparse.ArgumentParser(description="Lint documentation style.")
    parser.add_argument("files", nargs="+", help="Files to lint")
    
    args = parser.parse_args()
    
    total_issues = 0
    for file_path in args.files:
        print(f"Linting {file_path}...")
        issues = check_file(file_path)
        for issue in issues:
            print(f"  {issue}")
        total_issues += len(issues)
        
    if total_issues > 0:
        print(f"\nFound {total_issues} style issues.")
        sys.exit(1)
    else:
        print("\nNo style issues found.")

if __name__ == "__main__":
    main()
