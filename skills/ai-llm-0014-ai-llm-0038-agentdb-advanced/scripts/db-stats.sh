#!/bin/bash
DB_PATH=${1:-".agentdb/reasoningbank.db"}
if [ ! -f "$DB_PATH" ]; then
  echo "Error: Database file not found at $DB_PATH"
  exit 1
fi
echo "Database Statistics for $DB_PATH:"
echo "--------------------------------"
sqlite3 "$DB_PATH" "SELECT 'Total Patterns: ' || count(*) FROM patterns;"
sqlite3 "$DB_PATH" "SELECT 'Unique Domains: ' || count(distinct domain) FROM patterns;"
ls -lh "$DB_PATH" | awk '{print "File Size: " $5}'
