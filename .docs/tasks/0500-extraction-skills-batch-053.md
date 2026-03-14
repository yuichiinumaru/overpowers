# Extraction Task: 0500-extraction-skills-batch-053

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-053` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/suno-skill_SKILL.md` (Original: suno-skill)
- [ ] `.archive/staging/skills/agent-daily-paper_SKILL.md` (Original: agent-daily-paper)
- [ ] `.archive/staging/skills/news-writing_SKILL.md` (Original: news-writing)
- [ ] `.archive/staging/skills/evolving-agent_SKILL.md` (Original: evolving-agent)
- [ ] `.archive/staging/skills/high-visual-arvr-immersive-marketing-rijoy_SKILL.md` (Original: high-visual-arvr-immersive-marketing-rijoy)
- [ ] `.archive/staging/skills/rimet-xhs-spider_SKILL.md` (Original: rimet-xhs-spider)
- [ ] `.archive/staging/skills/openclaw-teaching_SKILL.md` (Original: openclaw-teaching)
- [ ] `.archive/staging/skills/amap-traffic_SKILL.md` (Original: amap-traffic)
- [ ] `.archive/staging/skills/otaku-reco_SKILL.md` (Original: otaku-reco)
- [ ] `.archive/staging/skills/otaku-wiki_SKILL.md` (Original: otaku-wiki)
- [ ] `.archive/staging/skills/moments-grid_SKILL.md` (Original: moments-grid)
- [ ] `.archive/staging/skills/stock-valuation-monitor_SKILL.md` (Original: stock-valuation-monitor)
- [ ] `.archive/staging/skills/qq-music-radio_SKILL.md` (Original: qq-music-radio)
- [ ] `.archive/staging/skills/docx-formatter_SKILL.md` (Original: docx-formatter)
- [ ] `.archive/staging/skills/daily-tang-poem_SKILL.md` (Original: daily-tang-poem)
- [ ] `.archive/staging/skills/cat-selfie_SKILL.md` (Original: cat-selfie)
- [ ] `.archive/staging/skills/zh-knowledge-manager_SKILL.md` (Original: zh-knowledge-manager)
- [ ] `.archive/staging/skills/smartsheet-write_SKILL.md` (Original: smartsheet-write)
- [ ] `.archive/staging/skills/daily-dxc-briefing_SKILL.md` (Original: daily-dxc-briefing)
- [ ] `.archive/staging/skills/mermaid-workflow-skill_SKILL.md` (Original: mermaid-workflow-skill)
- [ ] `.archive/staging/skills/threads_SKILL.md` (Original: threads)
- [ ] `.archive/staging/skills/catch-my-skill_SKILL.md` (Original: catch-my-skill)
- [ ] `.archive/staging/skills/claw-news_SKILL.md` (Original: claw-news)
- [ ] `.archive/staging/skills/elegant-sync_SKILL.md` (Original: elegant-sync)
- [ ] `.archive/staging/skills/vibe-3k_SKILL.md` (Original: vibe-3k)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
