# Extraction Task: 0500-extraction-skills-batch-059

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-059` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/uapi-get-convert-unixtime_SKILL.md` (Original: uapi-get-convert-unixtime)
- [ ] `.archive/staging/skills/uapi-get-daily-news-image_SKILL.md` (Original: uapi-get-daily-news-image)
- [ ] `.archive/staging/skills/uapi-get-game-epic-free_SKILL.md` (Original: uapi-get-game-epic-free)
- [ ] `.archive/staging/skills/uapi-get-game-minecraft-userinfo_SKILL.md` (Original: uapi-get-game-minecraft-historyid)
- [ ] `.archive/staging/skills/uapi-get-game-steam-summary_SKILL.md` (Original: uapi-get-game-steam-summary)
- [ ] `.archive/staging/skills/uapi-get-github-repo_SKILL.md` (Original: uapi-get-github-repo)
- [ ] `.archive/staging/skills/uapi-get-history-programmer-today_SKILL.md` (Original: uapi-get-history-programmer-today)
- [ ] `.archive/staging/skills/uapi-get-image-motou_SKILL.md` (Original: uapi-get-image-motou)
- [ ] `.archive/staging/skills/uapi-get-misc-district_SKILL.md` (Original: uapi-get-misc-district)
- [ ] `.archive/staging/skills/uapi-get-misc-weather_SKILL.md` (Original: uapi-get-misc-weather)
- [ ] `.archive/staging/skills/telegram-voice-message-skill_SKILL.md` (Original: telegram-voice-message-skill)
- [ ] `.archive/staging/skills/vdoob_SKILL.md` (Original: vdoob)
- [ ] `.archive/staging/skills/river-memory_SKILL.md` (Original: river-memory)
- [ ] `.archive/staging/skills/stock-expert_SKILL.md` (Original: stock-expert)
- [ ] `.archive/staging/skills/auto-complex-task-planner_SKILL.md` (Original: auto-complex-task-planner)
- [ ] `.archive/staging/skills/daily-scanner_SKILL.md` (Original: daily-scanner)
- [ ] `.archive/staging/skills/get-biji_SKILL.md` (Original: get-biji)
- [ ] `.archive/staging/skills/sales-analyzer_SKILL.md` (Original: sales-analyzer)
- [ ] `.archive/staging/skills/online-shopping-discount_SKILL.md` (Original: online-shopping-discount)
- [ ] `.archive/staging/skills/xianyu-auto-fulfill_SKILL.md` (Original: xianyu-auto-fulfill)
- [ ] `.archive/staging/skills/xianyu-auto-saler_SKILL.md` (Original: xianyu-auto-saler)
- [ ] `.archive/staging/skills/personal-taxi-song-qing_SKILL.md` (Original: personal-taxi-song-qing)
- [ ] `.archive/staging/skills/xuexitong-homework-submit_SKILL.md` (Original: xuexitong-homework-submit)
- [ ] `.archive/staging/skills/hk-stock-trending_SKILL.md` (Original: hk-stock-trending)
- [ ] `.archive/staging/skills/twitter-ai-trending_SKILL.md` (Original: twitter-ai-trending)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
