# Extraction Task: 0500-extraction-skills-batch-074

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-074` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/tiktok-title-magic_SKILL.md` (Original: tiktok-title-magic)
- [ ] `.archive/staging/skills/token-contract-scanner_SKILL.md` (Original: token-contract-scanner)
- [ ] `.archive/staging/skills/weibo-trending-bot_SKILL.md` (Original: weibo-trending-bot)
- [ ] `.archive/staging/skills/whale-tracker_SKILL.md` (Original: whale-tracker)
- [ ] `.archive/staging/skills/youtube-shorts-tool_SKILL.md` (Original: youtube-shorts-tool)
- [ ] `.archive/staging/skills/youtube-title-optimizer_SKILL.md` (Original: youtube-title-optimizer)
- [ ] `.archive/staging/skills/cnki-advanced-search_SKILL.md` (Original: cnki-advanced-search)
- [ ] `.archive/staging/skills/qualitative-thematic-analysis_SKILL.md` (Original: qualitative-thematic-analysis)
- [ ] `.archive/staging/skills/tencentads-miaowen-qa_SKILL.md` (Original: tencentads-miaowen-qa)
- [ ] `.archive/staging/skills/rssh2_SKILL.md` (Original: rssh2)
- [ ] `.archive/staging/skills/junior-high-math-research-plans_SKILL.md` (Original: junior-high-math-research-plans)
- [ ] `.archive/staging/skills/express-tracking_SKILL.md` (Original: express-tracking)
- [ ] `.archive/staging/skills/document-processor_SKILL.md` (Original: document-processor)
- [ ] `.archive/staging/skills/academic-citation-manager_SKILL.md` (Original: academic-citation-manager)
- [ ] `.archive/staging/skills/yoyoalphax-zentao_SKILL.md` (Original: yoyoalphax-zentao)
- [ ] `.archive/staging/skills/asr-skill_SKILL.md` (Original: asr-skill)
- [ ] `.archive/staging/skills/qwen-asr-skill_SKILL.md` (Original: qwen-asr-skill)
- [ ] `.archive/staging/skills/clawdiligence_SKILL.md` (Original: clawdiligence)
- [ ] `.archive/staging/skills/the-origin-huan-ai-soul-thought-protocol_SKILL.md` (Original: the-origin-huan-ai-soul-thought-protocol)
- [ ] `.archive/staging/skills/weather-query-ych_SKILL.md` (Original: weather-query-ych)
- [ ] `.archive/staging/skills/social-push-semi_SKILL.md` (Original: social-push-semi)
- [ ] `.archive/staging/skills/twitter-watch-reply_SKILL.md` (Original: twitter-watch-reply)
- [ ] `.archive/staging/skills/ai-quant-trader_SKILL.md` (Original: ai-quant-trader)
- [ ] `.archive/staging/skills/fund-news-daily_SKILL.md` (Original: fund-news-daily)
- [ ] `.archive/staging/skills/password-generator_SKILL.md` (Original: password-generator)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
