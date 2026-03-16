#!/bin/bash
# Apple Notes Helper
# A wrapper script to manage Apple Notes via the `memo` CLI

show_help() {
    echo "Usage: $0 <command> [options]"
    echo ""
    echo "Commands:"
    echo "  list                      - List all notes"
    echo "  list -f <folder>          - List notes in a specific folder"
    echo "  search <query>            - Search notes"
    echo "  add <title>               - Quick add a new note with title"
    echo "  edit                      - Interactive edit"
    echo "  delete                    - Interactive delete"
    echo "  move                      - Interactive move to folder"
    echo "  export                    - Interactive export"
    echo ""
    echo "Note: This script requires the 'memo' CLI tool to be installed on macOS."
}

if [ -z "$1" ]; then
    show_help
fi

COMMAND=$1
shift

if ! command -v memo &> /dev/null; then
    echo "Error: 'memo' CLI tool is not installed."
    echo "Install via Homebrew: brew tap antoniorodr/memo && brew install antoniorodr/memo/memo"
fi

case "$COMMAND" in
    list)
        if [ "$1" == "-f" ] && [ -n "$2" ]; then
            memo notes -f "$2"
        else
            memo notes
        fi
        ;;
    search)
        if [ -n "$1" ]; then
            memo notes -s "$1"
        else
            echo "Error: Search query required."
        fi
        ;;
    add)
        if [ -n "$1" ]; then
            memo notes -a "$1"
        else
            memo notes -a
        fi
        ;;
    edit)
        memo notes -e
        ;;
    delete)
        memo notes -d
        ;;
    move)
        memo notes -m
        ;;
    export)
        memo notes -ex
        ;;
    *)
        echo "Unknown command: $COMMAND"
        show_help
        ;;
esac
