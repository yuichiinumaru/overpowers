#!/usr/bin/env bash
# Helper script to prepare the payload for requesting a code review.
# This prints out the template with the correct base and head SHAs.

if [ "$#" -lt 1 ]; then
  echo "Usage: $0 <task-description> [base-sha]"
  echo "Example: $0 'Added verifyIndex() and repairIndex()' HEAD~1"
else
  DESCRIPTION="$1"
  BASE_REF="${2:-HEAD~1}"

  BASE_SHA=$(git rev-parse "$BASE_REF" 2>/dev/null || echo "UNKNOWN_BASE")
  HEAD_SHA=$(git rev-parse HEAD 2>/dev/null || echo "UNKNOWN_HEAD")

  cat << TEMPLATE
Please dispatch the Overpowers:code-reviewer subagent with the following details:

WHAT_WAS_IMPLEMENTED: ${DESCRIPTION}
PLAN_OR_REQUIREMENTS: Please refer to the current task plan/requirements
BASE_SHA: ${BASE_SHA}
HEAD_SHA: ${HEAD_SHA}
DESCRIPTION: ${DESCRIPTION}
TEMPLATE
fi
