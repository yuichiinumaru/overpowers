# Extraction Task: 0500-extraction-skills-batch-056

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-056` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/rey-linkedin-automation_SKILL.md` (Original: rey-linkedin-automation)
- [ ] `.archive/staging/skills/rey-memory_SKILL.md` (Original: rey-memory)
- [ ] `.archive/staging/skills/rey-polymarket-trader_SKILL.md` (Original: rey-polymarket-trader)
- [ ] `.archive/staging/skills/rey-skill-creator_SKILL.md` (Original: rey-skill-creator)
- [ ] `.archive/staging/skills/rey-social-scheduler_SKILL.md` (Original: rey-social-scheduler)
- [ ] `.archive/staging/skills/rey-web-search_SKILL.md` (Original: rey-web-search)
- [ ] `.archive/staging/skills/root-cause-tracing_SKILL.md` (Original: root-cause-tracing)
- [ ] `.archive/staging/skills/saas-builder_SKILL.md` (Original: saas-builder)
- [ ] `.archive/staging/skills/scheduler_SKILL.md` (Original: scheduler)
- [ ] `.archive/staging/skills/self-identity_SKILL.md` (Original: self-identity)
- [ ] `.archive/staging/skills/seo-content-engine_SKILL.md` (Original: seo-content-engine)
- [ ] `.archive/staging/skills/skill-self-improvement_SKILL.md` (Original: skill-self-improvement)
- [ ] `.archive/staging/skills/sns-scheduler_SKILL.md` (Original: sns-scheduler)
- [ ] `.archive/staging/skills/supervisor-proposer_SKILL.md` (Original: supervisor-proposer)
- [ ] `.archive/staging/skills/systematic-debug_SKILL.md` (Original: systematic-debug)
- [ ] `.archive/staging/skills/template-seller_SKILL.md` (Original: template-seller)
- [ ] `.archive/staging/skills/thought-logger_SKILL.md` (Original: thought-logger)
- [ ] `.archive/staging/skills/threat-model_SKILL.md` (Original: threat-model)
- [ ] `.archive/staging/skills/tiktok-poster_SKILL.md` (Original: tiktok-poster)
- [ ] `.archive/staging/skills/trend-analyzer_SKILL.md` (Original: trend-analyzer)
- [ ] `.archive/staging/skills/upwork-seller_SKILL.md` (Original: upwork-seller)
- [ ] `.archive/staging/skills/verification-checkpoint_SKILL.md` (Original: verification-checkpoint)
- [ ] `.archive/staging/skills/video-generator_SKILL.md` (Original: video-generator)
- [ ] `.archive/staging/skills/web-scraper_SKILL.md` (Original: web-scraper)
- [ ] `.archive/staging/skills/website-builder_SKILL.md` (Original: website-builder)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
