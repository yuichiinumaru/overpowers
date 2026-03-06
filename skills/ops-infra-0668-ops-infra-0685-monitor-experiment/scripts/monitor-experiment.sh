#!/bin/bash
set -e

if [ -z "$1" ]; then
    echo "Usage: ./monitor-experiment.sh <experiment-id>"
    exit 1
fi

EXPERIMENT_ID=$1
echo "Monitoring Beaker experiment: $EXPERIMENT_ID"

while true; do
    # Get the JSON output of the experiment status
    STATUS_JSON=$(beaker experiment get "$EXPERIMENT_ID" --format=json 2>/dev/null)

    # Check if the beaker command failed
    if [ $? -ne 0 ]; then
        echo "Failed to get experiment status. Is beaker configured correctly?"
        exit 1
    fi

    # We parse the json (using jq if available, otherwise grep)
    # The instructions say to look at status.exited and exitCode
    if command -v jq &> /dev/null; then
        EXITED=$(echo "$STATUS_JSON" | jq -r '.[0].jobs[0].status.exited // false')
        EXIT_CODE=$(echo "$STATUS_JSON" | jq -r '.[0].jobs[0].status.exitCode // 0')
    else
        # Fallback to simple grep parsing if jq is not installed
        # This is a bit fragile but works for simple cases
        if echo "$STATUS_JSON" | grep -q '"exited": true'; then
            EXITED="true"
            EXIT_CODE=$(echo "$STATUS_JSON" | grep '"exitCode"' | awk -F':' '{print $2}' | tr -d ' ,')
        else
            EXITED="false"
        fi
    fi

    if [ "$EXITED" = "true" ] || [ "$EXITED" = "True" ]; then
        echo "Experiment completed."

        if [ "$EXIT_CODE" = "0" ]; then
            echo "Success! (Exit code 0)"
            exit 0
        else
            echo "Experiment failed with exit code: $EXIT_CODE"
            echo "Fetching logs..."
            beaker experiment logs "$EXPERIMENT_ID"
            exit 1
        fi
    fi

    echo "Experiment is still running. Waiting 30 seconds..."
    sleep 30
done
