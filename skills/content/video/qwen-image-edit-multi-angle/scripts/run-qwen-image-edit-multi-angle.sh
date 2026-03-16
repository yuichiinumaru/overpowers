#!/bin/bash
# Wrapper script for qwen-image-edit-multi-angle operations

echo "Running qwen-image-edit-multi-angle workflow..."
echo "Checking prerequisites..."

# TODO: Add specific environment checks here

echo "Executing core logic..."
python3 "$(dirname "$0")/qwen_image_edit_multi_angle_helper.py" "$@"

echo "Done."
