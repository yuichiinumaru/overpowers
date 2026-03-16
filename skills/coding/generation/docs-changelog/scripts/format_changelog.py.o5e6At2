#!/usr/bin/env python3
"""
Format raw changelog data for Gemini CLI.
"""
import sys
import re
import argparse

def format_entry(line, repo_url):
    # Match "description by @author in #pr_number"
    match = re.search(r'^(.*) by (@\w+) in #(\d+)$', line.strip())
    if not match:
        return line.strip()
    
    desc, author, pr_num = match.groups()
    
    # Skip robot
    if author == "@gemini-cli-robot":
        return None
        
    return f"- {desc} by {author} in [#{pr_num}]({repo_url}/pull/{pr_num})"

def main():
    parser = argparse.ArgumentParser(description="Format raw changelog data.")
    parser.add_argument("input_file", help="File with raw PR data")
    parser.add_argument("--repo", default="https://github.com/google-gemini/gemini-cli", help="Base repo URL")
    
    args = parser.parse_args()
    
    try:
        with open(args.input_file, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File {args.input_file} not found.")
        sys.exit(1)

    formatted_lines = []
    for line in lines:
        formatted = format_entry(line, args.repo)
        if formatted:
            formatted_lines.append(formatted)
            
    print("### What's Changed")
    for line in formatted_lines:
        # Simple line wrapping logic could be added here if needed
        print(line)

if __name__ == "__main__":
    main()
