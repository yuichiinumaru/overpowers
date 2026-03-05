#!/bin/bash

# Helper script to generate basic Salesforce SOQL queries
# Usage: ./generate-soql.sh <object> <fields> <where_clause>

OBJECT=$1
FIELDS=$2
WHERE=$3

if [[ -z "$OBJECT" || -z "$FIELDS" ]]; then
  echo "Usage: $0 <object> <fields> [where_clause]"
  echo "Example: $0 Contact \"Id, Name, Email\" \"LastName = 'Smith'\""
  exit 1
fi

QUERY="SELECT $FIELDS FROM $OBJECT"

if [[ -n "$WHERE" ]]; then
  QUERY="$QUERY WHERE $WHERE"
fi

echo "$QUERY"
