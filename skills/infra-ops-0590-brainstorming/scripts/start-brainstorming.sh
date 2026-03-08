#!/bin/bash
# Brainstorming Session Setup
echo "Creating brainstorming workspace..."
mkdir -p brainstorming_sessions
DATE=$(date +%Y-%m-%d)
touch "brainstorming_sessions/session_$DATE.md"
echo "Session created at brainstorming_sessions/session_$DATE.md"
