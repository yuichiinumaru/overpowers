#!/bin/bash
# Script to bootstrap a new project

PROJECT_NAME=$1

if [ -z "$PROJECT_NAME" ]; then
    echo "Usage: $0 <project_name>"
    # Use return instead of exit for safe execution in some contexts, but here it's fine since it's a file
else
    echo "Bootstrapping project: $PROJECT_NAME"
    mkdir -p "$PROJECT_NAME"/{src,tests,docs,scripts}
    touch "$PROJECT_NAME"/README.md
    touch "$PROJECT_NAME"/.gitignore
    echo "Done."
fi
