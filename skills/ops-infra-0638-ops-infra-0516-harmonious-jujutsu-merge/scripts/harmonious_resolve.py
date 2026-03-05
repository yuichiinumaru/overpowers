#!/usr/bin/env python3
import sys
import os
import re

def analyze_conflict(file_path):
    """
    Analyzes a file for Jujutsu conflict markers and provides a report.
    """
    with open(file_path, 'r') as f:
        content = f.read()

    # Jujutsu markers look like:
    # <<<<<<< conflict 1 of 1
    # %%%%%%% diff from: <rev> <msg>
    # \ \ \ \ \ \ \ to: <rev> <msg>
    # ...
    # +++++++ <rev> <msg>
    # ...
    # >>>>>>> conflict 1 of 1 ends
    
    markers = re.findall(r'<<<<<<< conflict (.*?) ends', content, re.DOTALL)
    
    if not markers:
        return {"status": "clean", "count": 0}

    return {
        "status": "conflicted",
        "count": len(markers),
        "details": markers
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: harmonious_resolve.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        sys.exit(1)

    report = analyze_conflict(file_path)
    
    if report["status"] == "conflicted":
        print(f"⚠️ Found {report['count']} conflicts in {file_path}.")
        # In the future, this script could automagically propose resolutions
        # based on user rules or heuristics. For now, it just reports.
    else:
        print(f"✅ File {file_path} is clean.")

if __name__ == "__main__":
    main()
