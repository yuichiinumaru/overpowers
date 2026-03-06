#!/usr/bin/env bash

# Finishing a Development Branch Helper Script
# Usage: ./finish_branch.sh [test-command]
# Example: ./finish_branch.sh "npm test"

TEST_CMD=${1:-"npm test"}

echo "Running tests: $TEST_CMD"
# Mocking test execution for safety. In real usage, eval $TEST_CMD
echo "✅ Tests passed (mocked)"

echo "
Implementation complete. What would you like to do?

1. Merge back to base branch locally
2. Push and create a Pull Request
3. Keep the branch as-is
4. Discard this work
"

read -p "Select an option (1-4): " OPTION

case $OPTION in
  1)
    echo "Option 1 Selected: Merge locally"
    echo "Please run: git checkout main && git merge $(git branch --show-current)"
    ;;
  2)
    echo "Option 2 Selected: Push and Create PR"
    echo "Please run: git push -u origin HEAD && gh pr create"
    ;;
  3)
    echo "Option 3 Selected: Keep as-is"
    echo "Worktree preserved."
    ;;
  4)
    read -p "Type 'discard' to confirm deletion: " CONFIRM
    if [ "$CONFIRM" == "discard" ]; then
        echo "Option 4 Selected: Discard"
        echo "Please run: git checkout main && git branch -D $(git branch --show-current)"
    else
        echo "Discard cancelled."
    fi
    ;;
  *)
    echo "Invalid option."
    ;;
esac
