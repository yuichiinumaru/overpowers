#!/bin/bash

# Tool to create a GitHub issue with a standardized template for swarm coordination

if [ -z "$1" ] || [ -z "$2" ]; then
  echo "Usage: issue_template_creator.sh <type> <title> [extra_body]"
  echo "Types: integration, bug, feature"
  exit 1
fi

TYPE=$1
TITLE=$2
EXTRA_BODY=$3

case $TYPE in
  integration)
    BODY="## 🔄 Integration Task

### Overview
$TITLE

### Objectives
- [ ] Component integration
- [ ] Validation
- [ ] Testing and verification
- [ ] Documentation updates

### Swarm Coordination
- **Coordinator**: Overall progress tracking
- **Analyst**: Technical validation
- **Tester**: Quality assurance
- **Documenter**: Documentation updates"
    LABELS="integration,swarm-ready"
    ;;
  bug)
    BODY="## 🐛 Bug Report

### Problem Description
$TITLE

### Investigation Plan
- [ ] Root cause analysis
- [ ] Fix implementation
- [ ] Testing and validation

### Swarm Assignment
- **Debugger**: Issue investigation
- **Coder**: Fix implementation
- **Tester**: Validation and testing"
    LABELS="bug,swarm-ready"
    ;;
  feature)
    BODY="## ✨ Feature Request

### Feature Description
$TITLE

### Acceptance Criteria
- [ ] Criterion 1
- [ ] Criterion 2

### Swarm Coordination
- **Architect**: Design and planning
- **Coder**: Implementation
- **Tester**: Quality assurance"
    LABELS="enhancement,swarm-ready"
    ;;
  *)
    echo "Unknown type: $TYPE"
    exit 1
    ;;
esac

if [ -n "$EXTRA_BODY" ]; then
  BODY="$BODY

$EXTRA_BODY"
fi

echo "🚀 Creating $TYPE issue: $TITLE"
gh issue create --title "$TITLE" --body "$BODY" --label "$LABELS"
