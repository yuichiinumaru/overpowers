#!/usr/bin/env python3
import sys
import os

def init_design_md(title, project_id):
    template = f"""# Design System: {title}
**Project ID:** {project_id}

## 1. Visual Theme & Atmosphere
[Description of the mood, density, and aesthetic philosophy]

## 2. Color Palette & Roles
- **[Name]** ([Hex]): [Functional Role]

## 3. Typography Rules
[Description of font family, weight usage for headers vs. body]

## 4. Component Stylings
* **Buttons:** [Shape, color, behavior]
* **Cards/Containers:** [Corner roundness, background, shadow]
* **Inputs/Forms:** [Stroke style, background]

## 5. Layout Principles
[Whitespace strategy, margins, grid alignment]
"""
    with open("DESIGN.md", "w") as f:
        f.write(template)
    print("Initialized DESIGN.md")

if __name__ == "__main__":
    title = sys.argv[1] if len(sys.argv) > 1 else "Project Title"
    p_id = sys.argv[2] if len(sys.argv) > 2 else "Project ID"
    init_design_md(title, p_id)
