#!/usr/bin/env python3
import sys

def generate_animated_svg_wrapper(component_name):
    code = f"""import React from 'react';
import {{ cn }} from "@/lib/utils";

export const {component_name} = ({{ className, ...props }}) => {{
  return (
    <div className={{cn("animate-spin", className)}}>
      <svg
        viewBox="0 0 16 16"
        width="16"
        height="16"
        {{...props}}
      >
        <rect x="2" y="2" width="4" height="4" fill="currentColor" />
        <rect x="10" y="2" width="4" height="4" fill="currentColor" />
        <rect x="10" y="10" width="4" height="4" fill="currentColor" />
        <rect x="2" y="10" width="4" height="4" fill="currentColor" />
      </svg>
    </div>
  );
}};
"""
    print(code)

if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "PixelSpinner"
    generate_animated_svg_wrapper(name)
