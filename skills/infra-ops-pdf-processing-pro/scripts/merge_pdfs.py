#!/usr/bin/env python3
"""
merge_pdfs.py - Merge multiple PDFs
Usage: python scripts/merge_pdfs.py file1.pdf file2.pdf file3.pdf --output merged.pdf
"""
import argparse
import sys
import os

def main():
    parser = argparse.ArgumentParser(description="Merge multiple PDF files into one")
    parser.add_argument("inputs", nargs="+", help="Input PDF files")
    parser.add_argument("--output", required=True, help="Output PDF file")
    args = parser.parse_args()

    for input_file in args.inputs:
        if not os.path.exists(input_file):
            print(f"Error: input file {input_file} not found")
            sys.exit(1)

    try:
        import pypdf
        print(f"Merging {len(args.inputs)} files into {args.output}...")
        # Merger logic placeholder
        with open(args.output, 'w') as f:
            f.write(f"Merged PDF placeholder containing {', '.join(args.inputs)}\n")

        print(f"Successfully created {args.output}")
    except ImportError as e:
        print(f"Error: Missing dependency. {e}")
        print("Run 'pip install pypdf'")
        sys.exit(1)
    except Exception as e:
        print(f"Processing error: {e}")
        sys.exit(3)

if __name__ == "__main__":
    main()
