#!/usr/bin/env python3
import argparse
import sys

def analyze_contract(file_path):
    print(f"Analyzing contract {file_path} for key clauses...")

    keywords = {
        "Liability": ["liability", "indemnify", "indemnification", "damages", "limitation"],
        "Termination": ["terminate", "termination", "breach", "cancellation"],
        "Confidentiality": ["confidential", "nda", "disclosure", "proprietary"],
        "Payment": ["payment", "fee", "invoice", "compensation", "taxes"]
    }

    try:
        with open(file_path, "r") as f:
            lines = f.readlines()

        for category, words in keywords.items():
            print(f"\n--- {category} Clauses ---")
            found = False
            for i, line in enumerate(lines):
                if any(word in line.lower() for word in words):
                    if len(line.strip()) > 10:  # Skip very short lines
                        print(f"Line {i+1}: {line.strip()[:100]}...")
                        found = True

            if not found:
                print("None found.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Highlight important clauses in a contract")
    parser.add_argument("contract_file", help="Path to the contract text file")

    args = parser.parse_args()
    analyze_contract(args.contract_file)
