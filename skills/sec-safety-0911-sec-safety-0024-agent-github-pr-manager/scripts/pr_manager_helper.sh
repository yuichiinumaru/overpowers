#!/bin/bash

# Helper for GitHub Pull Request management using gh CLI.

ACTION=$1
PR_ARG=$2

function show_usage() {
    echo "Usage: $0 <action> [args]"
    echo "Actions:"
    echo "  create <title> <body> [base] - Create a PR"
    echo "  status [pr_num]              - Check PR status"
    echo "  merge [pr_num]               - Squash merge and delete branch"
    exit 1
}

if [ -z "$ACTION" ]; then
    show_usage
fi

case $ACTION in
    create)
        TITLE=$2
        BODY=$3
        BASE=${4:-"main"}
        if [ -z "$TITLE" ] || [ -z "$BODY" ]; then show_usage; fi
        gh pr create --title "$TITLE" --body "$BODY" --base "$BASE"
        ;;
    status)
        if [ -z "$PR_ARG" ]; then
            gh pr status --json state,statusCheckRollup
        else
            gh pr view "$PR_ARG" --json state,statusCheckRollup
        fi
        ;;
    merge)
        if [ -z "$PR_ARG" ]; then
            gh pr merge --squash --delete-branch
        else
            gh pr merge "$PR_ARG" --squash --delete-branch
        fi
        ;;
    *)
        show_usage
        ;;
esac
