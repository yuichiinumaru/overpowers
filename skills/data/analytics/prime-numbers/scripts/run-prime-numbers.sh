#!/bin/bash
# Wrapper script for prime-numbers operations

echo "Running prime-numbers workflow..."
echo "Checking prerequisites..."

# TODO: Add specific environment checks here

echo "Executing core logic..."
python3 "$(dirname "$0")/prime_numbers_helper.py" "$@"

echo "Done."
