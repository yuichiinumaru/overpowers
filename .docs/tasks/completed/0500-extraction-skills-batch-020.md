# Extraction Task: 0500-extraction-skills-batch-020

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-020` to execute this task or follow these manual steps for each item:

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

- [x] `.archive/staging/skills/feishu-multi-agent_SKILL.md` (Original: feishu-multi-agent)
- [x] `.archive/staging/skills/crypto-auto-progression_SKILL.md` (Original: crypto-auto-progression)
- [x] `.archive/staging/skills/gpu-check_SKILL.md` (Original: gpu-check)
- [x] `.archive/staging/skills/company-search-kimi_SKILL.md` (Original: company-search-kimi)
- [x] `.archive/staging/skills/finance-accounting_SKILL.md` (Original: finance-accounting)
- [x] `.archive/staging/skills/voice-chat-skill_SKILL.md` (Original: voice-chat-skill) → `skills/voice-chat/SKILL.md`
- [x] `.archive/staging/skills/139mail_SKILL.md` (Original: 139mail) → `skills/139mail/SKILL.md`
- [x] `.archive/staging/skills/voice-listener_SKILL.md` (Original: voice-listener) → `skills/voice-listener/SKILL.md`
- [x] `.archive/staging/skills/charactercard_SKILL.md` (Original: charactercard) → `skills/tavern-card/SKILL.md`
- [x] `.archive/staging/skills/shit-journal_SKILL.md` (Original: shit-journal) → `skills/shit-journal/SKILL.md`
- [x] `.archive/staging/skills/skills-5_SKILL.md` (Original: skills-5) → `skills/wecom-channel-fix/SKILL.md`
- [x] `.archive/staging/skills/social-persona-chloe_SKILL.md` (Original: social-persona-chloe) → `skills/social-persona-chloe/SKILL.md`
- [x] `.archive/staging/skills/moss-trade-bot-factory_SKILL.md` (Original: moss-trade-bot-factory) → `skills/crypto-bot-factory/SKILL.md`
- [x] `.archive/staging/skills/deep-research-skill_SKILL.md` (Original: deep-research-skill) → `skills/deep-research/SKILL.md`
- [x] `.archive/staging/skills/jimeng-generator_SKILL.md` (Original: jimeng-generator) → `skills/jimeng-generator/SKILL.md`
- [x] `.archive/staging/skills/v2ray-proxy_SKILL.md` (Original: v2ray-proxy) → `skills/v2ray-proxy/SKILL.md`
- [x] `.archive/staging/skills/financial-contant-writer_SKILL.md` (Original: financial-contant-writer) → `skills/financial-content-writer/SKILL.md` **(Note: Fixed typo in directory name)**
- [x] `.archive/staging/skills/moment-writer_SKILL.md` (Original: moment-writer) → `skills/moment-writer/SKILL.md`
- [x] `.archive/staging/skills/wechat-article-writer_SKILL.md` (Original: wechat-article-writer) → `skills/wechat-article-writer/SKILL.md`
- [x] `.archive/staging/skills/fy_SKILL.md` (Original: fy) → `skills/fy/SKILL.md`
- [x] `.archive/staging/skills/fenge-smart-search_SKILL.md` (Original: fenge-smart-search) → `skills/fenge-smart-search/SKILL.md`
- [x] `.archive/staging/skills/china-demand-mining_SKILL.md` (Original: china-demand-mining) → `skills/china-demand-mining/SKILL.md`
- [x] `.archive/staging/skills/china-hotel-comparison_SKILL.md` (Original: china-hotel-comparison) → `skills/china-hotel-comparison/SKILL.md`
- [x] `.archive/staging/skills/tianyi-revenue-tracker_SKILL.md` (Original: tianyi-revenue-tracker) → `skills/tianyi-revenue-tracker/SKILL.md`
- [x] `.archive/staging/skills/tianyi-self-upgrade_SKILL.md` (Original: tianyi-self-upgrade) → `skills/tianyi-self-upgrade/SKILL.md`


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
