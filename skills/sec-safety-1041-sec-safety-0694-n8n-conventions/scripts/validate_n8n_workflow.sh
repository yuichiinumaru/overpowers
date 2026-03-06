#!/bin/bash
# Simple validator for n8n workflow JSON files
workflow_file=$1

if [ -z "$workflow_file" ]; then
    echo "Usage: $0 <workflow.json>"
    return 1 2>/dev/null || true
fi

if ! jq -e '.nodes' "$workflow_file" >/dev/null 2>&1; then
    echo "Invalid n8n workflow: 'nodes' key missing."
    return 1 2>/dev/null || true
fi
echo "Workflow $workflow_file appears valid."
