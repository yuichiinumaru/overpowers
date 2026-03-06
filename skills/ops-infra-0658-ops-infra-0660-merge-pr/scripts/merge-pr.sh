#!/bin/bash
if [ -z "$1" ]; then echo 'Usage: ./merge-pr.sh <pr-number>'; exit 1; fi
gh pr merge "$1" --auto --squash
