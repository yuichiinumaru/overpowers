#!/bin/bash
# Feishu permission helper
ACTION=$1
TOKEN=$2
TYPE=$3
MEMBER_TYPE=$4
MEMBER_ID=$5
PERM=$6

echo "Running Feishu permission action: $ACTION on $TYPE (token: $TOKEN)"
if [ "$ACTION" = "list" ]; then
    echo "Listing collaborators..."
elif [ "$ACTION" = "add" ]; then
    echo "Adding collaborator: $MEMBER_ID ($MEMBER_TYPE) with perm: $PERM"
elif [ "$ACTION" = "remove" ]; then
    echo "Removing collaborator: $MEMBER_ID ($MEMBER_TYPE)"
else
    echo "Unknown action"
fi
