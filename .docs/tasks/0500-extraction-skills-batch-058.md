# Extraction Task: 0500-extraction-skills-batch-058

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-058` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/memo-teller_SKILL.md` (Original: memo-teller)
- [ ] `.archive/staging/skills/tencentcloud-aigc-recog-video_SKILL.md` (Original: tencentcloud-aigc-recog-image)
- [ ] `.archive/staging/skills/block-trades_SKILL.md` (Original: block-trades)
- [ ] `.archive/staging/skills/margin-trading-details_SKILL.md` (Original: margin-trading-details)
- [ ] `.archive/staging/skills/stock-list-all-stocks_SKILL.md` (Original: stock-list-all-stocks)
- [ ] `.archive/staging/skills/stock-quotes-list_SKILL.md` (Original: stock-quotes-list)
- [ ] `.archive/staging/skills/stock-security-info_SKILL.md` (Original: stock-security-info)
- [ ] `.archive/staging/skills/book-to-skill_SKILL.md` (Original: book-to-skill)
- [ ] `.archive/staging/skills/service-dominant-business-model-design_SKILL.md` (Original: service-dominant-business-model-design)
- [ ] `.archive/staging/skills/calculator-chat_SKILL.md` (Original: calculator-chat)
- [ ] `.archive/staging/skills/growth-tracker_SKILL.md` (Original: growth-tracker)
- [ ] `.archive/staging/skills/wacai-index-official-website-demand-dev_SKILL.md` (Original: wacai-index-official-website-demand-dev)
- [ ] `.archive/staging/skills/wacai-zhishudashi-baidu-ranking_SKILL.md` (Original: wacai-zhishudashi-baidu-ranking)
- [ ] `.archive/staging/skills/vibe-coding-skill_SKILL.md` (Original: vibe-coding-skill)
- [ ] `.archive/staging/skills/wechat-article-typeset_SKILL.md` (Original: wechat-article-typeset)
- [ ] `.archive/staging/skills/xiaohongshu-article-generator_SKILL.md` (Original: xiaohongshu-article-generator)
- [ ] `.archive/staging/skills/bioinfo-daily-skill_SKILL.md` (Original: bioinfo-daily-skill)
- [ ] `.archive/staging/skills/ip-query_SKILL.md` (Original: ip-query)
- [ ] `.archive/staging/skills/a-share-daily-report_SKILL.md` (Original: a-share-daily-report)
- [ ] `.archive/staging/skills/feishu-task-integration-skill_SKILL.md` (Original: feishu-task-integration-skill)
- [ ] `.archive/staging/skills/111xsxa_SKILL.md` (Original: 111xsxa)
- [ ] `.archive/staging/skills/uapi-get-answerbook-ask_SKILL.md` (Original: uapi-get-answerbook-ask)
- [ ] `.archive/staging/skills/uapi-get-avatar-gravatar_SKILL.md` (Original: uapi-get-avatar-gravatar)
- [ ] `.archive/staging/skills/uapi-get-clipzy-get_SKILL.md` (Original: uapi-get-clipzy-get)
- [ ] `.archive/staging/skills/uapi-get-clipzy-raw_SKILL.md` (Original: uapi-get-clipzy-raw)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
