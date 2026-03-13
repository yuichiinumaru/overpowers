#!/usr/bin/env python3
import sys

def get_luminance(hex_color):
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 3:
        hex_color = ''.join([c*2 for c in hex_color])
    
    r, g, b = [int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4)]
    
    def adjust(c):
        if c <= 0.03928:
            return c / 12.92
        else:
            return ((c + 0.055) / 1.055) ** 2.4
            
    r = adjust(r)
    g = adjust(g)
    b = adjust(b)
    
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def check_contrast(fg, bg):
    lum1 = get_luminance(fg)
    lum2 = get_luminance(bg)
    
    lighter = max(lum1, lum2)
    darker = min(lum1, lum2)
    
    ratio = (lighter + 0.05) / (darker + 0.05)
    
    print(f"Foreground: {fg}")
    print(f"Background: {bg}")
    print(f"Contrast Ratio: {ratio:.2f}:1")
    print("-" * 20)
    print("WCAG AA (4.5:1):", "PASS" if ratio >= 4.5 else "FAIL")
    print("WCAG AA Large (3:1):", "PASS" if ratio >= 3.0 else "FAIL")
    print("WCAG AAA (7:1):", "PASS" if ratio >= 7.0 else "FAIL")
    print("WCAG AAA Large (4.5:1):", "PASS" if ratio >= 4.5 else "FAIL")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: check_contrast.py <foreground_hex> <background_hex>")
        sys.exit(1)
    
    check_contrast(sys.argv[1], sys.argv[2])
