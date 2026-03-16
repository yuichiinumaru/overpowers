#!/bin/bash
# Wrapper script for polymarket operations

echo "Running polymarket workflow..."
echo "Checking prerequisites..."

# TODO: Add specific environment checks here

echo "Executing core logic..."
python3 "$(dirname "$0")/polymarket_helper.py" "$@"

echo "Done."
