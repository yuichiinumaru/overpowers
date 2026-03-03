#!/bin/bash
if [ -z "$1" ]; then
    echo "Usage: $0 <flow_name>"
    exit 1
fi
echo "Creating flow template for: $1"
cat << TEMPLATE > "$1_flow.md"
# Flow: $1

## Purpose
[Describe what this flow accomplishes]

## Steps
1. [Step 1]
2. [Step 2]
TEMPLATE
echo "Created $1_flow.md"
