#!/bin/bash
# Generates a boilerplate multi-cloud architecture document
output_file=$1

if [ -z "$output_file" ]; then
    echo "Usage: $0 <output_file.md>"
    return 1 2>/dev/null || true
fi

cat << 'TPL' > "$output_file"
# Multi-Cloud Architecture Design

## Executive Summary
...

## Provider Selection
| Service Component | Cloud Provider | Justification |
|-------------------|----------------|---------------|
| Compute           | AWS/Azure/GCP  |               |
| Storage           | AWS/Azure/GCP  |               |
| Identity          | AWS/Azure/GCP  |               |

## Network & Connectivity
...

## Security & Governance
...
TPL
echo "Generated multi-cloud architecture document at $output_file"
