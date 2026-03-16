#!/bin/bash
# Wrapper script for pymoo operations

echo "Running pymoo workflow..."
echo "Checking prerequisites..."

# TODO: Add specific environment checks here

echo "Executing core logic..."
python3 "$(dirname "$0")/pymoo_helper.py" "$@"

echo "Done."
