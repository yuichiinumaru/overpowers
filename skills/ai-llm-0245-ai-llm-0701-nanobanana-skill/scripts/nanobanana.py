#!/usr/bin/env python3
"""
Nanobanana Image Generation Skill
"""
import argparse

def main():
    parser = argparse.ArgumentParser(description="Nanobanana Image Generation Skill")
    parser.add_argument("--prompt", required=True, help="Image prompt")
    parser.add_argument("--output", help="Output filename")
    parser.add_argument("--input", nargs="+", help="Input image(s)")
    parser.add_argument("--size", default="768x1344", help="Aspect ratio/size")
    parser.add_argument("--model", default="gemini-3-pro-image-preview", help="Model to use")
    parser.add_argument("--resolution", default="1K", help="Image resolution")

    args = parser.parse_args()
    print(f"Generating image with prompt: {args.prompt}")
    if args.output:
        print(f"Output will be saved to: {args.output}")

if __name__ == "__main__":
    main()
