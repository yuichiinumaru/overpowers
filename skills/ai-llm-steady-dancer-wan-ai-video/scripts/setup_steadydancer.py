#!/usr/bin/env python3
import os
import sys
from pathlib import Path

def setup_steadydancer_dirs(comfyui_path):
    root = Path(comfyui_path).expanduser()
    if not root.exists():
        print(f"Error: ComfyUI path {comfyui_path} does not exist.")
        return

    dirs = [
        root / 'models' / 'checkpoints',
        root / 'models' / 'loras',
        root / 'models' / 'controlnet'
    ]

    print(f"Setting up SteadyDancer directories in {root}...")
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
        print(f"  Confirmed: {d}")

    print("\nNext steps:")
    print("1. Download Wan AI Video base model to models/checkpoints/")
    print("2. Download SteadyDancer LoRAs/control models to models/loras/ or models/controlnet/")
    print("3. Use reference dance video as driving source in your workflow.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: setup_steadydancer.py <comfyui_root_dir>")
        sys.exit(1)
    
    setup_steadydancer_dirs(sys.argv[1])
