# Extraction Task: 0500-extraction-skills-batch-068

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-068` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/ai-chatbot-v2_SKILL.md` (Original: ai-chatbot-v2)
- [ ] `.archive/staging/skills/openclaw-boss_SKILL.md` (Original: openclaw-boss)
- [ ] `.archive/staging/skills/find-the-book_SKILL.md` (Original: find-the-book)
- [ ] `.archive/staging/skills/openclaw-config-manager-skill_SKILL.md` (Original: openclaw-config-manager-skill)
- [ ] `.archive/staging/skills/digital-pet_SKILL.md` (Original: digital-pet)
- [ ] `.archive/staging/skills/zettelkasten-cn_SKILL.md` (Original: zettelkasten-cn)
- [ ] `.archive/staging/skills/zeelin-musk-activity-tracker_SKILL.md` (Original: zeelin-musk-activity-tracker)
- [ ] `.archive/staging/skills/nano-banana-korean-rendering_SKILL.md` (Original: nano-banana-korean-rendering)
- [ ] `.archive/staging/skills/scholar-search-skills_SKILL.md` (Original: scholar-search-skills)
- [ ] `.archive/staging/skills/sim-trade_SKILL.md` (Original: sim-trade)
- [ ] `.archive/staging/skills/story-music_SKILL.md` (Original: story-music)
- [ ] `.archive/staging/skills/hunyuan-3d_SKILL.md` (Original: hunyuan-3d)
- [ ] `.archive/staging/skills/hunyuan-video_SKILL.md` (Original: hunyuan-video)
- [ ] `.archive/staging/skills/baidu-milan-winter-olympics-2026_SKILL.md` (Original: baidu-milan-winter-olympics-2026)
- [ ] `.archive/staging/skills/juejin-article-trends_SKILL.md` (Original: juejin-article-trends)
- [ ] `.archive/staging/skills/nano-banana-pro-image-gen_SKILL.md` (Original: nano-banana-pro-image-gen)
- [ ] `.archive/staging/skills/pdf-to-image-preview_SKILL.md` (Original: pdf-to-image-preview)
- [ ] `.archive/staging/skills/toutiao-news-trends_SKILL.md` (Original: toutiao-news-trends)
- [ ] `.archive/staging/skills/wechat-article-search_SKILL.md` (Original: wechat-article-search)
- [ ] `.archive/staging/skills/family-expense-intent_SKILL.md` (Original: family-expense-intent)
- [ ] `.archive/staging/skills/family-intent-recognition_SKILL.md` (Original: family-intent-recognition)
- [ ] `.archive/staging/skills/shopping-assistant_SKILL.md` (Original: shopping-assistant)
- [ ] `.archive/staging/skills/taobaoke-tool_SKILL.md` (Original: taobaoke-tool)
- [ ] `.archive/staging/skills/protein-key-fragment-analysis_SKILL.md` (Original: protein-key-fragment-analysis)
- [ ] `.archive/staging/skills/mp-draft-push_SKILL.md` (Original: mp-draft-push)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
