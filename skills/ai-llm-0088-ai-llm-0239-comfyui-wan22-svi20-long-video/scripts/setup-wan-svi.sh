#!/bin/bash

# Setup script for Wan 2.2 + SVI 2.0 Long Video Generation
# Prepares folders and checks dependencies

set -e

# Load utilities
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
UTILS_PATH="$SCRIPT_DIR/comfyui-utils.sh"

if [ -f "$UTILS_PATH" ]; then
    source "$UTILS_PATH"
else
    echo "Warning: comfyui-utils.sh not found."
fi

# 1. Path Input
read -p "Enter your ComfyUI base path (e.g., ~/ComfyUI): " COMFY_PATH
COMFY_PATH="${COMFY_PATH/#\~/$HOME}"

if [ ! -d "$COMFY_PATH" ]; then
    echo "Error: Directory $COMFY_PATH not found."
    exit 1
fi

# 2. Folder Preparation
mkdir -p "$COMFY_PATH/models/checkpoints"
mkdir -p "$COMFY_PATH/models/loras"

echo "Structure verified/created in $COMFY_PATH"
echo "Next steps:"
echo "1. Place Wan 2.2 model in $COMFY_PATH/models/checkpoints/"
echo "2. Place SVI 2.0 LoRA in $COMFY_PATH/models/loras/"
echo "3. Ensure 'ComfyUI Wan Video Wrapper' is installed in custom_nodes/"

# 3. Check for Custom Node
if [[ $(check_custom_node "$COMFY_PATH" "ComfyUI-WanVideo") -eq 0 ]]; then
    echo "Custom node 'ComfyUI-WanVideo' found."
else
    echo "Recommendation: Install 'ComfyUI Wan Video Wrapper' from GitHub."
fi
