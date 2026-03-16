#!/bin/bash
if [ -z "$1" ]; then
    echo "Usage: $0 <task_name>"
    exit 1
fi
echo "Creating implementation plan for: $1"
cat << TEMPLATE > "plan_${1}.md"
# Implementation Plan: $1

## Requirements
- [ ] Requirement 1

## Architecture
[Brief architectural design]

## Step-by-Step Implementation
1. [ ] Step 1: ...
2. [ ] Step 2: ...

## Verification
- [ ] All tests pass
TEMPLATE
echo "Created plan_${1}.md"
