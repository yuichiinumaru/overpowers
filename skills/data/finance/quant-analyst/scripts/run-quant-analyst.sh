#!/bin/bash
# Wrapper script for quant-analyst operations

echo "Running quant-analyst workflow..."
echo "Checking prerequisites..."

# TODO: Add specific environment checks here

echo "Executing core logic..."
python3 "$(dirname "$0")/quant_analyst_helper.py" "$@"

echo "Done."
