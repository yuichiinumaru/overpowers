# Extraction Task: 0500-extraction-skills-batch-004

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-004` to execute this task or follow these manual steps for each item:

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

- [x] `.archive/staging/skills/openclawmp_SKILL.md` (Original: openclawmp)
- [x] `.archive/staging/skills/alarm-memo-assistant-pro_SKILL.md` (Original: alarm-memo-assistant-pro)
- [x] `.archive/staging/skills/claim-risk-auditor_SKILL.md` (Original: claim-risk-auditor)
- [x] `.archive/staging/skills/ecommerce-customer-service-pro_SKILL.md` (Original: ecommerce-customer-service-pro)
- [x] `.archive/staging/skills/fortune-master-pro_SKILL.md` (Original: fortune-master-pro)
- [x] `.archive/staging/skills/paper-assistant_SKILL.md` (Original: paper-assistant)
- [x] `.archive/staging/skills/reply-coach_SKILL.md` (Original: reply-coach)
- [x] `.archive/staging/skills/reviewer-rebuttal-coach_SKILL.md` (Original: reviewer-rebuttal-coach)
- [x] `.archive/staging/skills/rubric-gap-analyzer_SKILL.md` (Original: rubric-gap-analyzer)
- [x] `.archive/staging/skills/text-game-arcade-universe-v3_SKILL.md` (Original: text-game-arcade-universe-v3)
- [x] `.archive/staging/skills/clawlet_SKILL.md` (Original: clawlet)
- [x] `.archive/staging/skills/librag-knowledge-recall_SKILL.md` (Original: librag-knowledge-recall)
- [x] `.archive/staging/skills/alpha-pulse_SKILL.md` (Original: alpha-pulse)
- [x] `.archive/staging/skills/quant_SKILL.md` (Original: quant)
- [x] `.archive/staging/skills/agent-group_SKILL.md` (Original: agent-group)
- [x] `.archive/staging/skills/cloud-local-bridge_SKILL.md` (Original: cloud-local-bridge)
- [x] `.archive/staging/skills/wechat-article-reader_SKILL.md` (Original: wechat-article-reader)
- [x] `.archive/staging/skills/evomap-auto-task-publish-1-1-0_SKILL.md` (Original: evomap-auto-task-publish-1-1-0)
- [x] `.archive/staging/skills/self-evolving-skill-1-0-2_SKILL.md` (Original: self-evolving-skill-1-0-2)
- [x] `.archive/staging/skills/teacher-prep_SKILL.md` (Original: teacher-prep)
- [x] `.archive/staging/skills/agent-connect_SKILL.md` (Original: agent-connect)
- [x] `.archive/staging/skills/car-recommender_SKILL.md` (Original: car-recommender)
- [x] `.archive/staging/skills/plan-c_SKILL.md` (Original: plan-c)
- [x] `.archive/staging/skills/ts-interface-miner_SKILL.md` (Original: ts-interface-miner)
- [x] `.archive/staging/skills/code-quality-analyzer_SKILL.md` (Original: code-quality-analyzer)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
