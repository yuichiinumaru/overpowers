# Extraction Task: 0500-extraction-skills-batch-023

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-023` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/cn-economy-news_SKILL.md` (Original: cn-economy-news)
- [ ] `.archive/staging/skills/ai-employee-collab_SKILL.md` (Original: ai-employee-collab)
- [ ] `.archive/staging/skills/autoclip-pro_SKILL.md` (Original: autoclip-pro)
- [ ] `.archive/staging/skills/data-analysis-skill_SKILL.md` (Original: data-analysis-skill)
- [ ] `.archive/staging/skills/pdf-toolkit-pro_SKILL.md` (Original: pdf-toolkit-pro)
- [ ] `.archive/staging/skills/wechat-auto-publisher_SKILL.md` (Original: wechat-auto-publisher)
- [ ] `.archive/staging/skills/personal-love_SKILL.md` (Original: personal-friends)
- [ ] `.archive/staging/skills/personal-nutrition_SKILL.md` (Original: personal-hygiene)
- [ ] `.archive/staging/skills/personal-sleep_SKILL.md` (Original: personal-sleep)
- [ ] `.archive/staging/skills/personal-travel_SKILL.md` (Original: personal-travel)
- [ ] `.archive/staging/skills/weibo-hot-trend_SKILL.md` (Original: weibo-hot-trend)
- [ ] `.archive/staging/skills/subagent-context-compactor_SKILL.md` (Original: subagent-context-compactor)
- [ ] `.archive/staging/skills/workflows_simple-mode.md` (Original: workflows)
- [ ] `.archive/staging/skills/agent-task-logger_SKILL.md` (Original: agent-task-logger)
- [ ] `.archive/staging/skills/math-formula-calculator_SKILL.md` (Original: math-formula-calculator)
- [ ] `.archive/staging/skills/flomo-add_SKILL.md` (Original: flomo-add)
- [ ] `.archive/staging/skills/flomo-sync_SKILL.md` (Original: flomo-sync)
- [ ] `.archive/staging/skills/singapore-fnb-location_SKILL.md` (Original: singapore-fnb-location)
- [ ] `.archive/staging/skills/singapore-location-helper_SKILL.md` (Original: singapore-location-helper)
- [ ] `.archive/staging/skills/jenkins-fix_SKILL.md` (Original: jenkins-fix)
- [ ] `.archive/staging/skills/persona-simulator_SKILL.md` (Original: persona-simulator)
- [ ] `.archive/staging/skills/openclaw-memory-fix-skill_SKILL.md` (Original: openclaw-memory-fix-skill)
- [ ] `.archive/staging/skills/openclaw-memory-fix_SKILL.md` (Original: openclaw-memory-fix)
- [ ] `.archive/staging/skills/enterprise-security-suite_SKILL.md` (Original: enterprise-security-suite)
- [ ] `.archive/staging/skills/config-safe_SKILL.md` (Original: config-safe)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
