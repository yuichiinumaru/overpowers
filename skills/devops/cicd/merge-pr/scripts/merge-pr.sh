#!/bin/bash
set -eo pipefail

if [ -z "$1" ]; then
    echo "Usage: ./merge-pr.sh <PR_NUMBER_OR_URL>"
    exit 1
fi

PR="$1"
echo "Merging PR: $PR"

if [ -d "$HOME/dev/openclaw" ]; then
    cd "$HOME/dev/openclaw"
    echo "Using directory $HOME/dev/openclaw"
else
    echo "Using current directory $(pwd) instead of ~/dev/openclaw"
fi

# Sanity: confirm you are in the repo
git rev-parse --show-toplevel >/dev/null || {
    echo "Fatal: not a git repository. Are you in the right directory?"
    exit 1
}

WORKTREE_DIR=".worktrees/pr-${PR}"
echo "Using worktree: $WORKTREE_DIR"

if [ ! -d "$WORKTREE_DIR" ]; then
    echo "Error: Worktree $WORKTREE_DIR not found. Run /preparepr first."
    exit 1
fi

cd "$WORKTREE_DIR" || exit 1

# Load Local Artifacts
if [ -f .local/review.md ]; then
  echo "Found .local/review.md"
  sed -n '1,120p' .local/review.md
else
  echo "Missing .local/review.md. Stop and run /reviewpr, then /preparepr."
  exit 1
fi

if [ -f .local/prep.md ]; then
  echo "Found .local/prep.md"
  sed -n '1,120p' .local/prep.md
else
  echo "Missing .local/prep.md. Stop and run /preparepr first."
  exit 1
fi

# 1. Identify PR meta
gh pr view "$PR" --json number,title,state,isDraft,author,headRefName,baseRefName,headRepository,body --jq '{number,title,state,isDraft,author:.author.login,head:.headRefName,base:.baseRefName,headRepo:.headRepository.nameWithOwner,body}'
contrib=$(gh pr view "$PR" --json author --jq .author.login)
head=$(gh pr view "$PR" --json headRefName --jq .headRefName)
head_repo_url=$(gh pr view "$PR" --json headRepository --jq .headRepository.url)

# 2. Run sanity checks
gh pr checks "$PR"

git fetch origin main
git fetch origin "pull/${PR}/head:pr-${PR}"
git merge-base --is-ancestor origin/main "pr-${PR}" || echo "Warning: PR branch is behind main, run /preparepr"

# 3. Merge PR and delete branch
check_status=$(gh pr checks "$PR" 2>&1 || true)
if echo "$check_status" | grep -q "pending\|queued"; then
  echo "Checks still running, using --auto to queue merge"
  gh pr merge "$PR" --squash --delete-branch --auto
  echo "Merge queued. Monitor with: gh pr checks $PR --watch"
else
  gh pr merge "$PR" --squash --delete-branch
fi

# 4. Get merge SHA
merge_sha=$(gh pr view "$PR" --json mergeCommit --jq '.mergeCommit.oid')
echo "merge_sha=$merge_sha"

# 5. Optional comment
gh pr comment "$PR" -F - <<MSG
Merged via squash.

- Merge commit: $merge_sha

Thanks @$contrib!
MSG

# 6. Verify PR state is MERGED
state=$(gh pr view "$PR" --json state --jq .state)
echo "PR state: $state"

# 7. Clean up worktree only on success
if [ "$state" = "MERGED" ]; then
  cd - >/dev/null
  git worktree remove "$WORKTREE_DIR" --force
  git branch -D "temp/pr-${PR}" 2>/dev/null || true
  git branch -D "pr-${PR}" 2>/dev/null || true
fi
