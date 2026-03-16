#!/bin/bash
# Wrapper script for product-marketing-context operations

echo "Running product-marketing-context workflow..."
echo "Checking prerequisites..."

# TODO: Add specific environment checks here

echo "Executing core logic..."
python3 "$(dirname "$0")/product_marketing_context_helper.py" "$@"

echo "Done."
