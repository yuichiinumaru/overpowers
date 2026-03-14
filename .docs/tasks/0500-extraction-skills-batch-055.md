# Extraction Task: 0500-extraction-skills-batch-055

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-055` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/failure-analyzer_SKILL.md` (Original: failure-analyzer)
- [ ] `.archive/staging/skills/fiverr-seller_SKILL.md` (Original: fiverr-seller)
- [ ] `.archive/staging/skills/gumroad-seller_SKILL.md` (Original: gumroad-seller)
- [ ] `.archive/staging/skills/human-negotiator_SKILL.md` (Original: human-negotiator)
- [ ] `.archive/staging/skills/human-security_SKILL.md` (Original: human-security)
- [ ] `.archive/staging/skills/instagram-poster_SKILL.md` (Original: instagram-poster)
- [ ] `.archive/staging/skills/learning-engine_SKILL.md` (Original: learning-engine)
- [ ] `.archive/staging/skills/linkedin-poster_SKILL.md` (Original: linkedin-poster)
- [ ] `.archive/staging/skills/medium-writer_SKILL.md` (Original: medium-writer)
- [ ] `.archive/staging/skills/metamask-wallet_SKILL.md` (Original: metamask-wallet)
- [ ] `.archive/staging/skills/moltbook-negotiator_SKILL.md` (Original: moltbook-negotiator)
- [ ] `.archive/staging/skills/moltbook-optimizer_SKILL.md` (Original: moltbook-optimizer)
- [ ] `.archive/staging/skills/moltbook-security_SKILL.md` (Original: moltbook-security)
- [ ] `.archive/staging/skills/natural-conversation_SKILL.md` (Original: natural-conversation)
- [ ] `.archive/staging/skills/note-writer_SKILL.md` (Original: note-writer)
- [ ] `.archive/staging/skills/podcast-creator_SKILL.md` (Original: podcast-creator)
- [ ] `.archive/staging/skills/product-image-generator_SKILL.md` (Original: product-image-generator)
- [ ] `.archive/staging/skills/prompt-seller_SKILL.md` (Original: prompt-seller)
- [ ] `.archive/staging/skills/quality-checker_SKILL.md` (Original: quality-checker)
- [ ] `.archive/staging/skills/quality-gate_SKILL.md` (Original: quality-gate)
- [ ] `.archive/staging/skills/reddit-poster_SKILL.md` (Original: reddit-poster)
- [ ] `.archive/staging/skills/resources_SKILL.md` (Original: resources)
- [ ] `.archive/staging/skills/revenue-ideator_SKILL.md` (Original: revenue-ideator)
- [ ] `.archive/staging/skills/rey-clawhub-publisher_SKILL.md` (Original: rey-clawhub-publisher)
- [ ] `.archive/staging/skills/rey-deep-research_SKILL.md` (Original: rey-deep-research)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
