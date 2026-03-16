# Extraction Task: 0500-extraction-skills-batch-045

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-045` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/tushare-stock-skill_SKILL.md` (Original: tushare-stock-skill)
- [ ] `.archive/staging/skills/novel-workshop_SKILL.md` (Original: novel-workshop)
- [ ] `.archive/staging/skills/maomao-weather_SKILL.md` (Original: maomao-weather)
- [ ] `.archive/staging/skills/prompt-injection-guard_SKILL.md` (Original: prompt-injection-guard)
- [ ] `.archive/staging/skills/zongjie_SKILL.md` (Original: zongjie)
- [ ] `.archive/staging/skills/memory-shrink_SKILL.md` (Original: memory-shrink)
- [ ] `.archive/staging/skills/auto-memory-distiller_SKILL.md` (Original: auto-memory-distiller)
- [ ] `.archive/staging/skills/crs-report-generator_SKILL.md` (Original: crs-report-generator)
- [ ] `.archive/staging/skills/subtitle-converter_SKILL.md` (Original: subtitle-converter)
- [ ] `.archive/staging/skills/skill-governance_SKILL.md` (Original: skill-governance)
- [ ] `.archive/staging/skills/workspace-health_SKILL.md` (Original: workspace-health)
- [ ] `.archive/staging/skills/food-safety-legal_SKILL.md` (Original: food-safety-legal)
- [ ] `.archive/staging/skills/gitlab-private_SKILL.md` (Original: gitlab-private)
- [ ] `.archive/staging/skills/report-writing-skills_SKILL.md` (Original: report-writing-skills)
- [ ] `.archive/staging/skills/clawhub-login_SKILL.md` (Original: clawhub-login)
- [ ] `.archive/staging/skills/image-to-pdf_SKILL.md` (Original: image-to-pdf)
- [ ] `.archive/staging/skills/suning-bangke-0311_SKILL.md` (Original: suning-bangke-0311)
- [ ] `.archive/staging/skills/investment-advisor_SKILL.md` (Original: investment-advisor)
- [ ] `.archive/staging/skills/server-monitor_SKILL.md` (Original: server-monitor)
- [ ] `.archive/staging/skills/openclaw-itsm-skill_SKILL.md` (Original: openclaw-itsm-skill)
- [ ] `.archive/staging/skills/dmn-default-mode-network_SKILL.md` (Original: dmn-default-mode-network)
- [ ] `.archive/staging/skills/meeting-note_SKILL.md` (Original: meeting-note)
- [ ] `.archive/staging/skills/self-evolve-agent_SKILL.md` (Original: self-evolve-agent)
- [ ] `.archive/staging/skills/vue-table-operation_SKILL.md` (Original: vue-table-operation)
- [ ] `.archive/staging/skills/bazi-pan_SKILL.md` (Original: bazi-pan)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
