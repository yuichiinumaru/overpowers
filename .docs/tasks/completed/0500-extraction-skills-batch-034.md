# Extraction Task: 0500-extraction-skills-batch-034

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-034` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/code-analyzer_SKILL.md` (Original: code-analyzer)
- [ ] `.archive/staging/skills/lu-auto-deploy_SKILL.md` (Original: lu-auto-deploy)
- [ ] `.archive/staging/skills/lu-music-player_SKILL.md` (Original: lu-music-player)
- [ ] `.archive/staging/skills/lu-nas-monitor_SKILL.md` (Original: lu-nas-monitor)
- [ ] `.archive/staging/skills/openclaw-maintenance_SKILL.md` (Original: openclaw-maintenance)
- [ ] `.archive/staging/skills/usage-tracker-clawhub_SKILL.md` (Original: usage-tracker-clawhub)
- [ ] `.archive/staging/skills/constitution-inquiry_SKILL.md` (Original: constitution-inquiry)
- [ ] `.archive/staging/skills/huaweicloud-skill_SKILL.md` (Original: huaweicloud-skill)
- [ ] `.archive/staging/skills/stock-monitor-skill-0-1-0_SKILL.md` (Original: stock-monitor-skill-0-1-0)
- [ ] `.archive/staging/skills/yugioh-news_SKILL.md` (Original: yugioh-news)
- [ ] `.archive/staging/skills/bilibili-update-viewer_SKILL.md` (Original: bilibili-update-viewer)
- [ ] `.archive/staging/skills/telegram-voice-mode_SKILL.md` (Original: telegram-voice-mode)
- [ ] `.archive/staging/skills/aviation-healthcheck_SKILL.md` (Original: aviation-healthcheck)
- [ ] `.archive/staging/skills/moss-deep-search_SKILL.md` (Original: moss-deep-search)
- [ ] `.archive/staging/skills/skills-public_SKILL.md` (Original: skills-public)
- [ ] `.archive/staging/skills/zentao-analytics_SKILL.md` (Original: zentao-analytics)
- [ ] `.archive/staging/skills/openclaw-skillguard_SKILL.md` (Original: openclaw-skillguard)
- [ ] `.archive/staging/skills/academic-literature-search_SKILL.md` (Original: academic-literature-search)
- [ ] `.archive/staging/skills/intelligent-diagnosis-report_SKILL.md` (Original: intelligent-diagnosis-report)
- [ ] `.archive/staging/skills/operation-platform-enterprise-knowledge_SKILL.md` (Original: operation-platform-enterprise-knowledge)
- [ ] `.archive/staging/skills/sendfiles-to-feishu_SKILL.md` (Original: sendfiles-to-feishu)
- [ ] `.archive/staging/skills/video-downloader-skill_SKILL.md` (Original: video-downloader-skill)
- [ ] `.archive/staging/skills/agent-compete-scope_SKILL.md` (Original: agent-compete-scope)
- [ ] `.archive/staging/skills/agent-crypto-lens_SKILL.md` (Original: agent-crypto-lens)
- [ ] `.archive/staging/skills/agent-news-digest_SKILL.md` (Original: agent-news-digest)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
