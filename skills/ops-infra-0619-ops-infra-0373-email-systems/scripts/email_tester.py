#!/usr/bin/env python3
"""
Email DNS Records Tester
A simple checker to see if a domain has MX, SPF, and DMARC records.
Requires `dnspython`: pip install dnspython

Usage:
  python3 email_tester.py --domain example.com
"""

import argparse
import sys

try:
    import dns.resolver
except ImportError:
    print("Please install dnspython: pip install dnspython")
    sys.exit(1)

def check_domain(domain):
    print(f"Checking email records for domain: {domain}\n")

    # Check MX
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        print("✅ MX Records found:")
        for mx in mx_records:
            print(f"   - {mx.preference} {mx.exchange}")
    except Exception as e:
        print("❌ MX Records not found:", e)

    # Check SPF
    try:
        txt_records = dns.resolver.resolve(domain, 'TXT')
        spf_found = False
        for txt in txt_records:
            if 'v=spf1' in txt.to_text():
                print(f"✅ SPF Record found: {txt.to_text()}")
                spf_found = True
        if not spf_found:
            print("❌ SPF Record not found (no v=spf1 TXT record)")
    except Exception as e:
        print("❌ SPF Record lookup failed:", e)

    # Check DMARC
    dmarc_domain = f"_dmarc.{domain}"
    try:
        dmarc_records = dns.resolver.resolve(dmarc_domain, 'TXT')
        dmarc_found = False
        for txt in dmarc_records:
            if 'v=DMARC1' in txt.to_text():
                print(f"✅ DMARC Record found: {txt.to_text()}")
                dmarc_found = True
        if not dmarc_found:
            print("❌ DMARC Record not found")
    except Exception as e:
        print(f"❌ DMARC Record not found for {dmarc_domain}:", e)

def main():
    parser = argparse.ArgumentParser(description="Email DNS Records Tester")
    parser.add_argument("--domain", required=True, help="Domain to check (e.g. example.com)")

    args = parser.parse_args()
    check_domain(args.domain)

if __name__ == "__main__":
    main()
