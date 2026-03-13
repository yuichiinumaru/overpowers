#!/usr/bin/env bash
# Shortcuts for Linear MCP tools

echo "--- Linear MCP Helper ---"
echo "1. List my issues"
echo "2. Get issue details"
echo "3. List issue statuses"
echo "4. Search documentation"

read -p "Select [1-4]: " choice

case $choice in
  1) echo "Call: linear:list_my_issues()" ;;
  2) read -p "Issue ID: " id; echo "Call: linear:get_issue(issueId=\"$id\")" ;;
  3) echo "Call: linear:list_issue_statuses()" ;;
  4) read -p "Query: " q; echo "Call: linear:search_documentation(query=\"$q\")" ;;
  *) echo "Invalid choice"; exit 1 ;;
esac
