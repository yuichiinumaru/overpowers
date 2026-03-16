# Extraction Task: 0500-extraction-skills-batch-013

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-013` to execute this task or follow these manual steps for each item:

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

- [x] `.archive/staging/skills/file-transfer-thru-local-workspace_SKILL.md` (Original: file-transfer-thru-local-workspace)
- [x] `.archive/staging/skills/wechat-article-explainer_SKILL.md` (Original: wechat-article-explainer)
- [x] `.archive/staging/skills/mcp-zentao-pro_SKILL.md` (Original: mcp-zentao-pro) → `skills/mcp-zentao-pro/`
- [x] `.archive/staging/skills/a-stock-watcher_SKILL.md` (Original: a-stock-watcher) → `skills/a-stock-watcher/`
- [x] `.archive/staging/skills/ck-rag-skill_SKILL.md` (Original: ck-rag-skill) → `skills/ck-rag-skill/`
- [x] `.archive/staging/skills/sticker_SKILL.md` (Original: sticker) → `skills/sticker/`
- [x] `.archive/staging/skills/skill-maker-chenxi_SKILL.md` (Original: skill-maker-chenxi) → `skills/skill-maker-chenxi/`
- [x] `.archive/staging/skills/28-day-goal-supervisor_SKILL.md` (Original: 28-day-goal-supervisor) → `skills/28-day-goal-supervisor/`
- [x] `.archive/staging/skills/peter-bugfix-loop_SKILL.md` (Original: peter-bugfix-loop) → `skills/peter-bugfix-loop/`
- [x] `.archive/staging/skills/peter-code-review_SKILL.md` (Original: peter-code-review) → `skills/peter-code-review/`
- [x] `.archive/staging/skills/peter-commit-ops_SKILL.md` (Original: peter-commit-ops) → `skills/peter-commit-ops/`
- [x] `.archive/staging/skills/safe_SKILL.md` (Original: safe) → `skills/safe/`
- [x] `.archive/staging/skills/terminal-executor_SKILL.md` (Original: terminal-executor) → `skills/terminal-executor/`
- [x] `.archive/staging/skills/kimi-file-transfer_SKILL.md` (Original: kimi-file-transfer) → `skills/kimi-file-transfer/`
- [x] `.archive/staging/skills/cryptofolio_SKILL.md` (Original: cryptofolio) → `skills/cryptofolio/`
- [x] `.archive/staging/skills/irene-ai-news_SKILL.md` (Original: irene-ai-news) → `skills/irene-ai-news/`
- [x] `.archive/staging/skills/alicloud-compute-swas-open_SKILL.md` (Original: alicloud-compute-swas-open) → `skills/alicloud-compute-swas-open/`
- [x] `.archive/staging/skills/baby-guide_SKILL.md` (Original: baby-guide) → `skills/baby-guide/`
- [x] `.archive/staging/skills/bilibili-helper_SKILL.md` (Original: bilibili-helper) → `skills/bilibili-helper/`
- [x] `.archive/staging/skills/brand-namer_SKILL.md` (Original: brand-namer) → `skills/brand-namer/`
- [x] `.archive/staging/skills/fitness-plan_SKILL.md` (Original: fitness-plan) → `skills/fitness-plan/`
- [x] `.archive/staging/skills/fund-advisor-cn_SKILL.md` (Original: fund-advisor-cn) → `skills/fund-advisor-cn/`
- [x] `.archive/staging/skills/live-stream-script_SKILL.md` (Original: live-stream-script) → `skills/live-stream-script/`
- [x] `.archive/staging/skills/name-generator_SKILL.md` (Original: name-generator) → `skills/name-generator/`
- [x] `.archive/staging/skills/test-publish-check_SKILL.md` (Original: test-publish-check) → `skills/test-publish-check/`


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
