#!/bin/bash

# Automation for creating a new Conductor track
# Usage: ./new-track.sh <short-name> <type> <title>

set -e

SHORT_NAME=$1
TYPE=$2 # feature, bug, chore, refactor
TITLE=$3

if [ -z "$SHORT_NAME" ] || [ -z "$TYPE" ] || [ -z "$TITLE" ]; then
    echo "Usage: ./new-track.sh <short-name> <type> <title>"
    exit 1
fi

DATE=$(date +%Y%m%d)
TRACK_ID="${SHORT_NAME}_${DATE}"
TRACK_DIR="conductor/tracks/$TRACK_ID"

echo "Creating track $TRACK_ID in $TRACK_DIR..."

mkdir -p "$TRACK_DIR"

# Create metadata.json
cat <<EOF > "$TRACK_DIR/metadata.json"
{
  "id": "$TRACK_ID",
  "title": "$TITLE",
  "type": "$TYPE",
  "status": "pending",
  "created": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
  "updated": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
  "phases": {
    "total": 0,
    "completed": 0
  },
  "tasks": {
    "total": 0,
    "completed": 0
  }
}
EOF

# Create placeholder spec.md
cat <<EOF > "$TRACK_DIR/spec.md"
# Specification: $TITLE

**Track ID:** $TRACK_ID
**Type:** $TYPE
**Created:** $(date +%Y-%m-%d)
**Status:** Draft

## Summary
[1-2 sentence summary]

## Context
[Product context]

## Acceptance Criteria
- [ ] Criterion 1
EOF

# Create index.md
cat <<EOF > "$TRACK_DIR/index.md"
# Track: $TITLE

**ID:** $TRACK_ID
**Status:** Pending

## Documents
- [Specification](./spec.md)
- [Implementation Plan](./plan.md)

## Progress
- Phases: 0/0 complete
- Tasks: 0/0 complete
EOF

echo "Track files initialized. Don't forget to register in conductor/tracks.md"
