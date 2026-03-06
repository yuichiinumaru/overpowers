#!/bin/bash
# Jira helper script - auto-detects and uses CLI or MCP backend

# Backend Detection
if command -v jira >/dev/null 2>&1; then
    BACKEND="CLI"
else
    # Check for MCP tools - this is a heuristic
    if [ -n "$MCP_ATLASSIAN_AVAILABLE" ]; then
        BACKEND="MCP"
    else
        BACKEND="NONE"
    fi
fi

echo "Detected Jira backend: $BACKEND"

case "$1" in
    view)
        if [ "$BACKEND" == "CLI" ]; then
            jira issue view "$2"
        elif [ "$BACKEND" == "MCP" ]; then
            echo "Use MCP tool: mcp__atlassian__getJiraIssue(issueKey='$2')"
        else
            echo "No backend available. Install jira-cli."
        fi
        ;;
    list)
        if [ "$BACKEND" == "CLI" ]; then
            jira issue list -a$(jira me)
        elif [ "$BACKEND" == "MCP" ]; then
            echo "Use MCP tool: mcp__atlassian__searchJiraIssuesUsingJql(jql='assignee = currentUser()')"
        else
            echo "No backend available."
        fi
        ;;
    create)
        if [ "$BACKEND" == "CLI" ]; then
            jira issue create -t"$2" -s"$3" -b"$4"
        elif [ "$BACKEND" == "MCP" ]; then
            echo "Use MCP tool: mcp__atlassian__createJiraIssue(projectKey='...', summary='$3', type='$2', description='$4')"
        else
            echo "No backend available."
        fi
        ;;
    *)
        echo "Usage: $0 {view|list|create} [args...]"
        exit 1
        ;;
esac
