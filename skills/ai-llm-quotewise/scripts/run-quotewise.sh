#!/bin/bash
# Wrapper script for quotewise operations

echo "Running quotewise workflow..."
echo "Checking prerequisites..."

# TODO: Add specific environment checks here

echo "Executing core logic..."
python3 "$(dirname "$0")/quotewise_helper.py" "$@"

echo "Done."
