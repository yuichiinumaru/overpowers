#!/bin/bash

# Script to report task progress to swarm memory.
# Usage: ./report-progress.sh <worker_id> <task_name> <percentage> <current_step>

WORKER_ID=$1
TASK=$2
PERCENT=$3
STEP=$4

if [[ -z "$WORKER_ID" || -z "$TASK" || -z "$PERCENT" || -z "$STEP" ]]; then
    echo "Usage: $0 <worker_id> <task_name> <percentage> <current_step>"
    exit 1
fi

TIMESTAMP=$(date +%s)

# Construct progress JSON
PROGRESS_JSON=$(cat <<EOF
{
  "worker_id": "$WORKER_ID",
  "task": "$TASK",
  "progress_percentage": $PERCENT,
  "current_step": "$STEP",
  "timestamp": $TIMESTAMP
}
EOF
)

echo "Reporting progress for $WORKER_ID: $PERCENT% ($STEP)"

# Placeholder for actual memory coordination call
# mcp__claude-flow__memory_usage --action store --key "swarm$worker-$WORKER_ID$progress" --value "$PROGRESS_JSON"

echo "$PROGRESS_JSON"
