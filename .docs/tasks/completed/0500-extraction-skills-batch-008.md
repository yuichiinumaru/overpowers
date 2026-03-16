# Extraction Task: 0500-extraction-skills-batch-008

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-008` to execute this task or follow these manual steps for each item:

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

- [x] `.archive/staging/skills/amap-search-skill_SKILL.md` (Original: gold-price-checker)
- [x] `.archive/staging/skills/slide-sniper_SKILL.md` (Original: slide-sniper)
- [x] `.archive/staging/skills/task-watchdog_SKILL.md` (Original: task-watchdog)
- [x] `.archive/staging/skills/vibe-harvester_SKILL.md` (Original: vibe-harvester)
- [x] `.archive/staging/skills/visual-file-sorter_SKILL.md` (Original: visual-file-sorter)
- [x] `.archive/staging/skills/book-multi-lens_SKILL.md` (Original: book-multi-lens)
- [x] `.archive/staging/skills/openclaw-safe-guard_SKILL.md` (Original: openclaw-safe-guard)
- [x] `.archive/staging/skills/douyin-video-downloader_SKILL.md` (Original: douyin-video-downloader)
- [x] `.archive/staging/skills/blessing-generator_SKILL.md` (Original: blessing-generator)
- [x] `.archive/staging/skills/content-agency_SKILL.md` (Original: content-agency)
- [x] `.archive/staging/skills/csv-wizard_SKILL.md` (Original: csv-wizard)
- [x] `.archive/staging/skills/frontend-design-pro_SKILL.md` (Original: frontend-design-pro)
- [x] `.archive/staging/skills/github-analyzer_SKILL.md` (Original: github-analyzer)
- [x] `.archive/staging/skills/jd-interview-prep_SKILL.md` (Original: jd-interview-prep)
- [x] `.archive/staging/skills/long-article-illustration_SKILL.md` (Original: long-article-illustration)
- [x] `.archive/staging/skills/opinion-analyzer_SKILL.md` (Original: opinion-analyzer)
- [x] `.archive/staging/skills/project-evaluator_SKILL.md` (Original: project-evaluator)
- [x] `.archive/staging/skills/style-cloner_SKILL.md` (Original: style-cloner)
- [x] `.archive/staging/skills/vibe-coding-checker_SKILL.md` (Original: vibe-coding-checker)
- [x] `.archive/staging/skills/writing-style-cloner_SKILL.md` (Original: writing-style-cloner)
- [x] `.archive/staging/skills/pingcode-skills_SKILL.md` (Original: pingcode-skills)
- [x] `.archive/staging/skills/play-guitar-fretboard_SKILL.md` (Original: play-guitar-fretboard)
- [x] `.archive/staging/skills/oceanengine-ads_SKILL.md` (Original: oceanengine-ads)
- [x] `.archive/staging/skills/ai-revenue-tracker_SKILL.md` (Original: ai-revenue-tracker)
- [x] `.archive/staging/skills/zipcracker_SKILL.md` (Original: zipcracker)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
