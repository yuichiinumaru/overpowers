#!/usr/bin/env python3
import sys
import argparse
import json

def calculate_readiness_index(decision, event_model, data_accuracy, conversion, attribution, governance):
    """
    Calculates the Measurement Readiness & Signal Quality Index based on SKILL.md weights.
    Categories:
    - Decision Alignment (0-25)
    - Event Model Clarity (0-20)
    - Data Accuracy & Integrity (0-20)
    - Conversion Definition Quality (0-15)
    - Attribution & Context (0-10)
    - Governance & Maintenance (0-10)
    """
    # Clamp values to their maximums
    decision = min(max(0, decision), 25)
    event_model = min(max(0, event_model), 20)
    data_accuracy = min(max(0, data_accuracy), 20)
    conversion = min(max(0, conversion), 15)
    attribution = min(max(0, attribution), 10)
    governance = min(max(0, governance), 10)

    total_score = decision + event_model + data_accuracy + conversion + attribution + governance

    verdict = ""
    interpretation = ""

    if total_score >= 85:
        verdict = "Measurement-Ready"
        interpretation = "Safe to optimize and experiment"
    elif total_score >= 70:
        verdict = "Usable with Gaps"
        interpretation = "Fix issues before major decisions"
    elif total_score >= 55:
        verdict = "Unreliable"
        interpretation = "Data cannot be trusted yet"
    else:
        verdict = "Broken"
        interpretation = "Do not act on this data. Stop and recommend remediation first."

    return {
        "score": total_score,
        "verdict": verdict,
        "interpretation": interpretation,
        "breakdown": {
            "Decision Alignment (max 25)": decision,
            "Event Model Clarity (max 20)": event_model,
            "Data Accuracy & Integrity (max 20)": data_accuracy,
            "Conversion Definition Quality (max 15)": conversion,
            "Attribution & Context (max 10)": attribution,
            "Governance & Maintenance (max 10)": governance
        }
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate Measurement Readiness & Signal Quality Index")
    parser.add_argument("--decision", type=float, required=True, help="Decision Alignment score (0-25)")
    parser.add_argument("--event", type=float, required=True, help="Event Model Clarity score (0-20)")
    parser.add_argument("--accuracy", type=float, required=True, help="Data Accuracy & Integrity score (0-20)")
    parser.add_argument("--conversion", type=float, required=True, help="Conversion Definition Quality score (0-15)")
    parser.add_argument("--attribution", type=float, required=True, help="Attribution & Context score (0-10)")
    parser.add_argument("--governance", type=float, required=True, help="Governance & Maintenance score (0-10)")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")

    args = parser.parse_args()

    results = calculate_readiness_index(
        args.decision, args.event, args.accuracy,
        args.conversion, args.attribution, args.governance
    )

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print("\n=== Measurement Readiness & Signal Quality Index ===")
        print(f"Total Score: {results['score']}/100")
        print(f"Verdict: {results['verdict']}")
        print(f"Interpretation: {results['interpretation']}")
        print("\n--- Breakdown ---")
        for category, score in results['breakdown'].items():
            print(f"- {category}: {score}")

        if results['verdict'] == "Broken":
            print("\n⚠️ WARNING: Measurement setup is broken. Do not proceed with tracking changes until remediated.")
