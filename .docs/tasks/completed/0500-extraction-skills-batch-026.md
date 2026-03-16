# Extraction Task: 0500-extraction-skills-batch-026

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-026` to execute this task or follow these manual steps for each item:

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

- [x] `.archive/staging/skills/wechat-mp-writer-skill-mxx_SKILL.md` (Original: wechat-mp-writer-skill-mxx) → `skills/wechat-mp-writer/SKILL.md`
- [x] `.archive/staging/skills/zhouyi-divination_SKILL.md` (Original: zhouyi-divination) → `skills/zhouyi-divination/SKILL.md`
- [x] `.archive/staging/skills/complex-task-methodology_SKILL.md` (Original: complex-task-methodology) → `skills/complex-task-methodology/SKILL.md`
- [x] `.archive/staging/skills/openclaw-guardian-suite_SKILL.md` (Original: openclaw-guardian-suite) → `skills/openclaw-guardian-suite/SKILL.md`
- [x] `.archive/staging/skills/semantic-router_SKILL.md` (Original: semantic-router) → `skills/semantic-router/SKILL.md`
- [x] `.archive/staging/skills/subagent-isolation-guard_SKILL.md` (Original: subagent-isolation-guard) → `skills/subagent-isolation-guard/SKILL.md`
- [x] `.archive/staging/skills/yanjibus_SKILL.md` (Original: yanjibus) → `skills/yanjibus/SKILL.md`
- [x] `.archive/staging/skills/meme-scanner_SKILL.md` (Original: meme-scanner) → `skills/meme-scanner/SKILL.md`
- [x] `.archive/staging/skills/cursor-council_SKILL.md` (Original: polymarket-arb-bot) → `skills/cursor-council/SKILL.md`
- [x] `.archive/staging/skills/sulada-clawdchat_SKILL.md` (Original: sulada-clawdchat) → `skills/sulada-clawdchat/SKILL.md`
- [x] `.archive/staging/skills/sulada-habit-tracker_SKILL.md` (Original: sulada-habit-tracker) → `skills/sulada-habit-tracker/SKILL.md`
- [x] `.archive/staging/skills/sulada-knowledge-base_SKILL.md` (Original: sulada-knowledge-base) → `skills/sulada-knowledge-base/SKILL.md`
- [x] `.archive/staging/skills/testa_SKILL.md` (Original: testa) → `skills/testa/SKILL.md`
- [x] `.archive/staging/skills/zan-diary_SKILL.md` (Original: zan-diary) → `skills/zan-diary/SKILL.md`
- [x] `.archive/staging/skills/target-info-search-summarization_SKILL.md` (Original: target-info-search-summarization) → `skills/target-info-search-summarization/SKILL.md`
- [x] `.archive/staging/skills/openclaw-parking-query_SKILL.md` (Original: openclaw-parking-query) → `skills/openclaw-parking-query/SKILL.md`
- [x] `.archive/staging/skills/surf-query_SKILL.md` (Original: surf-query) → `skills/surf-query/SKILL.md`
- [x] `.archive/staging/skills/health-manager_SKILL.md` (Original: health-manager) → `skills/health-manager/SKILL.md`
- [x] `.archive/staging/skills/learning-planner_SKILL.md` (Original: learning-planner) → `skills/learning-planner/SKILL.md`
- [x] `.archive/staging/skills/reading-buddy_SKILL.md` (Original: reading-buddy) → `skills/reading-buddy/SKILL.md`
- [x] `.archive/staging/skills/reading-manager_SKILL.md` (Original: reading-manager) → `skills/reading-manager/SKILL.md`
- [x] `.archive/staging/skills/study-buddy_SKILL.md` (Original: study-buddy) → `skills/study-buddy/SKILL.md`
- [x] `.archive/staging/skills/trip_SKILL.md` (Original: trip) → `skills/trip/SKILL.md`
- [x] `.archive/staging/skills/feedback-loop_SKILL.md` (Original: feedback-loop) → `skills/feedback-loop/SKILL.md`
- [x] `.archive/staging/skills/skill-assessment_SKILL.md` (Original: skill-assessment) → `skills/skill-assessment/SKILL.md`

## Completion Summary

**Status**: ✅ **COMPLETED**  
**Date**: 2026-03-16  
**Processed**: 25/25 skills  
**Skipped**: 0  
**Failed**: 0  

All skills have been successfully processed with:
- Standardized YAML frontmatter (name, description, version, tags)
- Non-empty descriptions (critical for skill visibility)
- Proper directory structure: `skills/<skill-name>/SKILL.md`
- Original files removed from `.archive/staging/skills/`


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
