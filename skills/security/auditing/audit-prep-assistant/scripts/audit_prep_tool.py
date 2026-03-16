#!/usr/bin/env python3
import json
import argparse
import os

CHECKLIST = {
    "Step 1: Set Review Goals": [
        "Review goals documented",
        "Worst-case scenarios identified",
        "Key areas of concern noted"
    ],
    "Step 2: Resolve Easy Issues": [
        "Static analysis clean/triaged",
        "Test coverage >80%",
        "Dead code removed"
    ],
    "Step 3: Ensure Code Accessibility": [
        "Detailed file list provided",
        "Build instructions verified",
        "Stable version frozen/tagged",
        "Boilerplate identified"
    ],
    "Step 4: Generate Documentation": [
        "Flowcharts and diagrams created",
        "User stories documented",
        "Assumptions documented",
        "Actors and privileges mapped",
        "Glossary created"
    ]
}

def init_checklist(project_name):
    data = {
        "project": project_name,
        "status": "In Progress",
        "steps": {}
    }
    for step, tasks in CHECKLIST.items():
        data["steps"][step] = {task: False for task in tasks}
    
    filename = f"audit_prep_{project_name.lower().replace(' ', '_')}.json"
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Checklist initialized: {filename}")

def main():
    parser = argparse.ArgumentParser(description="Audit Prep Assistant Tool")
    subparsers = parser.add_argument_subparsers(dest="command")
    
    init_parser = subparsers.add_parser("init", help="Initialize a new audit prep checklist")
    init_parser.add_argument("--project", required=True, help="Project name")
    
    args = parser.parse_args()
    
    if args.command == "init":
        init_checklist(args.project)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
