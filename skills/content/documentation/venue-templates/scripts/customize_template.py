#!/usr/bin/env python3
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Customize Venue Template")
    parser.add_argument("--template", required=True, help="Path to template file")
    parser.add_argument("--title", help="Paper title")
    parser.add_argument("--authors", help="Authors list")
    parser.add_argument("--affiliations", help="Affiliations")
    parser.add_argument("--email", help="Contact email")
    parser.add_argument("--output", required=True, help="Output filename")

    args = parser.parse_args()

    if not os.path.exists(args.template):
        print(f"Error: Template {args.template} not found.")
        return

    with open(args.template, 'r') as f:
        content = f.read()

    if args.title:
        content = content.replace("TITLE_PLACEHOLDER", args.title)
    if args.authors:
        content = content.replace("AUTHORS_PLACEHOLDER", args.authors)
    if args.affiliations:
        content = content.replace("AFFILIATIONS_PLACEHOLDER", args.affiliations)
    if args.email:
        content = content.replace("EMAIL_PLACEHOLDER", args.email)

    with open(args.output, 'w') as f:
        f.write(content)

    print(f"Successfully saved customized template to: {args.output}")

if __name__ == "__main__":
    main()
