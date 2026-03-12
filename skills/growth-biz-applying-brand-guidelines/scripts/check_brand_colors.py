#!/usr/bin/env python3
"""
Brand Color Checker
Checks if a given hex color code matches the brand palette or returns the closest match.
"""
import sys
import argparse

BRAND_COLORS = {
    "Primary": "#0052CC",
    "Secondary": "#FF5630",
    "Accent": "#36B37E",
    "Background": "#F4F5F7",
    "Text": "#172B4D"
}

def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    if len(hex_code) != 6:
        raise ValueError("Invalid hex color code.")
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

def color_distance(c1, c2):
    return sum((a - b) ** 2 for a, b in zip(c1, c2)) ** 0.5

def main():
    parser = argparse.ArgumentParser(description="Brand Color Checker")
    parser.add_argument("--hex", type=str, required=True, help="Hex color code to check (e.g. '#0052CC' or '0052CC').")

    args = parser.parse_args()

    try:
        input_rgb = hex_to_rgb(args.hex)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    closest_match = None
    min_distance = float('inf')

    print(f"Checking color: #{args.hex.lstrip('#').upper()}")

    for name, hex_code in BRAND_COLORS.items():
        brand_rgb = hex_to_rgb(hex_code)
        dist = color_distance(input_rgb, brand_rgb)

        if dist == 0:
            print(f"MATCH FOUND: This is the brand's {name} color ({hex_code}).")
            return

        if dist < min_distance:
            min_distance = dist
            closest_match = (name, hex_code)

    print(f"No exact match found.")
    print(f"Closest brand color is {closest_match[0]} ({closest_match[1]}).")

if __name__ == "__main__":
    main()
