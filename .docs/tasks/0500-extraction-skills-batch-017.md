# Extraction Task: 0500-extraction-skills-batch-017

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-017` to execute this task or follow these manual steps for each item:

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

- [x] `.archive/staging/skills/amazon-product-scraper_SKILL.md` (Original: amazon-product-scraper) → `skills/amazon-product-scraper/`
- [x] `.archive/staging/skills/news-briefing_SKILL.md` (Original: news-briefing) → `skills/news-briefing/`
- [x] `.archive/staging/skills/engagelab-email_SKILL.md` (Original: engagelab-email) → `skills/engagelab-email/`
- [x] `.archive/staging/skills/juejin-publisher_SKILL.md` (Original: juejin-publisher) → `skills/juejin-publisher/`
- [ ] `.archive/staging/skills/malicious_skill_exfil_SKILL.md` (Original: malicious_skill_exfil) - File not found (already processed?)
- [x] `.archive/staging/skills/openclaw-skill-money-idea-generator_SKILL.md` (Original: openclaw-skill-money-idea-generator) → `skills/money-idea-generator/`
- [x] `.archive/staging/skills/zh_SKILL.md` (Original: zh) → `skills/zh/`
- [x] `.archive/staging/skills/my-weather-query_SKILL.md` (Original: my-weather-query) → `skills/my-weather-query/`
- [ ] `.archive/staging/skills/geekbench_SKILL.md` (Original: geekbench) - File not found (already processed?)
- [ ] `.archive/staging/skills/mentx-doctor_SKILL.md` (Original: mentx-doctor) - File not found (already processed?)
- [ ] `.archive/staging/skills/yanxue_SKILL.md` (Original: yanxue) - File not found (already processed?)
- [ ] `.archive/staging/skills/eastmoney-stock_SKILL.md` (Original: eastmoney-stock) - File not found (already processed?)
- [x] `.archive/staging/skills/melodylab-ai-song_SKILL.md` (Original: melodylab-ai-song) → `skills/melodylab-ai-song/`
- [x] `.archive/staging/skills/zeelin-liberal-arts-paper_SKILL.md` (Original: zeelin-academic-paper) → `skills/zeelin-liberal-arts-paper/`
- [x] `.archive/staging/skills/zeelin-ai-detector_SKILL.md` (Original: zeelin-ai-detector) → `skills/zeelin-ai-detector/`
- [x] `.archive/staging/skills/happycoding-aicoding_SKILL.md` (Original: happycoding-aicoding) → `skills/happycoding-aicoding/`
- [ ] `.archive/staging/skills/skill-install-guard_SKILL.md` (Original: skill-install-guard) - File not found (already processed?)
- [ ] `.archive/staging/skills/xhunt-hot-tweets-skill_SKILL.md` (Original: xhunt-hot-tweets-skill) - File not found (already processed?)
- [ ] `.archive/staging/skills/double729-plansuite_SKILL.md` (Original: double729-plansuite) - File not found (already processed?)
- [x] `.archive/staging/skills/naver-search_SKILL.md` (Original: naver-search) → `skills/naver-search/`
- [x] `.archive/staging/skills/meme-lord_SKILL.md` (Original: meme-lord) → `skills/meme-lord/`
- [x] `.archive/staging/skills/openclaw-installer_SKILL.md` (Original: openclaw-installer) → `skills/openclaw-installer/`
- [x] `.archive/staging/skills/play-dumb_SKILL.md` (Original: play-dumb) → `skills/play-dumb/`
- [x] `.archive/staging/skills/play-smart_SKILL.md` (Original: play-smart) → `skills/play-smart/`
- [x] `.archive/staging/skills/star-office-ui_SKILL.md` (Original: star-office-ui) → `skills/star-office-ui/`


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
