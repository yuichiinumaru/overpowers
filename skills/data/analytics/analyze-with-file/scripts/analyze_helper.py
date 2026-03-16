#!/usr/bin/env python3
import json
import os
import datetime
import argparse
import sys

def init_analysis(topic, output_dir="."):
    """Initialize a new analysis session."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    session_id = f"analysis_{timestamp}"
    session_dir = os.path.join(output_dir, session_id)

    os.makedirs(session_dir, exist_ok=True)

    # Create discussion.md
    discussion_path = os.path.join(session_dir, "discussion.md")
    with open(discussion_path, "w") as f:
        f.write(f"# Analysis Session: {topic}\n")
        f.write(f"Session ID: {session_id}\n")
        f.write(f"Started: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("## Initial Context\n")
        f.write("Topic pending analysis...\n\n")
        f.write("## Discussion Timeline\n\n")
        f.write("## Current Understanding\n\n")

    print(f"Initialized analysis session at {session_dir}")
    return session_dir

def add_round(session_dir, round_num, user_input, findings, insights):
    """Add a discussion round to discussion.md."""
    discussion_path = os.path.join(session_dir, "discussion.md")
    if not os.path.exists(discussion_path):
        print(f"Error: No discussion.md found in {session_dir}", file=sys.stderr)
        return False

    timestamp = datetime.datetime.now().strftime("%H:%M:%S")

    with open(discussion_path, "a") as f:
        f.write(f"### Round {round_num} (Added {timestamp})\n\n")
        f.write(f"#### User Input\n{user_input}\n\n")

        f.write("#### Analysis Results\n")
        for finding in findings:
            f.write(f"- {finding}\n")
        f.write("\n")

        f.write("#### Insights\n")
        for insight in insights:
            f.write(f"- {insight}\n")
        f.write("\n")

    print(f"Added Round {round_num} to {discussion_path}")
    return True

def generate_tasks(session_dir, recommendations):
    """Generate tasks.jsonl from recommendations."""
    tasks_path = os.path.join(session_dir, "tasks.jsonl")

    with open(tasks_path, "w") as f:
        for i, rec in enumerate(recommendations, 1):
            task = {
                "id": f"TASK-{i}",
                "description": rec.get("description", ""),
                "convergence_criteria": rec.get("criteria", []),
                "provenance": rec.get("source", "analysis")
            }
            f.write(json.dumps(task) + "\n")

    print(f"Generated tasks.jsonl at {tasks_path}")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze-with-file Helper")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Init parser
    init_parser = subparsers.add_parser("init", help="Initialize analysis session")
    init_parser.add_argument("--topic", required=True, help="Topic to analyze")
    init_parser.add_argument("--outdir", default=".", help="Output directory")

    # Add round parser
    round_parser = subparsers.add_parser("add-round", help="Add discussion round")
    round_parser.add_argument("--session", required=True, help="Session directory")
    round_parser.add_argument("--num", required=True, type=int, help="Round number")
    round_parser.add_argument("--input", required=True, help="User input")
    round_parser.add_argument("--findings", nargs="*", default=[], help="Findings list")
    round_parser.add_argument("--insights", nargs="*", default=[], help="Insights list")

    # Generate tasks parser
    tasks_parser = subparsers.add_parser("tasks", help="Generate tasks.jsonl")
    tasks_parser.add_argument("--session", required=True, help="Session directory")
    # For a real script, we'd pass a JSON file of recommendations, but for the helper
    # we'll just create a dummy one if called

    args = parser.parse_args()

    if args.command == "init":
        init_analysis(args.topic, args.outdir)
    elif args.command == "add-round":
        add_round(args.session, args.num, args.input, args.findings, args.insights)
    elif args.command == "tasks":
        dummy_recs = [
            {"description": "Implement feature X", "criteria": ["Tests pass"], "source": "Round 1"},
            {"description": "Refactor module Y", "criteria": ["No regressions"], "source": "Round 2"}
        ]
        generate_tasks(args.session, dummy_recs)
    else:
        parser.print_help()
        sys.exit(1)
