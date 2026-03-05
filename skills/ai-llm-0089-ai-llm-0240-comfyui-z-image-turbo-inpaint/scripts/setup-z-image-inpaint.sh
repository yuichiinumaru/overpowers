#!/bin/bash

# Setup script for Z-Image Turbo ControlNet Inpaint
# Prepares ControlNet folders and checks dependencies

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
CONTROLNET_DIR="$COMFY_PATH/models/controlnet"
mkdir -p "$CONTROLNET_DIR"

echo "Directory $CONTROLNET_DIR verified/created."
echo "Next steps:"
echo "1. Download 'Z-Image Turbo ControlNet Inpaint' weights."
echo "2. Place weights in $CONTROLNET_DIR"
echo "3. Restart ComfyUI and load the ControlNet Loader node."
