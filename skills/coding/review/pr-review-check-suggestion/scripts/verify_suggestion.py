#!/usr/bin/env python3
import sys

def verify_suggestion():
    print("--- PR Review Suggestion Verification Helper ---")
    issue = input("What is the identified issue? ")
    
    provable = input("Can this issue be proved from the code diff alone? (y/n): ")
    if provable.lower() == 'y':
        print("\nConfidence: HIGH (code is proof)")
        return

    library = input("Which library or framework does this finding relate to? ")
    version = input(f"What is the version of {library} in the project? (Check package.json/lockfile): ")
    
    print("\n--- Recommended Search Queries ---")
    current_year = "2024" # Should ideally be dynamic
    print(f"1. {library} {version} {issue} {current_year}")
    print(f"2. {library} official documentation {issue}")
    print(f"3. {library} GitHub issues {issue}")

    print("\n--- Confidence Calibration (if unable to verify) ---")
    print("Confidence Ceiling: MEDIUM max (requires verification for HIGH)")
    print("Note to include: 'Verify against project version and current documentation'")

if __name__ == "__main__":
    try:
        verify_suggestion()
    except KeyboardInterrupt:
        print("\nVerification cancelled.")
        sys.exit(0)
