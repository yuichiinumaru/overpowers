#!/usr/bin/env python3
import sys

PAYLOADS = {
    "default_creds": ["admin:admin", "admin:password", "root:root", "test:test"],
    "common_passwords": ["123456", "password", "12345678", "qwerty"],
    "rate_limit_headers": [
        "X-Forwarded-For: 127.0.0.1",
        "X-Real-IP: 127.0.0.1",
        "X-Originating-IP: 127.0.0.1"
    ]
}

CHECKLIST = [
    "Password policy enforcement (length, complexity)",
    "Username enumeration vulnerability",
    "Account lockout and rate limiting",
    "Session token entropy and length",
    "Session fixation (token change after login)",
    "MFA bypass techniques",
    "Insecure password reset workflow"
]

def main():
    print("--- Broken Authentication Testing Helper ---")
    print("\nChecklist:")
    for item in CHECKLIST:
        print(f"[ ] {item}")
        
    print("\nCommon Payloads:")
    for cat, items in PAYLOADS.items():
        print(f"\n{cat.replace('_', ' ').title()}:")
        for item in items:
            print(f"  - {item}")

if __name__ == "__main__":
    main()
