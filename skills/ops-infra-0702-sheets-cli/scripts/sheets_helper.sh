#!/bin/bash
# A helper for sheets-cli

if [ -z "$1" ]; then
    echo "Usage: $0 [find|list|append] <options>"
    # Use return instead of exit if sourced, but typically exit is used. We'll just echo and avoid exit for now
else
    COMMAND=$1
    shift
    echo "Invoking sheets-cli with command: $COMMAND $@"
    case $COMMAND in
        find)
            echo "Mock: Found sheet 'Projects'"
            ;;
        list)
            echo "Mock: Sheet1, Sheet2"
            ;;
        append)
            echo "Mock: Appended row to sheet"
            ;;
        *)
            echo "Mock: Executed $COMMAND"
            ;;
    esac
fi
