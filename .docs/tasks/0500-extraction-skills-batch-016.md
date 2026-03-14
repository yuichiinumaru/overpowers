# Extraction Task: 0500-extraction-skills-batch-016

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-016` to execute this task or follow these manual steps for each item:

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

- [x] `.archive/staging/skills/tavily-search-darry_SKILL.md` (Original: tavily-search-darry)
- [x] `.archive/staging/skills/bilibili-subtitle-download-skill_SKILL.md` (Original: bilibili-subtitle-download-skill)
- [x] `.archive/staging/skills/github-memory-sync_SKILL.md` (Original: github-memory-sync)
- [x] `.archive/staging/skills/wecom-calendar_SKILL.md` (Original: wecom-calendar)
- [ ] `.archive/staging/skills/task-experience-logger_SKILL.md` (Original: task-experience-logger)
- [ ] `.archive/staging/skills/okr_SKILL.md` (Original: okr)
- [ ] `.archive/staging/skills/hiskill_SKILL.md` (Original: hiskill)
- [ ] `.archive/staging/skills/siyuan-skill_SKILL.md` (Original: siyuan-skill)
- [x] `.archive/staging/skills/commands_pregnancy.md` (Original: commands)
- [x] `.archive/staging/skills/airdrop-hunter_SKILL.md` (Original: airdrop-hunter)
- [x] `.archive/staging/skills/arbitrage-scanner_SKILL.md` (Original: arbitrage-scanner)
- [x] `.archive/staging/skills/crypto-price-checker_SKILL.md` (Original: crypto-price-checker)
- [x] `.archive/staging/skills/defi-yield-finder_SKILL.md` (Original: defi-yield-finder)
- [Skipped] `.archive/staging/skills/market-sentiment_SKILL.md` (Original: market-sentiment)
- [x] `.archive/staging/skills/meme-detector_SKILL.md` (Original: meme-detector)
- [x] `.archive/staging/skills/nft-mint-monitor_SKILL.md` (Original: nft-mint-monitor)
- [ ] `.archive/staging/skills/nft-valuator_SKILL.md` (Original: nft-valuator)
- [ ] `.archive/staging/skills/token-sniper_SKILL.md` (Original: token-sniper)
- [ ] `.archive/staging/skills/tx-decoder_SKILL.md` (Original: tx-decoder)
- [ ] `.archive/staging/skills/whale-alert_SKILL.md` (Original: whale-alert)
- [ ] `.archive/staging/skills/weather-20_SKILL.md` (Original: weather-20)
- [ ] `.archive/staging/skills/feishu-upload-skill_SKILL.md` (Original: feishu-upload-skill)
- [ ] `.archive/staging/skills/bing-search-cn_SKILL.md` (Original: bing-search-cn)
- [ ] `.archive/staging/skills/kuro-self-reflection_SKILL.md` (Original: kuro-self-reflection)
- [ ] `.archive/staging/skills/mteam-transmission0-1_SKILL.md` (Original: mteam-transmission0-1)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
