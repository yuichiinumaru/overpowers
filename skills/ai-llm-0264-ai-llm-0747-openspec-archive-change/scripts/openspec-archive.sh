#!/bin/bash
# openspec-archive.sh
# Automates the archive change process as described in SKILL.md.
# This is a helper script meant to interactively guide the archival of openspec changes.

set -e

CHANGE_NAME="$1"

if [ -z "$CHANGE_NAME" ]; then
    echo "Fetching available changes..."
    # Fallback/mock logic for missing openspec-cn list tool
    if command -v openspec-cn >/dev/null 2>&1; then
        CHANGES=$(openspec-cn list --json | jq -r '.[] | .name')
    else
        echo "No change name provided. Please specify a change name: ./openspec-archive.sh <change_name>"
        exit 1
    fi

    if [ -z "$CHANGES" ]; then
        echo "No active changes found."
        exit 0
    fi
    echo "Select a change to archive:"
    select CHANGE_NAME in $CHANGES; do
        if [ -n "$CHANGE_NAME" ]; then
            break
        else
            echo "Invalid selection."
        fi
    done
fi

echo "Archiving change: $CHANGE_NAME"

# Check artifacts status
if command -v openspec-cn >/dev/null 2>&1; then
    STATUS_JSON=$(openspec-cn status --change "$CHANGE_NAME" --json)
    if echo "$STATUS_JSON" | jq -e '.artifacts[] | select(.status != "done")' > /dev/null; then
        echo "WARNING: Some artifacts are not marked as 'done'."
        read -p "Do you want to proceed anyway? (y/N): " proceed
        if [[ ! "$proceed" =~ ^[Yy]$ ]]; then
            echo "Archival aborted."
            exit 1
        fi
    fi
else
    echo "openspec-cn CLI not found. Skipping artifact verification."
fi

# Check tasks completion
if [ -f "tasks.md" ]; then
    UNFINISHED_TASKS=$(grep -c "\- \[ \]" tasks.md || true)
    if [ "$UNFINISHED_TASKS" -gt 0 ]; then
        echo "WARNING: Found $UNFINISHED_TASKS unfinished tasks in tasks.md."
        read -p "Do you want to proceed anyway? (y/N): " proceed
        if [[ ! "$proceed" =~ ^[Yy]$ ]]; then
            echo "Archival aborted."
            exit 1
        fi
    fi
fi

# Determine if sync is needed (simplified)
if [ -d "openspec/changes/$CHANGE_NAME/specs/" ]; then
    echo "Delta specs exist. Would you like to sync them to the main spec before archiving?"
    read -p "Sync? (y/N): " sync_choice
    if [[ "$sync_choice" =~ ^[Yy]$ ]]; then
        echo "Syncing specs... (simulated via openspec-sync-specs logic if available)"
        # e.g., run sync logic here
    fi
fi

# Execute archive
ARCHIVE_DIR="openspec/changes/archive"
mkdir -p "$ARCHIVE_DIR"

DATE_STR=$(date +%Y-%m-%d)
DEST="$ARCHIVE_DIR/$DATE_STR-$CHANGE_NAME"

if [ -e "$DEST" ]; then
    echo "Error: Destination $DEST already exists."
    exit 1
fi

if [ -d "openspec/changes/$CHANGE_NAME" ]; then
    mv "openspec/changes/$CHANGE_NAME" "$DEST"
    echo "## Archive Complete"
    echo "**Change:** $CHANGE_NAME"
    echo "**Archived to:** $DEST"
else
    echo "Error: Change directory openspec/changes/$CHANGE_NAME does not exist."
    exit 1
fi
