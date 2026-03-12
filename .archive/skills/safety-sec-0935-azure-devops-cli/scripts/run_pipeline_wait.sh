#!/bin/bash
set -e

PIPELINE_NAME=$1

if [ -z "$PIPELINE_NAME" ]; then
  echo "Usage: $0 <pipeline_name>"
  exit 1
fi

echo "Running pipeline: $PIPELINE_NAME"
RUN_ID=$(az pipelines run --name "$PIPELINE_NAME" --query "id" -o tsv)

if [ -z "$RUN_ID" ]; then
  echo "Failed to start pipeline"
  exit 1
fi

echo "Started run ID: $RUN_ID. Waiting for completion..."

while true; do
  STATUS=$(az pipelines runs show --run-id $RUN_ID --query "status" -o tsv)
  if [[ "$STATUS" != "inProgress" && "$STATUS" != "notStarted" ]]; then
    break
  fi
  sleep 10
done

RESULT=$(az pipelines runs show --run-id $RUN_ID --query "result" -o tsv)
if [[ "$RESULT" == "succeeded" ]]; then
  echo "Pipeline succeeded"
else
  echo "Pipeline failed with result: $RESULT"
  exit 1
fi