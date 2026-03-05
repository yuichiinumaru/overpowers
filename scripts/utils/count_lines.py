#!/usr/bin/env python3
import sys
import os

def count_lines(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            count = sum(1 for line in f)
        return count
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 count_lines.py <file_path>")
        sys.exit(1)
    
    path = sys.argv[1]
    line_count = count_lines(path)
    print(f"File: {path}")
    print(f"Line count: {line_count}")
