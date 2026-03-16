# Extraction Task: 0500-extraction-skills-batch-005

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-005` to execute this task or follow these manual steps for each item:

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

- [Skipped] `.archive/staging/skills/daily-market-insight_SKILL.md` (Original: daily-market-insight)
- [x] `.archive/staging/skills/ai-news-daily_SKILL.md` (Original: ai-news-daily)
- [x] `.archive/staging/skills/calorie_SKILL.md` (Original: calorie)
- [x] `.archive/staging/skills/auto-updater-skill_SKILL.md` (Original: auto-updater-skill)
- [x] `.archive/staging/skills/hello-world-skill_SKILL.md` (Original: hello-world-skill)
- [x] `.archive/staging/skills/btpanel_SKILL.md` (Original: btpanel)
- [x] `.archive/staging/skills/z-card-image_SKILL.md` (Original: z-card-image)
- [x] `.archive/staging/skills/self-learning_SKILL.md` (Original: self-learning)
- [x] `.archive/staging/skills/retire-age_SKILL.md` (Original: retire-age)
- [x] `.archive/staging/skills/auto-building_SKILL.md` (Original: auto-building)
- [x] `.archive/staging/skills/avatar-helper_SKILL.md` (Original: avatar-helper)
- [x] `.archive/staging/skills/lyric-sense_SKILL.md` (Original: lyric-sense)
- [x] `.archive/staging/skills/movie-subtitle-viewer_SKILL.md` (Original: movie-subtitle-viewer)
- [x] `.archive/staging/skills/openclaw-telegram-chat_SKILL.md` (Original: openclaw-telegram-chat)
- [x] `.archive/staging/skills/self-driven_SKILL.md` (Original: self-driven)
- [x] `.archive/staging/skills/memory-on-demand_SKILL.md` (Original: memory-on-demand)
- [x] `.archive/staging/skills/todo-manager_SKILL.md` (Original: todo-manager)
- [x] `.archive/staging/skills/fluid-memory_SKILL.md` (Original: fluid-memory)
- [x] `.archive/staging/skills/nalog-ru_SKILL.md` (Original: analizy-ru)
- [x] `.archive/staging/skills/ru-pack_SKILL.md` (Original: ru-pack)
- [x] `.archive/staging/skills/ai-video-script_SKILL.md` (Original: ai-video-script)
- [x] `.archive/staging/skills/bazi_SKILL.md` (Original: bazi)
- [x] `.archive/staging/skills/flyclaw_SKILL.md` (Original: flyclaw)
- [x] `.archive/staging/skills/navclaw_SKILL.md` (Original: navclaw)
- [x] `.archive/staging/skills/trainclaw_SKILL.md` (Original: trainclaw)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
