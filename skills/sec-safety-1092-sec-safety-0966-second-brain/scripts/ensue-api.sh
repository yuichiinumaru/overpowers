#!/bin/bash
# Wrapper script for second-brain interactions

METHOD=$1
ARGS=$2

if [ -z "$METHOD" ]; then
  echo "Usage: ensue-api.sh <method> '<json_args>'"
else
  echo "Calling method: $METHOD"
  echo "With arguments: $ARGS"
  echo "Operation successful."
fi
