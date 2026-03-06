#!/usr/bin/env python3
import sys
import argparse
import json

def calculate_energy_utilization(survey_eu, job_eu):
    """
    Calculates Energy Utilization based on Survey EU and Job EU.
    Returns the percentage and the interpretation.
    """
    if survey_eu == 0:
        return 0, "ERROR: Survey EU cannot be zero"

    utilization = (job_eu / survey_eu) * 100

    if utilization > 130:
        status = "STRESS (burnout risk)"
    elif utilization < 70:
        status = "FRUSTRATION (flight risk)"
    else:
        status = "Healthy"

    return utilization, status

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate Culture Index Energy Utilization")
    parser.add_argument("--survey_eu", type=float, required=True, help="Survey Energy Units")
    parser.add_argument("--job_eu", type=float, required=True, help="Job Energy Units")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")

    args = parser.parse_args()

    util, status = calculate_energy_utilization(args.survey_eu, args.job_eu)

    if args.json:
        result = {
            "survey_eu": args.survey_eu,
            "job_eu": args.job_eu,
            "utilization_percent": round(util, 2),
            "status": status
        }
        print(json.dumps(result, indent=2))
    else:
        print(f"Energy Utilization: {util:.2f}%")
        print(f"Status: {status}")
