#!/usr/bin/env python3
import os
import subprocess
import argparse
import sys

def get_git_commits(since=None, until=None):
    cmd = ["git", "log", "--pretty=format:%h - %s (%an)"]
    if since:
        cmd.extend(["--since", since])
    if until:
        cmd.extend(["--until", until])

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout.splitlines()
    except subprocess.CalledProcessError as e:
        print(f"Error getting git commits: {e}")
        return []

def main():
    parser = argparse.ArgumentParser(description="Changelog Generator")
    parser.add_argument("--since", help="Show commits more recent than a specific date")
    parser.add_argument("--until", help="Show commits older than a specific date")
    parser.add_argument("--output", default="CHANGELOG_DRAFT.md", help="Output file")

    args = parser.parse_args()

    print(f"Generating changelog...")
    commits = get_git_commits(args.since, args.until)

    if not commits:
        print("No commits found.")
        sys.exit(0)

    print(f"Found {len(commits)} commits. Saving draft to {args.output}...")

    with open(args.output, "w") as f:
        f.write("# Changelog Draft\n\n")
        f.write("## New Features\n\n")
        f.write("## Bug Fixes\n\n")
        f.write("## Improvements\n\n")
        f.write("## Raw Commits\n")
        for commit in commits:
            f.write(f"- {commit}\n")

    print(f"Done! Please review and edit {args.output}")

if __name__ == "__main__":
    main()
