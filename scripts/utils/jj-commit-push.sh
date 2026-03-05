#!/bin/bash
set -e

# Default variables
MESSAGE=""
BOOKMARK=""

function print_usage {
    echo -e "\033[1;34mUsage:\033[0m $0 -m \"<commit_message>\" [-b <bookmark_name>]"
    echo -e "Automates the Jujutsu workflow: sets the commit description, manages bookmarks, and pushes to origin."
    echo -e ""
    echo -e "\033[1;36mOptions:\033[0m"
    echo -e "  -m    The commit description (Required)"
    echo -e "  -b    The bookmark (branch) name (Optional. Creates or moves it to the current commit)"
    exit 1
}

# Parse arguments
while getopts "m:b:h" flag; do
    case "${flag}" in
        m) MESSAGE="${OPTARG}" ;;
        b) BOOKMARK="${OPTARG}" ;;
        h) print_usage ;;
        *) print_usage ;;
    esac
done

if [ -z "$MESSAGE" ]; then
    echo -e "\033[1;31mError: Commit message (-m) is required.\033[0m"
    print_usage
fi

echo -e "\033[1;32m🚀 Starting automated jj commit & push...\033[0m"

# 1. Update commit message
echo -e "\033[1;33m📝 Updating commit description...\033[0m"
jj describe -m "$MESSAGE"

# 2. Bookmarks handling
if [ -n "$BOOKMARK" ]; then
    echo -e "\033[1;33m🔖 Setting bookmark '$BOOKMARK' to current commit '@'...\033[0m"
    # Will move it if it exists or create it if it doesn't
    jj bookmark move "$BOOKMARK" --to @ 2>/dev/null || jj bookmark create "$BOOKMARK" -r @
    
    echo -e "\033[1;33m⬆️  Pushing bookmark '$BOOKMARK' to origin...\033[0m"
    # We use --allow-new in case the bookmark hasn't been published yet
    jj git push --bookmark "$BOOKMARK" --allow-new
else
    # Automatically get bookmarks for current commit (@)
    CURRENT_BKS=$(jj log -r @ -T 'bookmarks.map(|b| b.name()).join(" ")' --no-graph)
    
    if [ -z "$CURRENT_BKS" ]; then
        echo -e "\033[1;31m❌ Error: No bookmarks pointing to '@'. Please provide one explicitly with -b <bookmark_name>\033[0m"
        exit 1
    fi
    
    echo -e "\033[1;33m🔍 Detected bookmarks on current commit: $CURRENT_BKS\033[0m"
    echo -e "\033[1;33m⬆️  Pushing changes to origin...\033[0m"
    
    # Just generic push relying on jj default tracking
    jj git push 
fi

echo -e "\033[1;32m✅ Successfully committed and pushed!\033[0m"
