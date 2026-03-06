#!/usr/bin/env python3
"""
Generate images using Nano Image Generator.
"""
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Generate image using Nano Image Generator")
    parser.add_argument("prompt", help="Image description prompt")
    parser.add_argument("-o", "--output", required=True, help="Output filename")
    parser.add_argument("-a", "--aspect", default="1:1", help="Aspect ratio")
    parser.add_argument("-s", "--size", default="2K", help="Image size")
    args = parser.parse_args()

    print(f"Generating image with prompt: {args.prompt}")
    print(f"Output will be saved to: {args.output}")

if __name__ == "__main__":
    main()
