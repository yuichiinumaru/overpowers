#!/usr/bin/env python3
import argparse
import sys
import os

def main():
    parser = argparse.ArgumentParser(description="Nano Image Generator (Gemini 3 Pro Preview)")
    parser.add_argument("prompt", help="Image description")
    parser.add_argument("-o", "--output", required=True, help="Output file path")
    parser.add_argument("-a", "--aspect", default="1:1",
                        choices=["1:1", "2:3", "3:4", "4:5", "9:16", "3:2", "4:3", "5:4", "16:9", "21:9"],
                        help="Aspect ratio (default: 1:1)")
    parser.add_argument("-s", "--size", default="2K", choices=["1K", "2K", "4K"], help="Resolution (default: 2K)")

    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Warning: GEMINI_API_KEY environment variable is not set.", file=sys.stderr)

    print(f"Generating image with prompt: {args.prompt}", file=sys.stderr)
    print(f"Aspect ratio: {args.aspect}", file=sys.stderr)
    print(f"Size: {args.size}", file=sys.stderr)
    print(f"Output: {args.output}", file=sys.stderr)

    # Simulate saving image
    print(f"MEDIA: {args.output}")

if __name__ == "__main__":
    main()
