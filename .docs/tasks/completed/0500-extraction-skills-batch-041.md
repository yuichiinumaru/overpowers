# Extraction Task: 0500-extraction-skills-batch-041

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-041` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/youdaonote-news_SKILL.md` (Original: youdaonote-news)
- [ ] `.archive/staging/skills/feyman-coach_SKILL.md` (Original: feyman-coach)
- [ ] `.archive/staging/skills/tencentcloud-lighthouse-skill_SKILL.md` (Original: tencentcloud-lighthouse-skill)
- [ ] `.archive/staging/skills/market-insight-claude-skill_SKILL.md` (Original: market-insight-claude-skill)
- [ ] `.archive/staging/skills/barkpush_SKILL.md` (Original: barkpush)
- [ ] `.archive/staging/skills/issuefinder-tool_SKILL.md` (Original: issuefinder-tool)
- [ ] `.archive/staging/skills/tushare-data_SKILL.md` (Original: tushare-data)
- [ ] `.archive/staging/skills/hz-error-guard_SKILL.md` (Original: hz-error-guard)
- [ ] `.archive/staging/skills/xhs-content-generate_SKILL.md` (Original: xhs-content-generate)
- [ ] `.archive/staging/skills/kakaotalk_SKILL.md` (Original: kakaotalk)
- [ ] `.archive/staging/skills/korean-gov-programs_SKILL.md` (Original: korean-gov-programs)
- [ ] `.archive/staging/skills/openclaw-cache-kit_SKILL.md` (Original: openclaw-cache-kit)
- [ ] `.archive/staging/skills/realtime-interact-overlay_SKILL.md` (Original: realtime-interact-overlay)
- [ ] `.archive/staging/skills/hitem3d_SKILL.md` (Original: hitem3d)
- [ ] `.archive/staging/skills/solana-alerts_SKILL.md` (Original: solana-alerts)
- [ ] `.archive/staging/skills/solana-dca_SKILL.md` (Original: solana-dca)
- [ ] `.archive/staging/skills/solana-investor_SKILL.md` (Original: solana-investor)
- [ ] `.archive/staging/skills/solana-market_SKILL.md` (Original: solana-market)
- [ ] `.archive/staging/skills/solana-portfolio_SKILL.md` (Original: solana-portfolio)
- [ ] `.archive/staging/skills/tc-travel_SKILL.md` (Original: tc-travel)
- [ ] `.archive/staging/skills/ip-locator-skill_SKILL.md` (Original: ip-locator-skill)
- [ ] `.archive/staging/skills/agent-evolver_SKILL.md` (Original: agent-evolver)
- [ ] `.archive/staging/skills/baidunetdisk_SKILL.md` (Original: baidunetdisk-skill)
- [ ] `.archive/staging/skills/imessage_SKILL.md` (Original: imessage)
- [ ] `.archive/staging/skills/wps-office_SKILL.md` (Original: wps-office)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
