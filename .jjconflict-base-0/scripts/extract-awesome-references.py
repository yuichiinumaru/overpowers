#!/usr/bin/env python3
"""
Extract references from awesome-opencode data to docs/references.md
"""

import os
import re
from pathlib import Path

# Paths
AWESOME_DATA_DIR = Path("references/awesome-opencode/data")
OUTPUT_FILE = Path("docs/references.md")

CATEGORIES = [
    "agents",
    "plugins",
    "projects",
    "resources",
    "themes"
]

def parse_yaml(content):
    """Simple YAML parser for flat files."""
    data = {}
    current_key = None

    for line in content.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue

        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()

            # Handle quoted values
            if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
                value = value[1:-1]

            data[key] = value
            current_key = key
        elif current_key and line:
            # Continuation of previous value (multiline)
            data[current_key] += " " + line

    return data

def main():
    if not AWESOME_DATA_DIR.exists():
        print(f"Error: {AWESOME_DATA_DIR} not found.")
        return

    markdown_lines = [
        "# Awesome OpenCode References",
        "",
        "A curated list of plugins, agents, and resources extracted from [awesome-opencode](https://github.com/awesome-opencode/awesome-opencode).",
        "",
        "## Contents",
        ""
    ]

    # Generate Table of Contents
    for category in CATEGORIES:
        markdown_lines.append(f"- [{category.capitalize()}](#{category})")
    markdown_lines.append("")

    for category in CATEGORIES:
        cat_dir = AWESOME_DATA_DIR / category
        if not cat_dir.exists():
            continue

        markdown_lines.append(f"## {category.capitalize()}")
        markdown_lines.append("")

        items = []
        for file in sorted(cat_dir.glob("*.yaml")):
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    data = parse_yaml(content)
                    items.append(data)
            except Exception as e:
                print(f"Error parsing {file}: {e}")

        # Sort by name
        items.sort(key=lambda x: x.get('name', '').lower())

        for item in items:
            name = item.get('name', 'Unknown')
            repo = item.get('repo', '#')
            tagline = item.get('tagline', '')
            description = item.get('description', '')

            markdown_lines.append(f"### [{name}]({repo})")
            if tagline:
                markdown_lines.append(f"_{tagline}_")
            markdown_lines.append("")
            if description:
                markdown_lines.append(description)
            markdown_lines.append("")

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(markdown_lines))

    print(f"Successfully generated {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
