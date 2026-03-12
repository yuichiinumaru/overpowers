#!/bin/bash
# Check project-level first
if test -f .baoyu-skills/baoyu-infographic/EXTEND.md; then
    echo "project"
# Then user-level
elif test -f "$HOME/.baoyu-skills/baoyu-infographic/EXTEND.md"; then
    echo "user"
else
    echo "Not found"
fi
