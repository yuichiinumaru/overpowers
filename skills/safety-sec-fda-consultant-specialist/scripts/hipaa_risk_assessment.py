#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: hipaa_risk_assessment.py <project_path> [--category administrative|physical|technical]")
        sys.exit(1)

    project_path = sys.argv[1]
    category = "all"
    if "--category" in sys.argv:
        idx = sys.argv.index("--category")
        if idx + 1 < len(sys.argv):
            category = sys.argv[idx + 1]

    print(f"--- HIPAA Risk Assessment ---")
    print(f"Target: {project_path}")
    print(f"Category: {category}\n")

    safeguards = {
        "administrative": ["Security Officer", "Risk Analysis", "Training", "BAAs"],
        "physical": ["Facility Access", "Workstation Security", "Device Disposal"],
        "technical": ["Access Control", "Audit Logs", "Integrity Controls", "Encryption/TLS"]
    }

    targets = [category] if category != "all" and category in safeguards else safeguards.keys()

    for c in targets:
        print(f"[{c.upper()} SAFEGUARDS]")
        for item in safeguards[c]:
            print(f"  - {item}")
    
    print("\nAction: Please review these safeguard categories against the system architecture.")

if __name__ == "__main__":
    main()
