#!/usr/bin/env python3
"""
Automatically group changelog entries into high-level categories.
"""
import sys
import argparse

CATEGORIES = {
    "feat": "Important Features",
    "ui": "UI/UX Improvements",
    "ux": "UI/UX Improvements",
    "fix": "Bug Fixes",
    "chore": "Maintenance",
    "docs": "Documentation",
    "perf": "Performance Improvements",
}

def categorize(desc):
    desc = desc.lower()
    for key, title in CATEGORIES.items():
        if desc.startswith(key) or f" {key}:" in desc:
            return title
    return "Other Changes"

def main():
    if len(sys.stdin.isatty() and sys.argv < 2):
        print("Usage: generate_highlights.py <formatted_changelog.md> or pipe input")
        sys.exit(1)

    lines = sys.stdin.readlines() if not sys.stdin.isatty() else open(sys.argv[1]).readlines()
    
    grouped = {}
    for line in lines:
        if line.startswith("- "):
            cat = categorize(line[2:])
            if cat not in grouped:
                grouped[cat] = []
            grouped[cat].append(line.strip())

    for cat in sorted(grouped.keys()):
        print(f"\n#### {cat}")
        for item in grouped[cat]:
            print(item)

if __name__ == "__main__":
    main()
