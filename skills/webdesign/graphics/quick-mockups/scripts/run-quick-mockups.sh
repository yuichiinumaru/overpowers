#!/bin/bash
# Wrapper script for quick-mockups operations

echo "Running quick-mockups workflow..."
echo "Checking prerequisites..."

# TODO: Add specific environment checks here

echo "Executing core logic..."
python3 "$(dirname "$0")/quick_mockups_helper.py" "$@"

echo "Done."
