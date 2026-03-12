#!/usr/bin/env python3
import sys
import argparse

def validate_clinical_report(file_path):
    print(f"Validating {file_path}...")
    try:
        with open(file_path, "r") as f:
            content = f.read()

        required_sections = ["Patient Info", "Diagnosis", "Treatment"]
        missing = [s for s in required_sections if s.lower() not in content.lower()]

        if missing:
            print(f"WARNING: Missing required sections: {', '.join(missing)}")
            return False

        print("Validation passed. Report structure looks good.")
        return True
    except Exception as e:
        print(f"Error reading report: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate clinical report structure")
    parser.add_argument("report_file", help="Path to the clinical report file")

    args = parser.parse_args()
    validate_clinical_report(args.report_file)
