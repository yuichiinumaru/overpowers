#!/bin/bash
# notify.sh - Art Skill Voice Notification

WORKFLOWNAME=$1
ACTION=$2

if [ -z "$WORKFLOWNAME" ] || [ -z "$ACTION" ]; then
  echo "Usage: ./notify.sh <WORKFLOWNAME> <ACTION>"
  exit 1
fi

echo "Running the **$WORKFLOWNAME** workflow in the **Art** skill to $ACTION..."

curl -s -X POST http://localhost:8888/notify \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"Running the $WORKFLOWNAME workflow in the Art skill to $ACTION\"}" \
  > /dev/null 2>&1 &
