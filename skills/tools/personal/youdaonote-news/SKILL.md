---
name: youdaonote-news
description: "Youdao Cloud Note News Push: Analyzes collected notes to identify topics of interest and pushes the latest relevant news. Supports conversational triggers and daily scheduled pushes (e.g., 9 AM). Trigger phrases: 资讯推送, 设置资讯推送, 生成资讯推送."
metadata:
  openclaw:
    category: "news"
    tags: ['news', 'media', 'content']
    version: "1.0.0"
---

# YoudaoNote News — Youdao Cloud Note Information Push

Extracts topics from recently favorited notes and pushes relevant information. Triggered by conversation or scheduled (default 9:00 AM); dependencies are listed in metadata.

**Trigger Words**: Generate — `Information Push`, `Recent Focus`, `Hot Topic Push`, `Daily Briefing`, `Generate Information Push`, `Help me organize my favorited briefing`; Set — `Set` / `Enable` / `Information Push Settings`; Modify Time — `Modify Information Push Time`; Close — `Close` / `Cancel Information Push`.

> **Context Management**: After each step, only retain the structured summary and immediately discard the original output (full note content, raw search responses) to avoid context overflow.

## Core Workflow

Upon receiving an information push request, execute Steps 1-5.

### Step 1: Retrieve Content of Recently Favorited Notes

```bash
bash {baseDir}/get-favorite-notes.sh
```

Defaults to 30 notes, truncating each note's body to 500 characters, with a total size ≤45KB. Optional: `get-favorite-notes.sh [limit] [characters_per_note]`

### Step 2: Analyze Note Content and Extract Topics

Analyze the content from Step 1, cluster by relevance, and extract **no more than 5 topics**. Sorting criteria: newer collection time > number of associated notes > topic distinctiveness; similar topics will be merged. Each topic includes: topic name, thematic statement (for Step 3 search query), associated note titles, and a brief description (1-2 sentences).

### Step 3: Search for Latest Articles for Each Topic

Use the **thematic statement** of each topic as the query to retrieve **5 articles** per topic. Search topic by topic, **extracting the summary and discarding the raw response immediately after each search**.

**Search Tools** (degraded in order): 1) Perplexity: `echo '{"query":"<thematic statement>","max_results":5,"search_recency_filter":"day"}' | bash {baseDir}/perplexity-search-call.sh` (for Chinese, it's recommended to use heredoc/temporary files to pass JSON); 2) Brave: `web_search(..., provider: "brave", freshness: "pd")`; 3) Fallback: `bash {baseDir}/websearch-call.sh search '{"query":"keywords","limit":5,"engines":["duckduckgo","bing"]}'`

**Time Range** (two sets of parameters cannot be mixed): Perplexity uses `search_recency_filter`, with values `day`, `week`, `month`, `year` (default `day`). web_search uses `freshness`, with values `pd`, `pw`, `pm`, `py` (default `pd`). Results are further filtered by date. A maximum of 3 articles from the same source are allowed, and URLs are deduplicated. **Context Management**: For each topic, retain only "Title, Source, Date, URL, 80-150 character description".

### Step 4: Generate and Display Briefing

Output the briefing according to the template below, displayed directly in the conversation; followed by a statistical summary after the main content.

**Briefing Template** (must be followed):

```markdown
# Information Push — yyyy-MM-dd

Based on the last N favorited notes, we have compiled the latest updates on the following M topics of interest for you.

## Topic 1: xxx
> Reason for focus: Based on your favorited notes such as "Note A", "Note B", etc.

### Latest Updates
(Sorted by date in descending order if available)
1. **Article Title** — Source (Date)
   Article Description: Topic + core viewpoints + reading value, 80-150 characters, avoid generic openings.
   🔗 Link
```

**Response Format** (immediately follows the briefing):

```
| Item | Details |
|------|------|
| 📋 Number of Topics | {M} topics |
| 📰 Number of Articles | {Total Articles} latest articles |
| 📂 Data Source | Last {N} favorited notes |
| ⏰ Generation Time | {yyyy-MM-dd HH:mm} |
```

### Step 5: Guidance and Notification

When triggered by schedule: `openclaw nodes notify "📰 Today's information push has been generated, with M topics and N articles"` (not sent for manual triggers). After the briefing, check the scheduled task: `openclaw cron list --json | jq '.jobs[] | select(.name == "youdaonote-news")'`; if not set, append: `💡 Want to receive this automatically every day? Just say "Set Information Push", defaults to 9 AM.`

## Information Push Management

**Set** (Trigger words: `Set Information Push`, `Enable Information Push`, `Information Push Settings`): First, check `openclaw cron list --json | jq '.jobs[] | select(.name == "youdaonote-news")'`; if it exists, inform the user of the configuration and ask if they want to modify it; if it doesn't exist, run `openclaw cron add --name "youdaonote-news" --cron "0 9 * * *" --session isolated --message "Generate Information Push"` (replace cron with user-specified time if provided). Confirm and provide instructions for modification/cancellation.

**Modify Time** (Trigger word: `Modify Information Push Time`): Parse the target time (e.g., 8 AM → `0 8 * * *`, 8 PM → `0 20 * * *`), then `openclaw cron remove --name "youdaonote-news"` followed by `cron add` again. Confirm successful execution.

**Close** (Trigger words: `Close Information Push`, `Cancel Information Push`): Run `openclaw cron remove --name "youdaonote-news"`, confirm, and inform the user that it can be re-enabled at any time.
