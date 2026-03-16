# Extraction Task: 0500-extraction-skills-batch-035

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-035` to execute this task or follow these manual steps for each item:

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

- [x] `.archive/staging/skills/agent-onchain-watch_SKILL.md` (Original: agent-onchain-watch)
- [x] `.archive/staging/skills/agent-trend-radar_SKILL.md` (Original: agent-trend-radar)
- [x] `.archive/staging/skills/cell_SKILL.md` (Original: cell)
- [x] `.archive/staging/skills/epc_SKILL.md` (Original: epc)
- [x] `.archive/staging/skills/exchange_SKILL.md` (Original: exchange)
- [x] `.archive/staging/skills/huangli_SKILL.md` (Original: huangli)
- [x] `.archive/staging/skills/jisu-astro_SKILL.md` (Original: jisu-astro)
- [x] `.archive/staging/skills/jisu-baidu_SKILL.md` (Original: jisu-baidu)
- [x] `.archive/staging/skills/jisu-baiduai_SKILL.md` (Original: jisu-baiduai)
- [x] `.archive/staging/skills/jisu-bazi_SKILL.md` (Original: jisu-bazi)
- [x] `.archive/staging/skills/jisu-calendar_SKILL.md` (Original: jisu-calendar)
- [x] `.archive/staging/skills/jisu-car_SKILL.md` (Original: jisu-car)
- [x] `.archive/staging/skills/jisu-movie_SKILL.md` (Original: jisu-movie)
- [x] `.archive/staging/skills/jisu-news_SKILL.md` (Original: jisu-news)
- [x] `.archive/staging/skills/jisu-stock_SKILL.md` (Original: jisu-stock)
- [x] `.archive/staging/skills/mobileempty_SKILL.md` (Original: mobileempty)
- [x] `.archive/staging/skills/parts_SKILL.md` (Original: parts)
- [x] `.archive/staging/skills/stockhistory_SKILL.md` (Original: stockhistory)
- [x] `.archive/staging/skills/vin_SKILL.md` (Original: vin)
- [x] `.archive/staging/skills/resume-project-summarizer_SKILL.md` (Original: resume-project-summarizer)
- [x] `.archive/staging/skills/aliyun-asr_SKILL.md` (Original: aliyun-asr)
- [x] `.archive/staging/skills/aliyun-oss_SKILL.md` (Original: aliyun-oss)
- [x] `.archive/staging/skills/tencentcloud-tts_SKILL.md` (Original: tencentcloud-tts)
- [x] `.archive/staging/skills/openclaw-work-protocol_SKILL.md` (Original: openclaw-work-protocol)
- [x] `.archive/staging/skills/coding-as-dressing_SKILL.md` (Original: coding-as-dressing)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*

**Completion Date**: 2026-03-16  
**Processed by**: gamma  
**Method**: Automated batch processing script (`scripts/generators/process-skill-batches.py`)  
**Result**: 25/25 skills successfully migrated with standardized frontmatter
