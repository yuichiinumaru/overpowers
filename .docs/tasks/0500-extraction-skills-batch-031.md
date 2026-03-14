# Extraction Task: 0500-extraction-skills-batch-031

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-031` to execute this task or follow these manual steps for each item:

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

- [x] `.archive/staging/skills/ai-writing-assistant-cn-payment_SKILL.md` (Original: ai-writing-assistant-cn-payment)
- [x] `.archive/staging/skills/ai-writing-assistant-cn-v1-1_SKILL.md` (Original: ai-writing-assistant-cn-v1-1)
- [x] `.archive/staging/skills/ai-writing-assistant-cn_SKILL.md` (Original: ai-writing-assistant-cn)
- [x] `.archive/staging/skills/ozon-product-sourcing_SKILL.md` (Original: ozon-product-sourcing)
- [x] `.archive/staging/skills/voice-note-transcriber-cn-payment_SKILL.md` (Original: pdf-smart-tool-cn-payment)
- [x] `.archive/staging/skills/pdf-smart-tool-cn-v1-1_SKILL.md` (Original: pdf-smart-tool-cn-v1-1)
- [x] `.archive/staging/skills/pdf-smart-tool-cn_SKILL.md` (Original: pdf-smart-tool-cn)
- [x] `.archive/staging/skills/smart-customer-service-cn-payment_SKILL.md` (Original: smart-customer-service-cn-payment)
- [x] `.archive/staging/skills/smart-customer-service-cn_SKILL.md` (Original: smart-customer-service-cn)
- [x] `.archive/staging/skills/smart-expense-tracker-cn-payment_SKILL.md` (Original: smart-expense-tracker-cn-payment)
- [x] `.archive/staging/skills/smart-expense-tracker-cn-v1-1_SKILL.md` (Original: smart-expense-tracker-cn-v1-1)
- [x] `.archive/staging/skills/smart-expense-tracker-cn_SKILL.md` (Original: smart-expense-tracker-cn)
- [x] `.archive/staging/skills/smart-marketing-copy-cn-payment_SKILL.md` (Original: smart-marketing-copy-cn-payment)
- [x] `.archive/staging/skills/smart-resume-optimizer-cn_SKILL.md` (Original: smart-resume-optimizer-cn)
- [x] `.archive/staging/skills/voice-note-transcriber-cn-v1-1_SKILL.md` (Original: voice-note-transcriber-cn-v1-1)
- [x] `.archive/staging/skills/voice-note-transcriber-cn_SKILL.md` (Original: voice-note-transcriber-cn)
- [x] `.archive/staging/skills/bangai-recruit_SKILL.md` (Original: bangai-recruit)
- [x] `.archive/staging/skills/weibo-fresh-posts_SKILL.md` (Original: weibo-fresh-posts)
- [x] `.archive/staging/skills/communication-mqtt_SKILL.md` (Original: communication-mqtt)
- [x] `.archive/staging/skills/tencentcloud-faceid-detectaifakefaces_SKILL.md` (Original: tencentcloud-faceid-detectaifakefaces)
- [x] `.archive/staging/skills/okx-trading-exe_SKILL.md` (Original: okx-trading-exe)
- [x] `.archive/staging/skills/kugou-mysterious-shop_SKILL.md` (Original: kugou-mysterious-shop)
- [x] `.archive/staging/skills/brainhole-factory_SKILL.md` (Original: brainhole-factory)
- [x] `.archive/staging/skills/safe-edit_SKILL.md` (Original: safe-edit)
- [x] `.archive/staging/skills/quick-note_SKILL.md` (Original: quick-note)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*

**Completion Date**: 2026-03-16  
**Processed by**: gamma  
**Method**: Automated batch processing script (`scripts/generators/process-skill-batches.py`)  
**Result**: 25/25 skills successfully migrated with standardized frontmatter
