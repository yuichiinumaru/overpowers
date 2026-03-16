#!/bin/bash
# Wrapper script for pr-demo operations

echo "Running pr-demo workflow..."
echo "Checking prerequisites..."

# TODO: Add specific environment checks here

echo "Executing core logic..."
python3 "$(dirname "$0")/pr_demo_helper.py" "$@"

echo "Done."
