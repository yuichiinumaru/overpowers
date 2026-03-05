import os
import sys

def generate_report(name):
    """
    Initialize a literature research report with all mandatory sections.
    """
    filename = f"{name.lower().replace(' ', '_')}_literature_report.md"
    
    headers = ["Executive Summary", "Research Objectives", "Identifier Resolution", "Target/Disease Context", "Literature Search Results", "Key Themes Extraction", "Evidence Synthesis", "Biological Model Synthesis", "Testable Hypotheses", "Completeness Checklist", "References"]
    
    sections = ["# Literature Deep Research Report: " + name]
    for header in headers:
        sections.append(f"\n## {header}\n[Researching...]")
    
    with open(filename, 'w') as f:
        f.write('\n'.join(sections))
    
    print(f"Created initial report: {filename}")
    return filename

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_report.py <name>")
    else:
        generate_report(sys.argv[1])
