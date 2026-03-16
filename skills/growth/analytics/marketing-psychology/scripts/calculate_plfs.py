#!/usr/bin/env python3
"""
Helper script to calculate and format the Psychological Leverage & Feasibility Score (PLFS).
"""
import argparse

def calculate_plfs(leverage, fit, speed, ethics, cost):
    # Ensure all inputs are between 1 and 5
    for val, name in [(leverage, 'leverage'), (fit, 'fit'), (speed, 'speed'), (ethics, 'ethics'), (cost, 'cost')]:
        if not 1 <= val <= 5:
            print(f"Warning: {name} should be between 1 and 5 (got {val})")

    score = (leverage + fit + speed + ethics) - cost

    # Cap score at 15 and lower bound it
    score = min(max(score, -5), 15)

    if score >= 12:
        interpretation = "High-confidence lever - Apply immediately"
    elif score >= 8:
        interpretation = "Strong - Prioritize"
    elif score >= 4:
        interpretation = "Situational - Test carefully"
    elif score >= 1:
        interpretation = "Weak - Defer"
    else:
        interpretation = "Risky / low value - Do not recommend"

    return score, interpretation

def format_model_recommendation(model_name, plfs_score, interpretation, why, behavior, where, how, test, ethics):
    template = f"""### Mental Model: {model_name}

**PLFS:** `{plfs_score:+d}` ({interpretation})

* **Why it works (psychology)**
  {why}

* **Behavior targeted**
  {behavior}

* **Where to apply**
{chr(10).join([f"  * {w}" for w in where])}

* **How to implement**
{chr(10).join([f"  {i+1}. {h}" for i, h in enumerate(how)])}

* **What to test**
{chr(10).join([f"  * {t}" for t in test])}

* **Ethical guardrail**
  {ethics}
"""
    return template

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate PLFS score")
    parser.add_argument("--leverage", type=int, required=True, help="Behavioral Leverage (1-5)")
    parser.add_argument("--fit", type=int, required=True, help="Context Fit (1-5)")
    parser.add_argument("--speed", type=int, required=True, help="Speed to Signal (1-5)")
    parser.add_argument("--ethics", type=int, required=True, help="Ethical Safety (1-5)")
    parser.add_argument("--cost", type=int, required=True, help="Implementation Cost (1-5)")

    args = parser.parse_args()
    score, interpretation = calculate_plfs(args.leverage, args.fit, args.speed, args.ethics, args.cost)

    print(f"PLFS Score: {score:+d}")
    print(f"Interpretation: {interpretation}")
