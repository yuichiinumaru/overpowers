#!/usr/bin/env python3
import argparse
import sys

def generate_audit():
    print("# Paywall and Upgrade Flow CRO Audit")
    print("\n## 1. Initial Assessment")
    context = input("Upgrade Context (e.g., Freemium -> Paid): ")
    model = input("Product Model (What's free? What's paid?): ")
    journey = input("User Journey (When does it appear?): ")
    
    print("\n## 2. Core Principles Check")
    value_before_ask = input("Value Before Ask: Has user experienced real value first? (y/n): ")
    show_dont_tell = input("Show, Don't Just Tell: Does it demonstrate paid value? (y/n): ")
    friction_free = input("Friction-Free Path: Is it easy to upgrade? (y/n): ")
    respect_no = input("Respect the No: Is it easy to continue free? (y/n): ")

    print("\n## 3. Paywall Components Audit")
    headline = input("Headline: Focus on benefits? (y/n): ")
    value_demo = input("Value Demonstration: Preview feature/outcomes? (y/n): ")
    comparison = input("Feature Comparison: Clear differences? (y/n): ")
    pricing = input("Pricing: Simple and clear? (y/n): ")
    cta = input("CTA: Specific and value-oriented? (y/n): ")
    escape = input("Escape Hatch: Clear and non-guilt-tripping? (y/n): ")

    print("\n--- AUDIT SUMMARY ---")
    print(f"Context: {context}")
    print(f"Model: {model}")
    print(f"Journey: {journey}")
    
    print("\nRecommendations:")
    if value_before_ask.lower() != 'y':
        print("- Consider moving the trigger point to after a value-delivering action.")
    if show_dont_tell.lower() != 'y':
        print("- Add screenshots, videos, or previews of the Pro features in action.")
    if headline.lower() != 'y':
        print("- Rewrite the headline to focus on user benefits rather than the transaction.")
    if respect_no.lower() != 'y' or escape.lower() != 'y':
        print("- Ensure the close button or 'continue free' option is easily visible to maintain trust.")
    
    print("\nExperiment Ideas:")
    print("- Test trigger timing: immediately on click vs. after 3 attempts.")
    print("- Test headline variations focusing on different benefits.")
    print("- Test annual vs. monthly price anchoring.")

if __name__ == "__main__":
    try:
        generate_audit()
    except KeyboardInterrupt:
        print("\nAudit cancelled.")
        sys.exit(0)
