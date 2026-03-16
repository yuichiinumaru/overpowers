#!/bin/bash
# Helper script to run React core tests
# Usage: ./run-test.sh [channel] <pattern> [args...]

CHANNEL=$1
PATTERN=$2

if [ -z "$CHANNEL" ]; then
  echo "Usage: $0 [channel] <pattern> [args...]"
  echo "Channels: source (default), experimental, stable, classic, www, www-false"
  exit 1
fi

# If second arg is empty, then the first arg is the pattern and channel is default
if [ -z "$PATTERN" ]; then
  PATTERN=$CHANNEL
  CHANNEL="source"
  shift 1
else
  shift 2
fi

case "$CHANNEL" in
  experimental)
    CMD="yarn test -r=experimental --silent --no-watchman"
    ;;
  stable)
    CMD="yarn test-stable --silent --no-watchman"
    ;;
  classic)
    CMD="yarn test-classic --silent --no-watchman"
    ;;
  www)
    CMD="yarn test-www --silent --no-watchman"
    ;;
  www-false)
    CMD="yarn test-www --variant=false --silent --no-watchman"
    ;;
  source|default)
    CMD="yarn test --silent --no-watchman"
    ;;
  *)
    # Assume first arg was pattern
    PATTERN=$CHANNEL
    CMD="yarn test --silent --no-watchman"
    ;;
esac

echo "Running: $CMD $PATTERN $@"
$CMD "$PATTERN" "$@"
