# Extraction Task: 0500-extraction-skills-batch-065

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-065` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/vefaas-browser-use_SKILL.md` (Original: vefaas-browser-use)
- [ ] `.archive/staging/skills/liuliu-proactive-agent_SKILL.md` (Original: liuliu-proactive-agent)
- [ ] `.archive/staging/skills/novel-writer_SKILL.md` (Original: novel-writer)
- [ ] `.archive/staging/skills/scenario-analyzer_SKILL.md` (Original: scenario-analyzer)
- [ ] `.archive/staging/skills/stanley-druckenmiller-investment_SKILL.md` (Original: stanley-druckenmiller-investment)
- [ ] `.archive/staging/skills/realmrouter-switch_SKILL.md` (Original: realmrouter-switch)
- [ ] `.archive/staging/skills/ai-news_SKILL.md` (Original: ai-news)
- [ ] `.archive/staging/skills/postgres-mcp-skills_SKILL.md` (Original: postgres-mcp-skills)
- [ ] `.archive/staging/skills/pg-execute_SKILL.md` (Original: pg-execute)
- [ ] `.archive/staging/skills/pg-health_SKILL.md` (Original: pg-health)
- [ ] `.archive/staging/skills/pg-query-plan_SKILL.md` (Original: pg-query-plan)
- [ ] `.archive/staging/skills/setup-postgres-mcp_SKILL.md` (Original: setup-postgres-mcp)
- [ ] `.archive/staging/skills/family-chef-cn_SKILL.md` (Original: family-chef-cn)
- [ ] `.archive/staging/skills/glab-config_SKILL.md` (Original: glab-config)
- [ ] `.archive/staging/skills/unifuncs-search_SKILL.md` (Original: unifuncs-search)
- [ ] `.archive/staging/skills/china-holiday_SKILL.md` (Original: china-holiday)
- [ ] `.archive/staging/skills/stock-recommend_SKILL.md` (Original: stock-recommend)
- [ ] `.archive/staging/skills/academic-survey-self-improve_SKILL.md` (Original: academic-survey-self-improve)
- [ ] `.archive/staging/skills/my-system-info-skill_SKILL.md` (Original: my-system-info-skill)
- [ ] `.archive/staging/skills/russian-uncensored_SKILL.md` (Original: russian-uncensored)
- [ ] `.archive/staging/skills/flash-redeem-knight_SKILL.md` (Original: flash-redeem-knight)
- [ ] `.archive/staging/skills/team-dispatch_SKILL.md` (Original: team-dispatch)
- [ ] `.archive/staging/skills/feishu-project-connector-bytedance-internal_SKILL.md` (Original: feishu-project-connector-bytedance-internal)
- [ ] `.archive/staging/skills/bmap-jsapi-gl_SKILL.md` (Original: bmap-jsapi-gl)
- [ ] `.archive/staging/skills/jsapi-ui-kit_SKILL.md` (Original: jsapi-ui-kit)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
