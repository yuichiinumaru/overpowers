#!/bin/bash
# Read last check timestamp for SECUpdates
STATE_FILE="$HOME/.claude/skills/SECUpdates/State/last-check.json"
if [ -f "$STATE_FILE" ]; then
    cat "$STATE_FILE"
else
    echo '{"last_check_timestamp": "1970-01-01T00:00:00.000Z", "sources": {}}'
fi
