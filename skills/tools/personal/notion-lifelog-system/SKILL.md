---
name: general-tool-notion-lifelog-system
description: "Automated life logging system integrated with Notion. Identifies dates in messages and records them to a Notion database with smart analysis."
tags: ["notion", "lifelog", "automation", "productivity", "personal"]
version: 1.0.0
---

# LifeLog Life Logging System

Automatically records the user's daily life into Notion, supporting intelligent date recognition and automatic summary analysis.

## Core Features

1. **Real-time Recording** - Automatically records user's life moments into Notion when shared.
2. **Intelligent Date Recognition** - Automatically recognizes dates like "yesterday," "the day before yesterday," etc., and records them to the corresponding date.
3. **Backfill Tagging** - Content not recorded on the same day will be tagged as "🔁 Backfill."
4. **Automatic Summarization** - Runs LLM analysis automatically at midnight every day to generate emotional state, main events, location, and people.

## Notion Database Requirements

Create a Notion Database that includes: Date (title), Original Text (rich_text), Emotional State, Main Events, Location, People.

## Script Description

### 1. lifelog-append.sh
Real-time recording script that accepts user message content. Supports date expressions such as: today, yesterday, the day before yesterday, specific dates.

### 2. lifelog-daily-summary-v5.sh
Fetches original text for a specified date for LLM analysis.

### 3. lifelog-update.sh
Writes LLM analysis results back to Notion.

## Workflow
1. User sends life log → Calls `lifelog-append.sh` → Writes to Notion
2. Scheduled task triggers → Calls `lifelog-daily-summary-v5.sh`
3. LLM analyzes original text → Calls `lifelog-update.sh` → Fills in analysis fields
