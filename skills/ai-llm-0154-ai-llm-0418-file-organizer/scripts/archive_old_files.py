#!/usr/bin/env python3
import os
import shutil
import sys
import time
from pathlib import Path

def archive_old_files(target_dir, days=180):
    target_path = Path(target_dir).expanduser()
    if not target_path.exists():
        print(f"Error: {target_dir} does not exist.")
        return

    archive_dir = target_path / 'Archive'
    archive_dir.mkdir(exist_ok=True)

    now = time.time()
    seconds_threshold = days * 24 * 60 * 60

    count = 0
    for item in target_path.iterdir():
        if item.is_file() and item.name != 'Archive':
            mtime = item.stat().st_mtime
            if (now - mtime) > seconds_threshold:
                print(f"Archiving {item.name} (last modified {time.ctime(mtime)})")
                shutil.move(str(item), str(archive_dir / item.name))
                count += 1

    print(f"\nArchived {count} files to {archive_dir}/")

if __name__ == "__main__":
    directory = sys.argv[1] if len(sys.argv) > 1 else "."
    days = int(sys.argv[2]) if len(sys.argv) > 2 else 180
    archive_old_files(directory, days)
