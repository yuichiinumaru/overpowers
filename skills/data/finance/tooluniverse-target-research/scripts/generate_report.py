import os
import sys

def generate_report(name):
    """
    Initialize a comprehensive target intelligence report with all mandatory sections.
    """
    filename = f"{name.lower().replace(' ', '_')}_target_report.md"
    
    headers = ["Executive Summary", "Core Identity", "Path 0: Open Targets Foundation", "Path 1: Core Identity", "Path 2: Structure & Domains", "Path 3: Function & Pathways", "Path 4: Protein Interactions", "Path 5: Expression Profile", "Path 6: Variants & Disease", "Path 7: Drug Interactions", "Path 8: Literature & Research", "Evidence Quality Summary", "Recommendations", "References"]
    
    sections = ["# Target Intelligence Report: " + name]
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
