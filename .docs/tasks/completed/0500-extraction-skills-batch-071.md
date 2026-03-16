# Extraction Task: 0500-extraction-skills-batch-071

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-071` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/word-reader_SKILL.md` (Original: word-reader)
- [ ] `.archive/staging/skills/requirements-analysis_SKILL.md` (Original: requirements-analysis)
- [ ] `.archive/staging/skills/check-chinese-holiday_SKILL.md` (Original: check-chinese-holiday)
- [ ] `.archive/staging/skills/cover-letter_SKILL.md` (Original: cover-letter)
- [ ] `.archive/staging/skills/requirements-analyzer_SKILL.md` (Original: requirements-analyzer)
- [ ] `.archive/staging/skills/openclaw-reportstudio-community_SKILL.md` (Original: openclaw-reportstudio-community)
- [ ] `.archive/staging/skills/generic-mail-client_SKILL.md` (Original: generic-mail-client)
- [ ] `.archive/staging/skills/crypto-news_SKILL.md` (Original: crypto-news)
- [ ] `.archive/staging/skills/claw-prompt-injection-guard_SKILL.md` (Original: claw-prompt-injection-guard)
- [ ] `.archive/staging/skills/xtrade-futu-paper-trade_SKILL.md` (Original: xtrade-futu-paper-trade)
- [ ] `.archive/staging/skills/linkfoxai_SKILL.md` (Original: linkfoxai)
- [ ] `.archive/staging/skills/gofilshsearcher_SKILL.md` (Original: gofilshsearcher)
- [ ] `.archive/staging/skills/the-best-planner_SKILL.md` (Original: the-best-planner)
- [ ] `.archive/staging/skills/xianyufilter_SKILL.md` (Original: xianyufilter)
- [ ] `.archive/staging/skills/opportunity-assessment_SKILL.md` (Original: opportunity-assessment)
- [ ] `.archive/staging/skills/requirement-assessment_SKILL.md` (Original: requirement-assessment)
- [ ] `.archive/staging/skills/ai-side-hustle-agent_SKILL.md` (Original: ai-side-hustle-agent)
- [ ] `.archive/staging/skills/clawmart-auto-invoice_SKILL.md` (Original: clawmart-auto-invoice)
- [ ] `.archive/staging/skills/clawmart-customer-insights_SKILL.md` (Original: clawmart-customer-insights)
- [ ] `.archive/staging/skills/clawmart-quick-proposal_SKILL.md` (Original: clawmart-quick-proposal)
- [ ] `.archive/staging/skills/content-analytics_SKILL.md` (Original: content-analytics)
- [ ] `.archive/staging/skills/git-commit-helper_SKILL.md` (Original: git-commit-helper)
- [ ] `.archive/staging/skills/openclaw-setup-service_SKILL.md` (Original: openclaw-setup-service)
- [ ] `.archive/staging/skills/quick-proposal_SKILL.md` (Original: quick-proposal)
- [ ] `.archive/staging/skills/quick-translation_SKILL.md` (Original: quick-translation)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
