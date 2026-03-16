# Extraction Task: 0500-extraction-skills-batch-025

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-025` to execute this task or follow these manual steps for each item:

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

- [x] `.archive/staging/skills/hot-alert-cn_SKILL.md` (Original: hot-alert-cn)
- [x] `.archive/staging/skills/ithome-hot-cn_SKILL.md` (Original: ithome-hot-cn)
- [x] `.archive/staging/skills/jike-hot-cn_SKILL.md` (Original: jike-hot-cn)
- [x] `.archive/staging/skills/market-analysis-cn_SKILL.md` (Original: market-analysis-cn)
- [x] `.archive/staging/skills/mbti-agent_SKILL.md` (Original: mbti-agent)
- [x] `.archive/staging/skills/product-hunt-cn_SKILL.md` (Original: product-hunt-cn)
- [x] `.archive/staging/skills/quant-trading-cn_SKILL.md` (Original: quant-trading-cn)
- [x] `.archive/staging/skills/skill-finder-cn_SKILL.md` (Original: skill-finder-cn)
- [x] `.archive/staging/skills/sspai-hot-cn_SKILL.md` (Original: sspai-hot-cn)
- [x] `.archive/staging/skills/toutiao-hot-news-cn_SKILL.md` (Original: toutiao-hot-news-cn)
- [x] `.archive/staging/skills/v2ex-hot-cn_SKILL.md` (Original: v2ex-hot-cn)
- [x] `.archive/staging/skills/wechat-mp-cn_SKILL.md` (Original: wechat-mp-cn)
- [x] `.archive/staging/skills/xueqiu-hot-cn_SKILL.md` (Original: xueqiu-hot-cn)
- [x] `.archive/staging/skills/chat-with-l_SKILL.md` (Original: chat-with-l)
- [x] `.archive/staging/skills/feishu-doc-writing_SKILL.md` (Original: feishu-doc-writing)
- [x] `.archive/staging/skills/feishu-readability_SKILL.md` (Original: feishu-readability)
- [x] `.archive/staging/skills/publish-checklist_SKILL.md` (Original: publish-checklist)
- [x] `.archive/staging/skills/ram-review_SKILL.md` (Original: ram-review)
- [x] `.archive/staging/skills/ai-meeting-room_SKILL.md` (Original: ai-meeting-room)
- [x] `.archive/staging/skills/openclaw-starter-kit_SKILL.md` (Original: openclaw-starter-kit)
- [x] `.archive/staging/skills/ai-news-research_SKILL.md` (Original: ai-news-research)
- [x] `.archive/staging/skills/weather-query-ll_SKILL.md` (Original: weather-query-ll)
- [x] `.archive/staging/skills/google-deep-research_SKILL.md` (Original: google-deep-research)
- [x] `.archive/staging/skills/sharkflow_SKILL.md` (Original: cryptowatch)
- [x] `.archive/staging/skills/ai-novel-chongshengfuchou_SKILL.md` (Original: ai-novel-chongshengfuchou)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*

**Completion Date**: 2026-03-16  
**Processed by**: gamma  
**Method**: Automated batch processing script (`scripts/generators/process-skill-batches.py`)  
**Result**: 25/25 skills successfully migrated with standardized frontmatter
