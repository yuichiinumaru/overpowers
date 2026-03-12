#!/usr/bin/env python3
import os
import argparse

def generate_tree(dir_path, prefix="", ignore_dirs=None):
    if ignore_dirs is None:
        ignore_dirs = ['.git', '__pycache__', 'node_modules', 'venv', '.venv']

    try:
        entries = os.listdir(dir_path)
    except PermissionError:
        return

    entries.sort()
    entries = [e for e in entries if e not in ignore_dirs]

    for i, entry in enumerate(entries):
        path = os.path.join(dir_path, entry)
        is_last = (i == len(entries) - 1)

        connector = "└── " if is_last else "├── "
        print(f"{prefix}{connector}{entry}")

        if os.path.isdir(path):
            new_prefix = prefix + ("    " if is_last else "│   ")
            generate_tree(path, new_prefix, ignore_dirs)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate markdown directory structure")
    parser.add_argument("dir", nargs="?", default=".", help="Directory to scan")

    args = parser.parse_args()

    print(f"```text\n{os.path.basename(os.path.abspath(args.dir))}/")
    generate_tree(args.dir)
    print("```")
