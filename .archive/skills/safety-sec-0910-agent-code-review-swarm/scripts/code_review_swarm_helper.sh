#!/bin/bash
# Code Review Swarm Helper
# Automates the invocation of code review swarm agents via GitHub CLI

set -e

show_help() {
    echo "Usage: $0 <command> [options]"
    echo ""
    echo "Commands:"
    echo "  trigger <pr_number> <agents>  - Trigger a code review swarm on a PR"
    echo "  security <pr_number>          - Run specifically the security review agent"
    echo "  performance <pr_number>       - Run specifically the performance review agent"
    echo "  architecture <pr_number>      - Run specifically the architecture review agent"
    echo ""
    echo "Options:"
    echo "  --dry-run                     - Print commands without executing them"
}

if [ -z "$1" ]; then
    show_help
fi

COMMAND=$1
shift

DRY_RUN=false
for arg in "$@"; do
  if [ "$arg" == "--dry-run" ]; then
    DRY_RUN=true
    # remove --dry-run from args
    set -- "${@/--dry-run/}"
  fi
done

execute() {
    if [ "$DRY_RUN" = true ]; then
        echo "[DRY RUN] $@"
    else
        echo "Executing: $@"
        eval "$@"
    fi
}

case "$COMMAND" in
    trigger)
        if [ -z "$1" ] || [ -z "$2" ]; then
            echo "Error: PR number and agents required."
            echo "Example: $0 trigger 123 \"security,performance,style\""
        else
            PR_NUM=$1
            AGENTS=$2
            echo "Triggering swarm review for PR #$PR_NUM with agents: $AGENTS"
            execute "npx ruv-swarm github review-all --pr $PR_NUM --agents \"$AGENTS\""
        fi
        ;;

    security)
        if [ -z "$1" ]; then
            echo "Error: PR number required."
        else
            PR_NUM=$1
            echo "Running security review for PR #$PR_NUM"
            execute "npx ruv-swarm github review-security --pr $PR_NUM --check 'owasp-top-10,secrets,dependencies' --severity high,critical"
        fi
        ;;

    performance)
        if [ -z "$1" ]; then
            echo "Error: PR number required."
        else
            PR_NUM=$1
            echo "Running performance review for PR #$PR_NUM"
            execute "npx ruv-swarm github review-performance --pr $PR_NUM --profile 'cpu,memory,io' --suggest-optimizations"
        fi
        ;;

    architecture)
        if [ -z "$1" ]; then
            echo "Error: PR number required."
        else
            PR_NUM=$1
            echo "Running architecture review for PR #$PR_NUM"
            execute "npx ruv-swarm github review-architecture --pr $PR_NUM --check 'patterns,coupling,cohesion,solid' --suggest-refactoring"
        fi
        ;;

    *)
        echo "Unknown command: $COMMAND"
        show_help
        ;;
esac
