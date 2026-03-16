# Extraction Task: 0500-extraction-skills-batch-051

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-051` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/runningcoach_SKILL.md` (Original: runningcoach)
- [ ] `.archive/staging/skills/setup-wizard_SKILL.md` (Original: setup-wizard)
- [ ] `.archive/staging/skills/hd-sales-clue_SKILL.md` (Original: hd-sales-clue)
- [ ] `.archive/staging/skills/csgo-monitor_SKILL.md` (Original: csgo-monitor)
- [ ] `.archive/staging/skills/aicoin-trading_SKILL.md` (Original: aicoin-trading)
- [ ] `.archive/staging/skills/bizcard_SKILL.md` (Original: bizcard)
- [ ] `.archive/staging/skills/homepod-tts_SKILL.md` (Original: homepod-tts)
- [ ] `.archive/staging/skills/napcat-qq_SKILL.md` (Original: napcat-qq)
- [ ] `.archive/staging/skills/read-wechat-article_SKILL.md` (Original: read-wechat-article)
- [ ] `.archive/staging/skills/job-skills-advisor_SKILL.md` (Original: job-skills-advisor)
- [ ] `.archive/staging/skills/learn-anything-pro_SKILL.md` (Original: learn-anything-pro)
- [ ] `.archive/staging/skills/memecoin-analyst_SKILL.md` (Original: memecoin-analyst)
- [ ] `.archive/staging/skills/pdf-helper_SKILL.md` (Original: pdf-helper)
- [ ] `.archive/staging/skills/book-writer_SKILL.md` (Original: book-writer)
- [ ] `.archive/staging/skills/bili-mindmap_SKILL.md` (Original: bili-mindmap)
- [ ] `.archive/staging/skills/character-profile-cn_SKILL.md` (Original: character-profile-cn)
- [ ] `.archive/staging/skills/test-tt-skill_SKILL.md` (Original: tmap-lbs-service)
- [ ] `.archive/staging/skills/marriott_SKILL.md` (Original: marriott)
- [ ] `.archive/staging/skills/openclaw-framework_SKILL.md` (Original: openclaw-framework)
- [ ] `.archive/staging/skills/openclaw-skill-session-memory_SKILL.md` (Original: openclaw-skill-session-memory)
- [ ] `.archive/staging/skills/openclaw-skill-whisper-stt_SKILL.md` (Original: openclaw-skill-whisper-stt)
- [ ] `.archive/staging/skills/media-news-summary_SKILL.md` (Original: media-news-summary)
- [ ] `.archive/staging/skills/metaso-search_SKILL.md` (Original: metaso-search)
- [ ] `.archive/staging/skills/webchat-pro_SKILL.md` (Original: webchat-pro)
- [ ] `.archive/staging/skills/claw-a2a-client_SKILL.md` (Original: claw-a2a-client)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
