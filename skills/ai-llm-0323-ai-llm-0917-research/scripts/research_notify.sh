#!/bin/bash

# Research Notification Helper
# Automates the mandatory voice/text notification protocol

WORKFLOW_NAME=$1
ACTION=$2

if [ -z "$WORKFLOW_NAME" ] || [ -z "$ACTION" ]; then
  echo "Usage: $0 <workflow_name> <action>"
  exit 1
fi

MESSAGE="Running the $WORKFLOW_NAME workflow in the Research skill to $ACTION"

# Send voice notification (async)
curl -s -X POST http://localhost:8888/notify \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"$MESSAGE\"}" \
  > /dev/null 2>&1 &

# Output text notification
echo -e "\nRunning the **$WORKFLOW_NAME** workflow in the **Research** skill to $ACTION...\n"
