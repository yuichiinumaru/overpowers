#!/usr/bin/env python3
"""
Fetch failing CI runs for a PR using gh CLI.
Usage: inspect_pr_checks.py --repo <owner/repo> --pr <pr-number> [--json] [--max-lines 200] [--context 40]
"""

import subprocess
import json
import sys
import argparse
import re


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
    cmd = ["gh", "pr", "view"]
    if pr_num:
        cmd.append(str(pr_num))
    cmd.extend(["--json", "statusCheckRollup"])

    if repo and repo != ".":
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
            url = check.get("detailsUrl", "")
            run_id = None
            if url and "/runs/" in url:
                run_id_match = re.search(r"/runs/(\d+)", url)
                if run_id_match:
                    run_id = run_id_match.group(1)

            failing.append(
                {
                    "name": check.get("name", "Unknown"),
                    "state": state,
                    "category": check.get("__typename", check.get("type", "Unknown")),
                    "url": url,
                    "run_id": run_id,
                }
            )

    return failing


def get_run_logs(run_id, repo=None, max_lines=200):
    cmd = ["gh", "run", "view", run_id, "--log"]
    if repo and repo != ".":
        cmd.extend(["--repo", repo])

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        return f"Error fetching logs for run {run_id}: {result.stderr}"

    lines = result.stdout.splitlines()
    if len(lines) > max_lines:
        return "\n".join(lines[-max_lines:])
    return result.stdout


def main():
    parser = argparse.ArgumentParser(description="Fetch failing CI runs for a PR")
    parser.add_argument("--pr", help="PR number or URL", default="")
    parser.add_argument("--repo", help="Repository (owner/repo or path)", default=".")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")
    parser.add_argument("--max-lines", type=int, default=200, help="Max log lines to fetch")
    parser.add_argument("--context", type=int, default=40, help="Lines of context around failures (currently aliased to max-lines logic)")
    args = parser.parse_args()

    check_gh()

    pr_ref = args.pr
    if "github.com" in pr_ref and "/pull/" in pr_ref:
        pr_ref = pr_ref.split("/pull/")[-1].split("/")[0]

    failing = get_failing_checks(pr_ref, args.repo)

    if not failing:
        if args.json:
            print(json.dumps([]))
        else:
            print("No failing checks found!")
        sys.exit(0)

    for check in failing:
        if check["run_id"]:
            check["log_snippet"] = get_run_logs(check["run_id"], args.repo, args.max_lines)

    if args.json:
        print(json.dumps(failing, indent=2))
    else:
        for check in failing:
            print(f"--- Check: {check['name']} ({check['state']}) ---")
            print(f"URL: {check['url']}")
            if "log_snippet" in check:
                print("Logs:")
                print(check["log_snippet"])
            print("-" * 40)
        sys.exit(1)


if __name__ == "__main__":
    main()
