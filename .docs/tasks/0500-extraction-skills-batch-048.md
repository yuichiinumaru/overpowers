# Extraction Task: 0500-extraction-skills-batch-048

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-048` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/data-sync_SKILL.md` (Original: data-sync)
- [ ] `.archive/staging/skills/knowledge-distill_SKILL.md` (Original: knowledge-distill)
- [ ] `.archive/staging/skills/wx-skill-factory_SKILL.md` (Original: wx-skill-factory)
- [ ] `.archive/staging/skills/bsc-dev-monitor_SKILL.md` (Original: bsc-dev-monitor-v2)
- [ ] `.archive/staging/skills/sdd-dev-workflow_SKILL.md` (Original: sdd-dev-workflow)
- [ ] `.archive/staging/skills/feishu-advanced-builder_SKILL.md` (Original: feishu-advanced-builder)
- [ ] `.archive/staging/skills/medical-device-code-review_SKILL.md` (Original: medical-device-code-review)
- [ ] `.archive/staging/skills/auto-model-selector_SKILL.md` (Original: auto-model-selector)
- [ ] `.archive/staging/skills/12306-train-assistant_SKILL.md` (Original: 12306-train-assistant)
- [ ] `.archive/staging/skills/zhihu-assistant-skill_SKILL.md` (Original: zhihu-assistant-skill)
- [ ] `.archive/staging/skills/zh-humanizer_SKILL.md` (Original: zh-humanizer)
- [ ] `.archive/staging/skills/v2_SKILL.md` (Original: v2)
- [ ] `.archive/staging/skills/discord-dynasty_SKILL.md` (Original: discord-dynasty)
- [ ] `.archive/staging/skills/caoliao-qrcode-markdown-content-skill_SKILL.md` (Original: caoliao-qrcode-markdown-content-skill)
- [ ] `.archive/staging/skills/hy-3d-generation_SKILL.md` (Original: hy-3d-generation)
- [ ] `.archive/staging/skills/hy-image-generation_SKILL.md` (Original: hy-image-generation)
- [ ] `.archive/staging/skills/tencentcloud-image-face-fusion_SKILL.md` (Original: tencentcloud-image-face-fusion)
- [ ] `.archive/staging/skills/weavefox-xhs-intel_SKILL.md` (Original: weavefox-xhs-intel)
- [ ] `.archive/staging/skills/guidelines_SKILL.md` (Original: guidelines)
- [ ] `.archive/staging/skills/session-archive-backup_SKILL.md` (Original: session-archive-backup)
- [ ] `.archive/staging/skills/metabot-basic_SKILL.md` (Original: metabot-basic)
- [ ] `.archive/staging/skills/chinatravel_SKILL.md` (Original: chinatravel)
- [ ] `.archive/staging/skills/email-163-com_SKILL.md` (Original: email-163-com)
- [ ] `.archive/staging/skills/simmer-signal-service_SKILL.md` (Original: simmer-signal-service)
- [ ] `.archive/staging/skills/config-validator-zh-cn_SKILL.md` (Original: config-validator-zh-cn)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
