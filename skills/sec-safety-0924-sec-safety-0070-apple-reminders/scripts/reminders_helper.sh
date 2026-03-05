#!/bin/bash

# Helper for managing Apple Reminders via the 'remindctl' CLI on macOS.

ACTION=$1
ARG=$2

function show_usage() {
    echo "Usage: $0 <action> [args]"
    echo "Actions:"
    echo "  today            - Show today's reminders"
    echo "  add <title>      - Quick add a reminder"
    echo "  list             - List all reminder lists"
    echo "  complete <id>    - Complete a reminder by ID"
    echo "  status           - Check permission status"
    exit 1
}

if [ -z "$ACTION" ]; then
    show_usage
fi

case $ACTION in
    today)
        remindctl today
        ;;
    add)
        if [ -z "$ARG" ]; then show_usage; fi
        remindctl add "$ARG"
        ;;
    list)
        remindctl list
        ;;
    complete)
        if [ -z "$ARG" ]; then show_usage; fi
        remindctl complete "$ARG"
        ;;
    status)
        remindctl status
        ;;
    *)
        show_usage
        ;;
esac
