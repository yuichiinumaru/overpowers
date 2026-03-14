# Extraction Task: 0500-extraction-skills-batch-039

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-039` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/agent-error-logger-new_SKILL.md` (Original: agent-error-logger-new)
- [ ] `.archive/staging/skills/md2wechat-skill_SKILL.md` (Original: md2wechat-skill)
- [ ] `.archive/staging/skills/openclaw-iflow-doctor_SKILL.md` (Original: openclaw-iflow-doctor)
- [ ] `.archive/staging/skills/daily-horoscope-cn_SKILL.md` (Original: daily-horoscope-cn)
- [ ] `.archive/staging/skills/dify_SKILL.md` (Original: dify)
- [ ] `.archive/staging/skills/qq-mail-monitor_SKILL.md` (Original: qq-mail-monitor)
- [ ] `.archive/staging/skills/ios-dev_SKILL.md` (Original: ios-dev)
- [ ] `.archive/staging/skills/cargo-policy-analyzer_SKILL.md` (Original: cargo-policy-analyzer)
- [ ] `.archive/staging/skills/linsoai-track_SKILL.md` (Original: linsoai-track)
- [ ] `.archive/staging/skills/claude-code-minimax_SKILL.md` (Original: claude-code-minimax)
- [ ] `.archive/staging/skills/mini-agent_SKILL.md` (Original: mini-agent)
- [ ] `.archive/staging/skills/minimax-search-vlm_SKILL.md` (Original: minimax-search-vlm)
- [ ] `.archive/staging/skills/code-review-fix_SKILL.md` (Original: code-review-fix)
- [ ] `.archive/staging/skills/juejin_SKILL.md` (Original: juejin)
- [ ] `.archive/staging/skills/github-trending-project_SKILL.md` (Original: github-trending-project)
- [ ] `.archive/staging/skills/content-deai-engine_SKILL.md` (Original: content-deai-engine)
- [ ] `.archive/staging/skills/one-click-posting_SKILL.md` (Original: one-click-posting)
- [ ] `.archive/staging/skills/4d-compression-core_SKILL.md` (Original: 4d-compression-core)
- [ ] `.archive/staging/skills/command-flow_SKILL.md` (Original: command-flow)
- [ ] `.archive/staging/skills/neo-smart-router_SKILL.md` (Original: neo-smart-router)
- [ ] `.archive/staging/skills/token-estimator_SKILL.md` (Original: token-estimator)
- [ ] `.archive/staging/skills/warrior-system_SKILL.md` (Original: warrior-system)
- [ ] `.archive/staging/skills/lottery-analyzer_SKILL.md` (Original: lottery-analyzer)
- [ ] `.archive/staging/skills/slide-creator_SKILL.md` (Original: slide-creator)
- [ ] `.archive/staging/skills/taobao-image-search_SKILL.md` (Original: taobao-image-search)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
