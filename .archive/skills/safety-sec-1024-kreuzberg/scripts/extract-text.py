#!/usr/bin/env python3
import sys
import os

try:
    import kreuzberg
except ImportError:
    print("Error: kreuzberg package not found.")
    print("Install it with: pip install kreuzberg")
    sys.exit(1)

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <document.pdf|docx|etc>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    print(f"Extracting content from '{file_path}' using kreuzberg...")

    try:
        from kreuzberg import extract_file

        result = extract_file(file_path)

        print("\n--- Extracted Text Preview ---")
        if len(result.content) > 1000:
            print(result.content[:1000] + "...\n[TRUNCATED]")
        else:
            print(result.content)

        print("\n--- Metadata ---")
        print(result.metadata)

    except Exception as e:
        print(f"Error during extraction: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
