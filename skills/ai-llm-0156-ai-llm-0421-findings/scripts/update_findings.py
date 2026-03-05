#!/usr/bin/env python3
import sys
import os
from datetime import datetime

def update_findings(section, content, file_path="FINDINGS.md"):
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("# Findings & Decisions\n\n## Requirements\n-\n\n## Research Findings\n-\n\n## Technical Decisions\n| Decision | Rationale |\n|----------|-----------|\n\n## Issues Encountered\n| Issue | Resolution |\n|-------|------------|\n\n## Resources\n-\n")

    with open(file_path, "r") as f:
        lines = f.readlines()

    new_lines = []
    in_section = False
    found_section = False

    header = f"## {section}"
    
    for line in lines:
        if line.startswith(header):
            in_section = True
            found_section = True
            new_lines.append(line)
            continue
        
        if in_section and line.startswith("##"):
            # End of section, insert content before this header
            if section in ["Technical Decisions", "Issues Encountered"]:
                new_lines.append(content + "\n")
            else:
                new_lines.append(f"- {content}\n")
            in_section = False
        
        if not in_section:
            new_lines.append(line)
        elif line.strip() == "-" or line.strip() == "" or line.startswith("| "):
             # Skip placeholders or existing table lines if we are replacing or appending
             if section not in ["Technical Decisions", "Issues Encountered"]:
                 pass # We'll add our new line at the end of the section
             else:
                 new_lines.append(line)

    if in_section: # If we reached end of file while in section
        if section not in ["Technical Decisions", "Issues Encountered"]:
            new_lines.append(f"- {content}\n")
        else:
            new_lines.append(content + "\n")

    if not found_section:
        print(f"Error: Section '{section}' not found.")
        return

    with open(file_path, "w") as f:
        f.writelines(new_lines)
    print(f"Updated {section} in {file_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: update_findings.py <Section> <Content>")
        sys.exit(1)
    
    section = sys.argv[1]
    content = sys.argv[2]
    update_findings(section, content)
