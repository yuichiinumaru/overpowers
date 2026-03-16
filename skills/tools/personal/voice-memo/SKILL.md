---
name: voice-memo
description: "Manage voice memos — add transcriptions, search, and list recent memos with summaries and action items."
metadata:
  openclaw:
    category: "voice"
    tags: ['voice', 'audio', 'transcription']
    version: "1.0.0"
---

# voice-memo

Voice memo management. Store transcription text, summarize/extract keywords, and search.

## Script

```bash
# Add memo (summary, topics, and decisions will be analyzed and provided by the agent)
node scripts/voice_memo.js add \
  --content="Discussed the product roadmap in today's meeting" \
  --summary="Discussed Q2 roadmap. Decided to prioritize mobile." \
  --topics="roadmap,Q2,mobile" \
  --decisions="Prioritize mobile app for Q2|Bi-weekly design reviews" \
  --action_items="Create UI mockups (next Friday)|Create spike tickets"

# Keyword search
node scripts/voice_memo.js search --query="roadmap" --limit=10

# List recent memos
node scripts/voice_memo.js list --days=7 --limit=10

# Number of memos for a specific date
node scripts/voice_memo.js count --date=2026-02-24
```

## Summary Workflow

When the user sends voice memo text (transcription):

1. Analyze the text and extract the following:
   - summary: A 2-3 sentence Japanese summary
   - topics: Up to 5 related keywords (comma-separated)
   - decisions: Decisions made (pipe-separated, empty if none)
   - action_items: Action items "Who does what by when" (pipe-separated, empty if none)
2. Record using `voice_memo.js add`
3. Reply to the user with the results

## Reply Format

```
✅ Voice memo saved

📝 *Summary*
Discussed Q2 roadmap. Decided to prioritize mobile.

✅ *Decisions*
• Prioritize mobile app for Q2
• Bi-weekly design reviews

📋 *Action Items*
• Create UI mockups (next Friday)
• Create spike tickets

🏷️ roadmap, Q2, mobile
```

## Daily Thread

Create a voice memo thread every morning at 8:00 AM: `:studio_microphone: YYYY-MM-DD (Day of the week) Voice Memo Thread`
Send a reminder every night at 9:00 PM if no memos have been recorded.
