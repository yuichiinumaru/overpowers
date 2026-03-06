#!/bin/bash

# n8n health check helper
# Usage: ./n8n_health.sh [diagnostic]

MODE=${1:-"quick"}

if [ "$MODE" == "diagnostic" ]; then
    echo "Running detailed n8n diagnostics..."
    # Example using mcporter to call n8n-mcp health check
    mcporter call n8n-mcp.n8n_health_check mode=diagnostic
else
    echo "Running quick n8n health check..."
    mcporter call n8n-mcp.n8n_health_check mode=standard
fi
