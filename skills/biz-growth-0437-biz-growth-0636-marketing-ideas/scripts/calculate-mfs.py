#!/usr/bin/env python3
import sys
import argparse
import json

def calculate_mfs(impact, fit, speed, effort, cost):
    """
    Calculates Marketing Feasibility Score (MFS).
    MFS = (Impact + Fit + Speed) - (Effort + Cost)
    Score Range: -7 to +13
    """
    mfs = (impact + fit + speed) - (effort + cost)

    meaning = ""
    action = ""
    if mfs >= 10:
        meaning = "Extremely high leverage"
        action = "Do now"
    elif mfs >= 7:
        meaning = "Strong opportunity"
        action = "Prioritize"
    elif mfs >= 4:
        meaning = "Viable but situational"
        action = "Test selectively"
    elif mfs >= 1:
        meaning = "Marginal"
        action = "Defer"
    else:
        meaning = "Poor fit"
        action = "Do not recommend"

    return mfs, meaning, action

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate Marketing Feasibility Score (MFS)")
    parser.add_argument("--impact", type=int, choices=range(1,6), required=True, help="1-5")
    parser.add_argument("--fit", type=int, choices=range(1,6), required=True, help="1-5")
    parser.add_argument("--speed", type=int, choices=range(1,6), required=True, help="1-5")
    parser.add_argument("--effort", type=int, choices=range(1,6), required=True, help="1-5 (inverted: higher is worse)")
    parser.add_argument("--cost", type=int, choices=range(1,6), required=True, help="1-5 (inverted: higher is worse)")
    parser.add_argument("--json", action="store_true", help="Output JSON")

    args = parser.parse_args()

    mfs, meaning, action = calculate_mfs(args.impact, args.fit, args.speed, args.effort, args.cost)

    if args.json:
        print(json.dumps({
            "mfs": mfs,
            "meaning": meaning,
            "action": action
        }, indent=2))
    else:
        print(f"MFS Score: {mfs:+d}")
        print(f"Meaning: {meaning}")
        print(f"Action: {action}")
