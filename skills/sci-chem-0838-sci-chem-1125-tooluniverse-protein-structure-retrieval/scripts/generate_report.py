import os
import sys

def generate_report(name):
    """
    Initialize a protein structure research report with all mandatory sections.
    """
    filename = f"{name.lower().replace(' ', '_')}_structure_report.md"
    
    headers = ["Search Summary", "Best Available Structure", "Experimental Details", "Structure Composition", "Bound Ligands", "Binding Site Details", "Alternative Structures", "AlphaFold Prediction", "Structure Comparison", "Download Links", "References"]
    
    sections = ["# Protein Structure Report: " + name]
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
