#!/bin/bash

# Firecrawl Scrape Helper
# Requirement: uv, python, and firecrawl MCP configured

usage() {
    echo "Usage: $0 [command] [arg]"
    echo ""
    echo "Commands:"
    echo "  scrape [url]      Scrape content from a URL (default: markdown)"
    echo "  search [query]    Search and scrape content"
    echo ""
}

HARNESS_SCRIPT="/home/sephiroth/Work/overpowers/scripts/mcp/firecrawl_scrape.py"

case "$1" in
    scrape)
        url="$2"
        uv run python -m runtime.harness "$HARNESS_SCRIPT" --url "$url" --format "markdown"
        ;;
    search)
        query="$2"
        uv run python -m runtime.harness "$HARNESS_SCRIPT" --search "$query"
        ;;
    *)
        usage
        exit 1
        ;;
esac
