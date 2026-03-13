#!/usr/bin/env python3
import os
import sys

def init_philosophy(name):
    filename = f"{name.lower().replace(' ', '-')}.md"
    template = f"""# Design Philosophy: {name}

## 1. Atmosphere & Vibe
[Describe the emotional core and visual mood]

## 2. Forms & Space
[Describe geometric relationships and use of negative space]

## 3. Color & Material
[Describe the palette and texture qualities]

## 4. Scale & Rhythm
[Describe how size and repetition build meaning]

## 5. Composition & Balance
[Describe the structural arrangement]

---
*Meticulously crafted with painstaking attention to detail.*
"""
    with open(filename, "w") as f:
        f.write(template)
    print(f"Created philosophy template: {filename}")

if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "New Movement"
    init_philosophy(name)
