#!/bin/bash
if [ -z "$1" ]; then
    echo "Usage: $0 <path_to_skill_folder>"
    exit 1
fi
echo "Verifying skill structure in $1..."
if [ ! -f "$1/SKILL.md" ]; then
    echo "Error: SKILL.md not found in $1"
    exit 1
fi
echo "Skill verification passed."
