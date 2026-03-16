#!/bin/bash

# AgentDB Advanced Management Script.
# Usage: ./db-manage.sh {merge|maintain|info} <db_path> [args]

COMMAND=$1
DB_PATH=$2

if [[ -z "$COMMAND" || -z "$DB_PATH" ]]; then
    echo "Usage: $0 {merge|maintain|info} <db_path> [args]"
    exit 1
fi

case $COMMAND in
    merge)
        DB2=$3
        OUT=$4
        if [[ -z "$DB2" || -z "$OUT" ]]; then
            echo "Usage: $0 merge <db1> <db2> <output>"
            exit 1
        fi
        echo "Merging $DB_PATH and $DB2 into $OUT..."
        npx agentdb@latest merge "$DB_PATH" "$DB2" "$OUT"
        ;;
    maintain)
        echo "Running maintenance on $DB_PATH..."
        sqlite3 "$DB_PATH" "VACUUM;"
        sqlite3 "$DB_PATH" "ANALYZE;"
        echo "Maintenance complete."
        ;;
    info)
        echo "Database Info: $DB_PATH"
        npx agentdb@latest stats "$DB_PATH"
        ;;
    *)
        echo "Invalid command."
        exit 1
        ;;
esac
