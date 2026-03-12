import sys
import re

def validate_care_guidelines(content):
    required_sections = [
        "Title", "Keywords", "Abstract", "Introduction",
        "Patient Information", "Clinical Findings", "Timeline",
        "Diagnostic Assessment", "Therapeutic Interventions",
        "Follow-up and Outcomes", "Discussion", "Informed Consent"
    ]
    
    missing = []
    for section in required_sections:
        if not re.search(f"^#+.*{section}", content, re.MULTILINE | re.IGNORECASE):
            missing.append(section)
            
    return missing

def check_hipaa_identifiers(content):
    # Simplified check for common identifiers
    identifiers = {
        "Names": r"(Mr\.|Ms\.|Mrs\.)\s+[A-Z][a-z]+",
        "Phone numbers": r"\d{3}-\d{3}-\d{4}",
        "SSN": r"\d{3}-\d{2}-\d{4}",
        "Emails": r"[\w\.-]+@[\w\.-]+\.\w+"
    }
    
    found = []
    for id_type, pattern in identifiers.items():
        if re.search(pattern, content):
            found.append(id_type)
            
    return found

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_case_report.py <file_path>")
        sys.exit(1)
        
    with open(sys.argv[1], 'r') as f:
        content = f.read()
        
    missing_sections = validate_care_guidelines(content)
    if missing_sections:
        print("Missing CARE sections:")
        for s in missing_sections:
            print(f"- {s}")
    else:
        print("All mandatory CARE sections present.")
        
    hipaa_findings = check_hipaa_identifiers(content)
    if hipaa_findings:
        print("\nPotential HIPAA identifiers found (DO NOT PUBLISH):")
        for f in hipaa_findings:
            print(f"- {f}")
    else:
        print("\nNo obvious HIPAA identifiers found.")
