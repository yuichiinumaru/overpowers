# Extraction Task: 0500-extraction-skills-batch-064

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-064` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/openclaw-behavior-plan_SKILL.md` (Original: openclaw-behavior-plan)
- [ ] `.archive/staging/skills/wechat-article-pro_SKILL.md` (Original: wechat-article-pro)
- [ ] `.archive/staging/skills/context-guard_SKILL.md` (Original: context-guard)
- [ ] `.archive/staging/skills/food-expiry-reminder_SKILL.md` (Original: food-expiry-reminder)
- [ ] `.archive/staging/skills/zeelin-search-gsdata-es-bigdata_SKILL.md` (Original: zeelin-search-gsdata-es-bigdata)
- [ ] `.archive/staging/skills/call-geo-agent_SKILL.md` (Original: call-geo-agent)
- [ ] `.archive/staging/skills/bundle-deal-copy_SKILL.md` (Original: bundle-deal-copy)
- [ ] `.archive/staging/skills/faq-generator_SKILL.md` (Original: faq-generator)
- [ ] `.archive/staging/skills/father-day_SKILL.md` (Original: father-day)
- [ ] `.archive/staging/skills/gift-message_SKILL.md` (Original: gift-message)
- [ ] `.archive/staging/skills/holiday-marketing_SKILL.md` (Original: holiday-marketing)
- [ ] `.archive/staging/skills/inventory-clearance_SKILL.md` (Original: inventory-clearance)
- [ ] `.archive/staging/skills/new-product-launch_SKILL.md` (Original: new-product-launch)
- [ ] `.archive/staging/skills/product-video-script_SKILL.md` (Original: product-comparison)
- [ ] `.archive/staging/skills/product-title-optimizer_SKILL.md` (Original: product-title-optimizer)
- [ ] `.archive/staging/skills/promotion-copywriter_SKILL.md` (Original: promotion-copywriter)
- [ ] `.archive/staging/skills/shipping-policy_SKILL.md` (Original: shipping-policy)
- [ ] `.archive/staging/skills/usage-scenario_SKILL.md` (Original: usage-scenario)
- [ ] `.archive/staging/skills/kr-document-reviewer_SKILL.md` (Original: kr-document-reviewer)
- [ ] `.archive/staging/skills/ai-phone-calls-steponeai_SKILL.md` (Original: ai-phone-calls-steponeai)
- [ ] `.archive/staging/skills/chinese-toolkit_SKILL.md` (Original: chinese-toolkit)
- [ ] `.archive/staging/skills/download-organizer_SKILL.md` (Original: download-organizer)
- [ ] `.archive/staging/skills/file-sorter_SKILL.md` (Original: file-sorter)
- [ ] `.archive/staging/skills/music-tagger_SKILL.md` (Original: music-tagger)
- [ ] `.archive/staging/skills/ai-app-lab_SKILL.md` (Original: ai-app-lab)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
