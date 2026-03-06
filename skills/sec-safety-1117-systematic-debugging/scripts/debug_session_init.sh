#!/bin/bash
# debug_session_init.sh
# Initializes a new debugging session log.

DEBUG_LOG="DEBUG_LOG.md"

if [ -f "$DEBUG_LOG" ]; then
    echo "Existing $DEBUG_LOG found. Archiving to $DEBUG_LOG.bak"
    mv "$DEBUG_LOG" "$DEBUG_LOG.bak"
fi

cat <<EOF > "$DEBUG_LOG"
# Debugging Session: $(date)

## Phase 1: Root Cause Investigation
- **Error Message**: (Paste full error message here)
- **Reproduction Steps**: 
  1. 
- **Recent Changes**: (git diff summary)
- **Evidence Gathered**: (logs, traces)

## Phase 2: Pattern Analysis
- **Working Examples**: (Where does similar code work?)
- **Differences**: (Working vs. Broken)

## Phase 3: Hypothesis and Testing
- **Hypothesis**: "I think X is the root cause because Y"
- **Test Minimally**: (Smallest change to test)
- **Verification Result**: (Did it work?)

## Phase 4: Implementation
- **Failing Test Case**: (Path to reproduction script)
- **Fix Applied**: (Description of fix)
- **Final Verification**: (Evidence that it is fixed)

## Execution Limits
- Fix Attempts: 0/3
EOF

echo "Initialized $DEBUG_LOG. Follow the process in SKILL.md!"
