#!/bin/bash
# Apple Reminders Helper
# A wrapper script to manage Apple Reminders via the `remindctl` CLI

show_help() {
    echo "Usage: $0 <command> [options]"
    echo ""
    echo "Commands:"
    echo "  view [filter]             - View reminders (today, tomorrow, week, overdue, upcoming, completed, all)"
    echo "  add <title> [options]     - Add a reminder"
    echo "    Options: --list <name>, --due <date>"
    echo "  complete <id>             - Complete a reminder by ID"
    echo "  lists                     - Show all lists"
    echo ""
    echo "Note: This script requires the 'remindctl' CLI tool to be installed on macOS."
}

if [ -z "$1" ]; then
    show_help
fi

COMMAND=$1
shift

if ! command -v remindctl &> /dev/null; then
    echo "Error: 'remindctl' CLI tool is not installed."
    echo "Install via Homebrew: brew install steipete/tap/remindctl"
fi

case "$COMMAND" in
    view)
        FILTER=${1:-"today"}
        remindctl "$FILTER"
        ;;
    add)
        if [ -z "$1" ]; then
            echo "Error: Title required."
        else
            # We need to construct the command properly to handle the title with quotes
            # and pass through the rest of the arguments
            TITLE=$1
            shift
            remindctl add "$TITLE" "$@"
        fi
        ;;
    complete)
        if [ -z "$1" ]; then
            echo "Error: ID required."
        else
            remindctl complete "$@"
        fi
        ;;
    lists)
        remindctl list
        ;;
    *)
        echo "Unknown command: $COMMAND"
        show_help
        ;;
esac
