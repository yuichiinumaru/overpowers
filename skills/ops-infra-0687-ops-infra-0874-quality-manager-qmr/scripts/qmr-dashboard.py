#!/usr/bin/env python3
"""
QMR Performance Dashboard
Tracks and reports key quality indicators.
"""
import json
import datetime
import sys

def collect_metrics():
    # In a real environment, this would query issue trackers, QMS systems, etc.
    # For now, it returns a structured dataset representing the QMR dashboard.
    return {
        "timestamp": datetime.datetime.now().isoformat(),
        "kpis": {
            "customer_complaints": 12,
            "open_capas": 5,
            "audit_findings_open": 2,
            "training_completion_rate": "95%"
        },
        "regulatory_status": "Compliant",
        "iso_13485_status": "Valid",
        "fda_registration_status": "Active"
    }

def print_dashboard():
    dashboard = collect_metrics()
    print("=== QMR PERFORMANCE DASHBOARD ===")
    print(f"Report Date: {dashboard['timestamp']}")
    print("\n--- Key Performance Indicators ---")
    for k, v in dashboard['kpis'].items():
        print(f"  * {k.replace('_', ' ').title()}: {v}")

    print("\n--- Regulatory Compliance ---")
    print(f"  * ISO 13485 Status: {dashboard['iso_13485_status']}")
    print(f"  * FDA Registration: {dashboard['fda_registration_status']}")
    print(f"  * Overall Status: {dashboard['regulatory_status']}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--json":
        print(json.dumps(collect_metrics(), indent=2))
    else:
        print_dashboard()
