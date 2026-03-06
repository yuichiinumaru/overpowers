import os
import sys

def generate_report(name):
    """
    Initialize an infectious disease research report with all mandatory sections.
    """
    filename = f"{name.lower().replace(' ', '_')}_infectious_disease_report.md"
    
    headers = ["Executive Summary", "Pathogen Characterization", "Transmission & Epidemiology", "Mechanism of Infection", "Current Treatments", "Repurposing Candidates", "Novel Target Discovery", "Safety Considerations", "Evidence Grading Summary", "Recommendations", "References"]
    
    sections = ["# Infectious Disease Report: " + name]
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
