# Extraction Task: 0500-extraction-skills-batch-073

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-073` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/ai-market-research_SKILL.md` (Original: ai-market-research)
- [ ] `.archive/staging/skills/ai-seo-optimizer_SKILL.md` (Original: ai-seo-optimizer)
- [ ] `.archive/staging/skills/airdrop-checker_SKILL.md` (Original: airdrop-checker)
- [ ] `.archive/staging/skills/amazon-fba-calculator_SKILL.md` (Original: amazon-fba-calculator)
- [ ] `.archive/staging/skills/amazon-niche-finder_SKILL.md` (Original: amazon-niche-finder)
- [ ] `.archive/staging/skills/amazon-ppc-optimizer_SKILL.md` (Original: amazon-ppc-optimizer)
- [ ] `.archive/staging/skills/crypto-lending-optimizer_SKILL.md` (Original: crypto-lending-optimizer)
- [ ] `.archive/staging/skills/crypto-portfolio-optimizer_SKILL.md` (Original: crypto-portfolio-optimizer)
- [ ] `.archive/staging/skills/crypto-sentiment-analyzer_SKILL.md` (Original: crypto-sentiment-analyzer)
- [ ] `.archive/staging/skills/crypto-whale-alert-elite_SKILL.md` (Original: crypto-whale-alert-elite)
- [ ] `.archive/staging/skills/daily-briefing-pay_SKILL.md` (Original: daily-briefing-pay)
- [ ] `.archive/staging/skills/ecommerce-image-optimizer_SKILL.md` (Original: ecommerce-image-optimizer)
- [ ] `.archive/staging/skills/headline-magic_SKILL.md` (Original: headline-magic)
- [ ] `.archive/staging/skills/instagram-reels-analyzer_SKILL.md` (Original: instagram-reels-analyzer)
- [ ] `.archive/staging/skills/meme-safe-scanner_SKILL.md` (Original: meme-safe-scanner)
- [ ] `.archive/staging/skills/memecoin-launch-monitor-pro_SKILL.md` (Original: memecoin-launch-monitor-pro)
- [ ] `.archive/staging/skills/nft-floor-monitor_SKILL.md` (Original: nft-floor-monitor)
- [ ] `.archive/staging/skills/nft-sniper-bot-pro_SKILL.md` (Original: nft-sniper-bot-pro)
- [ ] `.archive/staging/skills/onchain-audit_SKILL.md` (Original: onchain-audit)
- [ ] `.archive/staging/skills/password-generator-pay_SKILL.md` (Original: password-generator-pay)
- [ ] `.archive/staging/skills/perplexica-search_SKILL.md` (Original: perplexica-search)
- [ ] `.archive/staging/skills/prompt-polisher_SKILL.md` (Original: prompt-polisher)
- [ ] `.archive/staging/skills/revenue-monitor-pay_SKILL.md` (Original: revenue-monitor-pay)
- [ ] `.archive/staging/skills/seo-checker_SKILL.md` (Original: seo-checker)
- [ ] `.archive/staging/skills/staking-reward-tracker-pro_SKILL.md` (Original: staking-reward-tracker-pro)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
