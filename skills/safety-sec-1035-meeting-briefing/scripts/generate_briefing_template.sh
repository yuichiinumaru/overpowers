#!/bin/bash
# Generate a meeting briefing template
output_file=$1

if [ -z "$output_file" ]; then
    echo "Usage: $0 <output_file.md>"
    return 1 2>/dev/null || true
fi

cat << 'TPL' > "$output_file"
# Meeting Briefing

**Date:** YYYY-MM-DD
**Attendees:**
-

## Background
...

## Key Objectives
1.

## Action Items
- [ ]
TPL
echo "Briefing template generated at $output_file."
