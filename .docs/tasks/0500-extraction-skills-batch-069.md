# Extraction Task: 0500-extraction-skills-batch-069

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-069` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/pinduoduo-automation_SKILL.md` (Original: pinduoduo-automation)
- [ ] `.archive/staging/skills/resume-screener-pro_SKILL.md` (Original: resume-screener-pro)
- [ ] `.archive/staging/skills/ppt-lecture-notes_SKILL.md` (Original: ppt-lecture-notes)
- [ ] `.archive/staging/skills/crypto-trading_SKILL.md` (Original: crypto-trading)
- [ ] `.archive/staging/skills/heartbeat-tasks_SKILL.md` (Original: heartbeat-tasks)
- [ ] `.archive/staging/skills/hk-leetf_SKILL.md` (Original: hk-leetf)
- [ ] `.archive/staging/skills/restaurant-evaluator_SKILL.md` (Original: restaurant-evaluator)
- [ ] `.archive/staging/skills/currency-converter_SKILL.md` (Original: currency-converter)
- [ ] `.archive/staging/skills/echo-test_SKILL.md` (Original: echo-test)
- [ ] `.archive/staging/skills/football-bayes_SKILL.md` (Original: football-bayes)
- [ ] `.archive/staging/skills/nsfc-grant-writer_SKILL.md` (Original: nsfc-grant-writer)
- [ ] `.archive/staging/skills/financial-analysis-skill_SKILL.md` (Original: financial-analysis-skill)
- [ ] `.archive/staging/skills/financial-analysis_SKILL.md` (Original: financial-analysis)
- [ ] `.archive/staging/skills/auto-monitor_SKILL.md` (Original: auto-monitor)
- [ ] `.archive/staging/skills/auto-workflow_SKILL.md` (Original: auto-workflow)
- [ ] `.archive/staging/skills/cache-cleanup_SKILL.md` (Original: cache-cleanup)
- [ ] `.archive/staging/skills/meta_SKILL.md` (Original: meta)
- [ ] `.archive/staging/skills/self-health-monitor_SKILL.md` (Original: self-health-monitor)
- [ ] `.archive/staging/skills/session-cleanup_SKILL.md` (Original: session-cleanup)
- [ ] `.archive/staging/skills/yidun-app-defense_SKILL.md` (Original: yidun-app-defense)
- [ ] `.archive/staging/skills/eleme-order_SKILL.md` (Original: eleme-order)
- [ ] `.archive/staging/skills/ai-dianzhang_SKILL.md` (Original: ai-dianzhang)
- [ ] `.archive/staging/skills/a2hmarket_SKILL.md` (Original: a2hmarket)
- [ ] `.archive/staging/skills/qmiao_SKILL.md` (Original: qmiao)
- [ ] `.archive/staging/skills/milk-tea-shop-accounting_SKILL.md` (Original: milk-tea-shop-accounting)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
