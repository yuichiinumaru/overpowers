#!/bin/bash

# Local Places Helper
# Requires local proxy running at http://127.0.0.1:8000

API_URL="http://127.0.0.1:8000"

usage() {
    echo "Usage: $0 [command] [args]"
    echo ""
    echo "Commands:"
    echo "  ping                     Check if server is running"
    echo "  resolve [location_text]  Resolve location text to coordinates"
    echo "  search [json_data]       Search places with JSON data"
    echo "  details [place_id]       Get details for a place ID"
    echo ""
}

case "$1" in
    ping)
        curl -s "$API_URL/ping"
        echo ""
        ;;
    resolve)
        location="$2"
        curl -s -X POST "$API_URL/locations/resolve" \
          -H "Content-Type: application/json" \
          -d "{\"location_text\": \"$location\", \"limit\": 5}"
        echo ""
        ;;
    search)
        data="$2"
        curl -s -X POST "$API_URL/places/search" \
          -H "Content-Type: application/json" \
          -d "$data"
        echo ""
        ;;
    details)
        id="$2"
        curl -s "$API_URL/places/$id"
        echo ""
        ;;
    *)
        usage
        exit 1
        ;;
esac
