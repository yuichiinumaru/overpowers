#!/bin/bash

# Script to automate GitHub issue creation with smart templates.
# Usage: ./issue-workflow.sh {bug|integration} <title> <description>

TYPE=$1
TITLE=$2
DESC=$3

if [[ -z "$TYPE" || -z "$TITLE" || -z "$DESC" ]]; then
    echo "Usage: $0 {bug|integration} <title> <description>"
    exit 1
fi

case $TYPE in
    bug)
        BODY="## 🐛 Bug Report

### Problem Description
$DESC

### Expected Behavior
[What should happen]

### Actual Behavior  
[What actually happens]

### Reproduction Steps
1. [Step 1]
2. [Step 2]

### INVESTIGATION PLAN
- [ ] Root cause analysis
- [ ] Fix implementation
- [ ] Testing and validation

---
🤖 Generated with Claude Code"
        LABELS="bug,investigation"
        ;;
    integration)
        BODY="## 🔄 Integration Task

### Overview
$DESC

### Objectives
- [ ] Component integration
- [ ] Validation  
- [ ] Documentation updates

### Swarm Coordination
- **Coordinator**: Overall progress tracking
- **Analyst**: Technical validation

---
🤖 Generated with Claude Code"
        LABELS="integration,task"
        ;;
    *)
        echo "Invalid type. Use 'bug' or 'integration'."
        exit 1
        ;;
esac

echo "Creating GitHub issue..."
gh issue create --title "$TITLE" --body "$BODY" --label "$LABELS"
