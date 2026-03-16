#!/usr/bin/env python3
"""
Tracking Plan Generator
Creates a basic tracking plan structure based on input parameters.
"""
import sys
import argparse

def generate_tracking_plan(events_file):
    """
    Generate a basic tracking plan structure based on input events file.
    """
    print("# Analytics Tracking Plan")
    print("\n## Objective")
    print("Define the key events to track to ensure trustworthy signals that directly support decisions.")

    print("\n## Events")

    with open(events_file, 'r') as f:
        events = f.readlines()

    for event in events:
        event = event.strip()
        if not event:
            continue
        print(f"\n### {event}")
        print("- **Trigger:** [When does this event fire?]")
        print("- **Properties:** [What properties are sent with this event?]")
        print("- **Purpose:** [Why are we tracking this?]")

def main():
    parser = argparse.ArgumentParser(description="Analytics Tracking Plan Generator")
    parser.add_argument("--events-file", type=str, required=True, help="File containing a list of events to track, one per line.")

    args = parser.parse_args()
    generate_tracking_plan(args.events_file)

if __name__ == "__main__":
    main()
