#!/usr/bin/env python3
"""
Fetch failing CI runs for a PR using gh CLI.
Usage: fetch_failing_runs.py <pr-number> [--repo owner/repo]
"""

import subprocess
import json
import sys
import argparse


def check_gh():
    """Verify gh CLI is installed and authenticated."""
    try:
        subprocess.run(["gh", "--version"], capture_output=True, check=True)
    except FileNotFoundError:
        print("Error: GitHub CLI (gh) not found. Install from https://cli.github.com/")
        sys.exit(1)

    result = subprocess.run(["gh", "auth", "status"], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: Not authenticated with GitHub CLI.\n{result.stderr}")
        sys.exit(1)


def get_failing_checks(pr_num, repo=None):
    """Get all failing checks for a PR."""
    cmd = ["gh", "pr", "view", str(pr_num), "--json", "statusCheckRollup"]
    if repo:
        cmd.extend(["--repo", repo])

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error fetching PR: {result.stderr}")
        sys.exit(1)

    data = json.loads(result.stdout)
    status = data.get("statusCheckRollup", [])

    failing = []
    for check in status:
        state = check.get("conclusion") or check.get("status", "")
        if state in ("failure", "timed_out", "cancelled"):
            failing.append(
                {
                    "name": check.get("name", "Unknown"),
                    "state": state,
                    "category": check.get("__typename", check.get("type", "Unknown")),
                    "url": check.get("detailsUrl", ""),
                }
            )

    return failing


def main():
    parser = argparse.ArgumentParser(description="Fetch failing CI runs for a PR")
    parser.add_argument("pr", help="PR number")
    parser.add_argument("--repo", help="Repository (owner/repo)")
    args = parser.parse_args()

    check_gh()

    failing = get_failing_checks(args.pr, args.repo)

    if not failing:
        print("No failing checks found!")
        sys.exit(0)

    print(json.dumps(failing, indent=2))


if __name__ == "__main__":
    main()
