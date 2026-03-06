#!/bin/bash

# Automation for creating a YAML handoff
# Usage: ./handoff.sh <description> <outcome>

set -e

DESC=$1
OUTCOME=$2 # SUCCEEDED, PARTIAL_PLUS, PARTIAL_MINUS, FAILED

if [ -z "$DESC" ] || [ -z "$OUTCOME" ]; then
    echo "Usage: ./handoff.sh <kebab-description> <OUTCOME>"
    exit 1
fi

DATE=$(date +%Y-%m-%d)
TIME=$(date +%H-%M)
SESSION_NAME=$(ls -td thoughts/shared/handoffs/*/ 2>/dev/null | head -1 | xargs basename || echo "general")
FILENAME="${DATE}_${TIME}_${DESC}.yaml"
FILEPATH="thoughts/shared/handoffs/${SESSION_NAME}/${FILENAME}"

mkdir -p "thoughts/shared/handoffs/${SESSION_NAME}"

cat <<EOF > "$FILEPATH"
---
session: ${SESSION_NAME}
date: ${DATE}
status: complete
outcome: ${OUTCOME}
---

goal: [Accomplishment]
now: [Next step]
test: [Verification command]

done_this_session:
  - task: [Task]
    files: []

next:
  - [Next Step 1]

files:
  created: []
  modified: []
EOF

echo "Handoff template created at $FILEPATH"
echo "Next: Fill in the details and run indexing script."
