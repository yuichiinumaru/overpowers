# Extraction Task: 0500-extraction-skills-batch-033

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-033` to execute this task or follow these manual steps for each item:

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

- [x] `.archive/staging/skills/nanobanana-ppt-skills_SKILL.md` (Original: nanobanana-ppt-skills)
- [x] `.archive/staging/skills/meihua-yishu_SKILL.md` (Original: meihua-yishu)
- [x] `.archive/staging/skills/truth-check_SKILL.md` (Original: truth-check)
- [x] `.archive/staging/skills/validate-agent_SKILL.md` (Original: validate-agent)
- [x] `.archive/staging/skills/zixun_SKILL.md` (Original: zixun)
- [x] `.archive/staging/skills/document-pro_SKILL.md` (Original: document-pro)
- [x] `.archive/staging/skills/email-reader_SKILL.md` (Original: email-reader)
- [x] `.archive/staging/skills/video-learn_SKILL.md` (Original: video-learn)
- [x] `.archive/staging/skills/openclaw-config-guide_SKILL.md` (Original: openclaw-config-guide)
- [x] `.archive/staging/skills/xiaoye-voice_SKILL.md` (Original: xiaoye-voice)
- [x] `.archive/staging/skills/bilibili-hot-monitor_SKILL.md` (Original: bilibili-hot-monitor)
- [x] `.archive/staging/skills/zxz-test_SKILL.md` (Original: zxz-test)
- [x] `.archive/staging/skills/a-stock-monitor_SKILL.md` (Original: a-stock-monitor)
- [x] `.archive/staging/skills/menews_SKILL.md` (Original: menews)
- [x] `.archive/staging/skills/china-tax-calculator_SKILL.md` (Original: china-tax-calculator)
- [x] `.archive/staging/skills/x-engagement_SKILL.md` (Original: x-engagement)
- [x] `.archive/staging/skills/jax-skill-security-scanner_SKILL.md` (Original: jax-skill-security-scanner)
- [x] `.archive/staging/skills/lobster-radio-skill_SKILL.md` (Original: lobster-radio-skill)
- [x] `.archive/staging/skills/folder-inspector_SKILL.md` (Original: folder-inspector)
- [x] `.archive/staging/skills/smart-memory-system_SKILL.md` (Original: smart-memory-system)
- [x] `.archive/staging/skills/amcjt-lottery_SKILL.md` (Original: amcjt-lottery-pro)
- [x] `.archive/staging/skills/neo4j-cypher-query-analyze_SKILL.md` (Original: neo4j-cypher-query-analyze)
- [x] `.archive/staging/skills/chinese-daily-assistant_SKILL.md` (Original: chinese-daily-assistant)
- [x] `.archive/staging/skills/orchestrator_SKILL.md` (Original: orchestrator)
- [x] `.archive/staging/skills/architecture-governance_SKILL.md` (Original: architecture-governance)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*

**Completion Date**: 2026-03-16  
**Processed by**: gamma  
**Method**: Automated batch processing script (`scripts/generators/process-skill-batches.py`)  
**Result**: 25/25 skills successfully migrated with standardized frontmatter
