# Extraction Task: 0500-extraction-skills-batch-042

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-042` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/wps-skill_SKILL.md` (Original: wps-skill)
- [ ] `.archive/staging/skills/bazi-daily_SKILL.md` (Original: bazi-daily)
- [ ] `.archive/staging/skills/aliyun-iqs-search_SKILL.md` (Original: aliyun-iqs-search)
- [ ] `.archive/staging/skills/wecom-meeting_SKILL.md` (Original: wecom-meeting)
- [ ] `.archive/staging/skills/paper-research-assistant_SKILL.md` (Original: paper-research-assistant)
- [ ] `.archive/staging/skills/content-headline-generator_SKILL.md` (Original: content-headline-generator)
- [ ] `.archive/staging/skills/content-structure-designer_SKILL.md` (Original: content-structure-designer)
- [ ] `.archive/staging/skills/seo-content-optimizer_SKILL.md` (Original: seo-content-optimizer)
- [ ] `.archive/staging/skills/social-media-optimizer_SKILL.md` (Original: social-media-optimizer)
- [ ] `.archive/staging/skills/prototype-generator_SKILL.md` (Original: prototype-generator)
- [ ] `.archive/staging/skills/glance-watch_SKILL.md` (Original: glance-watch)
- [ ] `.archive/staging/skills/xhs-note-creator_SKILL.md` (Original: xhs-note-creator)
- [ ] `.archive/staging/skills/github-search_SKILL.md` (Original: github-search)
- [ ] `.archive/staging/skills/technical-research_SKILL.md` (Original: technical-research)
- [ ] `.archive/staging/skills/living-agent-v1_SKILL.md` (Original: living-agent-v1)
- [ ] `.archive/staging/skills/hot-topic-finder_SKILL.md` (Original: hot-topic-finder)
- [ ] `.archive/staging/skills/.clawhub_SKILL.md` (Original: .clawhub)
- [ ] `.archive/staging/skills/a-stock-info_SKILL.md` (Original: a-stock-info)
- [ ] `.archive/staging/skills/astock-data_SKILL.md` (Original: astock-data)
- [ ] `.archive/staging/skills/baidu-web-search_SKILL.md` (Original: baidu-web-search)
- [ ] `.archive/staging/skills/oss-upload-online-access_SKILL.md` (Original: oss-upload-online-access)
- [ ] `.archive/staging/skills/writing-polish_SKILL.md` (Original: writing-polish)
- [ ] `.archive/staging/skills/compliance-review_SKILL.md` (Original: compliance-review)
- [ ] `.archive/staging/skills/juyingiot_SKILL.md` (Original: juyingiot)
- [ ] `.archive/staging/skills/skill-sharpener_SKILL.md` (Original: skill-sharpener)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
