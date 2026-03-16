---
name: ynote-news
description: "Youdao Cloud Note News Push: Analyzes collected notes to identify topics of interest and pushes the latest relevant news. Supports conversational triggers and daily scheduled pushes (e.g., 9 AM). Trigger phrases: 资讯推送, 设置资讯推送, 生成资讯推送."
metadata:
  openclaw:
    category: "news"
    tags: ['news', 'media', 'content']
    version: "1.0.0"
---

# YNote News — Youdao Cloud Note Information Push

Automatically extracts topics of interest based on recently favorited notes, searches for the latest information, generates a structured briefing, and pushes it to the user.

> **⚠️ Context Management**: This Skill involves a large amount of data (full note content + search results). After each step is completed, **only the structured summary is retained, and the original output is immediately discarded** to avoid context window overflow. See the "🔴 Context Management" annotations in each Step for details.

## Usage Scenarios and Summary

| Scenario | Description | How to Use |
|------|------|--------|
| **Conversation Trigger** | Request a "push of information based on recent favorites" at any time in OpenClaw | Enter the trigger phrase, and the Agent will display the briefing directly after executing 4 steps |
| **Scheduled Automatic Execution** | Automatically organize favorites and generate a briefing at a fixed time each day | Configure a scheduled task to trigger automatically at the set time; defaults to 9:00 if not set |

**Example Trigger Phrases**: Information Push, Recent Favorites, Hot Topic Push, Daily Briefing, Generate Information Push, Help Me Organize My Favorites Briefing

**Prerequisites**: `YNOTE_API_KEY` must be configured (to fetch notes); Step 3 uses Perplexity for search (has a built-in default Key, ready to use, supports time filtering). If it fails, it will fall back to Brave (requires `BRAVE_API_KEY`) or open-websearch (no Key required as a fallback). See "Prerequisites" for details.

## Prerequisites

1. **YNote MCP** (Required): `export YNOTE_API_KEY="your-api-key-here"`
2. **Web Search** (Step 3, Three-level Fallback):
   - **Perplexity** (Preferred): Use the Skill's Search API script (`perplexity-search-call.sh`); returns a list of articles. Key is built-in and ready to use.
   - **Brave** (Fallback): `BRAVE_API_KEY` needs to be configured in `openclaw.json`. Documentation: <https://docs.openclaw.ai/brave-search>
   - **open-websearch** (Bottom Fallback, No Key Required): Requires only Node.js, called via `websearch-call.sh`
3. **CLI Tools**: `curl`, `jq`, `node`

## Quick Reference

| Operation | Command |
|------|------|
| Get Recent Favorite Notes | `bash {baseDir}/get-favorite-notes.sh` (automatically truncates content, default limit=30) |
| Create Note | `bash {baseDir}/mcp-call.sh createNote '{"title":"Title","content":"# Content","folderId":""}'` |
| Search Notes | `bash {baseDir}/mcp-call.sh searchNotes '{"keyword":"Keyword"}'` |
| Get Note Content | `bash {baseDir}/mcp-call.sh getNoteTextContent '{"fileId":"<id>"}'` |
| Perplexity Search (Article List) | `echo '{"query":"Keyword","max_results":5,"search_recency_filter":"day"}' &#124; bash {baseDir}/perplexity-search-call.sh` (or use heredoc to pass JSON) |
| Web Search (Fallback) | `bash {baseDir}/websearch-call.sh search '{"query":"Keyword","limit":10,"engines":["duckduckgo","bing","baidu"]}'` |

## Core Workflow

Upon receiving a user's information push request, the following steps are executed. **After each step, only the structured summary is retained, and the original output is discarded.**

### Step 1: Get Content of Recently Favorited Notes

```bash
bash {baseDir}/get-favorite-notes.sh
```

The wrapper script automatically calls `getRecentFavoriteNotes` and **truncates the main content of each note to the first 500 characters**, ensuring the total size of 30 notes is ≤ 45KB, preventing context overflow.

Returned fields: `fileId`, `title`, `content` (first 500 characters, truncated beyond that), `collectTime` (millisecond timestamp).

Optional parameters: `get-favorite-notes.sh [limit] [characters_per_note]`, defaults to `30 500`.

### Step 2: Analyze Note Content and Extract Topics

The Agent analyzes the note content obtained in Step 1, clusters it by content relevance, and extracts **no more than 5 topics**. Each topic is summarized with a searchable theme statement to facilitate relevant article retrieval in Step 3.

**Sorting Weight**: Newness of favorite time > Number of associated notes > Topic distinctiveness. Similar themes should be merged.

Each topic includes:

| Field | Description |
|------|------|
| Topic Name | A concise and clear description of the theme (e.g., "AI Large Model Technology Trends") |
| Theme Statement (for search) | A sentence or several keywords to be used as the search query in Step 3 for retrieving relevant articles |
| Associated Notes | List of titles of related favorited notes |
| Brief Description | A 1-2 sentence summary of the content's tendency |

### Step 3: Search for the Latest Articles for Each Topic

Using the **theme statement** from each topic in Step 2 as the search query, retrieve **5 latest articles** for each topic. **Search is performed topic by topic, and after each search, the summary is extracted immediately, and the original response is discarded.**

**Search Tools** (automatically downgraded based on configuration):

1. **Perplexity** (Preferred): Use the Search API to return a list of articles (title, url, date, snippet). Call: `echo '{"query":"<Theme Statement>","max_results":5,"search_recency_filter":"<See table below>"}' | bash {baseDir}/perplexity-search-call.sh` (It is recommended to use heredoc or a temporary file to pass JSON to avoid encoding issues with Chinese characters via argv). Fallback to Brave upon call failure.
2. **Brave** (Fallback): `web_search("keyword", provider: "brave", freshness: "pd")`
3. **open-websearch** (Bottom Fallback): `bash {baseDir}/websearch-call.sh search '{"query":"Keyword","limit":5,"engines":["duckduckgo","bing"]}'`

**Time Range**: Perplexity uses `search_recency_filter`. The correspondence with user statements (defaults to `day` if not specified):

| User Statement | freshness | search_recency_filter |
|---------|-----------|------------------------|
| Not specified / Recent / Within 24 hours | `pd` | `day` |
| Recent days | `pw` | `week` |
| Recent month | `pm` | `month` |
| Recent year | `py` | `year` |

**Time Filtering**: Results may not strictly adhere to the set time range. They need to be filtered again by date: retain within the range, discard outside; those without dates can be retained, prioritizing those with dates. Each topic should still have approximately 5 articles; if fewer, retain the existing quantity.

**Filtering**: No more than 3 articles from the same source; deduplicate identical URLs; articles hitting multiple topics are assigned to the topic with higher relevance.

**🔴 Context Management**: After searching for each topic, only retain "title, source, date, URL, 80-150 character content introduction." Discard the original search response.

### Step 4: Generate and Display Briefing

Format the summaries from Step 3 according to the "Briefing Template" below and display it directly in the conversation.

## Briefing Template (Must be followed)

```markdown
# Information Push — yyyy-MM-dd

Based on the N most recent favorited notes, we have compiled the latest updates on the following M topics of interest for you.

## Topic 1: xxx
> Reason for Interest: Based on your favorited notes like "Note A", "Note B", etc.

### Latest Updates
(Sorted in reverse chronological order when dates are available, newest first)
1. **Article Title** — Source (Date)
   Article Content Introduction: Covers three elements—① Topic (What it's about) ② Core观点 (Main conclusions) ③ Reading Value (Why it's worth reading). 3-5 sentences or 80-150 characters. Avoid generic openings like "It introduces..." or "It discusses...".
   🔗 Link

2. **Article Title** — Source (Date)
   Article Content Introduction: ...
   🔗 Link

## Topic 2: xxx
> Reason for Interest: Based on your favorited note "Note C", etc.

### Latest Updates
1. ...
```

## Response Format (Must be followed)

After outputting the main body of the briefing, immediately follow it with a statistical summary:

```
| Item | Details |
|------|------|
| 📋 Number of Topics | {M} topics |
| 📰 Number of Articles | {Total number of articles} latest articles |
| 📂 Data Source | Last {N} favorited notes |
| ⏰ Generation Time | {yyyy-MM-dd HH:mm} |
```

### Step 5: Guidance and Notification

**When triggered by a scheduled task**, additionally send a desktop notification: `openclaw nodes notify "📰 Today's information push has been generated, with M topics and N articles"` (not sent for manual user triggers).

**Guidance to Enable Information Push**: After displaying the briefing, execute `openclaw cron list --json | jq '.jobs[] | select(.name == "ynote-daily-briefing")'` to check for the scheduled task. If not set, append: `💡 Would you like to automatically receive such briefings daily? Say "Set up information push" to enable it. It will be pushed by default every morning at 9:00.`

## Information Push Management

### Setting Up Information Push

**Setup** (Trigger phrases: Set up information push, Enable information push, Information push settings):
1. `openclaw cron list --json | jq '.jobs[] | select(.name == "ynote-daily-briefing")'` to check if it already exists.
2. If it exists → Inform the user of the current configuration (push time) and ask if they want to modify it.
3. If it does not exist → Create it (defaults to 9:00 daily; replace if user specifies a time): `openclaw cron add --name "ynote-daily-briefing" --cron "0 9 * * *" --session isolated --message "Generate information push"`
4. Reply with confirmation, including push time and instructions for modification/cancellation.

**Modifying Push Time** (Trigger phrases: Modify information push time):
1. Parse the target time (e.g., "Change to 8 o'clock" → `0 8 * * *`, "8 PM" → `0 20 * * *`).
2. `openclaw cron remove --name "ynote-daily-briefing"` and then `cron add` again.
3. Confirm successful modification.

**Disabling** (Trigger phrases: Disable information push, Cancel information push):
1. `openclaw cron remove --name "ynote-daily-briefing"`
2. Confirm cancellation and inform the user they can re-enable it at any time.

## Environment Variables

| Variable | Required | Default Value | Description |
|------|------|--------|------|
| `YNOTE_API_KEY` | ✅ | — | MCP Server API Key |
| `PERPLEXITY_API_KEY` | — | Built-in default | Perplexity search, ready to use |
| `BRAVE_API_KEY` | — | — | Brave search (used when Perplexity fails) |
| `YNOTE_MCP_URL` | — | `https://open.mail.163.com/api/ynote/mcp/sse` | MCP SSE endpoint |
| `YNOTE_MCP_TIMEOUT` | — | `30` | Timeout in seconds |

## Frequently Asked Questions

**Q: Error message about missing search API key?**
Search automatically falls back from Perplexity → Brave → open-websearch, with a final keyless fallback requiring only Node.js.

**Q: Too few search results?**
Adjust keyword combinations or increase the number of `engines` in open-websearch (e.g., `["duckduckgo","bing","baidu"]`).

**Q: No recent favorites?**
First, use the `ynote-clip` Skill to favorite some web pages, then generate the topic briefing.

**Q: How to set up automatic daily information push?**
Say "Set up information push". It defaults to 9:00 AM, but you can customize the time.
