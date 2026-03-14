# Extraction Task: 0500-extraction-skills-batch-052

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-052` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/internet-failure-analysis-expert_SKILL.md` (Original: internet-failure-analysis-expert)
- [ ] `.archive/staging/skills/chatskillproject_SKILL.md` (Original: chatskillproject)
- [ ] `.archive/staging/skills/qwtest1_SKILL.md` (Original: qwtest1)
- [ ] `.archive/staging/skills/system-time_SKILL.md` (Original: system-time)
- [ ] `.archive/staging/skills/a-stock-market_SKILL.md` (Original: a-stock-market)
- [ ] `.archive/staging/skills/status-web_SKILL.md` (Original: status-web)
- [ ] `.archive/staging/skills/first-principles-thinking-rabbot42_SKILL.md` (Original: first-principles-thinking-rabbot42)
- [ ] `.archive/staging/skills/skill-reviewer-rabbot42_SKILL.md` (Original: skill-reviewer-rabbot42)
- [ ] `.archive/staging/skills/raccoon-dataanalysis-skill_SKILL.md` (Original: raccoon-dataanalysis-skill)
- [ ] `.archive/staging/skills/official-feishu-toolkit_SKILL.md` (Original: official-feishu-toolkit)
- [ ] `.archive/staging/skills/dapianke_SKILL.md` (Original: dapianke)
- [ ] `.archive/staging/skills/pengyouquan-pangyu_SKILL.md` (Original: pengyouquan-pangyu)
- [ ] `.archive/staging/skills/pengyouquan_SKILL.md` (Original: pengyouquan)
- [ ] `.archive/staging/skills/skill-optimizer_SKILL.md` (Original: skill-optimizer)
- [ ] `.archive/staging/skills/self-evolving-agent_SKILL.md` (Original: self-evolving-agent)
- [ ] `.archive/staging/skills/suanming_SKILL.md` (Original: suanming)
- [ ] `.archive/staging/skills/coffee-prices_SKILL.md` (Original: coffee-prices)
- [ ] `.archive/staging/skills/xuyi_SKILL.md` (Original: xuyi)
- [ ] `.archive/staging/skills/fund-advisor_SKILL.md` (Original: fund-advisor)
- [ ] `.archive/staging/skills/dev-factory_SKILL.md` (Original: dev-factory)
- [ ] `.archive/staging/skills/security-news-feed_SKILL.md` (Original: security-news-feed)
- [ ] `.archive/staging/skills/seedance-3x3-optimizer_SKILL.md` (Original: seedance-3x3-optimizer)
- [ ] `.archive/staging/skills/elite-memory-skill_SKILL.md` (Original: elite-memory-skill)
- [ ] `.archive/staging/skills/xhs-enhancer_SKILL.md` (Original: xhs-enhancer)
- [ ] `.archive/staging/skills/suno-headless-skill_SKILL.md` (Original: suno-headless-skill)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
