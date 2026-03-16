# Extraction Task: 0500-extraction-skills-batch-061

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-061` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/vectcut_SKILL.md` (Original: vectcut)
- [ ] `.archive/staging/skills/fund-report-extractor_SKILL.md` (Original: fund-report-extractor)
- [ ] `.archive/staging/skills/ppt-generator-1_SKILL.md` (Original: ppt-generator-1)
- [ ] `.archive/staging/skills/feishu-routing_SKILL.md` (Original: feishu-routing)
- [ ] `.archive/staging/skills/feishu-calendar-tool_SKILL.md` (Original: feishu-calendar-manager)
- [ ] `.archive/staging/skills/sina-stock_SKILL.md` (Original: sina-stock)
- [ ] `.archive/staging/skills/deals-hunter_SKILL.md` (Original: deals-hunter)
- [ ] `.archive/staging/skills/feishu-wiki_SKILL.md` (Original: feishu-wiki)
- [ ] `.archive/staging/skills/life-book_SKILL.md` (Original: life-book)
- [ ] `.archive/staging/skills/weixin-reader-oc_SKILL.md` (Original: weixin-reader-oc)
- [ ] `.archive/staging/skills/weather-mcp_SKILL.md` (Original: weather-mcp)
- [ ] `.archive/staging/skills/weixin-content-creator_SKILL.md` (Original: weixin-content-creator)
- [ ] `.archive/staging/skills/car-insurance_SKILL.md` (Original: car-insurance)
- [ ] `.archive/staging/skills/health-guide_SKILL.md` (Original: health-guide)
- [ ] `.archive/staging/skills/pension-guide_SKILL.md` (Original: pension-guide)
- [ ] `.archive/staging/skills/startup-guide_SKILL.md` (Original: startup-guide)
- [ ] `.archive/staging/skills/tax-guide_SKILL.md` (Original: tax-guide)
- [ ] `.archive/staging/skills/welfare-guide_SKILL.md` (Original: welfare-guide)
- [ ] `.archive/staging/skills/xhs-note-health_SKILL.md` (Original: xhs-note-health)
- [ ] `.archive/staging/skills/flutter-schema_SKILL.md` (Original: flutter-schema)
- [ ] `.archive/staging/skills/skill-preflight-bootstrap_SKILL.md` (Original: skill-preflight-bootstrap)
- [ ] `.archive/staging/skills/agent-im-manager-v100_SKILL.md` (Original: agent-im-manager-v100)
- [ ] `.archive/staging/skills/netease-music-pusher_SKILL.md` (Original: netease-music-pusher)
- [ ] `.archive/staging/skills/jiaweisi-metatheory_SKILL.md` (Original: jiaweisi-metatheory)
- [ ] `.archive/staging/skills/video-analyzer_SKILL.md` (Original: video-analyzer)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
