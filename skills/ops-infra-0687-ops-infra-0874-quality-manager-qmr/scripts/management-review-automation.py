#!/usr/bin/env python3
"""
Management Review Automation
Generates the management review report template.
"""
import datetime

def generate_report():
    print("=== MANAGEMENT REVIEW REPORT ===")
    print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d')}")
    print("\n1. Review of Quality Policy and Objectives")
    print("\n2. Customer Feedback and Complaints")
    print("\n3. Internal and External Audit Results")
    print("\n4. Process Performance and Product Conformity")
    print("\n5. Status of CAPAs")
    print("\n6. Follow-up Actions from Previous Reviews")
    print("\n7. Changes that Could Affect the QMS")
    print("\n8. Recommendations for Improvement")
    print("\n9. New/Revised Regulatory Requirements")
    print("\n=== END OF REPORT ===")

if __name__ == "__main__":
    generate_report()
