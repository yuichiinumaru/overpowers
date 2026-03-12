#!/usr/bin/env python3
import argparse

def draft_post(platform, content):
    print(f"Drafting post for: {platform}")
    print("-" * 40)
    if platform == "LinkedIn":
        print(f"{content}\n\n#Feature #Update")
    elif platform == "Twitter":
        print(f"{content[:280]}")
    elif platform == "Reddit":
        print(f"Technical Implementation: {content}")
    print("-" * 40)

def main():
    parser = argparse.ArgumentParser(description="Social Media Drafter")
    parser.add_argument("--platform", choices=["LinkedIn", "Twitter", "Reddit"], required=True)
    parser.add_argument("--content", required=True)
    args = parser.parse_args()
    draft_post(args.platform, args.content)

if __name__ == "__main__":
    main()
