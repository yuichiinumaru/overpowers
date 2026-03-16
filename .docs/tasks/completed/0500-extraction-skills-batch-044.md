# Extraction Task: 0500-extraction-skills-batch-044

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-044` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/workflow-decomposer_SKILL.md` (Original: workflow-decomposer)
- [ ] `.archive/staging/skills/common-fetcher_SKILL.md` (Original: common-fetcher)
- [ ] `.archive/staging/skills/ag-model-usage_SKILL.md` (Original: ag-model-usage)
- [ ] `.archive/staging/skills/screen-vision_SKILL.md` (Original: screen-vision)
- [ ] `.archive/staging/skills/tg-checkin_SKILL.md` (Original: tg-checkin)
- [ ] `.archive/staging/skills/tg-history_SKILL.md` (Original: tg-history)
- [ ] `.archive/staging/skills/parallel-responder_SKILL.md` (Original: parallel-responder)
- [ ] `.archive/staging/skills/personify-memory_SKILL.md` (Original: personify-memory)
- [ ] `.archive/staging/skills/social-media-publish_SKILL.md` (Original: social-media-publish)
- [ ] `.archive/staging/skills/search-1-0-0_SKILL.md` (Original: search-1-0-0)
- [ ] `.archive/staging/skills/latte-news-fetcher-v2_SKILL.md` (Original: latte-news-fetcher-v2)
- [ ] `.archive/staging/skills/latte-news-fetcher_SKILL.md` (Original: latte-news-fetcher)
- [ ] `.archive/staging/skills/luogao-news-fetcher_SKILL.md` (Original: luogao-news-fetcher)
- [ ] `.archive/staging/skills/lsl-test-skill1_SKILL.md` (Original: lsl-test-skill1)
- [ ] `.archive/staging/skills/post2xhs_SKILL.md` (Original: post2xhs)
- [ ] `.archive/staging/skills/xhsauto_SKILL.md` (Original: xhsauto)
- [ ] `.archive/staging/skills/test-stock-performance-express_SKILL.md` (Original: test-stock-performance-express)
- [ ] `.archive/staging/skills/huxiu_SKILL.md` (Original: huxiu)
- [ ] `.archive/staging/skills/file-processor_SKILL.md` (Original: file-processor)
- [ ] `.archive/staging/skills/siliconflow-vision_SKILL.md` (Original: siliconflow-vision)
- [ ] `.archive/staging/skills/aha-point-generator_SKILL.md` (Original: aha-point-generator)
- [ ] `.archive/staging/skills/taiji-topo-file-downloader_SKILL.md` (Original: taiji-topo-file-downloader)
- [ ] `.archive/staging/skills/cyber-growth_SKILL.md` (Original: cyber-growth)
- [ ] `.archive/staging/skills/seedance-assistant_SKILL.md` (Original: seedance-assistant)
- [ ] `.archive/staging/skills/video-merger_SKILL.md` (Original: video-merger)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
