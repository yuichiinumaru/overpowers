#!/bin/bash
# GitHub PR Manager Helper
# Simplifies PR creation and management using the gh CLI

set -e

show_help() {
    echo "Usage: $0 <command> [options]"
    echo ""
    echo "Commands:"
    echo "  create [title] [body_file] - Create a new PR"
    echo "  status                     - Show status of current PR"
    echo "  merge [pr_number]          - Merge a PR (squash and delete branch)"
    echo "  template                   - Generate a PR description template"
}

if [ -z "$1" ]; then
    show_help
fi

COMMAND=$1
shift

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo "Error: gh CLI is not installed or not in PATH."
fi

case "$COMMAND" in
    create)
        TITLE=${1:-"Update"}
        BODY_FILE=$2

        CMD="gh pr create --title \"$TITLE\""
        if [ -n "$BODY_FILE" ] && [ -f "$BODY_FILE" ]; then
            CMD="$CMD --body-file \"$BODY_FILE\""
        else
            CMD="$CMD --fill"
        fi

        echo "Creating PR..."
        eval "$CMD"
        ;;

    status)
        echo "Checking PR status..."
        gh pr status
        gh pr checks
        ;;

    merge)
        PR_NUM=$1
        if [ -z "$PR_NUM" ]; then
            echo "Merging current branch's PR..."
            gh pr merge --squash --delete-branch
        else
            echo "Merging PR #$PR_NUM..."
            gh pr merge "$PR_NUM" --squash --delete-branch
        fi
        ;;

    template)
        cat << 'TEMPLATE' > pr_template.md
## Summary
Brief description of changes

## Motivation
Why these changes are needed

## Changes
- List of specific changes
- Breaking changes highlighted

## Testing
- How changes were tested
- Test coverage metrics

## Checklist
- [ ] Tests pass
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
TEMPLATE
        echo "Created PR template at pr_template.md"
        ;;

    *)
        echo "Unknown command: $COMMAND"
        show_help
        ;;
esac
