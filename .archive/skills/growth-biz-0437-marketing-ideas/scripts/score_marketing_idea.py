#!/usr/bin/env python3
"""
Marketing Idea Scorer (ICE Framework)
Scores and ranks a marketing idea based on Impact, Confidence, and Ease (ICE).
"""
import sys
import argparse

def score_idea(idea_name, impact, confidence, ease):
    """
    Calculate ICE score and provide basic feedback.
    """
    # Validation
    for val in [impact, confidence, ease]:
        if not (1 <= val <= 10):
            print("Error: Scores must be between 1 and 10.", file=sys.stderr)
            sys.exit(1)

    # ICE Score is typically Average or Sum. We'll use Average for a 1-10 scale.
    ice_score = (impact + confidence + ease) / 3.0

    print(f"--- ICE Score for: '{idea_name}' ---")
    print(f"Impact:     {impact}/10")
    print(f"Confidence: {confidence}/10")
    print(f"Ease:       {ease}/10")
    print(f"-----------------------------------")
    print(f"Total ICE Score: {ice_score:.1f} / 10.0")

    # Simple logic
    print("\nRecommendation:")
    if ice_score >= 8.0:
        print("🟢 HIGH PRIORITY: Excellent idea. Do this immediately.")
    elif ice_score >= 6.0:
        print("🟡 MEDIUM PRIORITY: Good idea, but consider if there are easier/higher impact wins first.")
    else:
        print("🔴 LOW PRIORITY: Too difficult, low impact, or too risky right now. Skip or table it.")

def main():
    parser = argparse.ArgumentParser(description="ICE Framework Marketing Idea Scorer")
    parser.add_argument("--idea", required=True, help="Name or short description of the idea")
    parser.add_argument("--impact", type=int, required=True, help="Impact (1-10): How much will this move the needle if it works?")
    parser.add_argument("--confidence", type=int, required=True, help="Confidence (1-10): How sure are you it will work?")
    parser.add_argument("--ease", type=int, required=True, help="Ease (1-10): How easy is it to implement? (10=easiest)")

    args = parser.parse_args()

    score_idea(args.idea, args.impact, args.confidence, args.ease)

if __name__ == "__main__":
    main()
