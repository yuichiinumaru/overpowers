#!/bin/bash
# Jules Launcher V2 — Dispatches Jules based on a JSON structural plan
# Usage: ./jules-launcher-v2.sh [-p REPLICAS] <tasklist_plan.json>

set -e

PARALLEL=1
while getopts "p:" opt; do
  case $opt in
    p) PARALLEL="$OPTARG" ;;
    \?) echo "Usage: $0 [-p replicas] path/to/plan.json"; exit 1 ;;
  esac
done
shift $((OPTIND-1))

if [ -z "$1" ]; then
    echo "❌ Missing argument: path to JSON orchestration plan."
    echo "Usage: $0 [-p replicas] path/to/plan.json"
    echo "Schema expects:"
    echo '{ "repo": "optional/repo", "tasks": [ { "prompt": "prompt.json", "task": "task.md" } ] }'
    exit 1
fi

PLAN_FILE="$1"
if [ ! -f "$PLAN_FILE" ]; then
    echo "❌ File not found: $PLAN_FILE"
    exit 1
fi

# Detect repository
REPO=$(jq -r '.repo // ""' "$PLAN_FILE" 2>/dev/null)

echo "=========================================================="
echo "⚠️ JULES LOGIN REQUIRED"
echo "=========================================================="
echo "Due to multiple account management, please ensure you are"
echo "logged into the correct account."
echo ""
echo "Launching jules login..."
jules login

# Discover the absolute path of prompt-tasker.py based on this script's directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)"
PYTHON_EXEC="$SCRIPT_DIR/prompt-tasker.py"

if [ ! -x "$PYTHON_EXEC" ]; then
    chmod +x "$PYTHON_EXEC"
fi

# Create a flat list of tasks to support both formats securely
# Grouped format: { "prompt": "p", "tasks": ["t1", "t2"] }
# Flat format: { "prompt": "p", "task": "t1" }
mapfile -t TASKS_LIST < <(
  jq -r '.tasks[] | if has("tasks") then .prompt as $p | .tasks[] | "\($p)\t\(.)" else "\(.prompt)\t\(.task)" end' "$PLAN_FILE"
)

LENGTH=${#TASKS_LIST[@]}
if [ "$LENGTH" -eq 0 ]; then
    echo "⚠️ No tasks found in $PLAN_FILE."
    exit 0
fi

LAUNCHED=0
for (( i=0; i<$LENGTH; i++ )); do
    IFS=$'\t' read -r PROMPT TASK <<< "${TASKS_LIST[$i]}"
    
    if [ -z "$PROMPT" ]; then
        echo "⚠️ Skipping index $i - 'prompt' field missing."
        continue
    fi
    
    # Build arguments securely
    OPTS=("-p" "$PROMPT")
    if [ -n "$TASK" ]; then
        OPTS+=("-t" "$TASK")
    fi
    if [ -n "$REPO" ]; then
        OPTS+=("--repo" "$REPO")
    fi
    
    # We enforce --redundancy 1 on the python script so we control it natively here.
    OPTS+=("--redundancy" "1")
    
    for (( r=0; r<$PARALLEL; r++ )); do
        # Execute the python dispatcher
        python3 "$PYTHON_EXEC" "${OPTS[@]}"
        
        LAUNCHED=$((LAUNCHED + 1))
        
        # The magical rotation check (now checks against 14 directly, max jobs per account)
        # Using 14 as the hard limit before requiring a new account.
        if [ $((LAUNCHED % 14)) -eq 0 ] && [ "$LAUNCHED" -lt $((LENGTH * PARALLEL)) ]; then
            echo "=========================================================="
            echo "⚠️ REACHED 14 JOBS DISPATCHED."
            echo "⚠️ JULES QUOTA LIMIT INCURSION ALERT."
            echo "=========================================================="
            echo "Please authenticate with a FRESH Google Account."
            jules login
        fi
        sleep 2
    done
done

echo "🎉 All $LAUNCHED tasks dispatched from plan! ($LENGTH tasks x $PARALLEL replicas)"
