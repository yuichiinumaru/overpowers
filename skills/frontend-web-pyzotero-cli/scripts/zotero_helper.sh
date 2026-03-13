#!/usr/bin/env bash
# Shortcuts for pyzotero CLI commands

echo "--- Pyzotero CLI Helper ---"
echo "1. List collections"
echo "2. Search library"
echo "3. Search full-text (PDFs)"
echo "4. List item types"

read -p "Select [1-4]: " choice

case $choice in
  1) cmd="pyzotero listcollections" ;;
  2) read -p "Query: " q; cmd="pyzotero search -q \"$q\"" ;;
  3) read -p "Query: " q; cmd="pyzotero search -q \"$q\" --fulltext" ;;
  4) cmd="pyzotero itemtypes" ;;
  *) echo "Invalid choice"; exit 1 ;;
esac

echo "Executing: $cmd"
eval $cmd
