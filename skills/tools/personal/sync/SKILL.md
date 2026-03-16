---
name: getnote-daily-sync
description: ">"
metadata:
  openclaw:
    category: "ai"
    tags: ['ai', 'automation', 'generation']
    version: "1.0.0"
---

# Get Notes → Notion Daily Report Skill

Automatically summarize your voice notes, meeting minutes, and inspiration notes recorded in **Get Notes** (biji.com) today, and generate a structured daily report to write into a **Notion** database.

---

## Daily Report Structure

After each synchronization, a new page will be created in Notion, containing:

- 📊 **Today's Overview** — What was done today, Top 3 action items needing follow-up, Key insights of the day
- 🗣️ **Client Meetings** — Recording information + Summary + Action items for each meeting
- 🎤 **Tech Talks / Recordings** — Summary of non-meeting recordings
- 💡 **Personal Inspiration** — Text-based notes
- 📌 **Follow-up Suggestions** — Summary of action items with time keywords

---

## Configuration (Environment Variables)

Set the following variables in your OpenClaw configuration or `.env` file:

| Variable Name | Required | Description |
|---|---|---|
| `GETNOTE_API_KEY` | ✅ | Get Notes API Key (obtain from Get Notes settings) |
| `GETNOTE_CLIENT_ID` | ✅ | Get Notes Client ID |
| `NOTION_TOKEN` | ✅ | Notion Integration Token ( [How to create](https://developers.notion.com/docs/create-a-notion-integration) ) |
| `NOTION_DATABASE_ID` | ✅ | Target Notion Database ID (extract from Database URL) |
| `MY_NAME` | ❌ | Your name keyword, used to filter action items starting with "I need to follow up" (e.g., `Alice,我`); leave blank to display all action items |

### Get Notion Database ID

Open your Notion database page. The URL format is:
```
https://www.notion.so/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx?v=...
```
Take the 32-character string before `?v=` as the `NOTION_DATABASE_ID`.

### Notion Database Field Requirements

The target Database needs to include the following fields (types must match):

| Field Name | Type |
|---|---|
| `Name` | Title |
| `date` | Date |
| `Summary` | Text |
| `Tags` | Multi-select |
| `Source` | Select |

---

## Usage

### Manual Trigger (Ask AI)

Simply converse:
> "Sync today's Get Notes to Notion"

### Scheduled Automatic Execution (Recommended)

Set up OpenClaw Cron to execute automatically every evening:

> "Sync today's Get Notes to Notion every night at 10 PM"

Or manually add a Cron Job:
```json
{
  "schedule": { "kind": "cron", "expr": "0 22 * * *", "tz": "Asia/Shanghai" },
  "payload": {
    "kind": "agentTurn",
    "message": "Sync today's Get Notes to Notion"
  },
  "sessionTarget": "isolated"
}
```

---

## How It Works

1. Call Get Notes Open API to fetch all notes for the day.
2. Categorize by type (Client Meetings / Tech Talks / Personal Inspiration), filter out test notes.
3. Extract structured fields such as recording information, summaries, action items, and key quotes.
4. Create a daily report page in Notion and write all content.

---

## Dependencies

- Python 3 (standard library, no extra installation required)
- Get Notes account (biji.com) + API Key
- Notion Integration + Target Database

---

## Run Script (Direct Execution)

```bash
export GETNOTE_API_KEY="your-key"
export GETNOTE_CLIENT_ID="your-client-id"
export NOTION_TOKEN="secret_xxx"
export NOTION_DATABASE_ID="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
export MY_NAME="Your Name"  # Optional

python3 skills/getnote-notion-daily/scripts/daily_sync.py
```
