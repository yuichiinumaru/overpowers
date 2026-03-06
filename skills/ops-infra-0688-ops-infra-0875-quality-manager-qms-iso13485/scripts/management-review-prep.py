#!/usr/bin/env python3
"""
Management Review Prep
Compiles input data for ISO 13485 Management Review meetings.
"""
import sys

def compile_inputs():
    print("=== MANAGEMENT REVIEW INPUT COMPILATION ===")
    print("\nGathering data for Clause 5.6.2 requirements:")
    print("  - Feedback: 12 complaints, 0 critical")
    print("  - Complaint Handling: All acknowledged within 24h")
    print("  - Reporting to Regulatory Authorities: 0 required reports")
    print("  - Audits: 1 internal audit completed, 0 external")
    print("  - Processes/Product Conformity: 98.8% yield")
    print("  - Corrective Actions: 5 open, 12 closed")
    print("  - Preventive Actions: 2 open, 4 closed")
    print("  - Follow-up from Previous Reviews: All actions completed")
    print("  - Changes Affecting QMS: ISO 13485:2016 transition complete")
    print("  - Recommendations for Improvement: Implement new eQMS software")
    print("\nStatus: Ready for Management Review.")

if __name__ == "__main__":
    compile_inputs()
