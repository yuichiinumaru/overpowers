#!/bin/bash

# Setup script for Z-Image Turbo ControlNet Union & Depth Anything V3
# Prepares directories and checks for custom nodes

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
mkdir -p "$COMFY_PATH/models/controlnet"

echo "Directories for checkpoints and ControlNet verified/created in $COMFY_PATH"
echo "Next steps:"
echo "1. Download Z-Image Turbo and place in models/checkpoints/"
echo "2. Download ControlNet Union and place in models/controlnet/"
echo "3. Ensure 'Depth Anything V3' custom nodes are installed via ComfyUI Manager."

# 3. Check for Custom Node (Example guess for folder name)
if [[ $(check_custom_node "$COMFY_PATH" "ComfyUI-DepthAnythingV3") -eq 0 ]]; then
    echo "Custom node for Depth Anything V3 found."
fi
