#!/bin/bash

# Query session logs

AGENT_ID=$1
QUERY_TYPE=$2
SESSION_ID=$3

if [ -z "$AGENT_ID" ] || [ -z "$QUERY_TYPE" ]; then
    echo "Usage: $0 <agentId> <list|extract|search|cost> [sessionId|keyword]"
    exit 1
fi

SESSIONS_DIR="$HOME/.openclaw/agents/$AGENT_ID/sessions"

if [ ! -d "$SESSIONS_DIR" ]; then
    echo "Error: Sessions directory not found at $SESSIONS_DIR"
    exit 1
fi

case $QUERY_TYPE in
    list)
        echo "Listing all sessions for agent $AGENT_ID:"
        for f in "$SESSIONS_DIR"/*.jsonl; do
            date=$(head -1 "$f" | jq -r '.timestamp' | cut -dT -f1)
            size=$(ls -lh "$f" | awk '{print $5}')
            echo "$date $size $(basename "$f")"
        done | sort -r
        ;;
    extract)
        if [ -z "$SESSION_ID" ]; then
            echo "Error: sessionId required for extract."
            exit 1
        fi
        echo "Extracting text from session $SESSION_ID:"
        jq -r 'select(.message.role == "user" or .message.role == "assistant") | .message.content[]? | select(.type == "text") | .text' "$SESSIONS_DIR/$SESSION_ID.jsonl"
        ;;
    search)
        if [ -z "$SESSION_ID" ]; then
            echo "Error: keyword required for search."
            exit 1
        fi
        echo "Searching for '$SESSION_ID' across all sessions:"
        grep -l "$SESSION_ID" "$SESSIONS_DIR"/*.jsonl
        ;;
    cost)
        if [ -z "$SESSION_ID" ]; then
            echo "Calculating total cost for all sessions:"
            for f in "$SESSIONS_DIR"/*.jsonl; do
                date=$(head -1 "$f" | jq -r '.timestamp' | cut -dT -f1)
                cost=$(jq -s '[.[] | .message.usage.cost.total // 0] | add' "$f")
                echo "$date $cost $(basename "$f")"
            done | sort -r
        else
            echo "Calculating total cost for session $SESSION_ID:"
            jq -s '[.[] | .message.usage.cost.total // 0] | add' "$SESSIONS_DIR/$SESSION_ID.jsonl"
        fi
        ;;
    *)
        echo "Invalid query type: $QUERY_TYPE"
        exit 1
        ;;
esac
