#!/bin/bash
# Review a PR locally
gh pr checkout $1
git diff main
echo "PR ready for review."
