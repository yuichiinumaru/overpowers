import sys
import re

RED_FLAGS = [
    (r"perpetual|forever|in perpetuity", "Perpetual confidentiality (Potential High Risk)"),
    (r"residuals", "Residuals clause (Medium/High Risk)"),
    (r"indemnify|indemnification", "Indemnity clause (Potential High Risk)"),
    (r"attorney's fees|attorneys' fees", "One-way attorneys' fees (Medium Risk)"),
    (r"injunctive relief|equitable relief", "Injunctive/Equitable relief (Medium Risk)"),
    (r"without marking|whether marked or not|regardless of marking", "Overbroad definition (Potential no marking requirement)"),
    (r"backup|back-up", "Backup/Destruction clause (Verify if practical carve-out exists)"),
    (r"non-solicitation|non-solicit", "Non-solicitation clause (Verify scope)"),
    (r"exclusive", "Exclusivity language (High Risk if unintended)"),
]

def scan_nda(text):
    print("--- NDA Red Flag Scan ---")
    found = 0
    for pattern, description in RED_FLAGS:
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            print(f"[!] FLAG: {description} (found {len(matches)} mentions)")
            found += 1
            
    if found == 0:
        print("No immediate red flags detected by simple keyword scan.")
    else:
        print(f"\nTotal categories of flags found: {found}")
    print("\nDisclaimer: This is a simple keyword scan and NOT legal advice. Always review the full context of the clauses.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python nda_red_flag_scanner.py <nda_file>")
    else:
        try:
            with open(sys.argv[1], 'r', encoding='utf-8') as f:
                scan_nda(f.read())
        except Exception as e:
            print(f"Error: {e}")
