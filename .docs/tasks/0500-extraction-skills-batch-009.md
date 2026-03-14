# Extraction Task: 0500-extraction-skills-batch-009

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-009` to execute this task or follow these manual steps for each item:

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

- [x] `.archive/staging/skills/minimax-plan-checker_SKILL.md` (Original: minimax-plan-checker)
- [x] `.archive/staging/skills/portainer_SKILL.md` (Original: airfoil)
- [x] `.archive/staging/skills/openclaw-ref_SKILL.md` (Original: openclaw-ref)
- [x] `.archive/staging/skills/smart-router-skill_SKILL.md` (Original: smart-router-skill)
- [x] `.archive/staging/skills/audiobooklm_SKILL.md` (Original: audiobooklm)
- [x] `.archive/staging/skills/toutiao-publish_SKILL.md` (Original: toutiao-publish)
- [x] `.archive/staging/skills/env-secure-manager_SKILL.md` (Original: env-secure-manager)
- [x] `.archive/staging/skills/resume-parser_SKILL.md` (Original: resume-parser)
- [x] `.archive/staging/skills/smart-memory-manager_SKILL.md` (Original: smart-memory-manager)
- [x] `.archive/staging/skills/stream-formatter_SKILL.md` (Original: stream-formatter)
- [x] `.archive/staging/skills/tool-call-retry_SKILL.md` (Original: tool-call-retry)
- [x] `.archive/staging/skills/project-deep-analyzer_SKILL.md` (Original: project-deep-analyzer)
- [x] `.archive/staging/skills/testhy_SKILL.md` (Original: testhy)
- [x] `.archive/staging/skills/pyzhihu-cli_SKILL.md` (Original: pyzhihu-cli)
- [x] `.archive/staging/skills/qiniu-kodo_SKILL.md` (Original: qiniu-kodo)
- [x] `.archive/staging/skills/auto-researcher_SKILL.md` (Original: auto-researcher)
- [x] `.archive/staging/skills/money-maker-hand_SKILL.md` (Original: money-maker-hand)
- [x] `.archive/staging/skills/security-audit-hand_SKILL.md` (Original: security-audit-hand)
- [x] `.archive/staging/skills/social-media-copywriter-generator_SKILL.md` (Original: social-media-copywriter-generator)
- [x] `.archive/staging/skills/wan-text2image_SKILL.md` (Original: wan-text2image)
- [x] `.archive/staging/skills/astock-daily_SKILL.md` (Original: astock-daily)
- [x] `.archive/staging/skills/react-nextjs-generator_SKILL.md` (Original: react-nextjs-generator)
- [x] `.archive/staging/skills/humanize-zh_SKILL.md` (Original: humanize-zh)
- [x] `.archive/staging/skills/cpa-codex-auth-sweep-cliproxy_SKILL.md` (Original: cpa-codex-auth-sweep-cliproxy)
- [x] `.archive/staging/skills/multi-agent-cn_SKILL.md` (Original: multi-agent-cn)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
