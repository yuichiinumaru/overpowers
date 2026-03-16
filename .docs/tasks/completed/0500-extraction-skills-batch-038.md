# Extraction Task: 0500-extraction-skills-batch-038

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-038` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/tapd_SKILL.md` (Original: tapd)
- [ ] `.archive/staging/skills/cnki-exp-search-automation_SKILL.md` (Original: cnki-exp-search-automation)
- [ ] `.archive/staging/skills/joplin-cli_SKILL.md` (Original: joplin-cli)
- [ ] `.archive/staging/skills/xiaohongshu-writing_SKILL.md` (Original: xiaohongshu-writing)
- [ ] `.archive/staging/skills/sdd_SKILL.md` (Original: sdd)
- [ ] `.archive/staging/skills/amber-electric-pro_SKILL.md` (Original: amber-electric-pro)
- [ ] `.archive/staging/skills/yoebao-bazi_SKILL.md` (Original: yoebao-bazi)
- [ ] `.archive/staging/skills/yoebao-yao_SKILL.md` (Original: yoebao-yao)
- [ ] `.archive/staging/skills/investment-post-management-report-updater_SKILL.md` (Original: investment-post-management-report-updater)
- [ ] `.archive/staging/skills/feishu-image-messaging_SKILL.md` (Original: feishu-image-messaging)
- [ ] `.archive/staging/skills/playwright-testing_SKILL.md` (Original: anti-slop-design)
- [ ] `.archive/staging/skills/game-design_SKILL.md` (Original: game-design)
- [ ] `.archive/staging/skills/game-marketing_SKILL.md` (Original: game-marketing)
- [ ] `.archive/staging/skills/kj-parallel-agents_SKILL.md` (Original: kj-parallel-agents)
- [ ] `.archive/staging/skills/kj-ralph-loop_SKILL.md` (Original: kj-ralph-loop)
- [ ] `.archive/staging/skills/skill-authoring_SKILL.md` (Original: skill-authoring)
- [ ] `.archive/staging/skills/systematic-debugging_SKILL.md` (Original: systematic-debugging)
- [ ] `.archive/staging/skills/tdd-discipline_SKILL.md` (Original: tdd-discipline)
- [ ] `.archive/staging/skills/verify-before-done_SKILL.md` (Original: verify-before-done)
- [ ] `.archive/staging/skills/ollama-memory_SKILL.md` (Original: ollama-memory)
- [ ] `.archive/staging/skills/claw-desktop-pet_SKILL.md` (Original: claw-desktop-pet)
- [ ] `.archive/staging/skills/story-chain-multiverse_SKILL.md` (Original: story-chain-multiverse)
- [ ] `.archive/staging/skills/openclaw-relation_SKILL.md` (Original: openclaw-relation)
- [ ] `.archive/staging/skills/mv-pipeline_SKILL.md` (Original: mv-pipeline)
- [ ] `.archive/staging/skills/compliance-check_SKILL.md` (Original: compliance-check)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
