#!/bin/bash

# Setup script for ComfyUI AEP v1.5 Music Generator
# This script helps prepare the environment for AEP v1.5

set -e

# Load utilities
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
UTILS_PATH="$SCRIPT_DIR/comfyui-utils.sh"

if [ -f "$UTILS_PATH" ]; then
    source "$UTILS_PATH"
else
    echo "Warning: comfyui-utils.sh not found. Some checks might be skipped."
fi

# 1. Dependency Check
if command -v check_dependencies &> /dev/null; then
    check_dependencies
fi

# 2. Path Input
read -p "Enter your ComfyUI base path (e.g., ~/ComfyUI): " COMFY_PATH
COMFY_PATH="${COMFY_PATH/#\~/$HOME}" # Expand tilde

if [ ! -d "$COMFY_PATH" ]; then
    echo "Error: Directory $COMFY_PATH not found."
    exit 1
fi

# 3. Model Folder Prep
CHECKPOINTS_DIR="$COMFY_PATH/models/checkpoints"
mkdir -p "$CHECKPOINTS_DIR"

echo "Please download AEP v1.5 weights from Hugging Face and place them in: $CHECKPOINTS_DIR"
echo "Recommended model: AEP v1.5 (safetensors)"

# 4. Custom Node Installation (Placeholder for specific AEP nodes if any)
# Example: git clone https://github.com/someuser/ComfyUI-AEP-Nodes "$COMFY_PATH/custom_nodes/ComfyUI-AEP-Nodes"

echo "Setup complete. Please restart your ComfyUI server after adding the model weights."
