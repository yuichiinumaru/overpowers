#!/usr/bin/env python3
"""
Quality Cost Analyzer
Analyzes Prevention, Appraisal, Internal Failure, and External Failure costs.
"""
import json
import sys

def get_quality_costs():
    return {
        "prevention_costs": 45000,
        "appraisal_costs": 32000,
        "internal_failure_costs": 15000,
        "external_failure_costs": 8000,
        "total_quality_costs": 100000,
        "currency": "USD"
    }

def print_costs():
    costs = get_quality_costs()
    print("=== QUALITY COST ANALYSIS ===")
    print(f"Total Quality Costs: {costs['total_quality_costs']} {costs['currency']}")
    print(f"  Prevention Costs: {costs['prevention_costs']} {costs['currency']} ({costs['prevention_costs']/costs['total_quality_costs']:.1%})")
    print(f"  Appraisal Costs: {costs['appraisal_costs']} {costs['currency']} ({costs['appraisal_costs']/costs['total_quality_costs']:.1%})")
    print(f"  Internal Failure Costs: {costs['internal_failure_costs']} {costs['currency']} ({costs['internal_failure_costs']/costs['total_quality_costs']:.1%})")
    print(f"  External Failure Costs: {costs['external_failure_costs']} {costs['currency']} ({costs['external_failure_costs']/costs['total_quality_costs']:.1%})")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--json":
        print(json.dumps(get_quality_costs(), indent=2))
    else:
        print_costs()
