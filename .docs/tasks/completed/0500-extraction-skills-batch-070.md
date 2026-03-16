# Extraction Task: 0500-extraction-skills-batch-070

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-070` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/xiaohongshu-auto-publish_SKILL.md` (Original: xiaohongshu-auto-publish)
- [ ] `.archive/staging/skills/article-writer_SKILL.md` (Original: article-writer)
- [ ] `.archive/staging/skills/api-logger_SKILL.md` (Original: api-logger)
- [ ] `.archive/staging/skills/virtual-boyfriend_SKILL.md` (Original: virtual-boyfriend)
- [ ] `.archive/staging/skills/daily-viz_SKILL.md` (Original: daily-viz)
- [ ] `.archive/staging/skills/house-buying-advisor_SKILL.md` (Original: house-buying-advisor)
- [ ] `.archive/staging/skills/promotion-review_SKILL.md` (Original: promotion-review)
- [ ] `.archive/staging/skills/lunar-reminder_SKILL.md` (Original: lunar-reminder)
- [ ] `.archive/staging/skills/fanqie-masterclass_SKILL.md` (Original: fanqie-masterclass)
- [ ] `.archive/staging/skills/metaso-search-v2_SKILL.md` (Original: metaso-search-v2)
- [ ] `.archive/staging/skills/nanobot-feishu-send_SKILL.md` (Original: nanobot-feishu-send)
- [ ] `.archive/staging/skills/cross-agent-collab_SKILL.md` (Original: cross-agent-collab)
- [ ] `.archive/staging/skills/chinese-baby-names_SKILL.md` (Original: chinese-baby-names)
- [ ] `.archive/staging/skills/meta-skill-generator_SKILL.md` (Original: meta-skill-generator)
- [ ] `.archive/staging/skills/reminder_SKILL.md` (Original: reminder)
- [ ] `.archive/staging/skills/feishu-voice-reply_SKILL.md` (Original: feishu-voice-reply)
- [ ] `.archive/staging/skills/post-to-xhs_SKILL.md` (Original: post-to-xhs)
- [ ] `.archive/staging/skills/xhs-login_SKILL.md` (Original: xhs-login)
- [ ] `.archive/staging/skills/xiaohongshu-mcp-skills_SKILL.md` (Original: xiaohongshu-mcp-skills)
- [ ] `.archive/staging/skills/a-stock-trading-assistant_SKILL.md` (Original: a-stock-trading-assistant)
- [ ] `.archive/staging/skills/sales-manager_SKILL.md` (Original: sales-manager)
- [ ] `.archive/staging/skills/secure-memory-stack_SKILL.md` (Original: secure-memory-stack)
- [ ] `.archive/staging/skills/sync-memory-skills_SKILL.md` (Original: sync-memory-skills)
- [ ] `.archive/staging/skills/system-repair-expert_SKILL.md` (Original: system-repair-expert)
- [ ] `.archive/staging/skills/musk-insider-bare_SKILL.md` (Original: musk-insider-bare)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
