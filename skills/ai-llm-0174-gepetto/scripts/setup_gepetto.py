#!/usr/bin/env python3
"""
setup_gepetto.py
Validates the spec file input and initializes the planning session directory
as per the Gepetto skill guidelines.
"""
import sys
import os

def print_help():
    help_text = """
═══════════════════════════════════════════════════════════════
GEPETTO: Spec File Required
═══════════════════════════════════════════════════════════════

This skill requires a markdown spec file path (must end with .md).
The planning directory is inferred from the spec file's parent directory.

To start a NEW plan:
  1. Create a markdown spec file describing what you want to build
  2. It can be as detailed or as vague as you like
  3. Place it in a directory where gepetto can save planning files
  4. Run: python setup_gepetto.py <path/to/your-spec.md>

To RESUME an existing plan:
  1. Run: python setup_gepetto.py <path/to/your-spec.md>

Example: python setup_gepetto.py planning/my-feature-spec.md
═══════════════════════════════════════════════════════════════
"""
    print(help_text)

def determine_mode(planning_dir, spec_file):
    expected_files = [
        "claude-research.md",
        "claude-interview.md",
        "claude-spec.md",
        "claude-plan.md",
        "claude-integration-notes.md",
        "claude-ralph-loop-prompt.md",
        "claude-ralphy-prd.md"
    ]

    found_files = []
    for f in expected_files:
        if os.path.exists(os.path.join(planning_dir, f)):
            found_files.append(f)

    sections_dir = os.path.join(planning_dir, "sections")
    reviews_dir = os.path.join(planning_dir, "reviews")

    if os.path.exists(sections_dir) and os.path.exists(os.path.join(sections_dir, "index.md")):
        found_files.append("sections/index.md")

    if os.path.exists(reviews_dir):
        found_files.append("reviews/")

    mode = "new"
    resume_step = 4

    if "claude-ralph-loop-prompt.md" in found_files and "claude-ralphy-prd.md" in found_files:
        mode = "complete"
        resume_step = "Done"
    elif "sections/index.md" in found_files:
        mode = "resume"
        resume_step = 14
    elif "claude-integration-notes.md" in found_files:
        mode = "resume"
        resume_step = 12
    elif "reviews/" in found_files:
        mode = "resume"
        resume_step = 11
    elif "claude-plan.md" in found_files:
        mode = "resume"
        resume_step = 10
    elif "claude-spec.md" in found_files:
        mode = "resume"
        resume_step = 9
    elif "claude-interview.md" in found_files:
        mode = "resume"
        resume_step = 8
    elif "claude-research.md" in found_files:
        mode = "resume"
        resume_step = 6

    return mode, resume_step

def main():
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    spec_path = sys.argv[1]

    if not spec_path.endswith('.md'):
        print_help()
        sys.exit(1)

    if not os.path.exists(spec_path):
        print(f"Error: Spec file '{spec_path}' does not exist.")
        sys.exit(1)

    planning_dir = os.path.dirname(os.path.abspath(spec_path))
    if not planning_dir:
        planning_dir = "."

    mode, resume_step = determine_mode(planning_dir, spec_path)

    print(f"Planning directory: {planning_dir}")
    print(f"Mode: {mode}")

    if mode == "resume":
        print(f"Resuming from step {resume_step}")
        print("To start fresh, delete the planning directory files.")
    elif mode == "new":
        print("Starting a new planning session.")

if __name__ == "__main__":
    main()
