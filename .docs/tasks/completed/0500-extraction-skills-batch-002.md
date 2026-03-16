# Extraction Task: 0500-extraction-skills-batch-002

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-002` to execute this task or follow these manual steps for each item:

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

- [x] `.archive/staging/skills/autonomous-loops_SKILL.md` (Original: autonomous-loops)
- [x] `.archive/staging/skills/clickhouse-io_SKILL.md` (Original: clickhouse-io)
- [x] `.archive/staging/skills/content-engine_SKILL.md` (Original: content-engine)
- [x] `.archive/staging/skills/content-hash-cache-pattern_SKILL.md` (Original: content-hash-cache-pattern)
- [x] `.archive/staging/skills/cost-aware-llm-pipeline_SKILL.md` (Original: cost-aware-llm-pipeline)
- [x] `.archive/staging/skills/cpp-coding-standards_SKILL.md` (Original: cpp-coding-standards)
- [x] `.archive/staging/skills/database-migrations_SKILL.md` (Original: database-migrations)
- [x] `.archive/staging/skills/deployment-patterns_SKILL.md` (Original: deployment-patterns)
- [x] `.archive/staging/skills/enterprise-agent-ops_SKILL.md` (Original: enterprise-agent-ops)
- [x] `.archive/staging/skills/foundation-models-on-device_SKILL.md` (Original: foundation-models-on-device)
- [x] `.archive/staging/skills/frontend-slides_SKILL.md` (Original: frontend-slides)
- [x] `.archive/staging/skills/investor-materials_SKILL.md` (Original: investor-materials)
- [x] `.archive/staging/skills/investor-outreach_SKILL.md` (Original: investor-outreach)
- [x] `.archive/staging/skills/liquid-glass-design_SKILL.md` (Original: liquid-glass-design)
- [x] `.archive/staging/skills/market-research_SKILL.md` (Original: market-research)
- [x] `.archive/staging/skills/nanoclaw-repl_SKILL.md` (Original: nanoclaw-repl)
- [x] `.archive/staging/skills/plankton-code-quality_SKILL.md` (Original: plankton-code-quality)
- [x] `.archive/staging/skills/ralphinho-rfc-pipeline_SKILL.md` (Original: ralphinho-rfc-pipeline)
- [x] `.archive/staging/skills/regex-vs-llm-structured-text_SKILL.md` (Original: regex-vs-llm-structured-text)
- [x] `.archive/staging/skills/skill-stocktake_SKILL.md` (Original: skill-stocktake)
- [x] `.archive/staging/skills/swift-concurrency-6-2_SKILL.md` (Original: swift-concurrency-6-2)
- [x] `.archive/staging/skills/swiftui-patterns_SKILL.md` (Original: swiftui-patterns)
- [x] `.archive/staging/skills/visa-doc-translate_SKILL.md` (Original: visa-doc-translate)
- [x] `.archive/staging/skills/aionui-webui-setup_SKILL.md` (Original: aionui-webui-setup)
- [x] `.archive/staging/skills/openclaw-setup_SKILL.md` (Original: openclaw-setup)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
