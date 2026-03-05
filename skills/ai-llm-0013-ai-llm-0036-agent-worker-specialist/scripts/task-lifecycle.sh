#!/bin/bash

# Script to report task lifecycle events.
# Usage: ./task-lifecycle.sh [start|progress|block|complete] "Task Name" [Details]

EVENT=$1
TASK_NAME=$2
DETAILS=$3
AGENT_ID=${AGENT_ID:-"worker-cli"}

if [ -z "$EVENT" ] || [ -z "$TASK_NAME" ]; then
  echo "Usage: $0 [start|progress|block|complete] \"Task Name\" [Details]"
  exit 1
fi

TIMESTAMP=$(date +%s)

case "$EVENT" in
  "start")
    echo "{\"agent\": \"$AGENT_ID\", \"status\": \"task-received\", \"task\": \"$TASK_NAME\", \"timestamp\": $TIMESTAMP}"
    ;;
  "progress")
    echo "{\"agent\": \"$AGENT_ID\", \"status\": \"in-progress\", \"task\": \"$TASK_NAME\", \"details\": \"$DETAILS\", \"timestamp\": $TIMESTAMP}"
    ;;
  "block")
    echo "{\"agent\": \"$AGENT_ID\", \"status\": \"blocked\", \"task\": \"$TASK_NAME\", \"reason\": \"$DETAILS\", \"timestamp\": $TIMESTAMP}"
    ;;
  "complete")
    echo "{\"agent\": \"$AGENT_ID\", \"status\": \"complete\", \"task\": \"$TASK_NAME\", \"deliverables\": \"$DETAILS\", \"timestamp\": $TIMESTAMP}"
    ;;
esac
