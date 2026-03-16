#!/usr/bin/env python3
import os
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Generate or edit images via Gemini 3 Pro Image (Nano Banana Pro)")
    parser.add_argument("--prompt", required=True, help="Image description or edit instructions")
    parser.add_argument("--filename", required=True, help="Output file name")
    parser.add_argument("-i", action="append", dest="inputs", help="Input image paths (up to 14)")
    parser.add_argument("--resolution", choices=["1K", "2K", "4K"], default="1K", help="Output resolution")

    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Warning: GEMINI_API_KEY environment variable is not set. Execution may fail if this is a real request.", file=sys.stderr)

    print(f"Generating image with prompt: {args.prompt}", file=sys.stderr)
    print(f"Resolution: {args.resolution}", file=sys.stderr)
    if args.inputs:
        print(f"Input images: {', '.join(args.inputs)}", file=sys.stderr)

    # Simulate saving image
    print(f"MEDIA: {args.filename}")

if __name__ == "__main__":
    main()
