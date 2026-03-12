#!/bin/bash
# Initialize a new hypothesis generation project

PROJECT_DIR=$1

if [ -z "$PROJECT_DIR" ]; then
    echo "Usage: $0 <project_directory>"
    return 1 2>/dev/null || exit 1
fi

mkdir -p "$PROJECT_DIR"
cd "$PROJECT_DIR"

# Try to copy assets if we're in the skill directory
SKILL_DIR="$(dirname "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")")"

if [ -d "$SKILL_DIR/assets" ]; then
    cp -r "$SKILL_DIR/assets/"* .
    echo "Copied template files to $PROJECT_DIR"
    echo "You can now edit the .tex files and use compile_report.sh"
else
    echo "Project directory created at $PROJECT_DIR"
    echo "Note: Could not find assets directory to copy templates."
fi
