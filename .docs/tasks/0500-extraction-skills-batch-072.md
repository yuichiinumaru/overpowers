# Extraction Task: 0500-extraction-skills-batch-072

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-072` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/reading-list_SKILL.md` (Original: reading-list)
- [ ] `.archive/staging/skills/redbook-cards-skill_SKILL.md` (Original: redbook-cards-skill)
- [ ] `.archive/staging/skills/wx-md-article_SKILL.md` (Original: wx-md-article)
- [ ] `.archive/staging/skills/domain-agent-hub_SKILL.md` (Original: domain-agent-hub)
- [ ] `.archive/staging/skills/session-monitor_SKILL.md` (Original: session-monitor)
- [ ] `.archive/staging/skills/dist_SKILL.md` (Original: dist)
- [ ] `.archive/staging/skills/personal-health-journal_SKILL.md` (Original: personal-health-journal)
- [ ] `.archive/staging/skills/easy-code-review_SKILL.md` (Original: easy-code-review)
- [ ] `.archive/staging/skills/hk-ai-stock-expert_SKILL.md` (Original: hk-ai-stock-expert)
- [ ] `.archive/staging/skills/interactive-games_SKILL.md` (Original: interactive-games)
- [ ] `.archive/staging/skills/veadk-skills_SKILL.md` (Original: veadk-skills)
- [ ] `.archive/staging/skills/website-monitor-skill_SKILL.md` (Original: website-monitor-skill)
- [ ] `.archive/staging/skills/marcus-a-stock_SKILL.md` (Original: marcus-a-stock)
- [ ] `.archive/staging/skills/apitest_SKILL.md` (Original: apitest)
- [ ] `.archive/staging/skills/pdf-ocr-skill_SKILL.md` (Original: pdf-ocr-skill)
- [ ] `.archive/staging/skills/rd-cost-skill_SKILL.md` (Original: rd-cost-skill)
- [ ] `.archive/staging/skills/real-estate-debt-analysis-skill_SKILL.md` (Original: real-estate-debt-analysis-skill)
- [ ] `.archive/staging/skills/xiaohongshu-mcporter-publish_SKILL.md` (Original: xiaohongshu-mcporter-publish)
- [ ] `.archive/staging/skills/diary-force_SKILL.md` (Original: diary-force)
- [ ] `.archive/staging/skills/openclaw-binance_SKILL.md` (Original: openclaw-binance)
- [ ] `.archive/staging/skills/harvard-paper-zh_SKILL.md` (Original: harvard-paper-zh)
- [ ] `.archive/staging/skills/multi-inbox-merge_SKILL.md` (Original: multi-inbox-merge)
- [ ] `.archive/staging/skills/nl2json_SKILL.md` (Original: nl2json)
- [ ] `.archive/staging/skills/diary-conversation_SKILL.md` (Original: diary-conversation)
- [ ] `.archive/staging/skills/ai-content-strategy_SKILL.md` (Original: ai-content-strategy)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
