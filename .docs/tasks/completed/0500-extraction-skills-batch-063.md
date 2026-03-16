# Extraction Task: 0500-extraction-skills-batch-063

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-063` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/portfolio-management_SKILL.md` (Original: portfolio-management)
- [ ] `.archive/staging/skills/eng-vocab-for-11yrold_SKILL.md` (Original: eng-vocab-for-11yrold)
- [ ] `.archive/staging/skills/caiyun-weather-skill_SKILL.md` (Original: caiyun-weather-skill)
- [ ] `.archive/staging/skills/stock-price-query_SKILL.md` (Original: stock-price-query)
- [ ] `.archive/staging/skills/code-review1_SKILL.md` (Original: code-review1)
- [ ] `.archive/staging/skills/double-check-article_SKILL.md` (Original: double-check-article)
- [ ] `.archive/staging/skills/agent-dev-toolkit_SKILL.md` (Original: agent-dev-toolkit)
- [ ] `.archive/staging/skills/chat-history_SKILL.md` (Original: chat-history)
- [ ] `.archive/staging/skills/knowledge-spider_SKILL.md` (Original: knowledge-spider)
- [ ] `.archive/staging/skills/multimodal_SKILL.md` (Original: multimodal)
- [ ] `.archive/staging/skills/subtitle-refiner_SKILL.md` (Original: subtitle-refiner)
- [ ] `.archive/staging/skills/github-repo-mirror_SKILL.md` (Original: github-repo-mirror)
- [ ] `.archive/staging/skills/trylife-hello_SKILL.md` (Original: trylife-hello)
- [ ] `.archive/staging/skills/code-project-analyzer_SKILL.md` (Original: code-project-analyzer)
- [ ] `.archive/staging/skills/stock-research-engine_SKILL.md` (Original: stock-research-engine)
- [ ] `.archive/staging/skills/longgang-job-hunter_SKILL.md` (Original: longgang-job-hunter)
- [ ] `.archive/staging/skills/bot-mood-share_SKILL.md` (Original: bot-mood-share)
- [ ] `.archive/staging/skills/clawhub-skill-publishing-guide_SKILL.md` (Original: clawhub-skill-publishing-guide)
- [ ] `.archive/staging/skills/videotranscript_SKILL.md` (Original: videotranscript)
- [ ] `.archive/staging/skills/patent-assistant_SKILL.md` (Original: patent-assistant)
- [ ] `.archive/staging/skills/privacy-eraser_SKILL.md` (Original: privacy-eraser)
- [ ] `.archive/staging/skills/crypto-kline-data_SKILL.md` (Original: crypto-kline-data)
- [ ] `.archive/staging/skills/crypto-kline-okx_SKILL.md` (Original: crypto-kline-okx)
- [ ] `.archive/staging/skills/uctoo-api-skill_SKILL.md` (Original: uctoo-api-skill)
- [ ] `.archive/staging/skills/remnawave-account-creator_SKILL.md` (Original: remnawave-account-creator)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
