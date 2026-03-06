#!/usr/bin/env python3
import sys
import argparse

def calculate_plfs(leverage, fit, speed, ethics, cost):
    # PLFS = (Leverage + Fit + Speed + Ethics) − Implementation Cost
    score = (leverage + fit + speed + ethics) - cost
    return min(max(score, -5), 15)

def get_interpretation(score):
    if score >= 12:
        return "High-confidence lever - Apply immediately"
    elif score >= 8:
        return "Strong - Prioritize"
    elif score >= 4:
        return "Situational - Test carefully"
    elif score >= 1:
        return "Weak - Defer"
    else:
        return "Risky / low value - Do not recommend"

def main():
    parser = argparse.ArgumentParser(description="Calculate PLFS for a mental model.")
    parser.add_argument("model", help="Name of the mental model")
    parser.add_argument("--leverage", type=int, choices=range(1, 6), required=True, help="Behavioral Leverage (1-5)")
    parser.add_argument("--fit", type=int, choices=range(1, 6), required=True, help="Context Fit (1-5)")
    parser.add_argument("--speed", type=int, choices=range(1, 6), required=True, help="Speed to Signal (1-5)")
    parser.add_argument("--ethics", type=int, choices=range(1, 6), required=True, help="Ethical Safety (1-5)")
    parser.add_argument("--cost", type=int, choices=range(1, 6), required=True, help="Implementation Cost (1-5)")
    
    parser.add_argument("--behavior", help="Target behavior")
    parser.add_argument("--where", help="Where to apply")
    
    args = parser.parse_args()

    score = calculate_plfs(args.leverage, args.fit, args.speed, args.ethics, args.cost)
    interpretation = get_interpretation(score)

    print(f"\n### Mental Model: {args.model}")
    print(f"**PLFS:** `{score:+}` ({interpretation})")
    
    if args.behavior:
        print(f"\n* **Behavior targeted**\n  {args.behavior}")
    
    if args.where:
        print(f"\n* **Where to apply**\n  {args.where}")
    
    print("\n* **Scoring Breakdown:**")
    print(f"  - Leverage: {args.leverage}")
    print(f"  - Fit: {args.fit}")
    print(f"  - Speed: {args.speed}")
    print(f"  - Ethics: {args.ethics}")
    print(f"  - Cost: {args.cost}")

if __name__ == "__main__":
    main()
