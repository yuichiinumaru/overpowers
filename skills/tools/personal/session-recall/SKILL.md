---
name: session-recall
description: "Session Recall - A skill for extracting information, managing memories, and recalling conversations from OpenClaw's session history."
metadata:
  openclaw:
    category: "utility"
    tags: []
    version: "1.0.0"
---

# Session Rollback Skill

## Overview

The Session Rollback skill is used to extract information from OpenClaw's session history, manage memory, and roll back conversations.

## Features

### 1. Extract Key Information and Write to memory/YYYY-MM-DD.md

Extract key information from the session and save it to a memory file.

**Usage:**
- Call the `write` tool to write content to the `memory/YYYY-MM-DD.md` file.
- Date format: Current date, e.g., `memory/2026-03-05.md`.

**Content Extraction Suggestions:**
- Important decisions made during the conversation.
- Key information points.
- To-do items.
- Information learned about the user.

**Example:**
```markdown
# 2026-03-05 Memory

## Important Information
- The user wants to know how to roll back sessions.
- The user asked me to publish a Feishu document skill to ClawHub.

## To-do
- [ ] Create session rollback skill.

## Conversation Summary
Today the user asked questions about sessions...
```

### 2. Query Keyword Occurrences/Context in Sessions

**Tools:**
- Use the `sessions_list` tool to list all sessions.
- Use the `sessions_history` tool to get the history of a specific session.
- Use the `read` tool to directly read JSONL files.

**Methods:**

#### Method 1: Using sessions_list
```bash
# List all recent sessions
sessions_list
```

#### Method 2: Using sessions_history
```bash
# Get the history of a specific session
sessions_history --sessionKey "agent:lin_xiaoman:feishu:direct:ou_xxx"
```

#### Method 3: Directly Reading JSONL Files
```bash
# Read session file
# Path format: ~/.openclaw/agents/<agentId>/sessions/<sessionId>.jsonl

# Example: Find the keyword "takeout"
# Use the read tool to read the file, then analyze the content.
```

**Finding Keyword Context:**
1. Use `sessions_list` to get basic information about all sessions.
2. Determine the target session based on `sessionKey`.
3. Use `sessions_history` to get the complete history.
4. Search for the keyword in the content and record the context.

### 3. Roll Back a Session Segment and Add to Current Conversation

**Method 1: Using the sessions_history tool**

1. Find the `sessionKey` of the target session.
2. Use `sessions_history` to get the history.
3. Tell the model the content to be rolled back through conversation.

**Method 2: Directly Reading JSONL Files**

1. Determine the `sessionId` (can be obtained from `sessions.json` or `sessions_list`).
2. Read the JSONL file:
   ```
   ~/.openclaw/agents/lin_xiaoman/sessions/<sessionId>.jsonl
   ```
3. Extract the desired conversation snippets.
4. Provide the content to the user or add it to the current context.

**Important Notes:**
- Current session `sessionKey` format: `agent:lin_xiaoman:feishu:direct:ou_2545d3b430b99a135bdab87d5a09b68a`
- Current session `sessionId`: `3fefc0bb-b7e9-4736-b374-d1be9d12caec`
- JSONL file path: `~/.openclaw/agents/lin_xiaoman/sessions/3fefc0bb-b7e9-4736-b374-d1be9d12caec.jsonl`

## Session File Locations

- Index file: `~/.openclaw/agents/<agentId>/sessions/sessions.json`
- Conversation records: `~/.openclaw/agents/<agentId>/sessions/<sessionId>.jsonl`
- Reset records: `~/.openclaw/agents/<agentId>/sessions/<sessionId>.jsonl.reset.<timestamp>`
- Deleted records: `~/.openclaw/agents/<agentId>/sessions/<sessionId>.jsonl.deleted.<timestamp>`

## Usage Examples

### Example 1: Find conversations about "takeout" today

1. List all sessions:
   ```
   sessions_list
   ```

2. Get the history of the current Feishu session:
   ```
   sessions_history --sessionKey "agent:lin_xiaoman:feishu:direct:ou_2545d3b430b99a135bdab87d5a09b68a"
   ```

3. Analyze the content to find conversations about "takeout".

### Example 2: Save today's important conversations to memory

Write a summary of today's conversation to `memory/2026-03-05.md`.

### Example 3: Roll back a previous session

1. List all sessions: `sessions_list`
2. Find the `sessionKey` of the target session.
3. Use `sessions_history` to get the history.
4. Tell the user the desired snippets.

## Precautions

- After using `sessions_history`, inform the user about the found content in the reply.
- JSONL files can be read directly using the `read` tool.
- Reset session files have a suffix containing `.reset.`.
- Deleted session files have a suffix containing `.deleted.`.
