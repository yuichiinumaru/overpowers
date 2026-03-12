#!/usr/bin/env python3
import argparse
import sys

def generate_bash_command(name, desc):
    template = f"""#!/bin/bash
# Description: {desc}
# Single Responsibility: Execute {name} action.

echo "Running custom command '{name}'..."
# Logic goes here...
echo "Completed."
"""
    print(f"Generated bash command '{name}.sh':")
    print("-" * 40)
    print(template)
    print("-" * 40)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Slash Command Factory")
    parser.add_argument("--name", required=True, help="Name of the slash command")
    parser.add_argument("--desc", required=True, help="Description of the command")
    args = parser.parse_args()
    generate_bash_command(args.name, args.desc)
