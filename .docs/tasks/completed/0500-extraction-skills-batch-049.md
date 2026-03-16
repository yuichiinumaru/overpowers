# Extraction Task: 0500-extraction-skills-batch-049

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-049` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/nico-safe-config-workflow_SKILL.md` (Original: nico-safe-config-workflow)
- [ ] `.archive/staging/skills/insight-writer_SKILL.md` (Original: insight-writer)
- [ ] `.archive/staging/skills/direct-analysis_SKILL.md` (Original: direct-analysis)
- [ ] `.archive/staging/skills/nini-writing-inspiration_SKILL.md` (Original: nini-writing-inspiration)
- [ ] `.archive/staging/skills/nini-zaregoto-miko_SKILL.md` (Original: nini-zaregoto-miko)
- [ ] `.archive/staging/skills/pywencaistock_SKILL.md` (Original: pywencaistock)
- [ ] `.archive/staging/skills/longtask-progress_SKILL.md` (Original: longtask-progress)
- [ ] `.archive/staging/skills/session-recall_SKILL.md` (Original: session-recall)
- [ ] `.archive/staging/skills/first-basic_SKILL.md` (Original: first-basic)
- [ ] `.archive/staging/skills/project-assistant_SKILL.md` (Original: project-assistant)
- [ ] `.archive/staging/skills/pomodoro-bot_SKILL.md` (Original: pomodoro-bot)
- [ ] `.archive/staging/skills/sec-audit_SKILL.md` (Original: sec-audit)
- [ ] `.archive/staging/skills/agent-heartbeat_SKILL.md` (Original: agent-heartbeat)
- [ ] `.archive/staging/skills/huangxianshi-divination_SKILL.md` (Original: huangxianshi-divination)
- [ ] `.archive/staging/skills/nomtiq_SKILL.md` (Original: nomtiq)
- [ ] `.archive/staging/skills/gta-real-estate-report_SKILL.md` (Original: gta-real-estate-report)
- [ ] `.archive/staging/skills/jimeng-ai_SKILL.md` (Original: jimeng-ai)
- [ ] `.archive/staging/skills/word-document-organizer_SKILL.md` (Original: word-document-organizer)
- [ ] `.archive/staging/skills/m-valuation_SKILL.md` (Original: m-valuation)
- [ ] `.archive/staging/skills/daily-hot-news_SKILL.md` (Original: daily-hot-news)
- [ ] `.archive/staging/skills/free-voice_SKILL.md` (Original: free-voice)
- [ ] `.archive/staging/skills/docx-to-md_SKILL.md` (Original: docx-to-md)
- [ ] `.archive/staging/skills/agent-avengers_SKILL.md` (Original: agent-avengers)
- [ ] `.archive/staging/skills/android-unused-resource-cleanup_SKILL.md` (Original: android-unused-resource-cleanup)
- [ ] `.archive/staging/skills/stock-screener-cn_SKILL.md` (Original: stock-screener-cn)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
