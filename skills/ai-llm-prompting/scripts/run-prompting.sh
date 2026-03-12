#!/bin/bash
# Wrapper script for prompting operations

echo "Running prompting workflow..."
echo "Checking prerequisites..."

# TODO: Add specific environment checks here

echo "Executing core logic..."
python3 "$(dirname "$0")/prompting_helper.py" "$@"

echo "Done."
