#!/usr/bin/env python3
import os
import sys
from pathlib import Path

def setup_flux2_dirs(comfyui_path):
    root = Path(comfyui_path).expanduser()
    if not root.exists():
        print(f"Error: ComfyUI path {comfyui_path} does not exist.")
        return

    dirs = [
        root / 'models' / 'checkpoints',
        root / 'models' / 'vae',
        root / 'models' / 'clip'
    ]

    print(f"Setting up Flux 2 directories in {root}...")
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
        print(f"  Confirmed: {d}")

    print("\nNext steps:")
    print("1. Download Flux 2 checkpoint to models/checkpoints/")
    print("2. Download Flux 2 VAE to models/vae/")
    print("3. Download T5xxl and CLIP-L text encoders to models/clip/")
    print("4. Update ComfyUI: git pull && pip install -r requirements.txt")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: setup_flux2.py <comfyui_root_dir>")
        sys.exit(1)
    
    setup_flux2_dirs(sys.argv[1])
