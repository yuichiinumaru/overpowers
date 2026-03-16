# Extraction Task: 0500-extraction-skills-batch-022

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-022` to execute this task or follow these manual steps for each item:

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

- [x] `.archive/staging/skills/social-hub_SKILL.md` (Original: social-hub) ✅
- [x] `.archive/staging/skills/ai-analyzer_SKILL.md` (Original: ai-analyzer) ✅
- [x] `.archive/staging/skills/emergency-card_SKILL.md` (Original: emergency-card) ✅
- [x] `.archive/staging/skills/family-health-analyzer_SKILL.md` (Original: family-health-analyzer) ✅
- [x] `.archive/staging/skills/fitness-analyzer_SKILL.md` (Original: fitness-analyzer) ✅
- [x] `.archive/staging/skills/food-database-query_SKILL.md` (Original: food-database-query) ✅
- [x] `.archive/staging/skills/goal-analyzer_SKILL.md` (Original: goal-analyzer) ✅
- [x] `.archive/staging/skills/health-trend-analyzer_SKILL.md` (Original: health-trend-analyzer) ✅
- [x] `.archive/staging/skills/mental-health-analyzer_SKILL.md` (Original: mental-health-analyzer) ✅
- [x] `.archive/staging/skills/nutrition-analyzer_SKILL.md` (Original: nutrition-analyzer) ✅
- [x] `.archive/staging/skills/occupational-health-analyzer_SKILL.md` (Original: occupational-health-analyzer) ✅
- [x] `.archive/staging/skills/oral-health-analyzer_SKILL.md` (Original: oral-health-analyzer) ✅
- [x] `.archive/staging/skills/rehabilitation-analyzer_SKILL.md` (Original: rehabilitation-analyzer) ✅
- [x] `.archive/staging/skills/sexual-health-analyzer_SKILL.md` (Original: sexual-health-analyzer) ✅
- [x] `.archive/staging/skills/skin-health-analyzer_SKILL.md` (Original: skin-health-analyzer) ✅
- [x] `.archive/staging/skills/sleep-analyzer_SKILL.md` (Original: sleep-analyzer) ✅
- [x] `.archive/staging/skills/tcm-constitution-analyzer_SKILL.md` (Original: tcm-constitution-analyzer) ✅
- [x] `.archive/staging/skills/travel-health-analyzer_SKILL.md` (Original: travel-health-analyzer) ✅
- [x] `.archive/staging/skills/weightloss-analyzer_SKILL.md` (Original: weightloss-analyzer) ✅
- [x] `.archive/staging/skills/noodle-create-writing_SKILL.md` (Original: noodle-create-writing) ✅
- [x] `.archive/staging/skills/fund-report-processor_SKILL.md` (Original: fund-report-processor) ✅
- [x] `.archive/staging/skills/wecom-doc_SKILL.md` (Original: wecom-doc) ✅
- [x] `.archive/staging/skills/ipo-alert_SKILL.md` (Original: ipo-alert) ✅
- [x] `.archive/staging/skills/config-manager-evomap_SKILL.md` (Original: config-manager-evomap) ✅
- [x] `.archive/staging/skills/yandex-calendar_SKILL.md` (Original: yandex-calendar) ✅


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
