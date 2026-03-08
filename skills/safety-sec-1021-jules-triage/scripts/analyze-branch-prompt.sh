#!/bin/bash
# Script to generate a prompt for analyzing a Jules branch

if [ -z "$1" ]; then
    echo "Usage: $0 <branch-name>"
    exit 1
fi

BRANCH=$1
WORKTREE_PATH="branches/$BRANCH"

if [ ! -d "$WORKTREE_PATH" ]; then
    echo "Warning: Worktree $WORKTREE_PATH does not exist."
fi

cat <<EOF
# Analyze Jules Branch: ${BRANCH}

## Your Task
Analyze the work in \`${WORKTREE_PATH}/\` and produce an assessment.

## Analysis Checklist

### 1. Code Quality (1-10)
- [ ] Code compiles/runs
- [ ] Follows project conventions
- [ ] Has adequate comments
- [ ] Error handling present
- [ ] No obvious bugs

### 2. Value Assessment
- [ ] Solves intended problem
- [ ] Novel approach (vs existing code)
- [ ] Reusable components
- [ ] Good documentation

### 3. Integration Complexity
- [ ] Self-contained (easy)
- [ ] Minor adaptations needed (medium)
- [ ] Major refactoring required (hard)
- [ ] Conflicts with existing code (very hard)

### 4. Conflict Detection
Check for conflicts with:
- Existing file paths
- Naming conventions
- Architecture patterns
- Dependencies

## Output Format

Produce \`.jules/triage/${BRANCH}.md\`:

\`\`\`markdown
# Triage: ${BRANCH}

## Recommendation
[✅ MERGE | 🔧 ADAPT | 📝 DOCS-ONLY | ❌ DISCARD]

## Scores
- Code Quality: X/10
- Value: X/10  
- Integration Ease: X/10

## Summary
[2-3 sentence summary of what this branch does]

## Valuable Components
1. [Component 1] - [why valuable]
2. [Component 2] - [why valuable]

## Integration Notes
[Specific notes on how to integrate, conflicts to resolve, adaptations needed]

## Conflicts Detected
- [File/pattern conflict 1]
- [File/pattern conflict 2]

## Action Items
- [ ] [Specific action 1]
- [ ] [Specific action 2]
\`\`\`
EOF
