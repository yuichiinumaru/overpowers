#!/usr/bin/env python3
import sys

def generate_8bit_css(component_name):
    css = f"""/* 8-bit Pixel Art Style for {component_name} */
.{component_name.lower()}-8bit {{
  position: relative;
  display: inline-block;
  padding: 10px 20px;
  background: white;
  border: none;
  cursor: pointer;
}}

/* Pixelated Borders */
.{component_name.lower()}-8bit::before {{
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  box-shadow: 
    0 -4px 0 -2px black,
    0 4px 0 -2px black,
    -4px 0 0 -2px black,
    4px 0 0 -2px black;
}}

/* Corner Pixels */
.{component_name.lower()}-8bit::after {{
  content: '';
  position: absolute;
  top: -2px; left: -2px; width: 4px; height: 4px;
  background: black;
  box-shadow: 
    calc(100% + 0px) 0 0 0 black,
    0 calc(100% + 0px) 0 0 black,
    calc(100% + 0px) calc(100% + 0px) 0 0 black;
}}
"""
    filename = f"{component_name.lower()}_8bit.css"
    with open(filename, 'w') as f:
        f.write(css)
    print(f"8-bit CSS generated: {filename}")

if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "Button"
    generate_8bit_css(name)
