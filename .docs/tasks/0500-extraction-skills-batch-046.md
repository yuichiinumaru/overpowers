# Extraction Task: 0500-extraction-skills-batch-046

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-046` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/daily-fengshui-attire_SKILL.md` (Original: daily-fengshui-attire)
- [ ] `.archive/staging/skills/daily-horoscope_SKILL.md` (Original: daily-horoscope)
- [ ] `.archive/staging/skills/jiugong-feixing_SKILL.md` (Original: jiugong-feixing)
- [ ] `.archive/staging/skills/lucky-day_SKILL.md` (Original: lucky-day)
- [ ] `.archive/staging/skills/meihua-yijing_SKILL.md` (Original: meihua-yijing)
- [ ] `.archive/staging/skills/swagger-skill_SKILL.md` (Original: swagger-skill)
- [ ] `.archive/staging/skills/funpay-assistant_SKILL.md` (Original: funpay-assistant)
- [ ] `.archive/staging/skills/team-manager_SKILL.md` (Original: team-manager)
- [ ] `.archive/staging/skills/xiaohongshu-ops-lobster_SKILL.md` (Original: xiaohongshu-ops-lobster)
- [ ] `.archive/staging/skills/mjzj-article_SKILL.md` (Original: mjzj-article)
- [ ] `.archive/staging/skills/mjzj-msg_SKILL.md` (Original: mjzj-msg)
- [ ] `.archive/staging/skills/mjzj-sp_SKILL.md` (Original: mjzj-sp)
- [ ] `.archive/staging/skills/bilibili-messager_SKILL.md` (Original: bilibili-messager)
- [ ] `.archive/staging/skills/douyin-messager_SKILL.md` (Original: douyin-messager)
- [ ] `.archive/staging/skills/skill-manager-all-in-one_SKILL.md` (Original: skill-manager-all-in-one)
- [ ] `.archive/staging/skills/idea2mvp_SKILL.md` (Original: idea2mvp)
- [ ] `.archive/staging/skills/ai-research-analyst_SKILL.md` (Original: ai-research-analyst)
- [ ] `.archive/staging/skills/binance-grid-trading_SKILL.md` (Original: binance-copy-trading)
- [ ] `.archive/staging/skills/binance-triangular-arbitrage_SKILL.md` (Original: binance-futures-trading)
- [ ] `.archive/staging/skills/binance-trading-bot_SKILL.md` (Original: binance-trading-bot)
- [ ] `.archive/staging/skills/cryptocom-trading-bot_SKILL.md` (Original: cryptocom-trading-bot)
- [ ] `.archive/staging/skills/novel-to-drama-script_SKILL.md` (Original: novel-to-drama-script)
- [ ] `.archive/staging/skills/polymarket-data-collector_SKILL.md` (Original: polymarket-arbitrage-finder)
- [ ] `.archive/staging/skills/polymarket-whale-movement_SKILL.md` (Original: polymarket-whale-movement)
- [ ] `.archive/staging/skills/stock-screener_SKILL.md` (Original: stock-quote-fetcher)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
