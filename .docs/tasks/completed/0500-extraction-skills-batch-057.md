# Extraction Task: 0500-extraction-skills-batch-057

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-057` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/youtube-automation_SKILL.md` (Original: youtube-automation)
- [ ] `.archive/staging/skills/wechat-mp-publisher-1-0-0_SKILL.md` (Original: wechat-mp-publisher-1-0-0)
- [ ] `.archive/staging/skills/openclaw-feishu-docs-perm-auto_SKILL.md` (Original: openclaw-feishu-docs-perm-auto)
- [ ] `.archive/staging/skills/gold-analyst_SKILL.md` (Original: gold-analyst)
- [ ] `.archive/staging/skills/dev-deploy_SKILL.md` (Original: dev-deploy)
- [ ] `.archive/staging/skills/qa-reviewer_SKILL.md` (Original: qa-reviewer)
- [ ] `.archive/staging/skills/player_SKILL.md` (Original: player)
- [ ] `.archive/staging/skills/agent-optimizer_SKILL.md` (Original: agent-optimizer)
- [ ] `.archive/staging/skills/input-validator_SKILL.md` (Original: input-validator)
- [ ] `.archive/staging/skills/chan-theory-analysis_SKILL.md` (Original: chan-theory-analysis)
- [ ] `.archive/staging/skills/stock-monitor-hkus_SKILL.md` (Original: stock-monitor-hkus)
- [ ] `.archive/staging/skills/telegram-offline-voice_SKILL.md` (Original: telegram-offline-voice)
- [ ] `.archive/staging/skills/telegram-voice-group_SKILL.md` (Original: telegram-voice-group)
- [ ] `.archive/staging/skills/master-orchestrator_SKILL.md` (Original: master-orchestrator)
- [ ] `.archive/staging/skills/skill-usage-tracker_SKILL.md` (Original: skill-usage-tracker)
- [ ] `.archive/staging/skills/paper-check_SKILL.md` (Original: paper-check)
- [ ] `.archive/staging/skills/stp_SKILL.md` (Original: stp)
- [ ] `.archive/staging/skills/ai-ceo-automation_SKILL.md` (Original: ai-ceo-automation)
- [ ] `.archive/staging/skills/ai-company_SKILL.md` (Original: ai-company)
- [ ] `.archive/staging/skills/fp-skill_SKILL.md` (Original: fp-skill)
- [ ] `.archive/staging/skills/claw-loudyai-skill_SKILL.md` (Original: claw-loudyai-skill)
- [ ] `.archive/staging/skills/magic-internet-access_SKILL.md` (Original: magic-internet-access)
- [ ] `.archive/staging/skills/async-web-search_SKILL.md` (Original: async-web-search)
- [ ] `.archive/staging/skills/agentearth_SKILL.md` (Original: ag-earth)
- [ ] `.archive/staging/skills/nova-three-level-memory_SKILL.md` (Original: nova-three-level-memory)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
