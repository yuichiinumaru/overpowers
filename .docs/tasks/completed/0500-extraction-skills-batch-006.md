# Extraction Task: 0500-extraction-skills-batch-006

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-006` to execute this task or follow these manual steps for each item:

1. **Read & Analyze**: Read the staged file to understand its purpose.
2. **Format & Standardize**: 
   - Inject the appropriate YAML frontmatter (name, description, tags, version: 1.0.0).
   - Ensure the name follows the standard convention (e.g., `domain-subdomain-name`).
   - Fix any broken internal links or outdated formatting.
3. **Move to Destination**: Save the formatted file to its final destination:
   - Skills -> `skills/<domain>-<subdomain>-<name>/SKILL.md`
   - Agents -> `agents/ovp-<name>.md`
   - Workflows -> `workflows/ovp-<name>.md`
4. **Clean Up**: Delete the file from the staging folder.
5. **Check off**: Mark the checkbox below.

## Batch Items

- [x] `.archive/staging/skills/bmad-brainstorming-coach_SKILL.md` (Original: bmad-brainstorming-coach)
- [x] `.archive/staging/skills/ai-news-zh_SKILL.md` (Original: ai-news-zh)
- [x] `.archive/staging/skills/lexiang-mcp-skill_SKILL.md` (Original: lexiang-mcp-skill)
- [x] `.archive/staging/skills/lexiang-skill_SKILL.md` (Original: lexiang-skill)
- [x] `.archive/staging/skills/mcp-vods_SKILL.md` (Original: mcp-vods)
- [x] `.archive/staging/skills/audio-summary_SKILL.md` (Original: audio-summary)
- [x] `.archive/staging/skills/weeek-tasks_SKILL.md` (Original: weeek-tasks)
- [x] `.archive/staging/skills/channel-reminders_SKILL.md` (Original: channel-reminders)
- [x] `.archive/staging/skills/openclaw-skill-search-web_SKILL.md` (Original: openclaw-skill-search-web)
- [x] `.archive/staging/skills/article-summarizer_SKILL.md` (Original: article-summarizer)
- [x] `.archive/staging/skills/dingtalk-docs_SKILL.md` (Original: dingtalk-docs)
- [x] `.archive/staging/skills/hooks_README.md` (Original: hooks)
- [x] `.archive/staging/skills/mijia-home_SKILL.md` (Original: mijia-home)
- [x] `.archive/staging/skills/shortvideo-hook_SKILL.md` (Original: shortvideo-hook)
- [x] `.archive/staging/skills/alpha_SKILL.md` (Original: alpha)
- [x] `.archive/staging/skills/channel_SKILL.md` (Original: channel)
- [x] `.archive/staging/skills/crypto_SKILL.md` (Original: crypto)
- [x] `.archive/staging/skills/explorer_SKILL.md` (Original: explorer)
- [x] `.archive/staging/skills/homekit_SKILL.md` (Original: homekit)
- [x] `.archive/staging/skills/wechat_SKILL.md` (Original: wechat)
- [x] `.archive/staging/skills/ai-research-to-obsidian_SKILL.md` (Original: ai-research-to-obsidian)
- [x] `.archive/staging/skills/pengbo-space_SKILL.md` (Original: pengbo-space)
- [x] `.archive/staging/skills/a-stock-kline-analyzer_SKILL.md` (Original: a-stock-kline-analyzer)
- [x] `.archive/staging/skills/web-publish_SKILL.md` (Original: web-publish)
- [x] `.archive/staging/skills/zerotoken_SKILL.md` (Original: zerotoken)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
