#!/bin/bash

# Helper script to upsert a row in a Google Sheet using sheets-cli
# Usage: ./upsert-row.sh <spreadsheet_id> <sheet_name> <key_col> <key_val> <values_json>

ID=$1
SHEET=$2
KEY_COL=$3
KEY_VAL=$4
VALUES=$5

if [[ -z "$ID" || -z "$SHEET" || -z "$KEY_COL" || -z "$KEY_VAL" || -z "$VALUES" ]]; then
  echo "Usage: $0 <spreadsheet_id> <sheet_name> <key_col> <key_val> <values_json>"
  exit 1
fi

# Try to update first
RESULT=$(sheets-cli update key --spreadsheet "$ID" --sheet "$SHEET" --key-col "$KEY_COL" --key "$KEY_VAL" --set "$VALUES")

if echo "$RESULT" | grep -q '"matchedRows": 0'; then
  echo "No match found. Appending new row..."
  # Merge key and values for append
  # This is a bit tricky with raw bash and JSON, but let's assume the user provides the full object for now
  sheets-cli append --spreadsheet "$ID" --sheet "$SHEET" --values "$VALUES"
else
  echo "Row updated successfully."
  echo "$RESULT"
fi
