#!/bin/bash

# Archive an Openspec change.
# Usage: ./archive_change.sh <change_name>

CHANGE_NAME="$1"

if [ -z "$CHANGE_NAME" ]; then
  echo "Usage: $0 <change_name>"
  exit 1
fi

CHANGE_DIR="openspec/changes/${CHANGE_NAME}"
ARCHIVE_ROOT="openspec/changes/archive"

if [ ! -d "$CHANGE_DIR" ]; then
  echo "Error: Change directory not found: $CHANGE_DIR"
  exit 1
fi

mkdir -p "$ARCHIVE_ROOT"

DATE=$(date +%Y-%m-%d)
TARGET_NAME="${DATE}-${CHANGE_NAME}"
TARGET_DIR="${ARCHIVE_ROOT}/${TARGET_NAME}"

if [ -d "$TARGET_DIR" ]; then
  echo "Error: Archive target already exists: $TARGET_DIR"
  echo "Please rename the existing archive or use a different name."
  exit 1
fi

mv "$CHANGE_DIR" "$TARGET_DIR"

if [ $? -eq 0 ]; then
  echo "Successfully archived ${CHANGE_NAME} to ${TARGET_DIR}"
else
  echo "Error: Failed to move directory."
  exit 1
fi
