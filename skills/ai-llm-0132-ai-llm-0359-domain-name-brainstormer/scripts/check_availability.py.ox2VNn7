#!/usr/bin/env python3
"""
Check domain name availability using WHOIS.
"""
import sys
import subprocess
import argparse

TLDS = [".com", ".io", ".dev", ".ai", ".app", ".co", ".xyz"]

def check_domain(domain):
    try:
        # Run whois command
        result = subprocess.run(["whois", domain], capture_output=True, text=True, timeout=10)
        output = result.stdout.lower()
        
        # Heuristics for "not found"
        if "no match" in output or "not found" in output or "not registered" in output or "no data found" in output:
            return "AVAILABLE"
        else:
            return "TAKEN"
    except subprocess.TimeoutExpired:
        return "TIMEOUT"
    except Exception as e:
        return f"ERROR: {e}"

def main():
    parser = argparse.ArgumentParser(description="Check domain availability.")
    parser.add_argument("names", nargs="+", help="Names to check (without TLD)")
    parser.add_argument("--tlds", nargs="+", default=TLDS, help="TLDs to check")
    
    args = parser.parse_args()
    
    print(f"{'Domain':<30} | {'Status':<10}")
    print("-" * 45)
    
    for name in args.names:
        for tld in args.tlds:
            full_domain = name + (tld if tld.startswith('.') else '.' + tld)
            status = check_domain(full_domain)
            print(f"{full_domain:<30} | {status:<10}")

if __name__ == "__main__":
    main()
