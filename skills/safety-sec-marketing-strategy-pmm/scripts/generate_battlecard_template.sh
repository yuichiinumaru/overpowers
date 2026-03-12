#!/bin/bash
# Generates a competitive battlecard template
output_file=$1

if [ -z "$output_file" ]; then
    echo "Usage: $0 <output_file.md>"
    return 1 2>/dev/null || true
fi

cat << 'TPL' > "$output_file"
# Competitive Battlecard: [Competitor Name]

## Overview
Brief description of the competitor.

## Strengths
-

## Weaknesses
-

## How We Win
-

## Key Features Comparison
| Feature | Us | Them |
|---|---|---|
| | | |

## Objection Handling
**Objection:** They are cheaper.
**Response:** ...
TPL
echo "Generated battlecard template at $output_file."
