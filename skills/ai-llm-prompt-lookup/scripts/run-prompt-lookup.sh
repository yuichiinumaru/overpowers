#!/bin/bash
# Wrapper script for prompt-lookup operations

echo "Running prompt-lookup workflow..."
echo "Checking prerequisites..."

# TODO: Add specific environment checks here

echo "Executing core logic..."
python3 "$(dirname "$0")/prompt_lookup_helper.py" "$@"

echo "Done."
