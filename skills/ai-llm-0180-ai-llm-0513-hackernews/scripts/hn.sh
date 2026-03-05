#!/bin/bash
# hn.sh - Hacker News API CLI helper

COMMAND=$1
SHIFTED_ARGS="${@:2}"

BASE_URL="https://hacker-news.firebaseio.com/v0"
SEARCH_URL="https://hn.algolia.com/api/v1"

# Default limit
LIMIT=10
JSON_OUTPUT=false

# Simple argument parsing
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --limit) LIMIT="$2"; shift ;;
        --json) JSON_OUTPUT=true ;;
    esac
    shift
done

fetch_item() {
    local id=$1
    if [ "$JSON_OUTPUT" = true ]; then
        curl -s "$BASE_URL/item/$id.json"
    else
        curl -s "$BASE_URL/item/$id.json" | jq -r '"\(.title) [\(.score) pts] - \(.url // "https://news.ycombinator.com/item?id=" + (.id|tostring))"'
    fi
}

list_stories() {
    local type=$1
    local ids=$(curl -s "$BASE_URL/${type}.json" | jq ".[0:$LIMIT][]")
    for id in $ids; do
        fetch_item "$id"
    done
}

case "$COMMAND" in
    top)
        list_stories "topstories"
        ;;
    new)
        list_stories "newstories"
        ;;
    best)
        list_stories "beststories"
        ;;
    ask)
        list_stories "askstories"
        ;;
    show)
        list_stories "showstories"
        ;;
    jobs)
        list_stories "jobstories"
        ;;
    item)
        id=$(echo "$SHIFTED_ARGS" | awk '{print $1}')
        fetch_item "$id"
        ;;
    user)
        user_id=$(echo "$SHIFTED_ARGS" | awk '{print $1}')
        curl -s "$BASE_URL/user/$user_id.json" | jq .
        ;;
    search)
        query=$(echo "$SHIFTED_ARGS" | sed 's/--limit.*//' | sed 's/--json.*//')
        if [ "$JSON_OUTPUT" = true ]; then
            curl -s "$SEARCH_URL/search?query=$query&hitsPerPage=$LIMIT"
        else
            curl -s "$SEARCH_URL/search?query=$query&hitsPerPage=$LIMIT" | jq -r '.hits[] | "\(.title) - \(.url // "https://news.ycombinator.com/item?id=" + .objectID)"'
        fi
        ;;
    whoishiring)
        # Search for latest "Who is hiring" thread
        latest_thread_id=$(curl -s "$SEARCH_URL/search?query=Who%20is%20hiring&tags=story,author_whoishiring&hitsPerPage=1" | jq -r '.hits[0].objectID')
        if [ "$latest_thread_id" != "null" ]; then
            echo "Latest 'Who is hiring' thread: https://news.ycombinator.com/item?id=$latest_thread_id"
            if [ "$JSON_OUTPUT" = true ]; then
                curl -s "$BASE_URL/item/$latest_thread_id.json"
            fi
        else
            echo "Could not find latest 'Who is hiring' thread."
        fi
        ;;
    *)
        echo "Usage: $0 <command> [options]"
        echo "Commands: top, new, best, ask, show, jobs, item <id>, user <user_id>, search <query>, whoishiring"
        echo "Options: --limit <n>, --json"
        ;;
esac
