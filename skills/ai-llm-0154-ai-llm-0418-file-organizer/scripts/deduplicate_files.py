#!/usr/bin/env python3
import os
import hashlib
import sys
from pathlib import Path
from collections import defaultdict

def get_file_hash(file_path):
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        return None

def find_duplicates(target_dir):
    target_path = Path(target_dir).expanduser()
    if not target_path.exists():
        print(f"Error: {target_dir} does not exist.")
        return

    hashes = defaultdict(list)
    names = defaultdict(list)

    print(f"Analyzing {target_path}...")
    for item in target_path.rglob('*'):
        if item.is_file():
            file_hash = get_file_hash(item)
            if file_hash:
                hashes[file_hash].append(item)
            names[item.name].append(item)

    print("\n--- Potential Duplicates (by Hash) ---")
    for file_hash, paths in hashes.items():
        if len(paths) > 1:
            print(f"\nHash: {file_hash}")
            for p in paths:
                size = p.stat().st_size / 1024
                print(f"  - {p} ({size:.2f} KB)")

    print("\n--- Potential Duplicates (by Name) ---")
    for name, paths in names.items():
        if len(paths) > 1:
            # Only show if not already captured by hash
            print(f"\nName: {name}")
            for p in paths:
                print(f"  - {p}")

if __name__ == "__main__":
    directory = sys.argv[1] if len(sys.argv) > 1 else "."
    find_duplicates(directory)
