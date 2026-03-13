#!/usr/bin/env bash
# Shortcuts for common gog commands

echo "--- GOG CLI Helper ---"
echo "1. Search Gmail (last 7 days)"
echo "2. List Calendar events"
echo "3. Search Drive"
echo "4. Create Calendar Event"

read -p "Select [1-4]: " choice

case $choice in
  1) cmd="gog gmail search 'newer_than:7d' --max 10" ;;
  2) cmd="gog calendar events primary" ;;
  3) read -p "Query: " q; cmd="gog drive search \"$q\" --max 10" ;;
  4) read -p "Summary: " s; cmd="gog calendar create primary --summary \"$s\"" ;;
  *) echo "Invalid choice"; exit 1 ;;
esac

echo "Executing: $cmd"
eval $cmd
