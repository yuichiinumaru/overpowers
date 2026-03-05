#!/usr/bin/env python3
import os
import json
import time
from datetime import datetime, timedelta

def main():
    history_path = os.path.expanduser("~/.claude/history.jsonl")
    if not os.path.exists(history_path):
        print(f"[!] History file not found: {history_path}")
        return

    # past 48 hours
    cutoff = time.time() - (48 * 3600)
    recent_entries = []

    print(f"Reading recent activity from {history_path}...")
    try:
        with open(history_path, "r") as f:
            for line in f:
                try:
                    entry = json.loads(line)
                    # timestamp is in ms
                    ts = entry.get("timestamp", 0) / 1000
                    if ts > cutoff:
                        recent_entries.append(entry)
                except json.JSONDecodeError:
                    continue
    except Exception as e:
        print(f"[!] Error reading history: {e}")
        return

    if not recent_entries:
        print("No activity found in the last 48 hours.")
        return

    print(f"Found {len(recent_entries)} recent interactions.")
    
    # Simple summary
    projects = set()
    for e in recent_entries:
        if e.get("project"):
            projects.add(e["project"])
    
    print(f"Active Projects: {', '.join(projects) if projects else 'None'}")
    
    # Save to a temporary summary file for analysis
    with open("recent_activity_summary.json", "w") as f:
        json.dump(recent_entries, f, indent=2)
    print("Exported recent activity to recent_activity_summary.json")

if __name__ == "__main__":
    main()
