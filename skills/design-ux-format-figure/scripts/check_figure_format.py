#!/usr/bin/env python3
import os
import argparse
import re

SECTIONS = [
    "Props",
    "State",
    "Helpers",
    "Setup",
    "Animations",
    "Drawing",
    "Event Handlers",
    "Lifecycle",
    "Reactive Blocks"
]

def check_format(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    with open(filepath, 'r') as f:
        content = f.read()

    # Extract script content
    script_match = re.search(r'<script.*?>\s*(.*?)\s*</script>', content, re.DOTALL)
    if not script_match:
        print(f"No <script> tag found in {filepath}")
        return
        
    script_content = script_match.group(1)
    
    # Find all section headers
    # Format: // ----------------------------------------------------------------
    #         // Section Name
    #         // ----------------------------------------------------------------
    found_sections = []
    
    lines = script_content.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('// ---') and i+1 < len(lines) and lines[i+1].startswith('// ') and i+2 < len(lines) and lines[i+2].startswith('// ---'):
            section_name = lines[i+1][3:].strip()
            if section_name in SECTIONS:
                found_sections.append(section_name)

    print(f"Found sections: {found_sections}")
    
    # Check order against expected SECTIONS
    expected_order = [s for s in SECTIONS if s in found_sections]
    
    if found_sections == expected_order:
        print("Sections are in the correct order.")
    else:
        print("Sections are NOT in the correct order.")
        print(f"Expected order for found sections: {expected_order}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check the formatting of a Svelte figure component.")
    parser.add_argument("filepath", help="Path to the Svelte file")
    args = parser.parse_args()
    check_format(args.filepath)
