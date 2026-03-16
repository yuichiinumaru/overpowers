#!/bin/bash

git add -A
git commit -m "{commit_prefix}: {task description} ({trackId})"


git add conductor/tracks/{trackId}/plan.md
git commit -m "chore: mark task X.Y complete ({trackId})"
