#!/usr/bin/env python3
"""
Competitor Matrix Generator
Creates a markdown template for competitive analysis.
"""
import sys
import argparse

def generate_matrix(competitors, features):
    """
    Generate a markdown table for competitor analysis.
    """
    print("# Competitive Analysis Matrix\n")

    # Header row
    header = "| Feature/Criterion | " + " | ".join(competitors) + " |"
    print(header)

    # Separator row
    separator = "|---|" + "|".join(["---" for _ in competitors]) + "|"
    print(separator)

    # Feature rows
    for feature in features:
        row = f"| {feature} | " + " | ".join([" " for _ in competitors]) + " |"
        print(row)

def main():
    parser = argparse.ArgumentParser(description="Competitor Matrix Generator")
    parser.add_argument("--competitors", nargs="+", required=True, help="List of competitors to analyze (e.g., 'Company A' 'Company B' 'Company C')")
    parser.add_argument("--features", nargs="+", required=True, help="List of features or criteria to compare (e.g., 'Price' 'Key Feature' 'Market Share')")

    args = parser.parse_args()

    generate_matrix(args.competitors, args.features)

if __name__ == "__main__":
    main()
