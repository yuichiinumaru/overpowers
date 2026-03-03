#!/bin/bash

# PRD Initializer Script
# This script scaffolds a new PRD file in the tasks/ directory.

FEATURE_NAME=$1

if [ -z "$FEATURE_NAME" ]; then
    echo "Usage: ./init_prd.sh <feature-name>"
    exit 1
fi

# Convert to kebab-case
FILENAME="prd-$(echo $FEATURE_NAME | tr '[:upper:]' '[:lower:]' | tr ' ' '-').md"
TARGET_DIR="tasks"
TARGET_PATH="${TARGET_DIR}/${FILENAME}"

# Ensure directory exists
mkdir -p "$TARGET_DIR"

if [ -f "$TARGET_PATH" ]; then
    echo "Error: PRD file already exists at $TARGET_PATH"
    exit 1
fi

# Create from template
cat <<EOF > "$TARGET_PATH"
# PRD: ${FEATURE_NAME}

## Introduction

[Brief description of the feature and the problem it solves.]

## Goals

- [Goal 1]
- [Goal 2]

## User Stories

### US-001: [Title]
**Description:** As a [user], I want [feature] so that [benefit].

**Acceptance Criteria:**
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] Typecheck/lint passes
- [ ] **[UI stories only]** Verify in browser using dev-browser skill

## Functional Requirements

- FR-1: [Requirement 1]
- FR-2: [Requirement 2]

## Non-Goals

- [Out of scope item 1]
- [Out of scope item 2]

## Technical Considerations

- [Consideration 1]
- [Consideration 2]

## Success Metrics

- [Metric 1]
- [Metric 2]

## Open Questions

- [Question 1]
- [Question 2]
EOF

echo "Scaffolded new PRD at: $TARGET_PATH"
