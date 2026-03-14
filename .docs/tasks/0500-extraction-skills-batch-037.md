# Extraction Task: 0500-extraction-skills-batch-037

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-037` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/image-compress_SKILL.md` (Original: image-compress)
- [ ] `.archive/staging/skills/rembg_SKILL.md` (Original: rembg)
- [ ] `.archive/staging/skills/file-reader_SKILL.md` (Original: file-reader)
- [ ] `.archive/staging/skills/kz-tax-code_SKILL.md` (Original: kz-tax-code)
- [ ] `.archive/staging/skills/x-manual-surf-notes_SKILL.md` (Original: x-manual-surf-notes)
- [ ] `.archive/staging/skills/reshape-your-life_SKILL.md` (Original: reshape-your-life)
- [ ] `.archive/staging/skills/iqc-python-tree_SKILL.md` (Original: iqc-python-tree)
- [ ] `.archive/staging/skills/dtek-light_SKILL.md` (Original: dtek-light)
- [ ] `.archive/staging/skills/rent_SKILL.md` (Original: rent)
- [ ] `.archive/staging/skills/stock-insight_SKILL.md` (Original: stock-insight)
- [ ] `.archive/staging/skills/crypto-research-assistant_SKILL.md` (Original: crypto-research-assistant)
- [ ] `.archive/staging/skills/crypto-trading-bot_SKILL.md` (Original: crypto-trading-bot)
- [ ] `.archive/staging/skills/weibo-hot-search-anonymous_SKILL.md` (Original: weibo-hot-search-anonymous)
- [ ] `.archive/staging/skills/paradiz_SKILL.md` (Original: paradiz)
- [ ] `.archive/staging/skills/auto-ppt_SKILL.md` (Original: auto-ppt)
- [ ] `.archive/staging/skills/twitter-web-autopost_SKILL.md` (Original: twitter-web-autopost)
- [ ] `.archive/staging/skills/zeelin-twitter-web-autopost_SKILL.md` (Original: zeelin-twitter-web-autopost)
- [ ] `.archive/staging/skills/budget-intel_SKILL.md` (Original: budget-intel)
- [ ] `.archive/staging/skills/narrative-voice_SKILL.md` (Original: narrative-voice)
- [ ] `.archive/staging/skills/sales-oratory-master_SKILL.md` (Original: sales-oratory-master)
- [ ] `.archive/staging/skills/weekly-skills-update_SKILL.md` (Original: weekly-skills-update)
- [ ] `.archive/staging/skills/weather-zh_SKILL.md` (Original: weather-cn)
- [ ] `.archive/staging/skills/ai-news-collectors_SKILL.md` (Original: ai-news-collectors)
- [ ] `.archive/staging/skills/ai-news-pusher_SKILL.md` (Original: ai-news-pusher)
- [ ] `.archive/staging/skills/ai-research-scraper_SKILL.md` (Original: ai-research-scraper)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
