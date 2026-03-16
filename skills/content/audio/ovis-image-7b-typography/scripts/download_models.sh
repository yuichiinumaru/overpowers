#!/bin/bash

# Download Ovis Image 7B models for ComfyUI.
# Usage: ./download_models.sh <comfyui_root_dir>

COMFYUI_ROOT="$1"

if [ -z "$COMFYUI_ROOT" ]; then
  echo "Usage: $0 <comfyui_root_dir>"
  exit 1
fi

if [ ! -d "$COMFYUI_ROOT" ]; then
  echo "Error: ComfyUI root directory not found: $COMFYUI_ROOT"
  exit 1
fi

TEXT_ENCODER_DIR="${COMFYUI_ROOT}/models/clip"
CHECKPOINTS_DIR="${COMFYUI_ROOT}/models/checkpoints"

mkdir -p "$TEXT_ENCODER_DIR"
mkdir -p "$CHECKPOINTS_DIR"

echo "Downloading Text Encoder (ovis_2.5.safetensors)..."
curl -L "https://huggingface.co/Comfy-Org/Ovis-Image/resolve/main/split_files/text_encoders/ovis_2.5.safetensors" -o "${TEXT_ENCODER_DIR}/ovis_2.5_text_encoder.safetensors"

echo "Downloading Diffusion Model (ovis_image_bf16.safetensors)..."
curl -L "https://huggingface.co/Comfy-Org/Ovis-Image/resolve/main/split_files/diffusion_models/ovis_image_bf16.safetensors" -o "${CHECKPOINTS_DIR}/ovis_image_7b_bf16.safetensors"

echo ""
echo "Done. Models downloaded to:"
echo "  - ${TEXT_ENCODER_DIR}/ovis_2.5_text_encoder.safetensors"
echo "  - ${CHECKPOINTS_DIR}/ovis_image_7b_bf16.safetensors"
echo ""
echo "Note: Ensure your ComfyUI is up to date to support Ovis."
