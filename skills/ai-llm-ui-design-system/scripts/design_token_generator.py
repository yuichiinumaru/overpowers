#!/usr/bin/env python3
# design_token_generator.py

import argparse
import sys
import json

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def adjust_color(rgb, factor):
    return tuple(min(255, int(c * factor)) for c in rgb)

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

def generate_tokens(brand_color, style):
    base_rgb = hex_to_rgb(brand_color)

    # Very simple color scale generation based on the table in SKILL.md
    colors = {
        'primary': {
            '50': '#f0f8ff', # placeholder logic
            '100': '#e0f0ff',
            '200': '#c0e0ff',
            '300': '#a0d0ff',
            '400': '#80c0ff',
            '500': brand_color,
            '600': rgb_to_hex(adjust_color(base_rgb, 0.8)),
            '700': rgb_to_hex(adjust_color(base_rgb, 0.6)),
            '800': rgb_to_hex(adjust_color(base_rgb, 0.4)),
            '900': rgb_to_hex(adjust_color(base_rgb, 0.2)),
        },
        'neutral': {
            '50': '#fafafa',
            '100': '#f5f5f5',
            '500': '#737373',
            '900': '#171717',
        }
    }

    if style == 'modern':
        font_sans = 'Inter'
        font_mono = 'Fira Code'
        radius = '8px'
    elif style == 'classic':
        font_sans = 'Helvetica'
        font_mono = 'Courier'
        radius = '4px'
    elif style == 'playful':
        font_sans = 'Poppins'
        font_mono = 'Source Code Pro'
        radius = '16px'
    else:
        font_sans = 'sans-serif'
        font_mono = 'monospace'
        radius = '8px'

    typography = {
        'fontFamily': {
            'sans': font_sans,
            'mono': font_mono
        },
        'fontSize': {
            'xs': '10px',
            'sm': '13px',
            'base': '16px',
            'lg': '20px',
            'xl': '25px',
            '2xl': '31px',
            '3xl': '39px',
            '4xl': '49px',
            '5xl': '61px'
        }
    }

    spacing = {
        '0': '0px',
        '1': '4px',
        '2': '8px',
        '3': '12px',
        '4': '16px',
        '5': '20px',
        '6': '24px',
        '8': '32px',
        '10': '40px',
        '12': '48px',
        '16': '64px'
    }

    breakpoints = {
        'xs': '0',
        'sm': '480px',
        'md': '640px',
        'lg': '768px',
        'xl': '1024px',
        '2xl': '1280px'
    }

    borders = {
        'radius': {
            'default': radius
        }
    }

    return {
        'colors': colors,
        'typography': typography,
        'spacing': spacing,
        'breakpoints': breakpoints,
        'borders': borders
    }

def output_css(tokens):
    print(":root {")
    for category, items in tokens.items():
        if isinstance(items, dict):
            for key, val in items.items():
                if isinstance(val, dict):
                    for subkey, subval in val.items():
                        print(f"  --{category}-{key}-{subkey}: {subval};")
                else:
                    print(f"  --{category}-{key}: {val};")
    print("}")

def output_scss(tokens):
    for category, items in tokens.items():
        if isinstance(items, dict):
            for key, val in items.items():
                if isinstance(val, dict):
                    for subkey, subval in val.items():
                        print(f"${category}-{key}-{subkey}: {subval};")
                else:
                    print(f"${category}-{key}: {val};")

def output_summary(tokens):
    print("Design Tokens Summary")
    print("=====================")
    print(f"Primary Color Base: {tokens['colors']['primary']['500']}")
    print(f"Font Sans: {tokens['typography']['fontFamily']['sans']}")
    print(f"Border Radius: {tokens['borders']['radius']['default']}")
    print("Colors generated: 50-900")
    print("Typography scale: xs-5xl")

def main():
    parser = argparse.ArgumentParser(description="Design Token Generator")
    parser.add_argument("brand_color", help="Primary brand color (hex)")
    parser.add_argument("style", nargs="?", default="modern", choices=["modern", "classic", "playful"], help="Design style preset")
    parser.add_argument("format", nargs="?", default="json", choices=["json", "css", "scss", "summary"], help="Output format")

    args = parser.parse_args()

    if not args.brand_color.startswith('#') or len(args.brand_color) != 7:
        print("Error: brand_color must be a valid hex color, e.g. #0066CC")
        sys.exit(1)

    tokens = generate_tokens(args.brand_color, args.style)

    if args.format == 'json':
        print(json.dumps(tokens, indent=2))
    elif args.format == 'css':
        output_css(tokens)
    elif args.format == 'scss':
        output_scss(tokens)
    elif args.format == 'summary':
        output_summary(tokens)

if __name__ == "__main__":
    main()
