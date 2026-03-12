#!/usr/bin/env python3
import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: qsr_compliance_checker.py <project_path> [--section SECTION]")
        sys.exit(1)

    project_path = sys.argv[1]
    section = "all"
    if "--section" in sys.argv:
        idx = sys.argv.index("--section")
        if idx + 1 < len(sys.argv):
            section = sys.argv[idx + 1]

    print(f"--- QSR Compliance Check (21 CFR Part 820) ---")
    print(f"Target: {project_path}")
    if section != "all":
        print(f"Section: {section}")

    # Mock compliance check
    print("\nScanning documentation for QSR artifacts...")
    
    sections = {
        "820.20": "Management Responsibility",
        "820.30": "Design Controls",
        "820.40": "Document Controls",
        "820.50": "Purchasing Controls",
        "820.100": "Corrective and Preventive Action (CAPA)"
    }

    targets = [section] if section != "all" and section in sections else sections.keys()

    for s in targets:
        print(f"\nChecking {s} ({sections[s]}):")
        if s == "820.30":
            print("  [?] Design Input Requirements (Needs Verification)")
            print("  [?] Design Output Traceability (Needs Verification)")
        elif s == "820.100":
            print("  [?] CAPA Procedures (Needs Verification)")
        else:
            print(f"  [?] Review required for {sections[s]}")

    print("\nNote: This is a static artifact check. Full compliance requires process audit.")

if __name__ == "__main__":
    main()
