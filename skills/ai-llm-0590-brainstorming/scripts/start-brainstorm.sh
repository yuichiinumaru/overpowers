#!/bin/bash
if [ -z "$1" ]; then
    echo "Usage: $0 <topic>"
    exit 1
fi
echo "Initializing brainstorming session for: $1"
cat << TEMPLATE > "brainstorm_${1// /_}.md"
# Brainstorming: $1

## User Intent
[What is the actual goal?]

## Requirements Exploration
- [ ] ...

## Design Alternatives
1. ...
2. ...

## Open Questions
- ...
TEMPLATE
echo "Created brainstorm_${1// /_}.md"
