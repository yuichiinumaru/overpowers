#!/bin/bash

# Script to generate a new specialized Claude Code agent.
# Usage: ./create-agent.sh <name> <description> <tags_comma_separated>

NAME=$1
DESC=$2
TAGS=$3

if [[ -z "$NAME" || -z "$DESC" ]]; then
    echo "Usage: $0 <name> <description> [tags_comma_separated]"
    exit 1
fi

FILENAME="agents/$(echo $NAME | tr '[:upper:]' '[:lower:]' | tr ' ' '-').md"
DATE=$(date +"%Y-%m-%d")

# Prepare tags for YAML
IFS=',' read -ra ADDR <<< "$TAGS"
YAML_TAGS=""
for i in "${ADDR[@]}"; do
    YAML_TAGS="$YAML_TAGS\n  - $i"
done

echo "Generating agent: $FILENAME"

cat <<EOF > "$FILENAME"
---
name: $NAME
description: $DESC
tags:$YAML_TAGS
---
# $NAME

## Purpose
$DESC

## Capabilities
- 
- 
- 

## Tools
- Read
- Write
- Bash

## Instructions
1. 
2. 
3. 

## Best Practices
- 
- 

---
*Created via agent-factory on $DATE*
EOF

echo "Agent document generated successfully."
