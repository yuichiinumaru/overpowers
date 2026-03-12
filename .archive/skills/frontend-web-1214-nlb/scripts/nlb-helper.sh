#!/bin/bash

# NLB Helper

usage() {
    echo "Usage: $0 search [query]"
    echo "This script generates an NLB search URL."
}

case "$1" in
    search)
        query="$2"
        if [ -z "$query" ]; then
            echo "Error: Search query required."
            usage
            exit 1
        fi
        
        # Simple URL encoding using jq (requires jq to be installed)
        encoded_query=$(echo -n "$query" | jq -sRr @uri)
        
        url="https://catalogue.nlb.gov.sg/search?query=$encoded_query"
        echo "NLB Search URL:"
        echo "$url"
        ;;
    *)
        usage
        exit 1
        ;;
esac
