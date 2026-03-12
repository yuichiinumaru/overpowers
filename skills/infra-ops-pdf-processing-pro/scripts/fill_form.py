#!/usr/bin/env python3
"""
fill_form.py - Fill PDF forms with data
Usage: python scripts/fill_form.py input.pdf data.json output.pdf [--validate]
"""
import argparse
import sys
import json
import os

def main():
    parser = argparse.ArgumentParser(description="Fill PDF forms with data")
    parser.add_argument("input", help="Input PDF file")
    parser.add_argument("data", help="Input JSON data file")
    parser.add_argument("output", help="Output PDF file")
    parser.add_argument("--validate", action="store_true", help="Validate form data before filling")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: input file {args.input} not found")
        sys.exit(1)

    if not os.path.exists(args.data):
        print(f"Error: data file {args.data} not found")
        sys.exit(1)

    try:
        with open(args.data, 'r') as f:
            data = json.load(f)
        if args.validate:
            print("Validating form data...")
            # Validation logic

        print(f"Filling form in {args.input} with data from {args.data}...")
        # PyPDF2/pdfrw form filling logic goes here

        # Stub output
        with open(args.output, 'w') as f:
            f.write(f"Filled PDF form placeholder based on {args.input}")

        print(f"Successfully generated {args.output}")
    except json.JSONDecodeError:
        print(f"Error: {args.data} contains invalid JSON.")
        sys.exit(2)
    except Exception as e:
        print(f"Processing error: {e}")
        sys.exit(3)

if __name__ == "__main__":
    main()
