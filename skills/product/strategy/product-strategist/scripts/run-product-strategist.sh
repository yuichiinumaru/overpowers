#!/bin/bash
# Wrapper script for product-strategist operations

echo "Running product-strategist workflow..."
echo "Checking prerequisites..."

# TODO: Add specific environment checks here

echo "Executing core logic..."
python3 "$(dirname "$0")/product_strategist_helper.py" "$@"

echo "Done."
