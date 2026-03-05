#!/bin/bash

# Postmortem Document Scaffolder

TYPE=${1:-"standard"}
TITLE=${2:-"Incident-Title"}
DATE=$(date +%Y-%m-%d)
FILENAME="postmortem-${DATE}-${TITLE}.md"

if [ "$TYPE" == "standard" ]; then
    cat <<EOF > "$FILENAME"
# Postmortem: ${TITLE}

**Date**: ${DATE}
**Authors**: @
**Status**: Draft
**Incident Severity**: SEV
**Incident Duration**: 

## Executive Summary

[Brief summary of what happened, root cause, and resolution]

**Impact**:
- 
- 

## Timeline (All times UTC)

| Time | Event |
|------|-------|
| | |

## Root Cause Analysis

### What Happened

### Why It Happened

1. **Proximate Cause**: 
2. **Contributing Factors**:
3. **5 Whys Analysis**:

## Detection

### What Worked
### What Didn't Work

## Response

### What Worked
### What Could Be Improved

## Impact

### Customer Impact
### Business Impact
### Technical Impact

## Lessons Learned

### What Went Well
### What Went Wrong
### Where We Got Lucky

## Action Items

| Priority | Action | Owner | Due Date | Ticket |
|----------|--------|-------|----------|--------|
| | | | | |

## Appendix
EOF
elif [ "$TYPE" == "quick" ]; then
    cat <<EOF > "$FILENAME"
# Quick Postmortem: ${TITLE}

**Date**: ${DATE} | **Duration**: | **Severity**: SEV3

## What Happened

## Timeline

## Root Cause

## Fix

## Lessons
EOF
else
    echo "Unknown type: $TYPE. Use 'standard' or 'quick'."
    exit 1
fi

echo "Created $FILENAME"
