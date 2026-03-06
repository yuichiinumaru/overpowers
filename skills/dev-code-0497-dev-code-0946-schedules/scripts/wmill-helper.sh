#!/usr/bin/env bash

# Helper script for Windmill schedules CLI commands

if [ $# -eq 0 ]; then
  echo "Usage: $0 <command> [args...]"
  echo "Commands:"
  echo "  sync push     Push schedules to Windmill"
  echo "  sync pull     Pull schedules from Windmill"
  echo "  schedule      List schedules"
  exit 1
fi

wmill "$@"
