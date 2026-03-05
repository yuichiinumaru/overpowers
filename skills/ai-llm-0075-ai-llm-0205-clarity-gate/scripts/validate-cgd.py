#!/usr/bin/env python3
import argparse
import yaml
import os
import re

def validate_cgd(file_path):
    print(f"Validating CGD: {file_path}")
    
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return False

    with open(file_path, 'r') as f:
        content = f.read()

    # 1. Check for YAML frontmatter
    if not content.startswith('---'):
        print("Error: Missing YAML frontmatter start (---)")
        return False
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        print("Error: Missing YAML frontmatter end (---)")
        return False
    
    try:
        header = yaml.safe_load(parts[1])
    except yaml.YAMLError as exc:
        print(f"Error: YAML parsing failed: {exc}")
        return False

    # 2. Required fields
    required_fields = [
        'clarity-gate-version', 'processed-date', 'processed-by', 
        'clarity-status', 'hitl-status', 'hitl-pending-count', 
        'points-passed', 'hitl-claims'
    ]
    
    for field in required_fields:
        if field not in header:
            print(f"Error: Missing required field '{field}' in frontmatter")
            return False

    # 3. Check for end marker
    if "<!-- CLARITY_GATE_END -->" not in content:
        print("Error: Missing end marker <!-- CLARITY_GATE_END -->")
        return False

    # 4. Check status line after end marker
    status_pattern = r"Clarity Gate: (CLEAR|UNCLEAR) \| (PENDING|REVIEWED|REVIEWED_WITH_EXCEPTIONS)"
    if not re.search(status_pattern, content):
        print("Error: Missing or invalid status line after end marker")
        return False

    print("✅ CGD structure is valid.")
    return True

def main():
    parser = argparse.ArgumentParser(description='Validate a Clarity-Gated Document (CGD).')
    parser.add_argument('file', help='Path to the CGD file')

    args = parser.parse_args()
    validate_cgd(args.file)

if __name__ == "__main__":
    main()
