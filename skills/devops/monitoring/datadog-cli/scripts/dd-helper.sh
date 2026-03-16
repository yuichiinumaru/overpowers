#!/bin/bash

# Datadog CLI Helper
# Requirements: 
# - npx (Node.js)
# - DD_API_KEY and DD_APP_KEY environment variables

usage() {
    echo "Usage: $0 [command] [args]"
    echo ""
    echo "Commands:"
    echo "  errors [from]            Quick error summary (default from: 1h)"
    echo "  search [query] [from]    Search logs"
    echo "  tail [query]             Tail logs in real-time"
    echo "  metrics [query] [from]   Query metrics"
    echo "  trace [id]               Follow a distributed trace"
    echo ""
}

case "$1" in
    errors)
        from="${2:-1h}"
        npx @leoflores/datadog-cli errors --from "$from" --pretty
        ;;
    search)
        query="$2"
        from="${3:-1h}"
        npx @leoflores/datadog-cli logs search --query "$query" --from "$from" --pretty
        ;;
    tail)
        query="$2"
        npx @leoflores/datadog-cli logs tail --query "$query" --pretty
        ;;
    metrics)
        query="$2"
        from="${3:-1h}"
        npx @leoflores/datadog-cli metrics query --query "$query" --from "$from" --pretty
        ;;
    trace)
        id="$2"
        npx @leoflores/datadog-cli logs trace --id "$id" --pretty
        ;;
    *)
        usage
        exit 1
        ;;
esac
