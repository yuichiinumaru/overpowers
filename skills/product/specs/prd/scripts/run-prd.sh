#!/bin/bash
# Wrapper script for prd operations

echo "Running prd workflow..."
echo "Checking prerequisites..."

# TODO: Add specific environment checks here

echo "Executing core logic..."
python3 "$(dirname "$0")/prd_helper.py" "$@"

echo "Done."
