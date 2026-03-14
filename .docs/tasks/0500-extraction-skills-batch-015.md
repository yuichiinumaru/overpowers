# Extraction Task: 0500-extraction-skills-batch-015

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-015` to execute this task or follow these manual steps for each item:

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

- [x] `.archive/staging/skills/dev-task_SKILL.md` (Original: dev-task)
- [x] `.archive/staging/skills/home-todo_SKILL.md` (Original: home-todo)
- [x] `.archive/staging/skills/smith-matrix_SKILL.md` (Original: smith-matrix)
- [x] `.archive/staging/skills/wework-archive-service_SKILL.md` (Original: wework-archive-service)
- [x] `.archive/staging/skills/video-pro-cza_SKILL.md` (Original: video-pro-cza) → `skills/video-pro-cza/`
- [x] `.archive/staging/skills/a-share-analysis_SKILL.md` (Original: a-share-analysis) → `skills/a-share-analysis/`
- [x] `.archive/staging/skills/daily-game-news_SKILL.md` (Original: daily-game-news) → `skills/daily-game-news/`
- [x] `.archive/staging/skills/daily-voice-quote_SKILL.md` (Original: daily-voice-quote) → `skills/daily-voice-quote/`
- [x] `.archive/staging/skills/zhihu-to-wechat_SKILL.md` (Original: zhihu-to-wechat) → `skills/zhihu-to-wechat/`
- [x] `.archive/staging/skills/task-management_SKILL.md` (Original: task-management) → `skills/task-management/`
- [x] `.archive/staging/skills/cn-video-gen_SKILL.md` (Original: cn-video-gen) → `skills/cn-video-gen/`
- [x] `.archive/staging/skills/hd-infoimage_SKILL.md` (Original: hd-infoimage) → `skills/hd-infoimage/`
- [x] `.archive/staging/skills/sketch-illustration_SKILL.md` (Original: sketch-illustration)
- [x] `.archive/staging/skills/xiaolongxia-eudic-vocab_SKILL.md` (Original: xiaolongxia-eudic-vocab)
- [x] `.archive/staging/skills/ai-evolution-engine-v2_SKILL.md` (Original: ai-evolution-engine-v2) → `skills/ai-evolution-engine-v2/`
- [x] `.archive/staging/skills/oc-cost-analyzer_SKILL.md` (Original: oc-cost-analyzer) → `skills/oc-cost-analyzer/`
- [x] `.archive/staging/skills/easy-openclaw_SKILL.md` (Original: easy-openclaw) → `skills/easy-openclaw/`
- [x] `.archive/staging/skills/docs-converter_SKILL.md` (Original: docs-converter) → `skills/docs-converter/`
- [x] `.archive/staging/skills/ren-wu-shou-wei-qi_SKILL.md` (Original: ren-wu-shou-wei-qi) → `skills/ren-wu-shou-wei-qi/`
- [x] `.archive/staging/skills/local-hub_SKILL.md` (Original: local-hub) → `skills/local-hub/`
- [x] `.archive/staging/skills/vk-client-search-repetitor_SKILL.md` (Original: vk-client-search-repetitor) → `skills/vk-client-search-repetitor/`
- [x] `.archive/staging/skills/create-agent-arch_SKILL.md` (Original: create-agent-arch) → `skills/create-agent-arch/`
- [x] `.archive/staging/skills/memory-system_SKILL.md` (Original: memory-system) → `skills/memory-system/`
- [x] `.archive/staging/skills/qintianjian_SKILL.md` (Original: qintianjian) → `skills/qintianjian/`
- [x] `.archive/staging/skills/openclaw-wecom-channel_SKILL.md` (Original: openclaw-wecom-channel) → `skills/openclaw-wecom-channel/`


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
