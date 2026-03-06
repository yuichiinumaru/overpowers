import os
import sys

def generate_report(name):
    """
    Initialize a precision oncology research report with all mandatory sections.
    """
    filename = f"{name.lower().replace(' ', '_')}_oncology_report.md"
    
    headers = ["Executive Summary", "Molecular Profile Validation", "Variant Interpretation", "Tumor Expression Context", "Treatment Options", "Pathway & Network Analysis", "Resistance Analysis", "Clinical Trial Matching", "Literature Evidence", "Synthesis & Next Steps", "References"]
    
    sections = ["# Precision Oncology Report: " + name]
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
