#!/bin/bash
# jj-jules-apply.sh
# Creates a new Jujutsu revision and applies a downloaded Jules diff.

set -e

if [ -z "$1" ]; then
    echo "❌ Missing argument: Session ID."
    echo "Usage: ./jj-jules-apply.sh <session_id>"
    exit 1
fi

SESSION_ID="$1"
DIFF_PATH=".archive/harvest/jules/${SESSION_ID}.diff"

if [ ! -f "$DIFF_PATH" ]; then
    echo "❌ Diff file not found at: $DIFF_PATH"
    echo "Have you run jules-harvester.py yet?"
    exit 1
fi

echo "=========================================================="
echo "Applying Jules Session: $SESSION_ID"
echo "=========================================================="

# Create a new revision describing the task
jj new -m "jules-task: $SESSION_ID"

# Apply the patch using jj (fall back to patch command if jj patch isn't supported)
# Assuming patch is available in the system
echo "Applying patch..."
if patch -p1 < "$DIFF_PATH"; then
    echo "✅ Patch applied successfully!"
else
    echo "⚠️ Conflicts detected during patch application."
    echo "The revision has been created, but you must resolve the conflicts."
    echo "Use 'jj abandon' if you want to abort this session."
    exit 1
fi

echo "✅ Task integrated into current jj workspace."
