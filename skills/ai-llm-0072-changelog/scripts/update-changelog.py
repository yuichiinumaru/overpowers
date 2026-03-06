#!/usr/bin/env python3
import argparse
from datetime import date
import os

def main():
    parser = argparse.ArgumentParser(description='Prepend a new entry to CHANGELOG.md')
    parser.add_argument('version', help='Version number (e.g. 1.4.0)')
    parser.add_argument('--added', help='Added features (comma separated)')
    parser.add_argument('--changed', help='Changed features (comma separated)')
    parser.add_argument('--fixed', help='Fixed bugs (comma separated)')
    parser.add_argument('--removed', help='Removed features (comma separated)')
    parser.add_argument('--file', default='CHANGELOG.md', help='Changelog file path')

    args = parser.parse_args()
    
    today = date.today().isoformat()
    new_entry = f"## [{args.version}] - {today}\n\n"
    
    if args.added:
        new_entry += "### Added\n"
        for item in args.added.split(','):
            new_entry += f"- {item.strip()}\n"
        new_entry += "\n"
        
    if args.changed:
        new_entry += "### Changed\n"
        for item in args.changed.split(','):
            new_entry += f"- {item.strip()}\n"
        new_entry += "\n"
        
    if args.fixed:
        new_entry += "### Fixed\n"
        for item in args.fixed.split(','):
            new_entry += f"- {item.strip()}\n"
        new_entry += "\n"

    if args.removed:
        new_entry += "### Removed\n"
        for item in args.removed.split(','):
            new_entry += f"- {item.strip()}\n"
        new_entry += "\n"

    if not os.path.exists(args.file):
        with open(args.file, 'w') as f:
            f.write("# Changelog\n\nAll notable changes to this project will be documented in this file.\n\n")

    with open(args.file, 'r') as f:
        lines = f.readlines()

    # Find the first entry line (starting with ##)
    insert_idx = 0
    for i, line in enumerate(lines):
        if line.startswith('## '):
            insert_idx = i
            break
    
    if insert_idx == 0 and len(lines) > 0:
        # If no entries found, append to end
        insert_idx = len(lines)

    lines.insert(insert_idx, new_entry)
    
    with open(args.file, 'w') as f:
        f.writelines(lines)
    
    print(f"Updated {args.file} with version {args.version}")

if __name__ == "__main__":
    main()
