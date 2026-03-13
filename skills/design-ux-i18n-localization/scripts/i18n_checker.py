#!/usr/bin/env python3
import sys
import os
import re

def check_i18n(project_path):
    if not os.path.exists(project_path):
        print(f"Error: {project_path} not found.")
        return

    # Pattern for hardcoded strings in JSX/TSX
    pattern = re.compile(r'>([^<{]+)<')

    print(f"--- Checking Hardcoded Strings in: {project_path} ---")
    for root, dirs, files in os.walk(project_path):
        for file in files:
            if file.endswith(('.tsx', '.jsx')):
                path = os.path.join(root, file)
                with open(path, "r") as f:
                    content = f.read()
                    matches = pattern.findall(content)
                    for match in matches:
                        clean = match.strip()
                        if clean and not clean.isnumeric():
                            print(f"[!] Potential hardcoded string in {path}: '{clean}'")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: i18n_checker.py <project_path>")
        sys.exit(1)
    
    check_i18n(sys.argv[1])
