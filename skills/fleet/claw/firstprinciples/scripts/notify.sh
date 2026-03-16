#!/bin/bash
# Send voice notification for FirstPrinciples workflow

WORKFLOW_NAME=${1:-UnknownWorkflow}
ACTION=${2:-Execute}

curl -s -X POST http://localhost:8888/notify \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"Running the $WORKFLOW_NAME workflow in the FirstPrinciples skill to $ACTION\"}" \
  > /dev/null 2>&1 &

echo "Running the **$WORKFLOW_NAME** workflow in the **FirstPrinciples** skill to $ACTION..."
