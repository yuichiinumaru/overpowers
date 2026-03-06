#!/bin/bash
# Generate TBP (To Be Published) document
echo "Generating TBP document skeleton..."
cat << 'DOC' > document_tbp.md
# Title
## Introduction
## Body
## Conclusion
DOC
echo "Skeleton created at document_tbp.md"
