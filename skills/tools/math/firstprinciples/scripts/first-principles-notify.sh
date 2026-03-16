#!/bin/bash

# Mandatory notification for FirstPrinciples skill
# Usage: ./first-principles-notify.sh <WORKFLOWNAME> <ACTION>

WORKFLOWNAME=$1
ACTION=$2

if [ -z "$WORKFLOWNAME" ] || [ -z "$ACTION" ]; then
    echo "Usage: ./first-principles-notify.sh <WORKFLOWNAME> <ACTION>"
    exit 1
fi

# 1. Send voice notification
curl -s -X POST http://localhost:8888/notify \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"Running the $WORKFLOWNAME workflow in the FirstPrinciples skill to $ACTION\"}" \
  > /dev/null 2>&1 &

# 2. Output text notification
echo "Running the **$WORKFLOWNAME** workflow in the **FirstPrinciples** skill to $ACTION..."
