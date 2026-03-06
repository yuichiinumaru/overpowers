#!/usr/bin/env bash

# Wrapper script for flight-search CLI as defined in SKILL.md
# It ensures fast-flights is installed and provides a handy interface.

if ! command -v flights-search &> /dev/null; then
    echo "flights-search command not found."
    echo "Attempting to install fast-flights..."
    pip install fast-flights
    if [ $? -ne 0 ]; then
        echo "Failed to install fast-flights. Please install it manually."
        exit 1
    fi
fi

if [ "$#" -lt 3 ]; then
    echo "Usage: ./search-flights.sh <origin> <destination> <date> [options]"
    echo "Example: ./search-flights.sh YYZ EWR 2026-02-06 --nonstop"
    exit 1
fi

echo "Running flights-search..."
flights-search "$@"
