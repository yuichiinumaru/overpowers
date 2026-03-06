#!/bin/bash
# Generate changelog from git commits
git log --oneline --since="1 week ago" > CHANGELOG_draft.md
echo "Changelog draft generated."
