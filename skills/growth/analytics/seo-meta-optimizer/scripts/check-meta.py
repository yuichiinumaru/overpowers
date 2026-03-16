#!/usr/bin/env python3
# Helper script to check the length of SEO meta tags

import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Check SEO meta tag lengths.")
    parser.add_argument("--title", help="Meta title to check.")
    parser.add_argument("--description", help="Meta description to check.")

    args = parser.parse_args()

    if not args.title and not args.description:
        print("Please provide at least one of --title or --description.")
        sys.exit(1)

    print("## SEO Meta Tag Check")

    if args.title:
        length = len(args.title)
        print(f"\n**Meta Title:** {args.title}")
        print(f"**Length:** {length} characters")
        if length < 50:
            print("❌ Too short. Recommended: 50-60 characters.")
        elif length > 60:
            print("❌ Too long. Recommended: 50-60 characters.")
        else:
            print("✅ Perfect length (50-60 characters).")

    if args.description:
        length = len(args.description)
        print(f"\n**Meta Description:** {args.description}")
        print(f"**Length:** {length} characters")
        if length < 150:
            print("❌ Too short. Recommended: 150-160 characters.")
        elif length > 160:
            print("❌ Too long. Recommended: 150-160 characters.")
        else:
            print("✅ Perfect length (150-160 characters).")

if __name__ == "__main__":
    main()
