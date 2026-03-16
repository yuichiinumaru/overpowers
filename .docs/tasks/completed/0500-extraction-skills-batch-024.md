# Extraction Task: 0500-extraction-skills-batch-024

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-024` to execute this task or follow these manual steps for each item:

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

- [x] `.archive/staging/skills/pexels-image-downloader_SKILL.md` (Original: pexels-image-downloader) ✅
- [x] `.archive/staging/skills/xhs-kit-publisher_SKILL.md` (Original: xhs-kit-publisher) ✅
- [x] `.archive/staging/skills/clouddream-a-data_SKILL.md` (Original: clouddream-a-data) ✅
- [x] `.archive/staging/skills/openclaw-expense-tracker_SKILL.md` (Original: openclaw-expense-tracker) ✅
- [x] `.archive/staging/skills/chinese-ai-agent-guide_SKILL.md` (Original: chinese-ai-agent-guide) ✅
- [x] `.archive/staging/skills/digital-human-training_SKILL.md` (Original: digital-human-training) ✅
- [x] `.archive/staging/skills/global-intel-summary_SKILL.md` (Original: global-intel-summary) ✅
- [x] `.archive/staging/skills/splunk-log-analyzer_SKILL.md` (Original: splunk-log-analyzer → log-analyzer) ✅
- [x] `.archive/staging/skills/openclaw-visual_SKILL.md` (Original: openclaw-visual) ✅
- [x] `.archive/staging/skills/phoenixclaw-image-gen_SKILL.md` (Original: phoenixclaw-image-gen → image-generation) ✅
- [x] `.archive/staging/skills/daily-security-check_SKILL.md` (Original: daily-security-check) ✅
- [x] `.archive/staging/skills/douyin-publish_SKILL.md` (Original: douyin-publish) ✅
- [x] `.archive/staging/skills/lark-wiki-writer_SKILL.md` (Original: lark-wiki-writer) ✅
- [x] `.archive/staging/skills/gif-maker_SKILL.md` (Original: gif-maker) ✅
- [x] `.archive/staging/skills/wechat-sticker-maker_SKILL.md` (Original: wechat-sticker-maker) ✅
- [x] `.archive/staging/skills/tianlong-analyst_SKILL.md` (Original: tianlong-analyst) ✅
- [x] `.archive/staging/skills/dianping-query_SKILL.md` (Original: dianping-query) ✅
- [x] `.archive/staging/skills/research-engine_SKILL.md` (Original: research-engine) ✅
- [x] `.archive/staging/skills/36kr-hot-cn_SKILL.md` (Original: 36kr-hot-cn) ✅
- [x] `.archive/staging/skills/weibo-hot-cn_SKILL.md` (Original: baidu-hot-cn) ✅
- [x] `.archive/staging/skills/douban-hot-cn_SKILL.md` (Original: douban-hot-cn) ✅
- [x] `.archive/staging/skills/finetune-service-cn_SKILL.md` (Original: finetune-service-cn) ✅
- [x] `.archive/staging/skills/github-trending-cn_SKILL.md` (Original: github-trending-cn) ✅
- [x] `.archive/staging/skills/hackernews-cn_SKILL.md` (Original: hackernews-cn) ✅
- [x] `.archive/staging/skills/hot-aggregator-cn_SKILL.md` (Original: hot-aggregator-cn) ✅


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
