#!/usr/bin/env python3
"""
Initialize a document with a scaffold based on the co-authoring workflow.
"""
import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: init_scaffold.py <filename.md> [title]")
        sys.exit(1)

    filename = sys.argv[1]
    title = sys.argv[2] if len(sys.argv) > 2 else "New Document"

    if not filename.endswith(".md"):
        filename += ".md"

    if os.path.exists(filename):
        print(f"Error: File '{filename}' already exists.")
        sys.exit(1)

    content = f"""# {title}

## Overview
[To be written]

## Context
[To be written]

## Problem Statement / Background
[To be written]

## Proposed Solution / Approach
[To be written]

## Technical Details / Implementation
[To be written]

## Impact / Expected Outcome
[To be written]

## Alternatives Considered
[To be written]

## Open Questions / Unknowns
[To be written]

---
*Drafted using the Doc Co-Authoring Workflow*
"""

    with open(filename, 'w') as f:
        f.write(content)

    print(f"Scaffold created: {filename}")

if __name__ == "__main__":
    main()
