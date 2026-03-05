import argparse
import sys

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def luminance(r, g, b):
    a = [v / 255.0 for v in [r, g, b]]
    a = [v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4 for v in a]
    return a[0] * 0.2126 + a[1] * 0.7152 + a[2] * 0.0722

def contrast_ratio(color1, color2):
    l1 = luminance(*hex_to_rgb(color1))
    l2 = luminance(*hex_to_rgb(color2))
    light = max(l1, l2)
    dark = min(l1, l2)
    return (light + 0.05) / (dark + 0.05)

def check_wcag(ratio):
    results = []
    if ratio >= 7.0:
        results.append("AAA (Normal/Large Text)")
    elif ratio >= 4.5:
        results.append("AA (Normal Text)")
        results.append("AAA (Large Text)")
    elif ratio >= 3.0:
        results.append("AA (Large Text)")
        results.append("AA (UI Components/Graphics)")
    else:
        results.append("FAIL")
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate WCAG contrast ratio between two hex colors.")
    parser.add_argument("color1", help="First color in hex format (e.g., #FFFFFF or FFFFFF)")
    parser.add_argument("color2", help="Second color in hex format (e.g., #000000 or 000000)")
    args = parser.parse_args()

    try:
        ratio = contrast_ratio(args.color1, args.color2)
        print(f"Contrast Ratio: {ratio:.2f}:1")
        print("WCAG Compliance:")
        for res in check_wcag(ratio):
            print(f"  - {res}")
    except ValueError:
        print("Invalid color format. Please use hex format like #FFFFFF or FFFFFF.")
        sys.exit(1)
