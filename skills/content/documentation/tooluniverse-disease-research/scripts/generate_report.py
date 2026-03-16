import os
import sys

def generate_report(disease_name):
    """
    Initialize a disease research report with all mandatory sections.
    """
    filename = f"{disease_name.lower().replace(' ', '_')}_disease_report.md"
    
    sections = [
        "# Disease Research Report: " + disease_name,
        "\n## 1. Executive Summary\n[Researching...]",
        "\n## 2. Disease Definition & Classification\n[Researching...]",
        "\n## 3. Clinical Presentation & Symptoms\n[Researching...]",
        "\n## 4. Epidemiology & Demographics\n[Researching...]",
        "\n## 5. Pathophysiology & Mechanisms\n[Researching...]",
        "\n## 6. Genetic Basis & Variants\n[Researching...]",
        "\n## 7. Diagnosis & Biomarkers\n[Researching...]",
        "\n## 8. Current Treatment Landscape\n[Researching...]",
        "\n## 9. Therapeutic Targets & Pipeline\n[Researching...]",
        "\n## 10. Research Trends & Literature\n[Researching...]",
        "\n## 11. Evidence Grading Summary\n[Researching...]",
        "\n## 12. Recommendations & Next Steps\n[Researching...]",
        "\n## 13. References\n[Researching...]"
    ]
    
    with open(filename, 'w') as f:
        f.write('\n'.join(sections))
    
    print(f"Created initial report: {filename}")
    return filename

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_report.py <disease_name>")
    else:
        generate_report(sys.argv[1])
