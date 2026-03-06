#!/bin/bash
SKILL_DIR=$1
echo "Analyzing $SKILL_DIR..."
cat "$SKILL_DIR/SKILL.md" | head -n 20
echo "---"
ls -la "$SKILL_DIR"
