#!/usr/bin/env python3
import re
import sys
import argparse
import os

def extract_keys(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    
    # Pattern: AIzaSy + 33 chars (total 39)
    # Based on .env pattern: AIzaSy[a-zA-Z0-9_-]{33}
    pattern = re.compile(r'AIzaSy[a-zA-Z0-9_-]{33}')
    
    unique_keys = set()
    
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            matches = pattern.findall(content)
            for match in matches:
                unique_keys.add(match)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    
    return sorted(list(unique_keys))

def main():
    parser = argparse.ArgumentParser(description="Scan, clean, and deduplicate Gemini API keys from a file.")
    parser.get_default('target_file')
    parser.add_argument("target_file", help="The file to scan for API keys.")
    parser.add_argument("-o", "--output", help="Optional output file to save the keys (comma separated).")
    
    args = parser.parse_args()
    
    keys = extract_keys(args.target_file)
    
    if not keys:
        print("No Gemini API keys found.")
        return

    result = ",".join(keys)
    
    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(result)
            print(f"Successfully saved {len(keys)} unique keys to {args.output}")
        except Exception as e:
            print(f"Error writing to output file: {e}")
            sys.exit(1)
    else:
        print(f"Found {len(keys)} unique keys:")
        print(result)

if __name__ == "__main__":
    main()
