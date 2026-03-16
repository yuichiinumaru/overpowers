#!/bin/bash

# Setup script for Z-Image Turbo Setup and Execution
# Prepares model directories and checks dependencies

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
mkdir -p "$COMFY_PATH/models/vae"
mkdir -p "$COMFY_PATH/models/clip"

echo "Directories for checkpoints, VAE, and CLIP verified/created in $COMFY_PATH"
echo "Next steps:"
echo "1. Download Z-Image Turbo and place in models/checkpoints/"
echo "2. Download ae.safetensors and place in models/vae/"
echo "3. Download Clip weights and place in models/clip/ (if separate)."
