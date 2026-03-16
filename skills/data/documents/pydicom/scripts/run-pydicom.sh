#!/bin/bash
# Wrapper script for pydicom operations

echo "Running pydicom workflow..."
echo "Checking prerequisites..."

# TODO: Add specific environment checks here

echo "Executing core logic..."
python3 "$(dirname "$0")/pydicom_helper.py" "$@"

echo "Done."
