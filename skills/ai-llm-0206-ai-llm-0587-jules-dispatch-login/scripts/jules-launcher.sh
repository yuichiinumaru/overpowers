#!/bin/bash
# Jules Launcher — Dispatches Jules remote sessions with redundancy and quota tracking
# Location: skills/jules-dispatch-login/scripts/jules-launcher.sh
#
# Usage:
#   ./jules-launcher.sh -t "009-rebuild-mcp-infrastructure"       # single task
#   ./jules-launcher.sh -t "009,010,011"                           # 3 tasks in parallel
#   ./jules-launcher.sh -n 5                                       # top 5 unchecked from tasklist
#   ./jules-launcher.sh -m "Analyze the docs/ directory"           # freeform prompt (no task file)
#   ./jules-launcher.sh -t "009" --no-redundancy                   # single session (no duplicate)
#
# Arguments:
#   -t  TASKS     Comma-separated task IDs or filenames from docs/tasks/ (without .md)
#   -n  COUNT     Auto-pick top N unchecked tasks from docs/tasklist.md
#   -m  MESSAGE   Freeform prompt message (no task file needed)
#   -p  PROMPT    Prompt template name from .agents/prompts/ (optional, appended before task)
#   --no-redundancy   Launch only 1 session per task (default: 2 for safety)
#
# CRITICAL: This script NEVER includes git/branch/commit instructions in prompts.
# See .agents/rules/jules-rules.md Section 1 (Anti-Git Golden Rule).

set -euo pipefail

# --- Configuration ---
OVERPOWERS_DIR="$(cd "$(dirname "$0")/../../.." && pwd)"
REPO_OWNER="yuichiinumaru"
TASKS_DIR="docs/tasks"
TASKLIST="docs/tasklist.md"
PROMPT_DIR=".agents/prompts"
REPORTS_DIR=".agents/reports"
LOG_DIR="/tmp/jules-dispatch"
REDUNDANCY=2  # Sessions per task (default: 2 for safety)
MAX_TASKS_PER_BATCH=7  # 7 tasks × 2 sessions = 14 (under 15 limit)

# --- Parse arguments ---
TASKS=""
COUNT=0
MESSAGE=""
PROMPT=""

while [[ $# -gt 0 ]]; do
  case $1 in
    -t) TASKS="$2"; shift 2 ;;
    -n) COUNT="$2"; shift 2 ;;
    -m) MESSAGE="$2"; shift 2 ;;
    -p) PROMPT="$2"; shift 2 ;;
    --no-redundancy) REDUNDANCY=1; shift ;;
    -h|--help)
      head -17 "$0" | tail -15
      exit 0
      ;;
    *) echo "❌ Unknown flag: $1"; exit 1 ;;
  esac
done

# --- Detect repo name from git remote ---
cd "$OVERPOWERS_DIR"
REPO_NAME=$(basename "$(git remote get-url origin 2>/dev/null | sed 's/\.git$//')" 2>/dev/null || basename "$OVERPOWERS_DIR")
REPO_FULL="$REPO_OWNER/$REPO_NAME"

# --- Validate ---
if [ -z "$TASKS" ] && [ "$COUNT" -eq 0 ] && [ -z "$MESSAGE" ]; then
  echo "❌ Provide at least one of: -t (tasks), -n (count), or -m (message)"
  echo "   Run with -h for help."
  exit 1
fi

# --- Build task array ---
TASK_ARRAY=()

if [ -n "$TASKS" ]; then
  IFS=',' read -ra TASK_ARRAY <<< "$TASKS"
elif [ "$COUNT" -gt 0 ]; then
  mapfile -t TASK_ARRAY < <(
    grep -E '^\- \[ \]' "$TASKLIST" |
    grep -oP '\[([^\]]+)\]\(tasks/\K[^)]+' |
    sed 's/\.md$//' |
    head -n "$COUNT"
  )
  if [ ${#TASK_ARRAY[@]} -eq 0 ]; then
    echo "⚠️  No open tasks found in $TASKLIST."
    exit 1
  fi
fi

# --- Guard: max tasks per batch ---
if [ ${#TASK_ARRAY[@]} -gt "$MAX_TASKS_PER_BATCH" ]; then
  echo "⚠️  ${#TASK_ARRAY[@]} tasks exceeds limit of $MAX_TASKS_PER_BATCH per batch."
  echo "   With redundancy=$REDUNDANCY, that's $((${#TASK_ARRAY[@]} * REDUNDANCY)) sessions (limit: 15)."
  echo "   Split into batches or use --no-redundancy."
  exit 1
fi

# --- Prepare ---
mkdir -p "$LOG_DIR" "$REPORTS_DIR"
TOTAL_SESSIONS=$((${#TASK_ARRAY[@]} * REDUNDANCY))

echo "🚀 Jules Launcher"
echo "   Repo:        $REPO_FULL"
echo "   Tasks:       ${TASK_ARRAY[*]:-"(freeform prompt)"}"
echo "   Redundancy:  ${REDUNDANCY}x per task"
echo "   Sessions:    $TOTAL_SESSIONS total"
echo ""

# --- Freeform prompt mode ---
if [ -n "$MESSAGE" ] && [ ${#TASK_ARRAY[@]} -eq 0 ]; then
  echo "📡 Launching freeform session..."
  SESSION_ID=$(jules remote new --repo "$REPO_FULL" --parallel "$REDUNDANCY" --session "$MESSAGE" 2>&1 | tee "$LOG_DIR/freeform-$(date +%s).log" | grep -oP '\d{10,}' | head -1 || true)
  echo "   ✅ Launched. Session ID: ${SESSION_ID:-"(check log)"}"
  echo "   Log: $LOG_DIR/freeform-*.log"
  exit 0
fi

# --- Task dispatch loop ---
LAUNCHED=0
SESSION_IDS=()

for TASK in "${TASK_ARRAY[@]}"; do
  # Normalize task name
  TASK_CLEAN=$(echo "$TASK" | sed 's|^docs/tasks/||' | sed 's/\.md$//')
  TASK_FILE="$TASKS_DIR/$TASK_CLEAN.md"

  if [ ! -f "$TASK_FILE" ]; then
    echo "⚠️  Task file not found: $TASK_FILE — skipping."
    continue
  fi

  # Read task content
  TASK_CONTENT=$(cat "$TASK_FILE")

  # Build prompt: template (if any) + task content
  # CRITICAL: NO git/branch/commit instructions. The platform handles that.
  FINAL_PROMPT=""

  if [ -n "$PROMPT" ] && [ -f "$PROMPT_DIR/$PROMPT.md" ]; then
    FINAL_PROMPT="$(cat "$PROMPT_DIR/$PROMPT.md")

"
  fi

  FINAL_PROMPT="${FINAL_PROMPT}${TASK_CONTENT}

## Important Rules
1. Save your progress report ONLY in '.agents/reports/${TASK_CLEAN}.md'. NEVER use dates in filenames.
2. NEVER modify or check off tasks in 'docs/tasklist.md'. Only mark checkboxes inside YOUR task file '${TASK_FILE}'.
3. Do NOT simplify, summarize, or delete unique details when deduplicating or refactoring. Merge ALL information."

  echo "📡 Dispatching: $TASK_CLEAN (${REDUNDANCY}x sessions)..."

  LOG_FILE="$LOG_DIR/${TASK_CLEAN}-$(date +%s).log"
  nohup jules remote new \
    --repo "$REPO_FULL" \
    --parallel "$REDUNDANCY" \
    --session "$FINAL_PROMPT" \
    > "$LOG_FILE" 2>&1 &

  LAUNCHED=$((LAUNCHED + 1))

  # Record session for fallback recovery
  echo "task=$TASK_CLEAN log=$LOG_FILE time=$(date -Iseconds)" >> "$LOG_DIR/dispatch-manifest.log"

  # Rate limit protection
  sleep 2
done

echo ""
echo "✅ Dispatched $LAUNCHED task(s) → $((LAUNCHED * REDUNDANCY)) session(s)"
echo "   Logs: $LOG_DIR/"
echo "   Manifest: $LOG_DIR/dispatch-manifest.log"
echo ""
echo "📋 Next steps:"
echo "   Monitor:  jules remote list --session"
echo "   Pull:     jules remote pull --session <ID> --apply"
echo "   Recover:  jj commit -m 'backup: pre-jules-pull' && jules remote pull --session <ID> --apply"
