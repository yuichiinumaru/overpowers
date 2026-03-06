#!/bin/bash
PROJECT_ID=$1
if [ -z "$PROJECT_ID" ]; then
  echo "Usage: ./project-fields.sh <PROJECT_ID>"
  exit 1
fi
gh project field-list "$PROJECT_ID" --owner @me --format json | jq -r '.fields[] | "\(.name) (\(.dataType))"'
