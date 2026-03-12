#!/bin/bash
# Wrapper script for prompt-optimizer operations

echo "Running prompt-optimizer workflow..."
echo "Checking prerequisites..."

# TODO: Add specific environment checks here

echo "Executing core logic..."
python3 "$(dirname "$0")/prompt_optimizer_helper.py" "$@"

echo "Done."
