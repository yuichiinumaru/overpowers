#!/bin/bash

SKILL_NAME=$1
OUTPUT_DIR=${3:-"skills"}

if [ -z "$SKILL_NAME" ]; then
    echo "Usage: $0 <skill-name> [--full|--minimal] [--output <dir>]"
    exit 1
fi

SKILL_PATH="$OUTPUT_DIR/$SKILL_NAME"

if [ -d "$SKILL_PATH" ]; then
    echo "Error: Skill $SKILL_NAME already exists at $SKILL_PATH"
    exit 1
fi

mkdir -p "$SKILL_PATH/scripts"
mkdir -p "$SKILL_PATH/references"
mkdir -p "$SKILL_PATH/assets"

cat <<EOF > "$SKILL_PATH/SKILL.md"
---
name: $SKILL_NAME
description: "[Domain] capability: includes [capability 1], [capability 2]. Use when [decidable triggers]."
tags:
- ai
- llm
---

# $SKILL_NAME Skill

One sentence that states the boundary and the deliverable.

## When to Use This Skill

Trigger when any of these applies:
- [Trigger 1: concrete task/keyword]
- [Trigger 2]
- [Trigger 3]

## Not For / Boundaries

- What this skill will not do (prevents misfires and over-promising)
- Required inputs; ask 1-3 questions if missing

## Quick Reference

### Common Patterns

**Pattern 1:** one-line explanation
\`\`\`text
[Command/snippet you can paste and run]
\`\`\`

## Examples

### Example 1
- Input:
- Steps:
- Expected output / acceptance:

### Example 2

### Example 3

## References

- \`references/index.md\`: navigation
- \`references/...\`: long-form docs split by topic

## Maintenance

- Sources: docs/repos/specs (do not invent)
- Last updated: $(date +%Y-%m-%d)
- Known limits: what is explicitly out of scope
EOF

touch "$SKILL_PATH/references/index.md"

echo "Created skill skeleton at $SKILL_PATH"
