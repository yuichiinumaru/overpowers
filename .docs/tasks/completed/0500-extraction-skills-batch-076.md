# Extraction Task: 0500-extraction-skills-batch-076

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-076` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/1688-distributor_SKILL.md` (Original: 1688-distributor)
- [ ] `.archive/staging/skills/vetmew-consultation_SKILL.md` (Original: vetmew-consultation)
- [ ] `.archive/staging/skills/heartbeat-manager_SKILL.md` (Original: heartbeat-manager)
- [ ] `.archive/staging/skills/agent-network-v2_SKILL.md` (Original: agent-network-v2)
- [ ] `.archive/staging/skills/openclaw-agent-network_SKILL.md` (Original: openclaw-agent-network)
- [ ] `.archive/staging/skills/openamc_SKILL.md` (Original: openamc)
- [ ] `.archive/staging/skills/wevoicereply_SKILL.md` (Original: wevoicereply)
- [ ] `.archive/staging/skills/gitlab-code-review_SKILL.md` (Original: gitlab-code-review)
- [ ] `.archive/staging/skills/dangdang_SKILL.md` (Original: dangdang)
- [ ] `.archive/staging/skills/jiandaoyun_SKILL.md` (Original: fenbi)
- [ ] `.archive/staging/skills/jinritoutiao_SKILL.md` (Original: jinritoutiao)
- [ ] `.archive/staging/skills/evomap-auto-maintainer_SKILL.md` (Original: evomap-auto-maintainer)
- [ ] `.archive/staging/skills/zhouyi-bazi_SKILL.md` (Original: zhouyi-bazi)
- [ ] `.archive/staging/skills/qingbo-search_SKILL.md` (Original: qingbo-search)
- [ ] `.archive/staging/skills/token-checker_SKILL.md` (Original: token-checker)
- [ ] `.archive/staging/skills/auto-create-skill_SKILL.md` (Original: auto-create-skill)
- [ ] `.archive/staging/skills/pre-sales-engineer-assistant_SKILL.md` (Original: pre-sales-engineer-assistant)
- [ ] `.archive/staging/skills/miliger-context-manager_SKILL.md` (Original: context-manager-v2)
- [ ] `.archive/staging/skills/image-content-extractor_SKILL.md` (Original: image-content-extractor)
- [ ] `.archive/staging/skills/interactive-card-reader_SKILL.md` (Original: interactive-card-reader)
- [ ] `.archive/staging/skills/miliger-clawhub-publisher_SKILL.md` (Original: miliger-clawhub-publisher)
- [ ] `.archive/staging/skills/miliger-playwright-scraper_SKILL.md` (Original: miliger-playwright-scraper)
- [ ] `.archive/staging/skills/miliger-qmd-manager_SKILL.md` (Original: miliger-qmd-manager)
- [ ] `.archive/staging/skills/openclaw-voice-skills_SKILL.md` (Original: openclaw-voice-skills)
- [ ] `.archive/staging/skills/talk-mode_SKILL.md` (Original: talk-mode)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
