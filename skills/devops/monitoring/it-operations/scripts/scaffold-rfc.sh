#!/bin/bash
# Script to scaffold a Request for Change (RFC)

if [ -z "$1" ]; then
    echo "Usage: $0 <change-name>"
    exit 1
fi

NAME=$1
DATE=$(date +%Y-%m-%d)
OUTPUT_FILE="rfc-${DATE}-${NAME}.md"

cat <<EOF > "$OUTPUT_FILE"
# Request for Change: ${NAME}

## Status
PROPOSED

## Metadata
- **Author**: 
- **Date**: ${DATE}
- **Proposed Window**: 
- **Systems Affected**: 

## Justification
Why is this change necessary? What problem does it solve?

## Scope of Work
Detailed description of the change.

## Risk Assessment
- **Impact (1-5)**: 
- **Likelihood of Issues (1-5)**: 
- **Complexity (1-5)**: 
- **Risk Mitigation**: 

## Step-by-Step Procedure
1. 
2. 

## Rollback Plan
How to revert the change if it fails.

## Verification Plan
How to confirm the change was successful.

## Approval
- **CAB Review Date**: 
- **Approver**: 

EOF

echo "Scaffolded RFC to $OUTPUT_FILE"
