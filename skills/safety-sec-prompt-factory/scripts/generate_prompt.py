#!/usr/bin/env python3
# Script to generate a prompt based on a template
import argparse

def main():
    parser = argparse.ArgumentParser(description="Generate a prompt.")
    parser.add_argument("--template", required=True, help="Prompt template name")
    parser.add_argument("--variables", help="Comma-separated variables (e.g., key=value)")
    args = parser.parse_args()

    print(f"Generating prompt using template: {args.template}")
    if args.variables:
        print(f"Applying variables: {args.variables}")

if __name__ == "__main__":
    main()
