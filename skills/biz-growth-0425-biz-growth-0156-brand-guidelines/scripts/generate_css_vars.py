#!/usr/bin/env python3
"""
CSS Variables Generator
Generates a CSS file with brand color variables based on input hex codes.
"""
import sys
import argparse

def generate_css(colors):
    """
    Generate CSS variables for brand colors.
    """
    print(":root {")
    for name, hex_code in colors.items():
        # Ensure hex code has a leading hash
        hex_code = f"#{hex_code.lstrip('#')}"
        print(f"  --brand-{name.lower()}: {hex_code};")
    print("}")

def main():
    parser = argparse.ArgumentParser(description="Brand CSS Variables Generator")
    parser.add_argument("--colors", nargs="+", required=True, help="List of brand colors in format Name=HexCode (e.g. Primary=#0052CC Secondary=#FF5630)")

    args = parser.parse_args()

    color_dict = {}
    for item in args.colors:
        try:
            name, hex_code = item.split('=')
            color_dict[name] = hex_code
        except ValueError:
            print(f"Warning: Ignoring invalid format '{item}'. Use Name=HexCode.")

    if color_dict:
        generate_css(color_dict)
    else:
        print("No valid colors provided.")

if __name__ == "__main__":
    main()
