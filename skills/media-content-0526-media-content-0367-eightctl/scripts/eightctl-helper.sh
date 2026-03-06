#!/bin/bash
# Helper script for eightctl to prevent repeated logins and handle common commands

command=$1
shift

if [ -z "$command" ]; then
    echo "Usage: ./eightctl-helper.sh <command> [args]"
    echo "Commands: status, on, off, temp <value>, alarm <args>, schedule <args>, audio <args>, base <args>"
    exit 1
fi

case "$command" in
    status|on|off|temp|alarm|schedule|audio|base)
        eightctl "$command" "$@"
        ;;
    *)
        echo "Unknown command: $command"
        exit 1
        ;;
esac
