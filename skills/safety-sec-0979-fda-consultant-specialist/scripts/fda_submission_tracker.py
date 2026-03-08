#!/usr/bin/env python3
import sys
import os
import json
from datetime import datetime

def main():
    if len(sys.argv) < 2:
        print("Usage: fda_submission_tracker.py <project_path> [--type 510k|pma|denovo]")
        sys.exit(1)

    project_path = sys.argv[1]
    sub_type = "510k"
    if "--type" in sys.argv:
        idx = sys.argv.index("--type")
        if idx + 1 < len(sys.argv):
            sub_type = sys.argv[idx + 1]

    milestones = {
        "510k": ["Planning", "Predicate Identified", "Performance Testing", "Labeling", "eSTAR Submission", "FDA Acknowledgment", "AI Requests", "SE Letter"],
        "pma": ["Clinical Trials", "Module 1", "Module 2", "Module 3", "Final Submission", "Panel Meeting", "Approval"],
        "denovo": ["De Novo Request", "Classification", "Safety/Effectiveness Evidence", "Decision"]
    }

    print(f"--- FDA {sub_type.upper()} Submission Tracker: {project_path} ---")
    
    # Simple mockup of tracking state
    tracker_file = os.path.join(project_path, f".fda_{sub_type}_status.json")
    if os.path.exists(tracker_file):
        with open(tracker_file, "r") as f:
            status = json.load(f)
    else:
        status = {m: "Pending" for m in milestones.get(sub_type, [])}

    for m in milestones.get(sub_type, []):
        st = status.get(m, "Pending")
        icon = "[ ]" if st == "Pending" else "[x]"
        print(f"{icon} {m:<30} Status: {st}")

if __name__ == "__main__":
    main()
