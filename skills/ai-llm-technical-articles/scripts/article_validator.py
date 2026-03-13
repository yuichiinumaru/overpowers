#!/usr/bin/env python3
import sys
import os
import re

def validate_article(file_path):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    with open(file_path, "r") as f:
        content = f.read()
        lines = content.split('\n')

    print(f"--- Validating Article: {file_path} ---")
    
    # 1. Title Principle
    header = lines[0] if lines else ""
    if not header.startswith("# "):
        print("[!] Missing H1 header.")
    else:
        title = header[2:]
        if len(title.split()) < 3:
            print("[?] Title might be too short. Remember: Title should BE the takeaway.")

    # 2. Length (30-80 lines)
    line_count = len(lines)
    if line_count < 30:
        print(f"[!] Article too short ({line_count} lines). Target: 30-80.")
    elif line_count > 80:
        print(f"[!] Article too long ({line_count} lines). Target: 30-80.")
    else:
        print(f"[OK] Length: {line_count} lines.")

    # 3. Bold constraint
    bold_count = len(re.findall(r"\*\*.*?\*\*", content))
    if bold_count > 1:
        print(f"[!] Found {bold_count} bold items. Reserve bold for TL;DR only.")

    # 4. Code blocks
    if "```" not in content:
        print("[!] No code blocks found. Code speaks louder than prose.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: article_validator.py <article.md>")
        sys.exit(1)
    
    validate_article(sys.argv[1])
