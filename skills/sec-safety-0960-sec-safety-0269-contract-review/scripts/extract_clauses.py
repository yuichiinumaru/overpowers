import sys
import re

def extract_clauses(text):
    clauses = {
        "Limitation of Liability": r"Limitation\s+of\s+Liability",
        "Indemnification": r"Indemnification",
        "Intellectual Property": r"Intellectual\s+Property|IP\s+Rights",
        "Data Protection": r"Data\s+Protection|Privacy",
        "Term and Termination": r"Term\s+and\s+Termination",
        "Governing Law": r"Governing\s+Law"
    }
    
    found = {}
    for name, pattern in clauses.items():
        match = re.search(f"{pattern}.*?(?=\n#|\n[A-Z\s]+:)", text, re.DOTALL | re.IGNORECASE)
        if match:
            found[name] = match.group(0).strip()
            
    return found

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_clauses.py <contract_file>")
        sys.exit(1)
        
    with open(sys.argv[1], 'r') as f:
        content = f.read()
        
    extracted = extract_clauses(content)
    for name, text in extracted.items():
        print(f"=== {name} ===\n{text[:200]}...\n")
