# Extraction Task: 0500-extraction-skills-batch-062

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-062` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/agent-retro_SKILL.md` (Original: agent-retro)
- [ ] `.archive/staging/skills/hugo-blog-publisher_SKILL.md` (Original: hugo-blog-publisher)
- [ ] `.archive/staging/skills/night-patch_SKILL.md` (Original: night-patch)
- [ ] `.archive/staging/skills/method-dev-agent_SKILL.md` (Original: method-dev-agent)
- [ ] `.archive/staging/skills/personal-scheduler_SKILL.md` (Original: personal-scheduler)
- [ ] `.archive/staging/skills/opencode-select-confirm_SKILL.md` (Original: opencode-select-confirm)
- [ ] `.archive/staging/skills/watermark-remover_SKILL.md` (Original: watermark-remover)
- [ ] `.archive/staging/skills/feishu-speaker_SKILL.md` (Original: feishu-speaker)
- [ ] `.archive/staging/skills/jimeng-video_SKILL.md` (Original: jimeng-video)
- [ ] `.archive/staging/skills/zeelin-meetingdirectives_SKILL.md` (Original: zeelin-meetingdirectives)
- [ ] `.archive/staging/skills/zeelin-meetinginstructions_SKILL.md` (Original: zeelin-meetinginstructions)
- [ ] `.archive/staging/skills/feishu-calendar-event_SKILL.md` (Original: feishu-calendar-event)
- [ ] `.archive/staging/skills/ticket-monitor-ichinosuke_SKILL.md` (Original: ticket-monitor-ichinosuke)
- [ ] `.archive/staging/skills/godot-mcp_SKILL.md` (Original: godot-mcp)
- [ ] `.archive/staging/skills/book-write_SKILL.md` (Original: book-write)
- [ ] `.archive/staging/skills/claw-helper_SKILL.md` (Original: claw-helper)
- [ ] `.archive/staging/skills/task-dispatcher_SKILL.md` (Original: task-dispatcher)
- [ ] `.archive/staging/skills/mao-emperors_SKILL.md` (Original: mao-emperors)
- [ ] `.archive/staging/skills/health-data-analyzer_SKILL.md` (Original: health-data-analyzer)
- [ ] `.archive/staging/skills/codex-runner_SKILL.md` (Original: codex-runner)
- [ ] `.archive/staging/skills/check_SKILL.md` (Original: check)
- [ ] `.archive/staging/skills/meeting-notes_SKILL.md` (Original: meeting-notes)
- [ ] `.archive/staging/skills/xiaohongshu-mcp-patch_SKILL.md` (Original: xiaohongshu-mcp-patch)
- [ ] `.archive/staging/skills/xiaohongshu-v2_SKILL.md` (Original: xiaohongshu-v2)
- [ ] `.archive/staging/skills/project-mode_SKILL.md` (Original: project-mode)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
