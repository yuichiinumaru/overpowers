# Extraction Task: 0500-extraction-skills-batch-066

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-066` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/kaozhutiskill_SKILL.md` (Original: kaozhutiskill)
- [ ] `.archive/staging/skills/kimi-cli_SKILL.md` (Original: kimi-cli)
- [ ] `.archive/staging/skills/polymarket-telegram-picks_SKILL.md` (Original: polymarket-telegram-picks)
- [ ] `.archive/staging/skills/bradford-lecture-analyzer_SKILL.md` (Original: bradford-lecture-analyzer)
- [ ] `.archive/staging/skills/reddit-voc-lobster-pro_SKILL.md` (Original: reddit-voc-lobster-pro)
- [ ] `.archive/staging/skills/say-xiaoai_SKILL.md` (Original: say-xiaoai)
- [ ] `.archive/staging/skills/broadcast-sign-transfer_SKILL.md` (Original: broadcast-sign-transfer)
- [ ] `.archive/staging/skills/vcloud-phone_SKILL.md` (Original: vcloud-phone)
- [ ] `.archive/staging/skills/rdm-assistant_SKILL.md` (Original: rdm-assistant)
- [ ] `.archive/staging/skills/gtcintelligence_SKILL.md` (Original: gtcintelligence)
- [ ] `.archive/staging/skills/metal-price_SKILL.md` (Original: metal-price)
- [ ] `.archive/staging/skills/gemini-image-generator_SKILL.md` (Original: gemini-image-generator)
- [ ] `.archive/staging/skills/daily-tech-broadcast_SKILL.md` (Original: daily-tech-broadcast)
- [ ] `.archive/staging/skills/tokflow_SKILL.md` (Original: tokflow)
- [ ] `.archive/staging/skills/amap-navigation_SKILL.md` (Original: amap-navigation)
- [ ] `.archive/staging/skills/railway-12306_SKILL.md` (Original: railway-12306)
- [ ] `.archive/staging/skills/xiaohongshu-publish-wangzh_SKILL.md` (Original: xiaohongshu-publish-wangzh)
- [ ] `.archive/staging/skills/bug-investigation_SKILL.md` (Original: bug-investigation)
- [ ] `.archive/staging/skills/component-api-design_SKILL.md` (Original: component-api-design)
- [ ] `.archive/staging/skills/design-to-code_SKILL.md` (Original: design-to-code)
- [ ] `.archive/staging/skills/frontend-performance_SKILL.md` (Original: frontend-performance)
- [ ] `.archive/staging/skills/modified-code-review_SKILL.md` (Original: modified-code-review)
- [ ] `.archive/staging/skills/refactor-safely_SKILL.md` (Original: refactor-safely)
- [ ] `.archive/staging/skills/xiaoai-bridge_SKILL.md` (Original: xiaoai-bridge)
- [ ] `.archive/staging/skills/football-predictor_SKILL.md` (Original: football-predictor)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
