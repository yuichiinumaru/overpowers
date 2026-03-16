import os
import sys

def generate_report(name):
    """
    Initialize a drug repurposing research report with all mandatory sections.
    """
    filename = f"{name.lower().replace(' ', '_')}_repurposing_report.md"
    
    headers = ["Executive Summary", "Candidate Compound Info", "Mechanism of Action", "Target Associations", "Repurposing Rationale", "Safety & ADMET Profile", "Clinical Evidence", "Literature Review", "Evidence Grading Summary", "Next Steps", "References"]
    
    sections = ["# Drug Repurposing Report: " + name]
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
