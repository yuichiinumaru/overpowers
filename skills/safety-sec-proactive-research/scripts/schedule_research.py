#!/usr/bin/env python3
# Script to schedule proactive research tasks
import argparse
import datetime

def main():
    parser = argparse.ArgumentParser(description="Schedule proactive research.")
    parser.add_argument("--topic", required=True, help="Topic to research")
    parser.add_argument("--frequency", default="daily", help="Research frequency")
    args = parser.parse_args()

    print(f"Scheduled research for '{args.topic}' with frequency: {args.frequency}")
    print(f"Next run at: {datetime.datetime.now() + datetime.timedelta(days=1)}")

if __name__ == "__main__":
    main()
