#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(description="Generate an ISO 13485 QMS Audit Plan template")
    parser.add_argument('--company', default="Medical Device Inc.", help="Company name")
    parser.add_argument('--auditor', default="Lead Auditor", help="Name of lead auditor")
    parser.add_argument('--date', default="YYYY-MM-DD", help="Date of audit")

    args = parser.parse_args()

    template = f"""# ISO 13485 QMS Audit Plan

**Company:** {args.company}
**Lead Auditor:** {args.auditor}
**Audit Date:** {args.date}

## 1. Audit Objective
To determine the conformity of the Quality Management System with the requirements of ISO 13485:2016 and applicable regulatory requirements.

## 2. Audit Scope
The audit will cover all QMS processes related to the design, development, and manufacturing of medical devices at the primary facility.

## 3. Audit Criteria
- ISO 13485:2016
- Company Quality Manual and SOPs
- Applicable Regulatory Requirements (e.g., FDA 21 CFR Part 820, EU MDR)

## 4. Audit Schedule

| Time | Process / Department | Clauses | Auditee(s) |
|------|----------------------|---------|------------|
| 09:00| Opening Meeting | - | Management Team |
| 09:30| Management Responsibility| 5.1-5.6 | Top Management |
| 10:30| Resource Management | 6.1-6.4 | HR, Facilities |
| 11:30| Document Control | 4.2 | QA/RA |
| 12:30| Lunch Break | - | - |
| 13:30| Product Realization | 7.1-7.6 | R&D, Production |
| 15:00| Measurement, Analysis & Improvement | 8.1-8.5 | QA |
| 16:30| Auditor Deliberation | - | Audit Team |
| 17:00| Closing Meeting | - | Management Team |

## 5. Nonconformity Grading System
- **Major Nonconformity:** A failure to fulfill one or more requirements of ISO 13485, or a situation that raises significant doubt about the QMS's ability to achieve intended outputs.
- **Minor Nonconformity:** A single identified lapse, which would not ordinarily affect the capability of the QMS.
- **Observation / Opportunity for Improvement (OFI):** Not a nonconformity, but an area where the system could be enhanced.

## Signatures

Lead Auditor: ___________________________ Date: ______________

Auditee Rep:  ___________________________ Date: ______________
"""
    print(template)

if __name__ == '__main__':
    main()
