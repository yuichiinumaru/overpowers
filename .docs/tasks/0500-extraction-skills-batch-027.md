# Extraction Task: 0500-extraction-skills-batch-027

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-027` to execute this task or follow these manual steps for each item:

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

- [x] `workspace-indexer_SKILL.md` → `skills/workspace-indexer/` (Original: workspace-indexer)
- [x] `iflytek-asr_SKILL.md` → `skills/iflytek-asr/` (Original: iflytek-asr)
- [x] `wechat-article-parser_SKILL.md` → `skills/wechat-article-parser/` (Original: wechat-article-parser)
- [x] `wechat-style-writer_SKILL.md` → `skills/wechat-style-writer/` (Original: wechat-style-writer)
- [x] `stockselectionmodel_SKILL.md` → `skills/stockselectionmodel/` (Original: stockselectionmodel)
- [x] `xhsredbook_SKILL.md` → `skills/xhsredbook/` (Original: xhsredbook)
- [x] `notion-sync-obsidian_SKILL.md` → `skills/notion-sync-obsidian/` (Original: notion-sync-obsidian)
- [x] `mac-camera-diary_SKILL.md` → `skills/mac-camera-diary/` (Original: mac-camera-diary)
- [x] `lunar-calendar_SKILL.md` → `skills/lunar-calendar/` (Original: lunar-calendar)
- [x] `spaces-group-assistant_SKILL.md` → `skills/spaces-group-assistant/` (Original: spaces-group-assistant)
- [x] `qunar-travel-query_SKILL.md` → `skills/qunar-travel-query/` (Original: qunar-travel-query)
- [x] `weixin-xlog-analyzer_SKILL.md` → `skills/weixin-xlog-analyzer/` (Original: weixin-xlog-analyzer)
- [x] `veadk-go-skills_SKILL.md` → `skills/veadk-go-skills/` (Original: veadk-go-skills)
- [x] `pinchtab-skills_SKILL.md` → `skills/pinchtab-skills/` (Original: pinchtab-skills)
- [x] `free-girlfriend_SKILL.md` → `skills/free-girlfriend/` (Original: free-girlfriend)
- [x] `feishu-deep-research_SKILL.md` → `skills/feishu-deep-research/` (Original: feishu-deep-research)
- [x] `character-creator_SKILL.md` → `skills/character-creator/` (Original: character-creator) **[Completed earlier]**
- [x] `fal-consumption-audit_SKILL.md` → `skills/fal-consumption-audit/` (Original: fal-consumption-audit)
- [x] `fal-llms-txt_SKILL.md` → `skills/fal-llms-txt/` (Original: fal-llms-txt)
- [x] `fashion-studio_SKILL.md` → `skills/fashion-studio/` (Original: fashion-studio)
- [x] `image-model-evaluation_SKILL.md` → `skills/image-model-evaluation/` (Original: image-model-evaluation)
- [x] `minimax-audio_SKILL.md` → `skills/minimax-audio/` (Original: minimax-audio)
- [x] `nano-pro-shuihu_SKILL.md` → `skills/nano-pro-shuihu/` (Original: nano-pro-shuihu)
- [x] `novel-to-script_SKILL.md` → `skills/novel-to-script/` (Original: novel-to-script)
- [x] `omnihuman-video_SKILL.md` → `skills/omnihuman-video/` (Original: omnihuman-video)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*

**Completion Date**: 2026-03-16 (character-creator completed earlier)  
**Processed by**: gamma (batch verification)  
**Result**: 25/25 skills complete
