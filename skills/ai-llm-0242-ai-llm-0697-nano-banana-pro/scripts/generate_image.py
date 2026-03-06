#!/usr/bin/env python3
"""
Generate images using Nano Banana Pro.
"""
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Generate image using Nano Banana Pro")
    parser.add_argument("--prompt", required=True, help="Image description prompt")
    parser.add_argument("--filename", required=True, help="Output filename")
    parser.add_argument("-i", "--input", action="append", help="Input image(s)")
    parser.add_argument("--resolution", default="1K", help="Image resolution")
    args = parser.parse_args()

    print(f"Generating image with prompt: {args.prompt}")
    print(f"Output will be saved to: {args.filename}")
    print(f"MEDIA: {args.filename}")

if __name__ == "__main__":
    main()
