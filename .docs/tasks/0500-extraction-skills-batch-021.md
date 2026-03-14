# Extraction Task: 0500-extraction-skills-batch-021

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-021` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/btc-shortterm-predictor_SKILL.md` (Original: btc-shortterm-predictor)
- [ ] `.archive/staging/skills/weather-arbitrage_SKILL.md` (Original: weather-arbitrage)
- [ ] `.archive/staging/skills/flap-skills_SKILL.md` (Original: flap-skills)
- [ ] `.archive/staging/skills/cocktail-boy_SKILL.md` (Original: cocktail-boy)
- [ ] `.archive/staging/skills/send-email-tool_SKILL.md` (Original: send-email-tool)
- [ ] `.archive/staging/skills/browser-session-manager_SKILL.md` (Original: browser-session-manager)
- [ ] `.archive/staging/skills/nano-banana-image-t8-mac_SKILL.md` (Original: nano-banana-image-t8-alluse)
- [ ] `.archive/staging/skills/a-stock-investment_SKILL.md` (Original: a-stock-investment)
- [ ] `.archive/staging/skills/gold-skill_SKILL.md` (Original: gold-skill)
- [ ] `.archive/staging/skills/sudu-gold_SKILL.md` (Original: sudu-gold)
- [ ] `.archive/staging/skills/project-code-standard_SKILL.md` (Original: project-code-standard)
- [ ] `.archive/staging/skills/akshare-router-cn_SKILL.md` (Original: akshare-router-cn)
- [ ] `.archive/staging/skills/feishu-doc-tech-optimizer_SKILL.md` (Original: feishu-doc-tech-optimizer)
- [ ] `.archive/staging/skills/imperial-engine_SKILL.md` (Original: imperial-engine)
- [ ] `.archive/staging/skills/number-two-migration_SKILL.md` (Original: number-two-migration)
- [ ] `.archive/staging/skills/number-two-restart_SKILL.md` (Original: number-two-restart)
- [ ] `.archive/staging/skills/ultimate-agent_SKILL.md` (Original: ultimate-agent)
- [ ] `.archive/staging/skills/local-mail-server_SKILL.md` (Original: local-mail-server)
- [ ] `.archive/staging/skills/douyin-hot-trend_SKILL.md` (Original: douyin-hot-trend)
- [ ] `.archive/staging/skills/douyin-video-analyzer_SKILL.md` (Original: douyin-video-analyzer)
- [ ] `.archive/staging/skills/feishu-file_SKILL.md` (Original: feishu-file)
- [ ] `.archive/staging/skills/feishu-voice_SKILL.md` (Original: feishu-voice)
- [ ] `.archive/staging/skills/find-reference-video_SKILL.md` (Original: find-reference-video)
- [ ] `.archive/staging/skills/video-channels-update-push_SKILL.md` (Original: video-channels-update-push)
- [ ] `.archive/staging/skills/social-hub-server_SKILL.md` (Original: social-hub-server)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
