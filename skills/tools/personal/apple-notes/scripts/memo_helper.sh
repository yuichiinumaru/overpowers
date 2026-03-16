#!/bin/bash

# Helper for managing Apple Notes via the 'memo' CLI on macOS.

ACTION=$1
ARG=$2

function show_usage() {
    echo "Usage: $0 <action> [args]"
    echo "Actions:"
    echo "  list [folder]    - List notes, optionally filtered by folder"
    echo "  search <query>   - Search notes (fuzzy)"
    echo "  add <title>      - Add a new note with title"
    echo "  export           - Export a note to HTML/Markdown (interactive)"
    exit 1
}

if [ -z "$ACTION" ]; then
    show_usage
fi

case $ACTION in
    list)
        if [ -z "$ARG" ]; then
            memo notes
        else
            memo notes -f "$ARG"
        fi
        ;;
    search)
        if [ -z "$ARG" ]; then show_usage; fi
        memo notes -s "$ARG"
        ;;
    add)
        if [ -z "$ARG" ]; then show_usage; fi
        memo notes -a "$ARG"
        ;;
    export)
        memo notes -ex
        ;;
    *)
        show_usage
        ;;
esac
