import os
import argparse
import sys

def initialize_planning_session(spec_file):
    """
    Scaffolds the Gepetto planning workflow structure based on a spec file.
    """
    if not spec_file.endswith(".md"):
        print("═══════════════════════════════════════════════════════════════")
        print("GEPETTO: Spec File Required")
        print("═══════════════════════════════════════════════════════════════\n")
        print("This skill requires a markdown spec file path (must end with .md).")
        print("The planning directory is inferred from the spec file's parent directory.\n")
        print("To start a NEW plan:")
        print("  1. Create a markdown spec file describing what you want to build")
        print("  2. It can be as detailed or as vague as you like")
        print("  3. Place it in a directory where gepetto can save planning files")
        print("  4. Run: /gepetto @path/to/your-spec.md\n")
        print("To RESUME an existing plan:")
        print("  1. Run: /gepetto @path/to/your-spec.md\n")
        print("Example: /gepetto @planning/my-feature-spec.md")
        print("═══════════════════════════════════════════════════════════════")
        sys.exit(1)

    planning_dir = os.path.dirname(os.path.abspath(spec_file))

    print(f"Planning directory: {planning_dir}")

    if not os.path.exists(spec_file):
        print(f"Creating initial spec file at {spec_file}...")
        os.makedirs(planning_dir, exist_ok=True)
        with open(spec_file, 'w') as f:
            f.write("# Initial Specification\n\nDescribe what you want to build here.")

    # Check existing files
    files_to_check = [
        "claude-research.md",
        "claude-interview.md",
        "claude-spec.md",
        "claude-plan.md",
        "claude-integration-notes.md",
        "claude-ralph-loop-prompt.md",
        "claude-ralphy-prd.md"
    ]

    dirs_to_check = [
        "reviews",
        "sections"
    ]

    found_files = []
    for filename in files_to_check:
        if os.path.exists(os.path.join(planning_dir, filename)):
            found_files.append(filename)

    for dirname in dirs_to_check:
        if os.path.exists(os.path.join(planning_dir, dirname)):
            found_files.append(dirname + "/")

    # Determine mode based on found files
    if not found_files:
        mode = "new"
        resume_step = 4
    elif set(found_files) == {"claude-research.md"}:
        mode = "resume"
        resume_step = 6
    elif set(found_files) == {"claude-research.md", "claude-interview.md"}:
        mode = "resume"
        resume_step = 8
    elif "claude-plan.md" in found_files and "reviews/" not in found_files:
        mode = "resume"
        resume_step = 10
    elif "claude-ralph-loop-prompt.md" in found_files and "claude-ralphy-prd.md" in found_files:
        mode = "complete"
        resume_step = "Done"
    else:
        # Simplistic fallback for intermediate states
        mode = "resume"
        resume_step = "Intermediate (Check docs)"

    print(f"Mode: {mode}")
    if mode == "resume":
        print(f"Resuming from step {resume_step}")
        print("To start fresh, delete the planning directory files.")

    if mode == "new":
        print(f"Ready to begin workflow at Step 4 (Research Decision) using {spec_file}")

def main():
    parser = argparse.ArgumentParser(description="Gepetto Initialization Script")
    parser.add_argument("spec_file", help="Path to the initial markdown spec file")

    args = parser.parse_args()

    initialize_planning_session(args.spec_file)

if __name__ == "__main__":
    main()
