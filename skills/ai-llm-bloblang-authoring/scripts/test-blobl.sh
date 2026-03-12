#!/bin/bash
# test-blobl.sh <target-directory>
TARGET_DIR=$1
if [ -z "$TARGET_DIR" ]; then
  echo "Usage: $0 <target-directory>"
  exit 1
fi

DATA_FILE="${TARGET_DIR}/data.json"
SCRIPT_FILE="${TARGET_DIR}/script.blobl"

if [ ! -f "$DATA_FILE" ]; then
  echo "Error: ${DATA_FILE} not found"
  exit 1
fi

if [ ! -f "$SCRIPT_FILE" ]; then
  echo "Error: ${SCRIPT_FILE} not found"
  exit 1
fi

rpk connect blobl -m "$SCRIPT_FILE" "$DATA_FILE"
