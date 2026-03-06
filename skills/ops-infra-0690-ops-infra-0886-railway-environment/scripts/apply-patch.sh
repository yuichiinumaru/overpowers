#!/bin/bash
# Helper script to construct and run the GraphQL mutation for Railway
ENV_ID="$1"
PATCH_JSON="$2"
COMMIT_MSG="$3"

if [ -z "$ENV_ID" ] || [ -z "$PATCH_JSON" ]; then
    echo "Usage: $0 <environment-id> <patch-json> [commit-message]"
else
    VARS=$(jq -n \
      --arg env "$ENV_ID" \
      --argjson patch "$PATCH_JSON" \
      --arg msg "${COMMIT_MSG:-Apply patch}" \
      '{environmentId: $env, patch: $patch, commitMessage: $msg}')

    SCRIPT_DIR="${CLAUDE_PLUGIN_ROOT:-.}/skills/lib/railway-api.sh"

    if [ -f "$SCRIPT_DIR" ]; then
        bash "$SCRIPT_DIR" \
          'mutation patchCommit($environmentId: String!, $patch: EnvironmentConfig, $commitMessage: String) {
            environmentPatchCommit(environmentId: $environmentId, patch: $patch, commitMessage: $commitMessage)
          }' \
          "$VARS"
    else
        echo "Railway API helper script not found at $SCRIPT_DIR"
        echo "Variables payload would be: $VARS"
    fi
fi
