#!/bin/bash
# Himalaya Email CLI Helper Script
# Provide shortcuts for the most common Himalaya commands.

if [ -z "$1" ]; then
    echo "Usage: $0 [list|read|write|reply|forward|delete|search] [args...]"
    echo "Example: $0 list --folder 'Sent'"
    echo "Example: $0 read 42"
    exit 1
fi

CMD=$1
shift

case "$CMD" in
    list)
        himalaya envelope list "$@"
        ;;
    read)
        himalaya message read "$@"
        ;;
    write)
        if [ "$#" -gt 0 ]; then
            himalaya message write "$@"
        else
            himalaya message write
        fi
        ;;
    reply)
        himalaya message reply "$@"
        ;;
    forward)
        himalaya message forward "$@"
        ;;
    delete)
        himalaya message delete "$@"
        ;;
    search)
        # Search syntax: himalaya envelope list from john@example.com subject meeting
        himalaya envelope list "$@"
        ;;
    *)
        echo "Unknown command: $CMD"
        echo "Valid commands: list, read, write, reply, forward, delete, search"
        exit 1
        ;;
esac