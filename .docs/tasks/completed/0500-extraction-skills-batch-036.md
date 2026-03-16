# Extraction Task: 0500-extraction-skills-batch-036

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-036` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/bilibili-video-publish_SKILL.md` (Original: bilibili-video-publish)
- [ ] `.archive/staging/skills/douyin-video-publish_SKILL.md` (Original: douyin-video-publish)
- [ ] `.archive/staging/skills/video-publish-all_SKILL.md` (Original: video-publish-all)
- [ ] `.archive/staging/skills/wechat-video-publish_SKILL.md` (Original: wechat-video-publish)
- [ ] `.archive/staging/skills/weixin-video-publish_SKILL.md` (Original: weixin-video-publish)
- [ ] `.archive/staging/skills/xiaohongshu-video-publish_SKILL.md` (Original: xiaohongshu-video-publish)
- [ ] `.archive/staging/skills/cross-exchange-trading-platform_SKILL.md` (Original: cross-exchange-trading-platform)
- [ ] `.archive/staging/skills/a-share-glossary-tutor_SKILL.md` (Original: a-share-glossary-tutor)
- [ ] `.archive/staging/skills/a-share-metrics-card_SKILL.md` (Original: a-share-metrics-card)
- [ ] `.archive/staging/skills/daily-report-writer_SKILL.md` (Original: daily-report-writer)
- [ ] `.archive/staging/skills/openclaw-starter-guide_SKILL.md` (Original: openclaw-starter-guide)
- [ ] `.archive/staging/skills/process-flow-navigator_SKILL.md` (Original: process-flow-navigator)
- [ ] `.archive/staging/skills/md-knowledge-spliter_SKILL.md` (Original: md-knowledge-spliter)
- [ ] `.archive/staging/skills/product-compare_SKILL.md` (Original: product-compare)
- [ ] `.archive/staging/skills/ocr-space_SKILL.md` (Original: ocr-space)
- [ ] `.archive/staging/skills/svg-animator_SKILL.md` (Original: svg-animator)
- [ ] `.archive/staging/skills/mediwise-health-suite_SKILL.md` (Original: mediwise-health-suite)
- [ ] `.archive/staging/skills/diagnosis-comparison_SKILL.md` (Original: diagnosis-comparison)
- [ ] `.archive/staging/skills/health-education_SKILL.md` (Original: health-education)
- [ ] `.archive/staging/skills/health-monitor_SKILL.md` (Original: health-monitor)
- [ ] `.archive/staging/skills/medical-search_SKILL.md` (Original: medical-search)
- [ ] `.archive/staging/skills/symptom-triage_SKILL.md` (Original: symptom-triage)
- [ ] `.archive/staging/skills/douyin-transcribe-skill_SKILL.md` (Original: douyin-transcribe-skill)
- [ ] `.archive/staging/skills/douyin-transcribe_SKILL.md` (Original: douyin-transcribe)
- [ ] `.archive/staging/skills/what-to-eat_SKILL.md` (Original: what-to-eat)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
