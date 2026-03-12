#!/usr/bin/env python3
"""
Check if design tokens follow naming conventions (kebab-case).
"""
import json
import os
import re
import sys

def is_kebab_case(s):
    return re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', s) is not None

def check_dict(d, path=""):
    errors = []
    for k, v in d.items():
        current_path = f"{path}.{k}" if path else k
        if not is_kebab_case(k) and k != "value": # 'value' is a Style Dictionary keyword
             errors.append(f"Invalid name: '{k}' at '{current_path}' (should be kebab-case)")
        
        if isinstance(v, dict):
            errors.extend(check_dict(v, current_path))
    return errors

def main():
    token_dir = "tokens"
    if not os.path.exists(token_dir):
        print(f"Error: Directory '{token_dir}' not found.")
        sys.exit(1)

    all_errors = []
    for root, _, files in os.walk(token_dir):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r') as f:
                        data = json.load(f)
                        errors = check_dict(data)
                        if errors:
                            print(f"Errors in {file_path}:")
                            for err in errors:
                                print(f"  - {err}")
                            all_errors.extend(errors)
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    if all_errors:
        print(f"\nFound {len(all_errors)} naming convention violations.")
        sys.exit(1)
    else:
        print("All tokens follow kebab-case conventions.")

if __name__ == "__main__":
    main()
