#!/bin/bash

# Script to generate research queries for a company/person.
# Usage: ./research-queries.sh "Entity Name" [Context]

ENTITY=$1
CONTEXT=$2

if [ -z "$ENTITY" ]; then
  echo "Usage: $0 \"Entity Name\" [Context]"
  exit 1
fi

echo "Researching: $ENTITY $CONTEXT"
echo "--------------------------------"
echo "1. $ENTITY homepage about"
echo "2. $ENTITY recent news last 90 days"
echo "3. $ENTITY funding rounds investors"
echo "4. $ENTITY leadership team LinkedIn"
echo "5. $ENTITY open job roles careers"
echo "6. $ENTITY product offerings solutions"
echo "7. $ENTITY key customers case studies"
