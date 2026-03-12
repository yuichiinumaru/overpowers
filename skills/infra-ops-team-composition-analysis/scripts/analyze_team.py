#!/usr/bin/env python3
import argparse

def analyze_team(stage):
    print(f"Analyzing team composition for stage: {stage}")
    print("Recommendation: 1 Product Manager, 3 Software Engineers, 1 Designer.")

def main():
    parser = argparse.ArgumentParser(description="Team Composition Analysis")
    parser.add_argument("--stage", choices=["Pre-Seed", "Seed", "Series A"], required=True)
    args = parser.parse_args()
    analyze_team(args.stage)

if __name__ == "__main__":
    main()
