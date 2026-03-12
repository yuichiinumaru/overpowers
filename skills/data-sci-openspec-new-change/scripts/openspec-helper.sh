#!/bin/bash
# OpenSpec-CN Helper Script
# Provides a wrapper to openspec-cn CLI tools.

if [ -z "$1" ]; then
    echo "Usage: $0 [new|status|instructions] [args...]"
    echo "Example: $0 new change \"feature_x\""
    echo "Example: $0 status --change \"feature_x\""
    echo "Example: $0 instructions <artifact-id> --change \"feature_x\""
    exit 1
fi

CMD=$1
shift

case "$CMD" in
    new)
        # e.g. new change "feature_x"
        openspec-cn new "$@"
        ;;
    status)
        openspec-cn status "$@"
        ;;
    instructions)
        openspec-cn instructions "$@"
        ;;
    *)
        echo "Unknown command: $CMD"
        echo "Valid commands: new, status, instructions"
        exit 1
        ;;
esac