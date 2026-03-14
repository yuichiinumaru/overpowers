# Extraction Task: 0500-extraction-skills-batch-060

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-060` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/teamolab-school_SKILL.md` (Original: teamolab-school)
- [ ] `.archive/staging/skills/somark-document-parser_SKILL.md` (Original: somark-document-parser)
- [ ] `.archive/staging/skills/notex-skills_SKILL.md` (Original: notex-skills)
- [ ] `.archive/staging/skills/aicone_SKILL.md` (Original: aicone)
- [ ] `.archive/staging/skills/openclaw-android_SKILL.md` (Original: openclaw-android)
- [ ] `.archive/staging/skills/yes-md-ja_SKILL.md` (Original: yes-md-ja)
- [ ] `.archive/staging/skills/yes-md-zh_SKILL.md` (Original: yes-md-zh)
- [ ] `.archive/staging/skills/skill-forge_SKILL.md` (Original: skill-forge)
- [ ] `.archive/staging/skills/document-format-skills_SKILL.md` (Original: document-format-skills)
- [ ] `.archive/staging/skills/check-user-fraud_SKILL.md` (Original: check-user-fraud)
- [ ] `.archive/staging/skills/paper-parse_SKILL.md` (Original: paper-parse)
- [ ] `.archive/staging/skills/feishu-api-bitable_SKILL.md` (Original: feishu-api-bitable)
- [ ] `.archive/staging/skills/feishu-docs_SKILL.md` (Original: feishu-docs)
- [ ] `.archive/staging/skills/strike163163-my-browser-control_SKILL.md` (Original: strike163163-my-browser-control)
- [ ] `.archive/staging/skills/feishu-knowledge-manager_SKILL.md` (Original: feishu-knowledge-manager)
- [ ] `.archive/staging/skills/finance-news-analyzer_SKILL.md` (Original: finance-news-analyzer)
- [ ] `.archive/staging/skills/free-model-finder_SKILL.md` (Original: free-model-finder)
- [ ] `.archive/staging/skills/lottery-checker_SKILL.md` (Original: lottery-checker)
- [ ] `.archive/staging/skills/auto-memory-manager_SKILL.md` (Original: auto-memory-manager)
- [ ] `.archive/staging/skills/camera-monitor_SKILL.md` (Original: camera-monitor)
- [ ] `.archive/staging/skills/memory-manager-publish_SKILL.md` (Original: memory-manager-publish)
- [ ] `.archive/staging/skills/smart-butler-publish_SKILL.md` (Original: smart-butler-publish)
- [ ] `.archive/staging/skills/smart-butler_SKILL.md` (Original: smart-butler)
- [ ] `.archive/staging/skills/task-reminder-publish_SKILL.md` (Original: task-reminder-publish)
- [ ] `.archive/staging/skills/task-reminder_SKILL.md` (Original: task-reminder)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
