#!/usr/bin/env python3
import argparse
import os
import sys
import datetime

def create_initial_report(patient_id):
    filename = f"{patient_id}_rare_disease_report.md"
    content = f"""# Rare Disease Diagnostic Report

**Patient ID**: {patient_id} | **Date**: {datetime.date.today()} | **Status**: In Progress

---

## Executive Summary
[Researching...]

---

## 1. Phenotype Analysis
### 1.1 Standardized HPO Terms
[Researching...]
### 1.2 Key Clinical Features
[Researching...]

---

## 2. Differential Diagnosis
### 2.1 Ranked Candidate Diseases
[Researching...]
### 2.2 Disease Details
[Researching...]

---

## 3. Recommended Gene Panel
### 3.1 Prioritized Genes
[Researching...]
### 3.2 Testing Strategy
[Researching...]

---

## 4. Variant Interpretation (if applicable)
### 4.1 Variant Details
[Researching...]
### 4.2 ACMG Classification
[Researching...]

---

## 5. Structural Analysis (if applicable)
### 5.1 Structure Prediction
[Researching...]
### 5.2 Variant Impact
[Researching...]

---

## 6. Clinical Recommendations
### 6.1 Diagnostic Next Steps
[Researching...]
### 6.2 Specialist Referrals
[Researching...]
### 6.3 Family Screening
[Researching...]

---

## 7. Data Gaps & Limitations
[Researching...]

---

## 8. Data Sources
[Will be populated as research progresses...]
"""
    with open(filename, 'w') as f:
        f.write(content)
    return filename

def main():
    parser = argparse.ArgumentParser(description='Rare Disease Diagnosis Workflow Scaffolder.')
    parser.add_argument('patient_id', help='Identifier for the patient')

    args = parser.parse_args()

    print(f"Initializing diagnostic workflow for patient: {args.patient_id}")
    report_file = create_initial_report(args.patient_id)
    print(f"Created initial report: {report_file}")
    
    print("\nNext steps:")
    print("1. Standardize phenotype by converting symptoms to HPO terms.")
    print("2. Match diseases using Orphanet and OMIM tools.")
    print("3. Identify and prioritize a gene panel using ClinGen.")
    print("4. (Optional) Interpret variants using ClinVar and gnomAD.")
    print(f"Update {report_file} as you gather evidence.")

if __name__ == "__main__":
    main()
