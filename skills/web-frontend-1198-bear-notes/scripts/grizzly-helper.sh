#!/bin/bash

# Bear Notes Helper via grizzly CLI
# Requirement: grizzly CLI must be installed

GRIZZLY_TOKEN_FILE="${GRIZZLY_TOKEN_FILE:-$HOME/.config/grizzly/token}"

usage() {
    echo "Usage: $0 [command] [args]"
    echo ""
    echo "Commands:"
    echo "  create [title] [tags] [content]  Create a new note"
    echo "  read [id]                        Read/Open a note by ID"
    echo "  append [id] [content]            Append text to a note"
    echo "  tags                             List all tags"
    echo "  search [tag]                     Search notes by tag"
    echo "  token [token]                    Save Bear API token"
    echo ""
}

case "$1" in
    create)
        title="$2"
        tags="$3"
        content="$4"
        if [ -z "$content" ]; then
            grizzly create --title "$title" --tag "$tags" < /dev/null
        else
            echo "$content" | grizzly create --title "$title" --tag "$tags"
        fi
        ;;
    read)
        id="$2"
        grizzly open-note --id "$id" --enable-callback --json
        ;;
    append)
        id="$2"
        content="$3"
        echo "$content" | grizzly add-text --id "$id" --mode append --token-file "$GRIZZLY_TOKEN_FILE"
        ;;
    tags)
        grizzly tags --enable-callback --json --token-file "$GRIZZLY_TOKEN_FILE"
        ;;
    search)
        tag="$2"
        grizzly open-tag --name "$tag" --enable-callback --json
        ;;
    token)
        token="$2"
        mkdir -p "$(dirname "$GRIZZLY_TOKEN_FILE")"
        echo "$token" > "$GRIZZLY_TOKEN_FILE"
        echo "Token saved to $GRIZZLY_TOKEN_FILE"
        ;;
    *)
        usage
        exit 1
        ;;
esac
