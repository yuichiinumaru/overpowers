#!/usr/bin/env python3
import os
import shutil
import sys
from pathlib import Path

def organize_downloads(target_dir):
    target_path = Path(target_dir).expanduser()
    if not target_path.exists():
        print(f"Error: {target_dir} does not exist.")
        return

    extensions = {
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.xls', '.pptx', '.csv'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
        'Archives': ['.zip', '.tar', '.gz', '.dmg', '.pkg'],
        'Code': ['.py', '.js', '.ts', '.html', '.css', '.cpp', '.c', '.go', '.rs']
    }

    for item in target_path.iterdir():
        if item.is_file():
            moved = False
            for folder, exts in extensions.items():
                if item.suffix.lower() in exts:
                    dest_folder = target_path / folder
                    dest_folder.mkdir(exist_ok=True)
                    print(f"Moving {item.name} to {folder}/")
                    shutil.move(str(item), str(dest_folder / item.name))
                    moved = True
                    break
            
            if not moved:
                other_folder = target_path / 'Other'
                other_folder.mkdir(exist_ok=True)
                print(f"Moving {item.name} to Other/")
                shutil.move(str(item), str(other_folder / item.name))

if __name__ == "__main__":
    directory = sys.argv[1] if len(sys.argv) > 1 else "~/Downloads"
    organize_downloads(directory)
