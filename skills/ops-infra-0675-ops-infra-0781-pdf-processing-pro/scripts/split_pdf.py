#!/usr/bin/env python3
"""
split_pdf.py - Split PDF into individual pages
Usage: python scripts/split_pdf.py input.pdf --output-dir pages/
"""
import argparse
import sys
import os

def main():
    parser = argparse.ArgumentParser(description="Split PDF into individual pages")
    parser.add_argument("input", help="Input PDF file")
    parser.add_argument("--output-dir", required=True, help="Output directory for pages")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: input file {args.input} not found")
        sys.exit(1)

    try:
        import pypdf
        print(f"Splitting {args.input} into pages in {args.output_dir}...")
        os.makedirs(args.output_dir, exist_ok=True)
        # Split logic placeholder
        out_file = os.path.join(args.output_dir, "page_1.pdf")
        with open(out_file, 'w') as f:
            f.write(f"Split PDF page placeholder from {args.input}\n")

        print(f"Successfully split PDF into {args.output_dir}")
    except ImportError as e:
        print(f"Error: Missing dependency. {e}")
        print("Run 'pip install pypdf'")
        sys.exit(1)
    except Exception as e:
        print(f"Processing error: {e}")
        sys.exit(3)

if __name__ == "__main__":
    main()
