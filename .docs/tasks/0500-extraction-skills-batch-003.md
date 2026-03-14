# Extraction Task: 0500-extraction-skills-batch-003

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-003` to execute this task or follow these manual steps for each item:

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

- [x] `.archive/staging/skills/pdf-analyzer_SKILL.md` (Original: pdf-analyzer)
- [x] `.archive/staging/skills/triple-layer-memory_SKILL.md` (Original: triple-layer-memory)
- [x] `.archive/staging/skills/douyin-cover-builder_SKILL.md` (Original: douyin-cover-builder)
- [x] `.archive/staging/skills/stock-watchlist_SKILL.md` (Original: stock-watchlist)
- [x] `.archive/staging/skills/molt-solver_SKILL.md` (Original: molt-solver)
- [x] `.archive/staging/skills/skilltree_SKILL.md` (Original: skilltree)
- [x] `.archive/staging/skills/skill-goldprice_SKILL.md` (Original: skill-goldprice)
- [x] `.archive/staging/skills/rednote-viral-writer_SKILL.md` (Original: rednote-viral-writer)
-[Skipped] `.archive/staging/skills/sensitive-check-skill_SKILL.md` (Original: sensitive-check-skill)
- [x] `.archive/staging/skills/anime-assistant_SKILL.md` (Original: anime-assistant)
- [x] `.archive/staging/skills/xhs-auto-content-by-hot_SKILL.md` (Original: xhs-auto-content-by-hot)
- [x] `.archive/staging/skills/txt-to-epub_SKILL.md` (Original: txt-to-epub)
- [x] `.archive/staging/skills/api-monitor_SKILL.md` (Original: api-monitor)
- [x] `.archive/staging/skills/qqbot-prompt-optimizer_SKILL.md` (Original: qqbot-prompt-optimizer)
- [x] `.archive/staging/skills/server-maintenance_SKILL.md` (Original: server-maintenance)
- [x] `.archive/staging/skills/tg-mysql-design_SKILL.md` (Original: tg-mysql-design)
- [x] `.archive/staging/skills/auto-logger_SKILL.md` (Original: auto-logger)
- [x] `.archive/staging/skills/cn-daily-tools_SKILL.md` (Original: cn-daily-tools)
- [x] `.archive/staging/skills/web-learner-1-0-0_SKILL.md` (Original: web-learner-1-0-0)
- [x] `.archive/staging/skills/feishu-user-md_SKILL.md` (Original: feishu-user-md)
- [x] `.archive/staging/skills/image-prompt-generator_SKILL.md` (Original: image-prompt-generator)
- [x] `.archive/staging/skills/xhs-writing-coach_SKILL.md` (Original: xhs-content-creator)
- [x] `.archive/staging/skills/claw-google-ads_SKILL.md` (Original: claw-google-ads)
- [x] `.archive/staging/skills/dingtalk-log_SKILL.md` (Original: dingtalk-log)
- [x] `.archive/staging/skills/lifelog_SKILL.md` (Original: lifelog)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
