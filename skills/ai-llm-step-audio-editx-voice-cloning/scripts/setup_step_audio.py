#!/usr/bin/env python3
import os
import sys
from pathlib import Path

def setup_step_audio_dirs(install_path):
    root = Path(install_path).expanduser()
    if not root.exists():
        print(f"Path {install_path} does not exist. Creating it...")
        root.mkdir(parents=True, exist_ok=True)

    dirs = [
        root / 'models',
        root / 'references',
        root / 'output'
    ]

    print(f"Setting up Step Audio EditX directories in {root}...")
    for d in dirs:
        d.mkdir(parents=True, exist_ok=True)
        print(f"  Confirmed: {d}")

    print("\nNext steps:")
    print("1. Clone Step-Audio-EditX repo into this directory.")
    print("2. Run: pip install -r requirements.txt")
    print("3. Download pre-trained models into models/ folder.")
    print("4. Place 10-30s reference audio in references/ for cloning.")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    setup_step_audio_dirs(target)
