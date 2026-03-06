import os
import sys

def generate_report(name):
    """
    Initialize a pharmacovigilance safety report with all mandatory sections.
    """
    filename = f"{name.lower().replace(' ', '_')}_safety_report.md"
    
    headers = ["Executive Summary", "Drug Profile", "Adverse Event Analysis", "Signal Detection (PRR/ROR)", "Safety Label Warnings", "Pharmacogenomic Risk Variants", "Serious Adverse Events", "Risk-Benefit Assessment", "Evidence Grading Summary", "Recommendations", "References"]
    
    sections = ["# Pharmacovigilance Safety Report: " + name]
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
