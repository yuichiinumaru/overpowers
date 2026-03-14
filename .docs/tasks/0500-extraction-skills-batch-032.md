# Extraction Task: 0500-extraction-skills-batch-032

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-032` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/feishu-notes-bot_SKILL.md` (Original: feishu-notes-bot)
- [ ] `.archive/staging/skills/ilove323-outlook-calendar_SKILL.md` (Original: ilove323-outlook-calendar)
- [ ] `.archive/staging/skills/daily-hot-push_SKILL.md` (Original: daily-hot-push)
- [ ] `.archive/staging/skills/tech-solution-generator_SKILL.md` (Original: tech-solution-generator)
- [ ] `.archive/staging/skills/xiaohongshu-viral-content_SKILL.md` (Original: xiaohongshu-viral-content)
- [ ] `.archive/staging/skills/code-review_SKILL.md` (Original: code-review)
- [ ] `.archive/staging/skills/development_SKILL.md` (Original: development)
- [ ] `.archive/staging/skills/doc-review_SKILL.md` (Original: doc-review)
- [ ] `.archive/staging/skills/doc-writing_SKILL.md` (Original: doc-writing)
- [ ] `.archive/staging/skills/requirement-discovery_SKILL.md` (Original: requirement-discovery)
- [ ] `.archive/staging/skills/testing_SKILL.md` (Original: testing)
- [ ] `.archive/staging/skills/groq-voice-transcriber_SKILL.md` (Original: groq-voice-transcriber)
- [ ] `.archive/staging/skills/bobo-session-cleanup_SKILL.md` (Original: bobo-session-cleanup)
- [ ] `.archive/staging/skills/qwen-image-skill_SKILL.md` (Original: qwen-image-skill)
- [ ] `.archive/staging/skills/ai-automation-workflow_SKILL.md` (Original: ai-automation-workflow)
- [ ] `.archive/staging/skills/hengqin-subsidy-helper_SKILL.md` (Original: hengqin-subsidy-helper)
- [ ] `.archive/staging/skills/macau-clinic-ai_SKILL.md` (Original: macau-clinic-ai)
- [ ] `.archive/staging/skills/medical-document-processor_SKILL.md` (Original: medical-document-processor)
- [ ] `.archive/staging/skills/medical-note-assistant_SKILL.md` (Original: medical-note-assistant)
- [ ] `.archive/staging/skills/neuro-note-assistant_SKILL.md` (Original: neuro-note-assistant)
- [ ] `.archive/staging/skills/xiaohongshu-content_SKILL.md` (Original: xiaohongshu-content)
- [ ] `.archive/staging/skills/maoyan-cli_SKILL.md` (Original: maoyan-cli)
- [ ] `.archive/staging/skills/fastmoss-report_SKILL.md` (Original: fastmoss-report)
- [ ] `.archive/staging/skills/crayfish-diary_SKILL.md` (Original: crayfish-diary)
- [ ] `.archive/staging/skills/viral-script-writer_SKILL.md` (Original: viral-script-writer)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
