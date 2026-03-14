# Extraction Task: 0500-extraction-skills-batch-054

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-054` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/code-detective_SKILL.md` (Original: code-detective)
- [ ] `.archive/staging/skills/football-english_SKILL.md` (Original: football-english)
- [ ] `.archive/staging/skills/quiz-battle_SKILL.md` (Original: quiz-battle)
- [ ] `.archive/staging/skills/accounts_SKILL.md` (Original: accounts)
- [ ] `.archive/staging/skills/affiliate-link_SKILL.md` (Original: affiliate-link)
- [ ] `.archive/staging/skills/affiliate-marketing_SKILL.md` (Original: affiliate-marketing)
- [ ] `.archive/staging/skills/analytics-tracker_SKILL.md` (Original: analytics-tracker)
- [ ] `.archive/staging/skills/arbitrage-bot_SKILL.md` (Original: arbitrage-bot)
- [ ] `.archive/staging/skills/auto-reply_SKILL.md` (Original: auto-reply)
- [ ] `.archive/staging/skills/autonomous-actions_SKILL.md` (Original: autonomous-actions)
- [ ] `.archive/staging/skills/bankr-trading_SKILL.md` (Original: bankr-trading)
- [ ] `.archive/staging/skills/business-automation_SKILL.md` (Original: business-automation)
- [ ] `.archive/staging/skills/code-docs-generator_SKILL.md` (Original: code-docs-generator)
- [ ] `.archive/staging/skills/code-review-pro_SKILL.md` (Original: code-review-pro)
- [ ] `.archive/staging/skills/content-ideas_SKILL.md` (Original: content-ideas)
- [ ] `.archive/staging/skills/course-creator_SKILL.md` (Original: course-creator)
- [ ] `.archive/staging/skills/creative-ideator_SKILL.md` (Original: creative-ideator)
- [ ] `.archive/staging/skills/daily-routine_SKILL.md` (Original: daily-routine)
- [ ] `.archive/staging/skills/defi-optimizer_SKILL.md` (Original: defi-optimizer)
- [ ] `.archive/staging/skills/dev-guidelines_SKILL.md` (Original: dev-guidelines)
- [ ] `.archive/staging/skills/digital-product-creator_SKILL.md` (Original: digital-product-creator)
- [ ] `.archive/staging/skills/email-manager_SKILL.md` (Original: email-manager)
- [ ] `.archive/staging/skills/email-marketing-copy_SKILL.md` (Original: email-marketing-copy)
- [ ] `.archive/staging/skills/emergency-response_SKILL.md` (Original: emergency-response)
- [ ] `.archive/staging/skills/engagement-helper_SKILL.md` (Original: engagement-helper)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
