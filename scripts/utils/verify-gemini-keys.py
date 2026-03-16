#!/usr/bin/env python3
# /// script
# dependencies = [
#   "requests",
# ]
# ///

import requests
import sys
import argparse
import os
import re

def verify_key(key):
    """Verifies a Gemini API key by calling the listModels endpoint."""
    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={key}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return True
        return False
    except Exception:
        return False

def main():
    parser = argparse.ArgumentParser(description="Verify Gemini API keys from a file.")
    parser.add_argument("target_file", help="The file containing API keys (comma or line separated).")
    parser.add_argument("-o", "--output", help="Optional output file to save only the valid keys.")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.target_file):
        print(f"Error: File '{args.target_file}' not found.")
        sys.exit(1)
        
    try:
        with open(args.target_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        # Use regex to automatically detect keys (same pattern as extractor)
        pattern = re.compile(r'AIzaSy[a-zA-Z0-9_-]{33}')
        raw_keys = pattern.findall(content)
        
        if not raw_keys:
            # Fallback to splitting if no regex matches found (for backward compatibility)
            content = content.strip()
            if ',' in content:
                raw_keys = [k.strip() for k in content.split(',')]
            else:
                raw_keys = [k.strip() for k in content.splitlines()]
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
        
    # Deduplicate before verifying
    unique_keys = sorted(list(set(raw_keys)))
    total_keys = len(unique_keys)
    
    print(f"Verifying {total_keys} unique keys...")
    
    valid_keys = []
    for i, key in enumerate(unique_keys, 1):
        if verify_key(key):
            valid_keys.append(key)
            status = "VALID"
        else:
            status = "INVALID"
        
        print(f"[{i}/{total_keys}] {key[:10]}...{key[-5:]}: {status}")
        
    if not valid_keys:
        print("No valid Gemini API keys found.")
        return

    result = ",".join(valid_keys)
    
    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(result)
            print(f"\nSuccessfully saved {len(valid_keys)} valid keys to {args.output}")
        except Exception as e:
            print(f"Error writing to output file: {e}")
            sys.exit(1)
    else:
        print(f"\nFound {len(valid_keys)} valid keys:")
        print(result)

if __name__ == "__main__":
    main()
