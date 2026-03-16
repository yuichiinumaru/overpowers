# Extraction Task: 0500-extraction-skills-batch-029

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-029` to execute this task or follow these manual steps for each item:

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

- [x] `.archive/staging/skills/crypto-strategy-suite_SKILL.md` (Original: crypto-strategy-suite)
- [x] `.archive/staging/skills/code-flow-visualizer_SKILL.md` (Original: code-flow-visualizer)
- [x] `.archive/staging/skills/error-message-decoder_SKILL.md` (Original: error-message-decoder)
- [x] `.archive/staging/skills/performance-profiler_SKILL.md` (Original: performance-profiler)
- [x] `.archive/staging/skills/regex-generator_SKILL.md` (Original: regex-generator)
- [x] `.archive/staging/skills/focus-mind_SKILL.md` (Original: focus-mind)
- [x] `.archive/staging/skills/snapdesign-rednote_SKILL.md` (Original: snapdesign-rednote)
- [x] `.archive/staging/skills/minimax-opus-tune_SKILL.md` (Original: minimax-opus-tune)
- [x] `.archive/staging/skills/ai-entrepreneur-guide_SKILL.md` (Original: ai-entrepreneur-guide)
- [x] `.archive/staging/skills/oceanbase-datapilot_SKILL.md` (Original: oceanbase-datapilot)
- [x] `.archive/staging/skills/prediction-market-reporter_SKILL.md` (Original: prediction-market-reporter)
- [x] `.archive/staging/skills/huamu668-memos-cloud_SKILL.md` (Original: huamu668-memos-cloud)
- [x] `.archive/staging/skills/huamu668-openclaw-security_SKILL.md` (Original: huamu668-openclaw-security)
- [x] `.archive/staging/skills/tcn-diagnosis_SKILL.md` (Original: tcn-diagnosis)
- [x] `.archive/staging/skills/writing-assistant-pro_SKILL.md` (Original: writing-assistant-pro)
- [x] `.archive/staging/skills/btceth-dulwin-engine_SKILL.md` (Original: btceth-dulwin-engine)
- [x] `.archive/staging/skills/code-snippet-oc_SKILL.md` (Original: code-snippet-oc)
- [x] `.archive/staging/skills/currency-converter-zh_SKILL.md` (Original: currency-converter-zh)
- [x] `.archive/staging/skills/daily-reminder_SKILL.md` (Original: daily-reminder)
- [x] `.archive/staging/skills/email-draft-oc_SKILL.md` (Original: email-draft-oc)
- [x] `.archive/staging/skills/expense-tracker-oc_SKILL.md` (Original: expense-tracker-oc)
- [x] `.archive/staging/skills/file-organizer-zh_SKILL.md` (Original: file-organizer-zh)
- [x] `.archive/staging/skills/habit-tracker-oc_SKILL.md` (Original: habit-tracker-oc)
- [x] `.archive/staging/skills/link-saver_SKILL.md` (Original: link-saver)
- [x] `.archive/staging/skills/meeting-notes-oc_SKILL.md` (Original: meeting-notes-oc)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*

**Completion Date**: 2026-03-16  
**Processed by**: gamma  
**Method**: Automated batch processing script (`scripts/generators/process-skill-batches.py`)  
**Result**: 25/25 skills successfully migrated with standardized frontmatter
