#!/bin/bash
# PREVC Code Review Scaffolding

PR_NAME=${1:-"new_pr"}
FILENAME="code_review_${PR_NAME}.md"

cat <<EOF > "$FILENAME"
# Code Review: ${PR_NAME}

## 1. Plan (P) - Context & Goal
- Objective:
- Context Preserved? (Yes/No):
- Specifications:

## 2. Refinement (R) - Code Quality
- Maintainability:
- Performance:
- Style Consistency:

## 3. Evaluation (E) - Security & Best Practices
- Security Vulnerabilities:
- Best Practices:
- Trade-offs:

## 4. Verification (V) - Validation
- Testing Adequacy:
- Verification against Specs:

## 5. Completion (C) - Summary & Recommendation
- Conclusion:
- Action Items for Author:
EOF

echo "Scaffolded code review: $FILENAME"
