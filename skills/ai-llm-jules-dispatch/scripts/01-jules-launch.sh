#!/bin/bash
# Jules Launcher V2 — Dispatches Jules based on a JSON structural plan
# Usage: ./jules-launcher-v2.sh <tasklist_plan.json>

set -e

if [ -z "$1" ]; then
    echo "❌ Missing argument: path to JSON orchestration plan."
    echo "Usage: $0 path/to/plan.json"
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
echo "⚠️ INITIAL JULES LOGIN"
echo "=========================================================="
echo "Authenticating via 'npx jules login'..."
echo "Please interact with the browser tab to select your account."
npx jules login
echo "✅ Authentication successful!"

# Discover the absolute path of 01-prompt-helper.py based on this script's directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)"
PYTHON_EXEC="$SCRIPT_DIR/01-prompt-helper.py"

if [ ! -x "$PYTHON_EXEC" ]; then
    chmod +x "$PYTHON_EXEC"
fi

LENGTH=$(jq '.tasks | length' "$PLAN_FILE")
if [ "$LENGTH" -eq 0 ]; then
    echo "⚠️ No tasks found in $PLAN_FILE."
    exit 0
fi

LAUNCHED=0
TOTAL_ITEMS=0

for (( i=0; i<$LENGTH; i++ )); do
    TYPE=$(jq -r ".tasks[$i].task | type" "$PLAN_FILE")
    if [ "$TYPE" == "array" ]; then
        ARR_LEN=$(jq ".tasks[$i].task | length" "$PLAN_FILE")
        TOTAL_ITEMS=$((TOTAL_ITEMS + ARR_LEN))
    else
        TOTAL_ITEMS=$((TOTAL_ITEMS + 1))
    fi
done

for (( i=0; i<$LENGTH; i++ )); do
    PROMPT=$(jq -r ".tasks[$i].prompt // empty" "$PLAN_FILE")
    TYPE=$(jq -r ".tasks[$i].task | type" "$PLAN_FILE")
    
    if [ -z "$PROMPT" ]; then
        echo "⚠️ Skipping index $i - 'prompt' field missing."
        continue
    fi
    
    if [ "$TYPE" == "array" ]; then
        TASK_ARRAY_LEN=$(jq ".tasks[$i].task | length" "$PLAN_FILE")
        for (( j=0; j<$TASK_ARRAY_LEN; j++ )); do
            TASK=$(jq -r ".tasks[$i].task[$j]" "$PLAN_FILE")
            
            OPTS=("-p" "$PROMPT")
            if [ -n "$TASK" ]; then
                OPTS+=("-t" "$TASK")
            fi
            if [ -n "$REPO" ]; then
                OPTS+=("--repo" "$REPO")
            fi
            
            python3 "$PYTHON_EXEC" "${OPTS[@]}" || {
                EXIT_CODE=$?
                if [ $EXIT_CODE -eq 69 ]; then
                    echo "=========================================================="
                    echo "⚠️ JULES QUOTA LIMIT REACHED (~$LAUNCHED tasks dispatched)"
                    echo "=========================================================="
                    echo "Re-authenticating via 'npx jules login' to reset quota..."
                    echo "Please select a FRESH Google Account in the browser tab!"
                    npx jules login
                    echo "✅ Authentication successful! Retrying last task..."
                    python3 "$PYTHON_EXEC" "${OPTS[@]}" # Retry the failed one
                else
                    exit $EXIT_CODE
                fi
            }
            LAUNCHED=$((LAUNCHED + 1))
            sleep 2
        done
    else
        TASK=$(jq -r ".tasks[$i].task // empty" "$PLAN_FILE")
        OPTS=("-p" "$PROMPT")
        if [ -n "$TASK" ]; then
            OPTS+=("-t" "$TASK")
        fi
        if [ -n "$REPO" ]; then
            OPTS+=("--repo" "$REPO")
        fi
        
        python3 "$PYTHON_EXEC" "${OPTS[@]}" || {
            EXIT_CODE=$?
            if [ $EXIT_CODE -eq 69 ]; then
                echo "=========================================================="
                echo "⚠️ JULES QUOTA LIMIT REACHED (~$LAUNCHED tasks dispatched)"
                echo "=========================================================="
                echo "Re-authenticating via 'npx jules login' to reset quota..."
                echo "Please select a FRESH Google Account in the browser tab!"
                npx jules login
                echo "✅ Authentication successful! Retrying last task..."
                python3 "$PYTHON_EXEC" "${OPTS[@]}" # Retry the failed one
            else
                exit $EXIT_CODE
            fi
        }
        LAUNCHED=$((LAUNCHED + 1))
        sleep 2
    fi
done

echo "🎉 All $LAUNCHED tasks dispatched from plan!"
