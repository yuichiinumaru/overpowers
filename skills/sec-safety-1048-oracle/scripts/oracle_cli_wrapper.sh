#!/bin/bash
# Wrapper for oracle CLI usage patterns
action=$1

if [ -z "$action" ]; then
    echo "Usage: $0 [bundle|run]"
    return 1 2>/dev/null || true
fi

if [ "$action" == "bundle" ]; then
    echo "Bundling files for Oracle..."
elif [ "$action" == "run" ]; then
    echo "Running Oracle CLI session..."
else
    echo "Unknown action: $action"
fi
