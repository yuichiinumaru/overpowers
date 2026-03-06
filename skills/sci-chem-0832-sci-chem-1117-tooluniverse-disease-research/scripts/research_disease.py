import sys
from datetime import datetime

# Simulated helper to initialize a disease report
def create_report_file(disease_name):
    """Create initial report file with template"""
    filename = f"{disease_name.lower().replace(' ', '_')}_research_report.md"

    template = f"""# Disease Research Report: {disease_name}

**Report Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}
**Disease Identifiers**: Pending research...

---

## Executive Summary

*Research in progress...*

---

## 1. Disease Identity & Classification
"""
    with open(filename, 'w') as f:
        f.write(template)
    print(f"Initialized {filename}")
    return filename

if __name__ == "__main__":
    if len(sys.argv) > 1:
        create_report_file(sys.argv[1])
    else:
        print("Usage: python research_disease.py <disease_name>")
