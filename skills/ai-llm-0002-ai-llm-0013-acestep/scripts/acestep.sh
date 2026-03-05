#!/bin/bash

# ACE-Step Music Generation Script
# Implements the functionality described in SKILL.md

CONFIG_FILE="$(dirname "$0")/config.json"

# Check dependencies
check_dependencies() {
    if ! command -v curl &> /dev/null; then
        echo "Error: curl is not installed."
        exit 1
    fi
    if ! command -v jq &> /dev/null; then
        echo "jq is not installed. Attempting to install..."
        if [[ "$OSTYPE" == "linux-gnu"* ]]; then
            sudo apt-get update && sudo apt-get install -y jq
        elif [[ "$OSTYPE" == "darwin"* ]]; then
            brew install jq
        else
            echo "Please install jq manually: https://jqlang.github.io/jq/download/"
            exit 1
        fi
    fi
}

load_config() {
    if [[ -f "$CONFIG_FILE" ]]; then
        API_URL=$(jq -r '.api_url' "$CONFIG_FILE")
        API_KEY=$(jq -r '.api_key' "$CONFIG_FILE")
    else
        API_URL="http://127.0.0.1:8001"
        API_KEY=""
    fi
}

health_check() {
    curl -s "$API_URL/health" | jq .
}

list_models() {
    curl -s "$API_URL/v1/models" | jq .
}

get_status() {
    local task_id=$1
    curl -s -X POST "$API_URL/query_result" \
        -H "Content-Type: application/json" \
        -d "{\"task_id_list\": [\"$task_id\"]}" | jq .
}
generate_music() {
    local prompt=""
    local lyrics=""
    local duration=60
    local bpm=120
    local batch_size=1
    local thinking="true"

    while [[ "$#" -gt 0 ]]; do
        case $1 in
            -c|--caption) prompt="$2"; shift ;;
            -l|--lyrics) lyrics="$2"; shift ;;
            -d|--description) sample_query="$2"; sample_mode="true"; shift ;;
            --duration) duration="$2"; shift ;;
            --bpm) bpm="$2"; shift ;;
            --batch) batch_size="$2"; shift ;;
            --no-thinking) thinking="false" ;;
            *) if [[ -z "$prompt" ]]; then prompt="$1"; fi ;;
        esac
        shift
    done

    local data=""
    if [[ "$sample_mode" == "true" ]]; then
        data=$(jq -n \
            --arg sq "$sample_query" \
            --argjson t "$thinking" \
            --argjson d "$duration" \
            --argjson b "$bpm" \
            --argjson bs "$batch_size" \
            '{sample_mode: true, sample_query: $sq, thinking: $t, batch_size: $bs, param_obj: {duration: $d, bpm: $b}}')
    else
        data=$(jq -n \
            --arg p "$prompt" \
            --arg l "$lyrics" \
            --argjson t "$thinking" \
            --argjson d "$duration" \
            --argjson b "$bpm" \
            --argjson bs "$batch_size" \
            '{prompt: $p, lyrics: $l, thinking: $t, batch_size: $bs, param_obj: {duration: $d, bpm: $b}}')
    fi

    curl -s -X POST "$API_URL/release_task" \
        -H "Content-Type: application/json" \
        -d "$data" | jq .
}

main() {
    check_dependencies
    load_config

    case $1 in
        health) health_check ;;
        models) list_models ;;
        status) get_status "$2" ;;
        generate) shift; generate_music "$@" ;;
        config)
            if [[ "$2" == "--set" ]]; then
                # Very basic set logic for demonstration
                tmp_config=$(jq --arg k "$3" --arg v "$4" '.[$k] = $v' "$CONFIG_FILE")
                echo "$tmp_config" > "$CONFIG_FILE"
                echo "Updated $3 to $4"
            else
                cat "$CONFIG_FILE"
            fi
            ;;
        *) echo "Usage: $0 {health|models|status <id>|generate <args>|config}" ;;
    esac
}

main "$@"
