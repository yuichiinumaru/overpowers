#!/usr/bin/env python3
import sys
import argparse
import json

def main():
    parser = argparse.ArgumentParser(description="Generate tailwind.config.js with custom theme.")
    parser.add_argument('--colors', nargs='+', help="Colors to add (e.g., brand:blue)", default=[])
    parser.add_argument('--fonts', nargs='+', help="Fonts to add (e.g., display:Inter)", default=[])
    args = parser.parse_args()

    colors_dict = {}
    for color in args.colors:
        if ':' in color:
            name, val = color.split(':', 1)
            colors_dict[name] = val
            
    fonts_dict = {}
    for font in args.fonts:
        if ':' in font:
            name, val = font.split(':', 1)
            fonts_dict[name] = [val, 'sans-serif']

    config_str = """/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: ["class"],
  content: [
    './pages/**/*.{ts,tsx}',
    './components/**/*.{ts,tsx}',
    './app/**/*.{ts,tsx}',
    './src/**/*.{ts,tsx}',
  ],
  theme: {
    extend: {
      colors: %s,
      fontFamily: %s,
    },
  },
  plugins: [require("tailwindcss-animate")],
}
""" % (json.dumps(colors_dict, indent=6), json.dumps(fonts_dict, indent=6))

    with open("tailwind.config.js", "w") as f:
        f.write(config_str)

    print("Generated tailwind.config.js with specified theme options.")

if __name__ == "__main__":
    main()
