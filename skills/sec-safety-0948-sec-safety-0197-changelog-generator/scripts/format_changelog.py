import sys
import re

def categorize_commits(commits):
    categories = {
        "Features": [],
        "Improvements": [],
        "Fixes": [],
        "Security": [],
        "Other": []
    }
    
    for commit in commits:
        commit = commit.strip()
        if not commit: continue
        
        lower_commit = commit.lower()
        if any(kw in lower_commit for kw in ["feat", "new", "add"]):
            categories["Features"].append(commit)
        elif any(kw in lower_commit for kw in ["fix", "bug", "resolved"]):
            categories["Fixes"].append(commit)
        elif any(kw in lower_commit for kw in ["perf", "refactor", "improve", "update"]):
            categories["Improvements"].append(commit)
        elif any(kw in lower_commit for kw in ["sec", "vulnerability", "cve"]):
            categories["Security"].append(commit)
        else:
            categories["Other"].append(commit)
            
    return categories

def format_markdown(categories):
    output = "# Changelog\n\n"
    for cat, commits in categories.items():
        if commits:
            output += f"## {cat}\n"
            for c in commits:
                output += f"{c}\n"
            output += "\n"
    return output

if __name__ == "__main__":
    commits = sys.stdin.readlines()
    categories = categorize_commits(commits)
    print(format_markdown(categories))
