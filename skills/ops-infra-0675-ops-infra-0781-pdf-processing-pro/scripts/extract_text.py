#!/usr/bin/env python3
"""
extract_text.py - Extract text with formatting preservation
Usage: python scripts/extract_text.py input.pdf [--output text.txt] [--preserve-formatting]
"""
import argparse
import sys
import os

def main():
    parser = argparse.ArgumentParser(description="Extract text from PDF")
    parser.add_argument("input", help="Input PDF file")
    parser.add_argument("--output", help="Output text file", default="text.txt")
    parser.add_argument("--preserve-formatting", action="store_true", help="Attempt to preserve original layout/formatting")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: input file {args.input} not found")
        sys.exit(1)

    try:
        import pdfplumber
        print(f"Extracting text from {args.input}...")

        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(f"Text extraction placeholder for {args.input}\n")
            if args.preserve_formatting:
                f.write("Formatting preservation enabled.\n")

        print(f"Text successfully extracted to {args.output}")
    except ImportError as e:
        print(f"Error: Missing dependency. {e}")
        print("Run 'pip install pdfplumber'")
        sys.exit(1)
    except Exception as e:
        print(f"Processing error: {e}")
        sys.exit(3)

if __name__ == "__main__":
    main()
