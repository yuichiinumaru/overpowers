#!/bin/bash
# Wrapper script for eightctl to interact with Eight Sleep pods

# Ensure eightctl is installed
if ! command -v eightctl &> /dev/null; then
    echo "eightctl not found. Please install it."
    exit 1
fi

COMMAND=$1
shift

case "$COMMAND" in
    status)
        eightctl status
        ;;
    on)
        eightctl on
        ;;
    off)
        eightctl off
        ;;
    temp)
        if [ -z "$1" ]; then
            echo "Usage: $0 temp <temperature>"
            exit 1
        fi
        eightctl temp "$1"
        ;;
    alarm)
        eightctl alarm "$@"
        ;;
    schedule)
        eightctl schedule "$@"
        ;;
    audio)
        eightctl audio "$@"
        ;;
    base)
        eightctl base "$@"
        ;;
    *)
        echo "Usage: $0 {status|on|off|temp|alarm|schedule|audio|base} [args...]"
        exit 1
        ;;
esac
