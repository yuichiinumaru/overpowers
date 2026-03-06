#!/usr/bin/env python3
import sys

def print_compliance_checklist():
    checklist = {
        "Legal Basis (Art. 6)": [
            "Consent obtained and documented?",
            "Contractual necessity identified?",
            "Legal obligation established?",
            "Legitimate interests assessed and documented?"
        ],
        "Individual Rights (Art. 13-21)": [
            "Privacy notice provided (Right to info)?",
            "Process for access requests (SARs) in place?",
            "Mechanism for rectification/erasure (RTBF)?",
            "Data portability procedures established?"
        ],
        "Accountability (Art. 25-35)": [
            "Records of Processing Activities (ROPA) maintained?",
            "Privacy by Design/Default implemented?",
            "DPIA conducted for high-risk processing?",
            "DPO appointed (if required)?"
        ],
        "International Transfers (Art. 44-49)": [
            "Transfer mechanisms identified (SCCs, BCRs)?",
            "Transfer Risk Assessment (TIA) performed?",
            "Adequacy decisions verified?"
        ]
    }

    print("--- GDPR/DSGVO Compliance Checklist ---")
    for category, items in checklist.items():
        print(f"\n[{category}]")
        for item in items:
            print(f"  [ ] {item}")

if __name__ == "__main__":
    print_compliance_checklist()
