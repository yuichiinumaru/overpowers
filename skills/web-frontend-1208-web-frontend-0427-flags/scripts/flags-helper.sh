#!/bin/bash

# Feature Flags Helper
# Requirement: yarn

usage() {
    echo "Usage: $0 [command] [args]"
    echo ""
    echo "Commands:"
    echo "  all              Show all flags across all channels"
    echo "  diff [ch1] [ch2] Compare flags between two channels"
    echo "  cleanup          Show flags grouped by cleanup status"
    echo "  csv              Output in CSV format"
    echo ""
}

case "$1" in
    all)
        yarn flags
        ;;
    diff)
        if [ -z "$2" ] || [ -z "$3" ]; then
            echo "Error: Two channels required for diff"
            exit 1
        fi
        yarn flags --diff "$2" "$3"
        ;;
    cleanup)
        yarn flags --cleanup
        ;;
    csv)
        yarn flags --csv
        ;;
    *)
        usage
        exit 1
        ;;
esac
