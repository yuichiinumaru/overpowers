# Extraction Task: 0500-extraction-skills-batch-007

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-007` to execute this task or follow these manual steps for each item:

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

- [x] `.archive/staging/skills/dog-potty-training_SKILL.md` (Original: dog-potty-training)
- [x] `.archive/staging/skills/amulett_SKILL.md` (Original: amulett)
- [x] `.archive/staging/skills/generate-qr-code-amzulin_SKILL.md` (Original: generate-qr-code-amzulin)
- [Skipped] `.archive/staging/skills/content-creation-publisher_SKILL.md` (Original: content-creation-publisher)
- [x] `.archive/staging/skills/md-ppt-generator_SKILL.md` (Original: md-ppt-generator)
- [x] `.archive/staging/skills/dingtalk-push_SKILL.md` (Original: dingtalk-push)
- [x] `.archive/staging/skills/image-read_SKILL.md` (Original: image-read)
- [x] `.archive/staging/skills/scholar-paper-downloader_SKILL.md` (Original: scholar-paper-downloader)
- [x] `.archive/staging/skills/desearch-skill_SKILL.md` (Original: desearch-skill)
- [x] `.archive/staging/skills/xiaohongshu-skills_SKILL.md` (Original: xiaohongshu-skills)
- [x] `.archive/staging/skills/xhs-auth_SKILL.md` (Original: xhs-auth)
- [x] `.archive/staging/skills/xhs-content-ops_SKILL.md` (Original: xhs-content-ops)
- [x] `.archive/staging/skills/xhs-publish_SKILL.md` (Original: xhs-publish)
- [x] `.archive/staging/skills/daily-news-siyou_SKILL.md` (Original: daily-news-siyou)
- [x] `.archive/staging/skills/feishu-edge-tts_SKILL.md` (Original: feishu-edge-tts)
- [x] `.archive/staging/skills/feishu-voice-skill_SKILL.md` (Original: feishu-voice-skill)
- [x] `.archive/staging/skills/stock-monitor-siyou_SKILL.md` (Original: stock-monitor-siyou)
- [x] `.archive/staging/skills/wsl-chrome-cdp_SKILL.md` (Original: wsl-chrome-cdp)
- [x] `.archive/staging/skills/nimble_SKILL.md` (Original: nimble)
- [x] `.archive/staging/skills/segway_SKILL.md` (Original: segway)
- [x] `.archive/staging/skills/create-subagent_SKILL.md` (Original: create-subagent)
- [x] `.archive/staging/skills/openstoryline-use_SKILL.md` (Original: openstoryline-use)
- [x] `.archive/staging/skills/anime-calendar_SKILL.md` (Original: anime-calendar)
- [x] `.archive/staging/skills/anime-update_SKILL.md` (Original: anime-update)
- [x] `.archive/staging/skills/china-scenic-spots_SKILL.md` (Original: china-scenic-spots)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
