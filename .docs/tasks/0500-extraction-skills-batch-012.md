# Extraction Task: 0500-extraction-skills-batch-012

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-012` to execute this task or follow these manual steps for each item:

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

- [x] `.archive/staging/skills/convert-markdown_SKILL.md` (Original: convert-markdown)
- [x] `.archive/staging/skills/qqbot_SKILL.md` (Original: qqbot)
- [x] `.archive/staging/skills/csdn-publisher_SKILL.md` (Original: csdn-publisher)
- [x] `.archive/staging/skills/idea-storm_SKILL.md` (Original: idea-storm)
- [x] `.archive/staging/skills/mem9-ai_SKILL.md` (Original: mem9-ai)
- [Skipped] `.archive/staging/skills/bililidownloader_SKILL.md` (Original: bililidownloader)
- [x] `.archive/staging/skills/lark-card-sender_SKILL.md` (Original: lark-card-sender)
- [x] `.archive/staging/skills/feishu-process-feedback_SKILL.md` (Original: feishu-process-feedback)
- [x] `.archive/staging/skills/newsnow-reader_SKILL.md` (Original: newsnow-reader)
- [ ] `.archive/staging/skills/eva-soul-by-openclaw_SKILL.md` (Original: eva-soul-by-openclaw)
- [ ] `.archive/staging/skills/universal-search_SKILL.md` (Original: universal-search)
- [ ] `.archive/staging/skills/agent-memory-system_SKILL.md` (Original: agent-memory-system)
- [ ] `.archive/staging/skills/clawhub-market-analyzer_SKILL.md` (Original: clawhub-market-analyzer)
- [ ] `.archive/staging/skills/xiaohongshu-ai-money-guide_SKILL.md` (Original: xiaohongshu-ai-money-guide)
- [ ] `.archive/staging/skills/139mail-skill_SKILL.md` (Original: 139mail-skill)
- [ ] `.archive/staging/skills/patent-disclosure-writer_SKILL.md` (Original: patent-disclosure-writer)
- [ ] `.archive/staging/skills/user-insight_SKILL.md` (Original: user-insight)
- [ ] `.archive/staging/skills/le2le-blog-writer_SKILL.md` (Original: le2le-blog-writer)
- [ ] `.archive/staging/skills/dingtalk-docs-0-3-1_SKILL.md` (Original: dingtalk-docs-0-3-1)
- [ ] `.archive/staging/skills/personal-toutiao-pub_SKILL.md` (Original: personal-toutiao-pub)
- [ ] `.archive/staging/skills/personal-video-dl_SKILL.md` (Original: personal-video-dl)
- [ ] `.archive/staging/skills/xhs-post-factory_SKILL.md` (Original: xhs-post-factory)
- [ ] `.archive/staging/skills/xiaohongshu-operate_SKILL.md` (Original: xiaohongshu-operate)
- [ ] `.archive/staging/skills/dlt-lottery_SKILL.md` (Original: dlt-lottery)
- [ ] `.archive/staging/skills/weather-plus-cn_SKILL.md` (Original: weather-plus-cn)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
