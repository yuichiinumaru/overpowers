import sys
import re

# Red Flags for RED classification (Significant Issues)
RED_CRITERIA = [
    (r"non-solicit|non-solicitation", "Non-solicitation provision found"),
    (r"non-compete", "Non-compete provision found"),
    (r"exclusivity", "Exclusivity provision found"),
    (r"standstill", "Standstill provision found"),
    (r"assignment of ip|ip assignment|grants to (receiving party|recipient) all right", "IP assignment/license found"),
    (r"liquidated damages", "Liquidated damages found"),
    (r"mandatory arbitration", "Mandatory arbitration found"),
    (r"perpetual|forever|in perpetuity", "Perpetual confidentiality obligation"),
    (r"indemnify|indemnification", "Indemnity clause (not standard in NDAs)"),
]

# Yellow Flags for YELLOW classification (Counsel Review Needed)
YELLOW_CRITERIA = [
    (r"residuals", "Residuals clause found"),
    (r"audit rights", "Audit rights found"),
    (r"10 years|ten years", "Long duration (10 years)"),
    (r"without marking|whether marked or not", "Broad definition of confidential info"),
]

def triage_nda(text):
    print("--- NDA Triage Report ---")
    red_findings = []
    for pattern, desc in RED_CRITERIA:
        if re.search(pattern, text, re.IGNORECASE):
            red_findings.append(desc)
            
    yellow_findings = []
    for pattern, desc in YELLOW_CRITERIA:
        if re.search(pattern, text, re.IGNORECASE):
            yellow_findings.append(desc)
            
    # Check for missing standard carveouts (Heuristic)
    carveouts = ["public knowledge", "prior possession", "independent development", "legal compulsion"]
    missing_carveouts = []
    for c in carveouts:
        if c.split()[0] not in text.lower(): # Simple check
            missing_carveouts.append(c)
            
    if missing_carveouts:
        yellow_findings.append(f"Potential missing standard carveouts: {', '.join(missing_carveouts)}")

    if red_findings:
        print("Classification: RED (Significant Issues)")
        print("Reasons:")
        for f in red_findings:
            print(f" - {f}")
        print("\nRecommendation: Full legal review required. Do not sign. Prepare counterproposal or standard form.")
    elif yellow_findings:
        print("Classification: YELLOW (Counsel Review Needed)")
        print("Reasons:")
        for f in yellow_findings:
            print(f" - {f}")
        print("\nRecommendation: Send to designated reviewer with specific issues flagged.")
    else:
        print("Classification: GREEN (Standard Approval)")
        print("\nRecommendation: Approve via standard delegation. No major red flags detected by keyword scan.")
        
    print("\nDisclaimer: This is an automated keyword screening and NOT legal advice. A full manual review is always required.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python nda_triager.py <nda_file>")
    else:
        try:
            with open(sys.argv[1], 'r', encoding='utf-8') as f:
                triage_nda(f.read())
        except Exception as e:
            print(f"Error: {e}")
