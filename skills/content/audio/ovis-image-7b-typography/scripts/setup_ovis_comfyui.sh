#!/bin/bash
# Ovis Image 7B ComfyUI Setup Helper
# This script ensures the required model weights and text encoders are downloaded to ComfyUI.

set -e

COMFYUI_DIR=${COMFYUI_DIR:-"$HOME/ComfyUI"}
MODELS_DIR="$COMFYUI_DIR/models"
CHECKPOINTS_DIR="$MODELS_DIR/checkpoints"
CLIP_DIR="$MODELS_DIR/clip"

if [ ! -d "$COMFYUI_DIR" ]; then
    echo "Error: ComfyUI directory not found at $COMFYUI_DIR."
    echo "Please set COMFYUI_DIR environment variable."
    exit 1
fi

mkdir -p "$CHECKPOINTS_DIR"
mkdir -p "$CLIP_DIR"

echo "Downloading Ovis Image 7B Main Model (ovis_image_7b_bf16.safetensors)..."
wget -nc -O "$CHECKPOINTS_DIR/ovis_image_7b_bf16.safetensors" "https://huggingface.co/AIDC-AI/Ovis1.6-Gemma2-9B/resolve/main/ovis_image_7b_bf16.safetensors"

echo "Downloading Ovis Text Encoder (ovis_2.5_text_encoder.safetensors)..."
wget -nc -O "$CLIP_DIR/ovis_2.5_text_encoder.safetensors" "https://huggingface.co/AIDC-AI/Ovis1.6-Gemma2-9B/resolve/main/ovis_2.5_text_encoder.safetensors"

echo "Models downloaded successfully. Please start ComfyUI to use them."
