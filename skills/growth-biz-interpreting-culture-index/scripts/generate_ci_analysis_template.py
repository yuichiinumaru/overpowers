#!/usr/bin/env python3
"""
Culture Index Analysis Template Generator
Outputs a standard markdown template for analyzing a Culture Index profile.
"""
import sys
import argparse

def generate_template(name, role):
    """
    Generate standard analysis template.
    """
    print(f"# Culture Index Analysis for {name}")
    if role:
        print(f"**Role:** {role}\n")

    print("## 1. Profile Summary")
    print("**(Insert general profile type here: Visionary, Specialist, etc.)**")
    print("- **A (Autonomy):** [Score relative to arrow]")
    print("- **B (Social):** [Score relative to arrow]")
    print("- **C (Pace):** [Score relative to arrow]")
    print("- **D (Conformity):** [Score relative to arrow]\n")

    print("## 2. Key Traits & Tendencies")
    print("### Strengths")
    print("- ")
    print("- ")
    print("### Potential Blind Spots / Areas for Coaching")
    print("- ")
    print("- \n")

    print("## 3. Ideal Work Environment")
    print("- **Gas (What motivates them):** ")
    print("- **Brake (What demotivates them):** \n")

    print("## 4. Communication Style")
    print("- **How to speak to them:** ")
    print("- **How they communicate:** \n")

    print("## 5. Management & Coaching Tips")
    print("- **Best way to manage:** ")
    print("- **Potential conflicts to watch out for:** ")

def main():
    parser = argparse.ArgumentParser(description="Culture Index Analysis Template Generator")
    parser.add_argument("--name", required=True, help="Name of the individual")
    parser.add_argument("--role", help="Role or job title")

    args = parser.parse_args()

    generate_template(args.name, args.role)

if __name__ == "__main__":
    main()
