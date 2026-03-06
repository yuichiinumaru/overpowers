#!/bin/bash

# Generate a Parallel Feature Development Plan template.
# Usage: ./generate_parallel_plan.sh <feature_name>

FEATURE_NAME="$1"

if [ -z "$FEATURE_NAME" ]; then
  echo "Usage: $0 <feature_name>"
  exit 1
fi

FILE_NAME="parallel_plan_${FEATURE_NAME}.md"

cat <<EOF > "$FILE_NAME"
# Parallel Development Plan: ${FEATURE_NAME}

## 1. Feature Decomposition
- **Goal:**
- **Status:** Planning

## 2. Work Streams & Assignment
| Work Stream | Description | Assigned To | Ownership Strategy |
|:------------|:------------|:------------|:-------------------|
| Stream 1    |             | Agent A     | Directory/Layer/Module |
| Stream 2    |             | Agent B     | Directory/Layer/Module |
| Stream 3    |             | Agent C     | Directory/Layer/Module |

## 3. File Ownership Boundaries
### Agent A (Stream 1)
- \`src/path/to/dir1/\`
- \`src/path/to/file1.ts\`

### Agent B (Stream 2)
- \`src/path/to/dir2/\`
- \`src/path/to/file2.ts\`

## 4. Shared Files & Coordination
- **Shared File:** \`src/shared/contract.ts\`
- **Single Owner:** Agent A
- **Coordination Process:** Agent B and C send change requests to Agent A.

## 5. Integration Strategy
- [ ] **Vertical Slice:** Independent feature blocks (UI + API + Test)
- [ ] **Horizontal Layer:** Specialization by layer (All UI, All API, etc.)
- [ ] **Hybrid:** Combination approach

## 6. Branch Management
- **Main Feature Branch:** \`feature/${FEATURE_NAME}\`
- **Sub-branches (if multi-branch):**
  - \`feature/${FEATURE_NAME}-stream1\`
  - \`feature/${FEATURE_NAME}-stream2\`

## 7. Verification & Handoff
- [ ] All unit tests pass in isolation
- [ ] Integration tests pass after merge
- [ ] Code review completed for each stream
EOF

echo "Parallel development plan template generated: $FILE_NAME"
