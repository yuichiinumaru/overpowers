#!/bin/bash

# ReasoningBank AgentDB Management Helper

DB_PATH=${1:-"./.agentdb/reasoningbank.db"}
ACTION=$2

case $ACTION in
  "init")
    echo "Initializing ReasoningBank AgentDB at $DB_PATH..."
    npx agentdb@latest init "$DB_PATH" --dimension 1536
    ;;
  "stats")
    echo "Getting statistics for $DB_PATH..."
    npx agentdb@latest stats "$DB_PATH"
    ;;
  "migrate")
    SOURCE=$3
    if [ -z "$SOURCE" ]; then
      echo "Usage: $0 <db_path> migrate <source_db>"
      exit 1
    fi
    echo "Migrating from $SOURCE to $DB_PATH..."
    npx agentdb@latest migrate --source "$SOURCE" --target "$DB_PATH"
    ;;
  "export")
    OUTPUT=${3:-"./backup.json"}
    echo "Exporting $DB_PATH to $OUTPUT..."
    npx agentdb@latest export "$DB_PATH" "$OUTPUT"
    ;;
  "mcp")
    echo "Starting AgentDB MCP server..."
    npx agentdb@latest mcp
    ;;
  *)
    echo "Usage: $0 [db_path] <init|stats|migrate|export|mcp>"
    echo "Default db_path: ./.agentdb/reasoningbank.db"
    ;;
esac
