#!/bin/bash

# Wrapper for Dify component analysis and refactoring commands
# Assumes existence of 'pnpm analyze-component' and 'pnpm refactor-component' in web/

set -e

PATH_TO_COMPONENT=$1
MODE=$2 # "analyze" or "refactor"

if [ -z "$PATH_TO_COMPONENT" ]; then
    echo "Usage: ./analyze_component.sh <relative_path_to_component> [analyze|refactor]"
    exit 1
fi

MODE=${MODE:-"analyze"}

# Navigate to web directory (adjust if needed based on root context)
# Assuming this script is run from project root or skill scripts folder
PROJECT_ROOT=$(git rev-parse --show-toplevel 2>/dev/null || pwd)
cd "$PROJECT_ROOT/web" 2>/dev/null || { echo "Error: web/ directory not found."; exit 1; }

if [ "$MODE" == "refactor" ]; then
    echo "Generating refactoring prompt for $PATH_TO_COMPONENT..."
    pnpm refactor-component "$PATH_TO_COMPONENT"
else
    echo "Analyzing complexity for $PATH_TO_COMPONENT..."
    pnpm analyze-component "$PATH_TO_COMPONENT" --json
fi
