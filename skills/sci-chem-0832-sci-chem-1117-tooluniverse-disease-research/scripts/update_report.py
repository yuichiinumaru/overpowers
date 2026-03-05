import os
import sys
import re

def update_report(filename, section_name, content):
    """
    Update a specific section in the research report.
    """
    if not os.path.exists(filename):
        print(f"Error: {filename} not found.")
        return

    with open(filename, 'r') as f:
        report_content = f.read()

    # Find the section and replace its content
    # Look for the section header and the following content until the next header or end of file
    pattern = rf"(## {re.escape(section_name)}\n)([\s\S]*?)(?=\n## |\Z)"
    
    if not re.search(pattern, report_content):
        print(f"Error: Section '{section_name}' not found in {filename}.")
        return

    # Replace [Researching...] or existing content with new content
    updated_content = re.sub(pattern, rf"\1{content.strip()}\n", report_content)

    with open(filename, 'w') as f:
        f.write(updated_content)

    print(f"Updated section '{section_name}' in {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python update_report.py <filename> <section_name> <content>")
    else:
        update_report(sys.argv[1], sys.argv[2], sys.argv[3])
