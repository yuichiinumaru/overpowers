#!/bin/bash
if [ -z "$1" ]; then
    echo "Usage: $0 <post_title>"
    exit 1
fi
SLUG=$(echo "$1" | tr '[:upper:]' '[:lower:]' | tr ' ' '-')
DATE=$(date +%Y-%m-%d)
FILENAME="${DATE}-${SLUG}.md"
echo "Scaffolding Technical Blog Post: $FILENAME"
cat << TEMPLATE > "$FILENAME"
---
title: "$1"
date: $DATE
author: [Author]
---

# $1

## Introduction
...

## Implementation Details
...

## Conclusion
...
TEMPLATE
echo "Created $FILENAME"
