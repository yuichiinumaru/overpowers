#!/usr/bin/env python3
import sys

def generate_css_variables():
    code = """:root {
  /* Core Palette */
  --color-primary: #000;
  --color-secondary: #666;
  --color-accent: #00f;
  --color-background: #fff;
  --color-surface: #f5f5f5;
  --color-border: #e0e0e0;
  
  /* Typography */
  --font-display: 'Clash Display', sans-serif;
  --font-body: 'Satoshi', sans-serif;
  
  /* Spacing (4px grid) */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  
  /* Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 16px;
  --radius-full: 9999px;
}
"""
    print(code)

if __name__ == "__main__":
    generate_css_variables()
