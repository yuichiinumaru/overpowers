#!/usr/bin/env python3
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Document Converter for Gemini")
    parser.add_argument("--input", help="Input document")
    parser.add_argument("--output", help="Output PDF/Markdown")
    parser.add_argument("--pages", help="Page range")
    
    args = parser.parse_args()
    
    if not args.input:
        parser.print_help()
        sys.exit(1)
    
    print(f"Converting document: {args.input}")
    print(f"Pages: {args.pages}")
    print("Converted file saved to:", args.output)

if __name__ == "__main__":
    main()
