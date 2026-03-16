#!/bin/bash
# Pyrefly Type Coverage Helper Script

if [ -z "$1" ]; then
    echo "Usage: $0 [check] <FILENAME>"
    echo "Example: $0 check torch/_dynamo/utils.py"
    exit 1
fi

CMD=$1
shift

case "$CMD" in
    check)
        if [ -z "$1" ]; then
            echo "Error: Filename required for 'check' command."
            exit 1
        fi
        pyrefly check "$@"
        ;;
    *)
        echo "Unknown command: $CMD"
        echo "Valid commands: check"
        exit 1
        ;;
esac