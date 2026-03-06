#!/usr/bin/env python3
import json
import argparse
import sys

def generate_competitive_matrix(competitors, features, outfile):
    """Generates a skeleton JSON or Markdown matrix for competitive landscape analysis."""

    matrix = {}
    for comp in competitors:
        matrix[comp] = {feature: "TBD" for feature in features}

    if outfile.endswith(".json"):
        with open(outfile, 'w') as f:
            json.dump(matrix, f, indent=2)
        print(f"Generated JSON matrix at {outfile}")
    elif outfile.endswith(".md"):
        with open(outfile, 'w') as f:
            f.write("# Competitive Analysis Matrix\n\n")

            # Header
            header = "| Competitor | " + " | ".join(features) + " |"
            f.write(header + "\n")

            # Separator
            separator = "|-" + "-|-".join(["-" * len(f) for f in features]) + "-|"
            separator = "|---|-" + "-|-".join(["-" * len(f) for f in features]) + "-|"

            separator = "|---|" + "|".join(["---" for _ in features]) + "|"
            f.write(separator + "\n")

            # Rows
            for comp in competitors:
                row = f"| **{comp}** | " + " | ".join(["TBD" for _ in features]) + " |"
                f.write(row + "\n")
        print(f"Generated Markdown matrix at {outfile}")
    else:
        print("Error: Output file must be .json or .md")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a competitive landscape matrix skeleton.")
    parser.add_argument("--competitors", nargs='+', required=True, help="List of competitors")
    parser.add_argument("--features", nargs='+', required=True, help="List of features to compare")
    parser.add_argument("--out", required=True, help="Output file (must end in .json or .md)")

    args = parser.parse_args()
    generate_competitive_matrix(args.competitors, args.features, args.out)
