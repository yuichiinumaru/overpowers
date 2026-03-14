# Extraction Task: 0500-extraction-skills-batch-018

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-018` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/email-backup_SKILL.md` (Original: email-backup)
- [ ] `.archive/staging/skills/amap-jsapi-skill_SKILL.md` (Original: amap-jsapi-skill)
- [ ] `.archive/staging/skills/amap-lbs-skill_SKILL.md` (Original: amap-lbs-skill)
- [ ] `.archive/staging/skills/bank-analysis_SKILL.md` (Original: bank-analysis)
- [ ] `.archive/staging/skills/chinese-writing-assistant_SKILL.md` (Original: chinese-writing-assistant)
- [ ] `.archive/staging/skills/movie-butler_SKILL.md` (Original: movie-butler)
- [ ] `.archive/staging/skills/xiaohongshu-algorithm-optimizer_SKILL.md` (Original: xiaohongshu-algorithm-optimizer)
- [ ] `.archive/staging/skills/xinqing-journal_SKILL.md` (Original: mood-diary)
- [ ] `.archive/staging/skills/zhichu-tracker_SKILL.md` (Original: smart-ledger)
- [ ] `.archive/staging/skills/wechat-article-crayon_SKILL.md` (Original: wechat-article-crayon)
- [ ] `.archive/staging/skills/bing-bing-xia-jiang_SKILL.md` (Original: bing-bing-xia-jiang)
- [ ] `.archive/staging/skills/multi-agent-collaboration_SKILL.md` (Original: multi-agent-collaboration)
- [ ] `.archive/staging/skills/bilibili-player_SKILL.md` (Original: bilibili-player)
- [ ] `.archive/staging/skills/jarvis-tts_SKILL.md` (Original: jarvis-tts)
- [ ] `.archive/staging/skills/office-automation-test_SKILL.md` (Original: office-automation-test)
- [ ] `.archive/staging/skills/abby-autonomy_SKILL.md` (Original: abby-autonomy)
- [ ] `.archive/staging/skills/abby-browser_SKILL.md` (Original: abby-browser)
- [ ] `.archive/staging/skills/friday_SKILL.md` (Original: friday)
- [ ] `.archive/staging/skills/stock-monitor-pro_SKILL.md` (Original: stock-monitor-pro)
- [ ] `.archive/staging/skills/group-chat-response_SKILL.md` (Original: group-chat-response)
- [ ] `.archive/staging/skills/response-timing_SKILL.md` (Original: response-timing)
- [ ] `.archive/staging/skills/team-communication_SKILL.md` (Original: team-communication)
- [ ] `.archive/staging/skills/csdn-publish_SKILL.md` (Original: csdn-publish)
- [ ] `.archive/staging/skills/boss-skill_SKILL.md` (Original: boss-skill)
- [ ] `.archive/staging/skills/learning-system-skill_SKILL.md` (Original: learning-system-skill)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
