# Extraction Task: 0500-extraction-skills-batch-011

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-011` to execute this task or follow these manual steps for each item:

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

- [x] `.archive/staging/skills/bazhuayu-rpa-webhook_SKILL.md` (Original: bazhuayu-rpa-webhook) → `skills/bazhuayu-rpa-webhook/`
- [x] `.archive/staging/skills/evomap-lite-client_SKILL.md` (Original: evomap-lite-client) → `skills/evomap-lite-client/`
- [x] `.archive/staging/skills/html-cn-render-fix_SKILL.md` (Original: html-cn-render-fix) → `skills/html-cn-render-fix/`
- [x] `.archive/staging/skills/stock-daily-report_SKILL.md` (Original: stock-daily-report) → `skills/stock-daily-report/`
- [x] `.archive/staging/skills/polymarket-arbitrage-pro_SKILL.md` (Original: polymarket-arbitrage-pro) → `skills/polymarket-arbitrage-pro/`
- [x] `.archive/staging/skills/feishu-probe-optimize_SKILL.md` (Original: feishu-probe-optimize)
- [x] `.archive/staging/skills/crayfish-plugin-assistant_SKILL.md` (Original: crayfish-plugin-assistant)
- [x] `.archive/staging/skills/coder-helper_SKILL.md` (Original: coder-helper)
- [x] `.archive/staging/skills/bizyair-images_SKILL.md` (Original: bizyair-images)
- [x] `.archive/staging/skills/goods-images_SKILL.md` (Original: goods-images)
- [x] `.archive/staging/skills/async-programming_SKILL.md` (Original: async-programming) → `skills/async-programming/`
- [x] `.archive/staging/skills/git-workflow_SKILL.md` (Original: git-workflow) → `skills/git-workflow/`
- [x] `.archive/staging/skills/deepseek-chat_SKILL.md` (Original: deepseek-chat) → `skills/deepseek-chat/`
- [x] `.archive/staging/skills/feishu-article-collector_SKILL.md` (Original: feishu-article-collector) → `skills/feishu-article-collector/`
- [x] `.archive/staging/skills/agent-memory-patterns_SKILL.md` (Original: agent-memory-patterns) → `skills/agent-memory-patterns/`
- [x] `.archive/staging/skills/agent-security-audit_SKILL.md` (Original: agent-security-audit) → `skills/agent-security-audit/`
- [x] `.archive/staging/skills/ephemeral-media-hosting_SKILL.md` (Original: ephemeral-media-hosting)
- [x] `.archive/staging/skills/trade-with-taro_SKILL.md` (Original: trade-with-taro)
- [x] `.archive/staging/skills/inkroam-topic-expert_SKILL.md` (Original: inkroam-topic-expert)
- [x] `.archive/staging/skills/community-manager-cn_SKILL.md` (Original: community-manager-cn)
- [x] `.archive/staging/skills/cron-expression_SKILL.md` (Original: cron-expression)
- [x] `.archive/staging/skills/dashboard-builder_SKILL.md` (Original: dashboard-builder)
- [x] `.archive/staging/skills/employee-survey_SKILL.md` (Original: employee-survey)
- [x] `.archive/staging/skills/first-aid_SKILL.md` (Original: first-aid)
- [x] `.archive/staging/skills/taobao-listing_SKILL.md` (Original: taobao-listing)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
