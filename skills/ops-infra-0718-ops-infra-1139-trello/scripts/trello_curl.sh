#!/bin/bash
# Helper for Trello REST API

if [[ -z "$TRELLO_API_KEY" || -z "$TRELLO_TOKEN" ]]; then
  echo "Error: TRELLO_API_KEY and TRELLO_TOKEN must be set."
  exit 1
fi

AUTH="key=$TRELLO_API_KEY&token=$TRELLO_TOKEN"
BASE_URL="https://api.trello.com/1"

COMMAND=$1
shift

case $COMMAND in
  "list_boards")
    curl -s "$BASE_URL/members/me/boards?$AUTH&fields=name,id" | jq '.[] | {name, id}'
    ;;
  "list_lists")
    BOARD_ID=$1
    curl -s "$BASE_URL/boards/$BOARD_ID/lists?$AUTH&fields=name,id" | jq '.[] | {name, id}'
    ;;
  "list_cards")
    LIST_ID=$1
    curl -s "$BASE_URL/lists/$LIST_ID/cards?$AUTH&fields=name,id,desc" | jq '.[] | {name, id}'
    ;;
  "create_card")
    LIST_ID=$1
    NAME=$2
    DESC=$3
    curl -s -X POST "$BASE_URL/cards?$AUTH" \
      -d "idList=$LIST_ID" \
      -d "name=$NAME" \
      -d "desc=$DESC" | jq '{name, id, url}'
    ;;
  *)
    echo "Usage: $0 {list_boards|list_lists <boardId>|list_cards <listId>|create_card <listId> <name> <desc>}"
    exit 1
    ;;
esac
