#!/usr/bin/env python3
"""
Regulatory Compliance Tracker
Monitors multi-jurisdictional compliance status.
"""
import json
import sys

def get_compliance_status():
    return {
        "eu_mdr_2017_745": {"status": "Compliant", "last_audit": "2023-11-15", "next_audit": "2024-11-15"},
        "fda_qsr_21_cfr_820": {"status": "Compliant", "last_audit": "2023-08-20", "next_audit": "2025-08-20"},
        "iso_13485_2016": {"status": "Certified", "last_audit": "2023-10-01", "next_audit": "2024-10-01"}
    }

def print_status():
    status = get_compliance_status()
    print("=== REGULATORY COMPLIANCE TRACKER ===")
    for jurisdiction, details in status.items():
        print(f"\nJurisdiction/Standard: {jurisdiction.upper().replace('_', ' ')}")
        print(f"  Status: {details['status']}")
        print(f"  Last Audit: {details['last_audit']}")
        print(f"  Next Audit: {details['next_audit']}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--json":
        print(json.dumps(get_compliance_status(), indent=2))
    else:
        print_status()
