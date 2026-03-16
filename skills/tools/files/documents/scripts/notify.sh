#!/bin/bash
# Mandatory notification for Documents skill

WORKFLOW=$1
ACTION=$2

if [ -z "$WORKFLOW" ] || [ -z "$ACTION" ]; then
    echo "Usage: $0 <WORKFLOWNAME> <ACTION>"
    exit 1
fi

MESSAGE="Running the $WORKFLOW workflow in the Documents skill to $ACTION"

# Send voice notification (if server available)
curl -s -X POST http://localhost:8888/notify \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"$MESSAGE\"}" \
  > /dev/null 2>&1 &

# Output text notification
echo "Running the **$WORKFLOW** workflow in the **Documents** skill to $ACTION..."
