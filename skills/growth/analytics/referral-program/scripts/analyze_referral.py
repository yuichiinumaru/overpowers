#!/usr/bin/env python3
import argparse
import json

def analyze_program(incentive_type, audience, program_type):
    score = 0
    recommendations = []

    # Simple heuristic analysis
    if incentive_type == "cash":
        score += 5
        recommendations.append("Cash is universally appealing but can attract low-quality referrals. Monitor fraud.")
    elif incentive_type == "discount":
        score += 8
        recommendations.append("Discounts drive product usage. Ensure the discount is significant enough (>15%).")
    elif incentive_type == "credit":
        score += 7
        recommendations.append("Credits work best for subscription or recurring purchase models.")

    if program_type == "two-sided":
        score += 10
        recommendations.append("Two-sided incentives (give X, get Y) are proven to be the most effective structure.")
    elif program_type == "one-sided":
        score += 4
        recommendations.append("One-sided incentives create friction. Consider rewarding both the referrer and referee.")

    result = {
        "score": score,
        "max_score": 20,
        "audience": audience,
        "recommendations": recommendations,
        "verdict": "Strong" if score > 12 else "Needs Improvement"
    }

    return result

def main():
    parser = argparse.ArgumentParser(description="Analyze a referral program structure")
    parser.add_argument("--incentive", choices=["cash", "discount", "credit", "swag", "other"], required=True)
    parser.add_argument("--type", choices=["one-sided", "two-sided", "tiered"], required=True)
    parser.add_argument("--audience", required=True)

    args = parser.parse_args()

    res = analyze_program(args.incentive, args.audience, args.type)
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    main()
