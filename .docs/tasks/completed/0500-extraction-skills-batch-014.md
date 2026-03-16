# Extraction Task: 0500-extraction-skills-batch-014

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-014` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/video-script-creator_SKILL.md` (Original: video-script-creator)
- [ ] `.archive/staging/skills/wechat-mp-writer_SKILL.md` (Original: wechat-mp-writer)
- [ ] `.archive/staging/skills/xhs-viral-note-writer_SKILL.md` (Original: xhs-viral-note-writer)
- [ ] `.archive/staging/skills/chinese-novelist-skill_SKILL.md` (Original: chinese-novelist-skill)
- [ ] `.archive/staging/skills/raspberry-pi-camera-service_SKILL.md` (Original: raspberry-pi-camera-service)
- [ ] `.archive/staging/skills/raspberry-pi-gpio_SKILL.md` (Original: raspberry-pi-gpio)
- [ ] `.archive/staging/skills/lead-processor_SKILL.md` (Original: lead-processor)
- [ ] `.archive/staging/skills/daily-review-assistant_SKILL.md` (Original: daily-review-assistant)
- [ ] `.archive/staging/skills/stock-review_SKILL.md` (Original: stock-review)
- [ ] `.archive/staging/skills/brand-slogan_SKILL.md` (Original: brand-slogan)
- [ ] `.archive/staging/skills/marketing-calendar_SKILL.md` (Original: marketing-calendar)
- [ ] `.archive/staging/skills/drawio-coderknock_SKILL.md` (Original: drawio-coderknock)
- [ ] `.archive/staging/skills/alimail_SKILL.md` (Original: alimail)
- [ ] `.archive/staging/skills/openclaw-cleaner_SKILL.md` (Original: openclaw-cleaner)
- [ ] `.archive/staging/skills/free-weather-api_SKILL.md` (Original: free-weather-api)
- [ ] `.archive/staging/skills/111_SKILL.md` (Original: 111)
- [ ] `.archive/staging/skills/baidu-map-api_SKILL.md` (Original: baidu-map-api)
- [ ] `.archive/staging/skills/wechat-mp-publisher1_SKILL.md` (Original: wechat-mp-publisher1)
- [ ] `.archive/staging/skills/d4-world-boss_SKILL.md` (Original: d4-world-boss)
- [ ] `.archive/staging/skills/dnfm-tracker_SKILL.md` (Original: dnfm-tracker)
- [ ] `.archive/staging/skills/baidu-ecommerce-search_SKILL.md` (Original: baidu-ecommerce-search)
- [ ] `.archive/staging/skills/regex-assistant_SKILL.md` (Original: regex-assistant)
- [ ] `.archive/staging/skills/chinese-daily-report-generator_SKILL.md` (Original: chinese-daily-report-generator)
- [ ] `.archive/staging/skills/awesun-remote-control_SKILL.md` (Original: awesun-remote-control)
- [ ] `.archive/staging/skills/redbookskills_SKILL.md` (Original: redbookskills)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
