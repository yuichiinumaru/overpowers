#!/usr/bin/env python3
import sys

def generate_image(description, output_path):
    print(f"Generating image for description: '{description}'...")
    print(f"Saved to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        description = sys.argv[1]
        output = sys.argv[3] if len(sys.argv) > 3 else "figures/output.png"
        generate_image(description, output)
    else:
        print("Usage: python generate_image.py <description> -o <output_path>")
