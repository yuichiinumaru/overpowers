#!/bin/bash

# ComfyUI Utility Helpers
# Provides common functions for monitoring and managing ComfyUI environments.

# 1. Dependency Checks
check_dependencies() {
    echo "Checking dependencies..."
    if ! command -v python3 &> /dev/null; then
        echo "Error: python3 is not installed."
        return 1
    fi
    
    # Check for common AI libs if possible
    python3 -c "import torch" &> /dev/null
    if [ $? -ne 0 ]; then
        echo "Warning: PyTorch not found in default python3 environment."
    fi
}

# 2. VRAM / RAM Monitoring
monitor_resources() {
    echo "--- Resource Monitor ---"
    
    # CPU/RAM (Linux/macOS)
    if command -v free &> /dev/null; then
        free -h | grep -E "Mem|total"
    elif command -v vm_stat &> /dev/null; then
        vm_stat | head -n 5
    fi

    # GPU (NVIDIA)
    if command -v nvidia-smi &> /dev/null; then
        nvidia-smi --query-gpu=memory.total,memory.used,memory.free --format=csv,noheader,nounits
    else
        echo "GPU: nvidia-smi not found. Ensure NVIDIA drivers are installed for VRAM monitoring."
    fi
}

# 3. Path Verification
verify_comfy_paths() {
    local base_path=$1
    if [ -z "$base_path" ]; then
        echo "Usage: verify_comfy_paths <path_to_comfyui>"
        return 1
    fi

    if [ ! -d "$base_path" ]; then
        echo "Error: Directory $base_path does not exist."
        return 1
    fi

    echo "Checking ComfyUI structure in $base_path..."
    local folders=("models/checkpoints" "models/loras" "models/controlnet" "custom_nodes")
    for folder in "${folders[@]}"; do
        if [ -d "$base_path/$folder" ]; then
            echo "[OK] $folder"
        else
            echo "[MISSING] $folder"
        fi
    done
}

# 4. Custom Node Finder
check_custom_node() {
    local base_path=$1
    local node_name=$2
    if [ -z "$base_path" ] || [ -z "$node_name" ]; then
        echo "Usage: check_custom_node <path_to_comfyui> <node_folder_name>"
        return 1
    fi

    if [ -d "$base_path/custom_nodes/$node_name" ]; then
        echo "Found custom node: $node_name"
        return 0
    else
        echo "Custom node NOT found: $node_name"
        return 1
    fi
}

# Execute if called directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    case "$1" in
        "check")
            check_dependencies
            ;;
        "monitor")
            monitor_resources
            ;;
        "verify")
            verify_comfy_paths "$2"
            ;;
        "find-node")
            check_custom_node "$2" "$3"
            ;;
        *)
            echo "Commands: check, monitor, verify <path>, find-node <path> <name>"
            ;;
    esac
fi
