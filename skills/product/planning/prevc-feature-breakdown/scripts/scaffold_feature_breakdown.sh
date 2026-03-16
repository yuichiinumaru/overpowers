#!/bin/bash
# PREVC Feature Breakdown Scaffolding

FEAT_NAME=${1:-"new_feature"}
FILENAME="feature_breakdown_${FEAT_NAME}.md"

cat <<EOF > "$FILENAME"
# Feature Breakdown: ${FEAT_NAME}

## 1. Plan (P)
- Requirements:
- Constraints:
- Architecture:

## 2. Refinement (R)
- Task Breakdown:
- Dependencies:
- Estimation:

## 3. Evaluation (E)
- Trade-offs:
- Risk Assessment:

## 4. Verification (V)
- Testing Strategy:
- Verification Steps:

## 5. Completion (C)
- Rollout Plan:
- Documentation:
EOF

echo "Scaffolded feature breakdown: $FILENAME"
