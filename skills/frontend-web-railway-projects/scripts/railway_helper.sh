#!/usr/bin/env bash
# Shortcuts for Railway CLI commands

echo "--- Railway Project Helper ---"
echo "1. List projects (JSON summary)"
echo "2. Show current status"
echo "3. Link to a project"
echo "4. Whoami (Workspaces)"

read -p "Select [1-4]: " choice

case $choice in
  1) cmd="railway list --json | jq '.[] | {id, name}'" ;;
  2) cmd="railway status --json" ;;
  3) read -p "Project ID/Name: " p; cmd="railway link -p $p" ;;
  4) cmd="railway whoami --json" ;;
  *) echo "Invalid choice"; exit 1 ;;
esac

echo "Executing: $cmd"
eval $cmd
