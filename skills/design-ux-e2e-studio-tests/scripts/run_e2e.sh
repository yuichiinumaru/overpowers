#!/bin/bash

# Helper to run e2e studio tests
# Usage: ./run_e2e.sh [feature_name] [additional_args]

FEATURE=$1
shift
ARGS=$@

cd e2e/studio

if [ -z "$FEATURE" ]; then
  echo "Running all e2e tests..."
  pnpm run e2e $ARGS
else
  # Check if it's a file path or a grep pattern
  if [[ "$FEATURE" == *.spec.ts ]]; then
    echo "Running test file: $FEATURE"
    pnpm run e2e -- "features/$FEATURE" $ARGS
  else
    echo "Running tests matching: $FEATURE"
    pnpm run e2e -- --grep "$FEATURE" $ARGS
  fi
fi
