#!/usr/bin/env python3
import sys
import re

PREFERRED = {
    "the Claude AI": "Claude",
    "auto-coding": "Code generation",
    "bot": "Agent",
    "revolutionize": "Streamline",
    "synergize": "Integrate"
}

AVOID = [
    "cutting-edge",
    "game-changer",
    "leverage",
    "utilize",
    "paradigm shift"
]

def check_text(text):
    issues = []
    
    # Check for preferred terms
    for wrong, preferred in PREFERRED.items():
        if re.search(r'\b' + re.escape(wrong) + r'\b', text, re.IGNORECASE):
            issues.append(f"Preferred Term: Use '{preferred}' instead of '{wrong}'")
            
    # Check for avoid terms
    for term in AVOID:
        if re.search(r'\b' + re.escape(term) + r'\b', text, re.IGNORECASE):
            issues.append(f"Avoid Term: '{term}' is overused or vague")
            
    # Check for "we believe/think"
    if re.search(r'\bwe (believe|think)\b', text, re.IGNORECASE):
        issues.append("Tone Issue: Avoid 'we believe' or 'we think'. Be more confident.")
        
    # Check for ALL CAPS (simple check)
    if re.search(r'\b[A-Z]{5,}\b', text):
        issues.append("Tone Issue: Avoid ALL CAPS except for brief emphasis.")
        
    return issues

def main():
    if len(sys.argv) < 2:
        print("Usage: brand_voice_checker.py \"Your text here\"")
        sys.exit(1)
        
    text = sys.argv[1]
    issues = check_text(text)
    
    if not issues:
        print("Text matches brand voice guidelines! ✅")
    else:
        print("--- Brand Voice Issues Found ---")
        for issue in issues:
            print(f"- {issue}")

if __name__ == "__main__":
    main()
