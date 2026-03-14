# Extraction Task: 0500-extraction-skills-batch-050

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-050` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/banshee-s-last-cry_SKILL.md` (Original: banshee-s-last-cry)
- [ ] `.archive/staging/skills/cultivation-chronicle-cn_SKILL.md` (Original: cultivation-chronicle-cn)
- [ ] `.archive/staging/skills/whispers-from-the-star-cn_SKILL.md` (Original: whispers-from-the-star-cn)
- [ ] `.archive/staging/skills/e-crm-a_SKILL.md` (Original: e-crm-a)
- [ ] `.archive/staging/skills/mx-link_SKILL.md` (Original: mx-link)
- [ ] `.archive/staging/skills/market-data-hub_SKILL.md` (Original: market-data-hub)
- [ ] `.archive/staging/skills/fund-query_SKILL.md` (Original: fund-query)
- [ ] `.archive/staging/skills/pazzilivo-test_SKILL.md` (Original: pazzilivo-test)
- [ ] `.archive/staging/skills/google-free-media-skill_SKILL.md` (Original: google-free-media-skill)
- [ ] `.archive/staging/skills/comfyui-image-generator_SKILL.md` (Original: comfyui-image-generator)
- [ ] `.archive/staging/skills/youtube-publisher_SKILL.md` (Original: youtube-publisher)
- [ ] `.archive/staging/skills/ai-learning-journal_SKILL.md` (Original: ai-learning-journal)
- [ ] `.archive/staging/skills/openclaw-router_SKILL.md` (Original: openclaw-router)
- [ ] `.archive/staging/skills/flomo-to-obsidian_SKILL.md` (Original: flomo-to-obsidian)
- [ ] `.archive/staging/skills/ac-stock-ultrashort_SKILL.md` (Original: ac-stock-ultrashort)
- [ ] `.archive/staging/skills/getnote-daily-sync_SKILL.md` (Original: getnote-daily-sync)
- [ ] `.archive/staging/skills/phy-architect-mentor_SKILL.md` (Original: phy-architect-mentor)
- [ ] `.archive/staging/skills/phy-ux-reviewer_SKILL.md` (Original: phy-ux-reviewer)
- [ ] `.archive/staging/skills/phy-xiaohongshu-gtm_SKILL.md` (Original: phy-xiaohongshu-gtm)
- [ ] `.archive/staging/skills/x-twitter-collector_SKILL.md` (Original: x-twitter-collector)
- [ ] `.archive/staging/skills/flutter-architecture_SKILL.md` (Original: flutter-architecture)
- [ ] `.archive/staging/skills/movie-search_SKILL.md` (Original: movie-search)
- [ ] `.archive/staging/skills/clawhub-skill-explorer_SKILL.md` (Original: clawhub-skill-explorer)
- [ ] `.archive/staging/skills/openclaw-troubleshooting_SKILL.md` (Original: openclaw-troubleshooting)
- [ ] `.archive/staging/skills/biliup-skills_SKILL.md` (Original: biliup-skills)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
