#!/bin/bash
LOCATION=$1
if [ -z "$LOCATION" ]; then
  LOCATION=""
fi
curl -s "wttr.in/${LOCATION}?format=3"
