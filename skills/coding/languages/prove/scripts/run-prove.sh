#!/bin/bash
# Wrapper script for prove operations

echo "Running prove workflow..."
echo "Checking prerequisites..."

# TODO: Add specific environment checks here

echo "Executing core logic..."
python3 "$(dirname "$0")/prove_helper.py" "$@"

echo "Done."
