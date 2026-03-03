#!/bin/bash
# setup-hanyuan.sh - ComfyUI Hanyuan Video 1.5 setup helper

COMFYUI_PATH=${1:-"./ComfyUI"}

echo "Setting up Hanyuan Video 1.5 structure in $COMFYUI_PATH..."

mkdir -p "$COMFYUI_PATH/models/checkpoints"
mkdir -p "$COMFYUI_PATH/models/vae"
mkdir -p "$COMFYUI_PATH/models/clip"

echo "Directories created. Please download Hanyuan weights to models/checkpoints/."
echo "Launch ComfyUI with: python main.py --highvram"
