#!/usr/bin/env python3
import subprocess
import json
import sys
import argparse

def check_gh():
    try:
        subprocess.run(["gh", "--version"], capture_output=True, check=True)
    except FileNotFoundError:
        print("Error: GitHub CLI (gh) not found. Please install it.")
        sys.exit(1)
    
    try:
        subprocess.run(["gh", "auth", "status"], capture_output=True, check=True)
    except subprocess.CalledProcessError:
        print("Error: Not authenticated with GitHub CLI. Run 'gh auth login'.")
        sys.exit(1)

def fetch_prs(repo=None, state="open", limit=1000):
    cmd = ["gh", "pr", "list", "--state", state, "--limit", str(limit), "--json", "number,title,state,createdAt,updatedAt,labels,author,headRefName,baseRefName,isDraft,mergeable,body"]
    if repo:
        cmd.extend(["--repo", repo])
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error fetching PRs: {e.stderr}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Fetch GitHub PRs using gh CLI")
    parser.add_argument("type", choices=["prs"], help="Type of data to fetch (currently only 'prs' supported)")
    parser.add_argument("--repo", help="Repository in 'owner/repo' format")
    parser.add_argument("--state", default="open", help="PR state (open, closed, merged, all)")
    parser.add_argument("--limit", type=int, default=1000, help="Maximum number of PRs to fetch")
    parser.add_argument("--output", choices=["json"], default="json", help="Output format")
    
    args = parser.parse_args()
    
    check_gh()
    
    if args.type == "prs":
        prs = fetch_prs(repo=args.repo, state=args.state, limit=args.limit)
        if prs is not None:
            print(json.dumps(prs, indent=2))
        else:
            sys.exit(1)

if __name__ == "__main__":
    main()
