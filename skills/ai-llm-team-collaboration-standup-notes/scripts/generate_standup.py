#!/usr/bin/env python3
import subprocess
import sys
from datetime import datetime

def get_git_commits(days=1):
    try:
        # Get commits since yesterday (or N days)
        cmd = ["git", "log", f"--since={days} days ago", "--oneline", "--author=$(git config user.email)"]
        # Note: author filter needs expansion in subshell
        result = subprocess.run(f"git log --since='{days} days ago' --oneline --author=\"$(git config user.email)\"", 
                                shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Error fetching commits: {e}"

def generate_standup_notes():
    today = datetime.now().strftime("%Y-%m-%d")
    commits = get_git_commits()
    
    print(f"# Standup Notes - {today}")
    print("\n## Yesterday / Since Last Standup")
    if commits:
        for line in commits.split('\n'):
            print(f"- {line}")
    else:
        print("- [Describe work done]")
        
    print("\n## Today")
    print("- [Task 1]")
    print("- [Task 2]")
    
    print("\n## Blockers")
    print("- None")

if __name__ == "__main__":
    generate_standup_notes()
