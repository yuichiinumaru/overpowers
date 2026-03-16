#!/usr/bin/env python3
"""
Initialize a gepetto planning session from a spec file
"""
import sys
import os
import glob

def main():
    if len(sys.argv) < 2:
        print("Usage: python gepetto_init.py <path_to_spec.md>")
        print("Must provide a spec file path ending in .md")
        sys.exit(1)

    spec_file = sys.argv[1]

    if not spec_file.endswith(".md"):
        print("Error: Spec file must end with .md")
        sys.exit(1)

    if not os.path.exists(spec_file):
        print(f"Error: Spec file not found at {spec_file}")
        sys.exit(1)

    planning_dir = os.path.dirname(os.path.abspath(spec_file))

    print("═══════════════════════════════════════════════════════════════")
    print("GEPETTO: Session Initialized")
    print("═══════════════════════════════════════════════════════════════")
    print(f"Planning directory: {planning_dir}")
    print(f"Spec file: {spec_file}")
    print("")

    # Scan for existing planning files to determine mode
    if os.path.exists(os.path.join(planning_dir, "claude-research.md")):
        mode = "resume"

        if os.path.exists(os.path.join(planning_dir, "claude-ralph-loop-prompt.md")) and \
           os.path.exists(os.path.join(planning_dir, "claude-ralphy-prd.md")):
            print("Mode: complete")
            print("Planning is already complete.")
        elif os.path.exists(os.path.join(planning_dir, "sections", "index.md")):
            print("Mode: resume")
            print("Resuming from section files...")
        elif os.path.exists(os.path.join(planning_dir, "claude-integration-notes.md")):
            print("Mode: resume")
            print("Resuming from integrated plan...")
        elif os.path.exists(os.path.join(planning_dir, "reviews")) and \
             os.path.isdir(os.path.join(planning_dir, "reviews")):
            print("Mode: resume")
            print("Resuming from external reviews...")
        elif os.path.exists(os.path.join(planning_dir, "claude-plan.md")):
            print("Mode: resume")
            print("Resuming from plan review...")
        elif os.path.exists(os.path.join(planning_dir, "claude-spec.md")):
            print("Mode: resume")
            print("Resuming from implementation plan generation...")
        elif os.path.exists(os.path.join(planning_dir, "claude-interview.md")):
            print("Mode: resume")
            print("Resuming from spec synthesis...")
        else:
            print("Mode: resume")
            print("Resuming from interview phase...")
    else:
        mode = "new"
        print("Mode: new")
        print("Starting a fresh planning session.")

        # Create necessary directories
        os.makedirs(os.path.join(planning_dir, "sections"), exist_ok=True)
        os.makedirs(os.path.join(planning_dir, "reviews"), exist_ok=True)

    print("")
    print(f"To reset state, delete planning files in {planning_dir}")
    print("═══════════════════════════════════════════════════════════════")

if __name__ == "__main__":
    main()
