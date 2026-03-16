#!/usr/bin/env python3
import argparse
import sys
import os

def create_scaffold(target_dir=".claude"):
    """Create a basic progressive disclosure scaffolding."""
    os.makedirs(target_dir, exist_ok=True)

    # Root file template
    root_file = "AGENTS.md" if target_dir == ".agents" else "CLAUDE.md"
    root_content = f"""# Project Title

Brief project description.

## Quick Reference
- **Package Manager:** npm/yarn/pnpm
- **Build:** `npm run build`
- **Test:** `npm test`

## Detailed Instructions
For specific guidelines, see:
- [TypeScript Conventions]({target_dir}/typescript.md)
- [Testing Guidelines]({target_dir}/testing.md)
- [Code Style]({target_dir}/code-style.md)
- [Git Workflow]({target_dir}/git-workflow.md)
- [Architecture Patterns]({target_dir}/architecture.md)
"""

    if not os.path.exists(root_file):
        with open(root_file, 'w') as f:
            f.write(root_content)
        print(f"Created {root_file}")
    else:
        print(f"{root_file} already exists. Skipping creation.")

    # Topics
    topics = [
        "typescript", "testing", "code-style",
        "git-workflow", "architecture"
    ]

    for topic in topics:
        filepath = os.path.join(target_dir, f"{topic}.md")
        if not os.path.exists(filepath):
            with open(filepath, 'w') as f:
                f.write(f"""# {topic.replace('-', ' ').title()} Guidelines

## Overview
Context for when these guidelines apply.

## Rules
- Specific, actionable instruction 1
- Specific, actionable instruction 2

## Examples

### Good
```
// example
```

### Avoid
```
// example
```
""")
            print(f"Created {filepath}")
        else:
            print(f"{filepath} already exists. Skipping.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Agent MD Refactor Helper")
    parser.add_argument("command", choices=["scaffold"], help="Command to execute")
    parser.add_argument("--dir", default=".claude", help="Target directory for linked files")
    
    args = parser.parse_args()
    
    if args.command == "scaffold":
        create_scaffold(args.dir)
