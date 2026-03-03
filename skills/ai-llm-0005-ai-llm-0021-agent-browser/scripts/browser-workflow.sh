#!/bin/bash

# Script to demonstrate a common agent-browser workflow.
# Usage: ./browser-workflow.sh login <url> <username> <password> <output_state_file>

COMMAND=$1

case $COMMAND in
    login)
        URL=$2
        USER=$3
        PASS=$4
        STATE=$5
        if [[ -z "$URL" || -z "$USER" || -z "$PASS" || -z "$STATE" ]]; then
            echo "Usage: $0 login <url> <username> <password> <output_state_file>"
            exit 1
        fi
        echo "Starting login workflow for $URL..."
        agent-browser open "$URL"
        agent-browser snapshot -i
        # This assumes @e1 is username, @e2 is password, @e3 is submit
        # In a real scenario, the agent would identify these from the snapshot.
        echo "Filling credentials..."
        agent-browser fill @e1 "$USER"
        agent-browser fill @e2 "$PASS"
        agent-browser click @e3
        agent-browser wait --load networkidle
        echo "Saving state to $STATE..."
        agent-browser state save "$STATE"
        ;;
    extract)
        URL=$2
        SELECTOR=$3
        if [[ -z "$URL" || -z "$SELECTOR" ]]; then
            echo "Usage: $0 extract <url> <selector>"
            exit 1
        fi
        agent-browser open "$URL"
        agent-browser wait --load networkidle
        agent-browser get text "$SELECTOR"
        ;;
    *)
        echo "Usage: $0 {login|extract} <args>"
        exit 1
        ;;
esac
