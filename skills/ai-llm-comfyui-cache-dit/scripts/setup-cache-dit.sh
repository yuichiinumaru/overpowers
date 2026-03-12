#!/bin/bash

# Setup script for ComfyUI Cache DiT Optimizer
# Prepares custom nodes directory and checks dependencies

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

# 2. Custom Node Installation
echo "To install the Cache DiT node:"
echo "1. Navigate to $COMFY_PATH/custom_nodes/"
echo "2. Clone the Cache DiT repository (e.g., git clone https://github.com/city96/ComfyUI-CacheDiT)"
echo "3. Restart your ComfyUI server."

# 3. Check for Custom Node
if [[ $(check_custom_node "$COMFY_PATH" "ComfyUI-CacheDiT") -eq 0 ]]; then
    echo "Custom node 'ComfyUI-CacheDiT' already found."
else
    echo "Recommendation: Follow the installation steps above."
fi
