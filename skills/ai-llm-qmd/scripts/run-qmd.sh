#!/bin/bash
# Wrapper script for qmd operations

echo "Running qmd workflow..."
echo "Checking prerequisites..."

# TODO: Add specific environment checks here

echo "Executing core logic..."
python3 "$(dirname "$0")/qmd_helper.py" "$@"

echo "Done."
