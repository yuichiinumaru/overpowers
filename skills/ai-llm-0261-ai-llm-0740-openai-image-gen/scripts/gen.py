#!/usr/bin/env python3
import argparse
import sys
import os

def main():
    parser = argparse.ArgumentParser(description="OpenAI Image Generator")
    parser.add_argument("--prompt", help="Image description", default="A random image")
    parser.add_argument("--count", type=int, default=1, help="Number of images")
    parser.add_argument("--model", default="gpt-image-1", help="Model to use")
    parser.add_argument("--size", default="1024x1024", help="Image size")
    parser.add_argument("--quality", default="standard", help="Image quality")
    parser.add_argument("--out-dir", default="./out/images", help="Output directory")
    parser.add_argument("--background", help="Background style")
    parser.add_argument("--output-format", default="png", help="Output format")
    parser.add_argument("--style", default="vivid", help="Image style")

    args = parser.parse_args()

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Warning: OPENAI_API_KEY environment variable is not set.", file=sys.stderr)

    print(f"Generating {args.count} image(s) with model: {args.model}", file=sys.stderr)
    print(f"Prompt: {args.prompt}", file=sys.stderr)
    print(f"Size: {args.size}", file=sys.stderr)
    print(f"Quality: {args.quality}", file=sys.stderr)

    os.makedirs(args.out_dir, exist_ok=True)
    out_file = os.path.join(args.out_dir, f"output.{args.output_format}")

    # Simulate saving image
    print(f"MEDIA: {out_file}")

if __name__ == "__main__":
    main()
