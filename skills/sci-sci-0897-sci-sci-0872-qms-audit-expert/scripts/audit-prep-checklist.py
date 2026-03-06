#!/usr/bin/env python3
"""
Helper script to generate a basic QMS audit preparation checklist.
"""
import argparse
import datetime

def generate_checklist(auditee, scope, process, date):
    """Generates a markdown checklist for QMS audit preparation."""

    output = f"""# QMS Audit Preparation Checklist

**Auditee / Department:** {auditee}
**Audit Scope:** {scope}
**Target Process:** {process}
**Target Date:** {date}
**Checklist Generated:** {datetime.date.today().isoformat()}

## 1. Audit Planning (T-30 Days)
- [ ] Define precise audit scope and criteria (ISO 13485 clauses applicable)
- [ ] Review previous audit findings and CAPAs for this process
- [ ] Identify key process owners and personnel to interview
- [ ] Draft and distribute the formal Audit Plan to stakeholders
- [ ] Confirm auditor(s) assignment and independence

## 2. Document Review (T-14 Days)
- [ ] Request and review the current Standard Operating Procedure (SOP) for {process}
- [ ] Review related Work Instructions (WIs) and forms
- [ ] Review process risk assessments (FMEA, etc.)
- [ ] Review relevant quality metrics or KPIs for the past 12 months
- [ ] Prepare specific audit questions based on document review

## 3. Logistics and Communication (T-7 Days)
- [ ] Confirm meeting rooms or virtual meeting links
- [ ] Send final agenda to all participants
- [ ] Request access to necessary electronic systems (eQMS, ERP)
- [ ] Confirm availability of physical records (if applicable)

## 4. Audit Execution Preparation (T-2 Days)
- [ ] Finalize custom audit checklist based on {scope}
- [ ] Prepare attendance/sign-in sheet for opening meeting
- [ ] Review sampling plans for records review
- [ ] Mental walkthrough of process flow

## 5. Post-Audit Deliverables
- [ ] Draft Audit Report within 5 working days
- [ ] Document Nonconformances (Major/Minor) and Observations clearly
- [ ] Conduct Closing Meeting to present findings
- [ ] Ensure auditee understands required corrective actions (CAPA)
"""
    return output

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a QMS Audit Preparation Checklist")
    parser.add_argument("--auditee", required=True, help="Name of the auditee or department")
    parser.add_argument("--scope", required=True, help="Scope of the audit (e.g., ISO 13485 Clause 7.3)")
    parser.add_argument("--process", required=True, help="Specific process being audited (e.g., Design Control)")
    parser.add_argument("--date", required=True, help="Target date for the audit (YYYY-MM-DD)")

    args = parser.parse_args()

    print(generate_checklist(args.auditee, args.scope, args.process, args.date))
