#!/usr/bin/env python3
"""
Verify Kubb documentation conventions.
"""
import sys
import re
import argparse

def check_file(file_path):
    issues = []
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            lines = content.split('\n')
    except Exception as e:
        return [f"Error reading file: {e}"]

    # Check for alert components [!NOTE], [!TIP], etc.
    # Pattern: > [!TAG]
    valid_alerts = ["NOTE", "TIP", "WARNING", "IMPORTANT"]
    alerts = re.findall(r'> \[!(.*?)\]', content)
    for alert in alerts:
        if alert not in valid_alerts:
            issues.append(f"Invalid alert tag: [!{alert}]. Use one of {valid_alerts}")

    # Check for H1 backticks
    if lines and lines[0].startswith('# '):
        if '`' in lines[0]:
            issues.append("H1 heading should not contain backticks.")

    # Check for kebab-case filename
    file_name = file_path.split('/')[-1]
    if not re.match(r'^[a-z0-9-]+(\.md)?$', file_name):
        issues.append(f"Filename '{file_name}' should use kebab-case.")

    # Check for code-group completion
    if "::: code-group" in content:
        if content.count("::: code-group") != content.count(":::"):
            # This is a bit naive but checks for matching triplets
            issues.append("::: code-group might be missing closing :::")

    return issues

def main():
    parser = argparse.ArgumentParser(description="Verify Kubb docs.")
    parser.add_argument("files", nargs="+", help="Files to verify")
    
    args = parser.parse_args()
    
    total_issues = 0
    for file_path in args.files:
        print(f"Verifying {file_path}...")
        issues = check_file(file_path)
        for issue in issues:
            print(f"  [!] {issue}")
        total_issues += len(issues)
        
    if total_issues > 0:
        print(f"\nFound {total_issues} issues.")
        sys.exit(1)
    else:
        print("\nNo issues found.")

if __name__ == "__main__":
    main()
