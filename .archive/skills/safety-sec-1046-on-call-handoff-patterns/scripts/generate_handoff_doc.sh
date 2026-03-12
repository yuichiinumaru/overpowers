#!/bin/bash
# Generate an on-call handoff document
output_file=$1

if [ -z "$output_file" ]; then
    echo "Usage: $0 <output_file.md>"
    return 1 2>/dev/null || true
fi

cat << 'TPL' > "$output_file"
# On-Call Handoff

**Date:** $(date +%Y-%m-%d)
**Outgoing On-Call:**
**Incoming On-Call:**

## Shift Summary
-

## Ongoing Incidents
- None

## Pending Action Items
- [ ]

## Notes for Incoming On-Call
-
TPL
echo "Handoff document generated at $output_file"
