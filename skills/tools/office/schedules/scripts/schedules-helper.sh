#!/bin/bash
# Helper script to wrap Windmill schedules CLI commands

if [ "$1" == "push" ]; then
    echo "Pushing schedules to Windmill..."
    wmill sync push
elif [ "$1" == "pull" ]; then
    echo "Pulling schedules from Windmill..."
    wmill sync pull
elif [ "$1" == "list" ]; then
    echo "Listing schedules..."
    wmill schedule
else
    echo "Usage: $0 [push|pull|list]"
    echo "  push : Push schedules to Windmill"
    echo "  pull : Pull schedules from Windmill"
    echo "  list : List schedules"
    exit 1
fi
