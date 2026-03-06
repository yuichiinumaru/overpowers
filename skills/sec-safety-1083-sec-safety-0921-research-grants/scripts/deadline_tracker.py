#!/usr/bin/env python3
import sys

def track_deadline(project_name):
    print(f"Tracking deadlines for {project_name}...")
    print("Milestones:")
    print("- Draft 1: ...")
    print("- Final Submission: ...")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        track_deadline(sys.argv[1])
    else:
        print("Usage: python deadline_tracker.py <project_name>")
