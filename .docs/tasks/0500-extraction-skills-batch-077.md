# Extraction Task: 0500-extraction-skills-batch-077

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-077` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/voice-chat_SKILL.md` (Original: voice-chat)
- [ ] `.archive/staging/skills/voice-wake_SKILL.md` (Original: voice-wake)
- [ ] `.archive/staging/skills/qmd-manager_SKILL.md` (Original: qmd-manager)
- [ ] `.archive/staging/skills/quote-reader_SKILL.md` (Original: quote-reader)
- [ ] `.archive/staging/skills/session-memory-enhanced_SKILL.md` (Original: session-memory-enhanced)
- [ ] `.archive/staging/skills/smart-memory-sync_SKILL.md` (Original: smart-memory-sync)
- [ ] `.archive/staging/skills/smart-model-switch_SKILL.md` (Original: smart-model-switch)
- [ ] `.archive/staging/skills/terminal-ocr_SKILL.md` (Original: terminal-ocr)
- [ ] `.archive/staging/skills/tutu-smart-control_SKILL.md` (Original: tutu-smart-control)
- [ ] `.archive/staging/skills/system-data-intelligence-skill_SKILL.md` (Original: system-data-intelligence-skill)
- [ ] `.archive/staging/skills/system-data-intelligence_SKILL.md` (Original: system-data-intelligence)
- [ ] `.archive/staging/skills/convertible-bond-assistant_SKILL.md` (Original: convertible-bond-assistant)
- [ ] `.archive/staging/skills/roboneo-merge-dev-to-pre-or-beta_SKILL.md` (Original: roboneo-merge-dev-to-pre-or-beta)
- [ ] `.archive/staging/skills/clawhub-installer_SKILL.md` (Original: clawhub-installer)
- [ ] `.archive/staging/skills/ppt2png_SKILL.md` (Original: ppt2png)
- [ ] `.archive/staging/skills/ppt2wechat_SKILL.md` (Original: ppt2wechat)
- [ ] `.archive/staging/skills/knowledge_SKILL.md` (Original: knowledge)
- [ ] `.archive/staging/skills/alive-check-monitor_SKILL.md` (Original: alive-check-monitor)
- [ ] `.archive/staging/skills/cn-weather_SKILL.md` (Original: cn-weather)
- [ ] `.archive/staging/skills/alpha-hound-cn_SKILL.md` (Original: alpha-hound-cn)
- [ ] `.archive/staging/skills/momentum-reversal-cn_SKILL.md` (Original: momentum-reversal-cn)
- [ ] `.archive/staging/skills/self-improving-agent-cn_SKILL.md` (Original: self-improving-agent-cn)
- [ ] `.archive/staging/skills/feishu-doc-orchestrator_SKILL.md` (Original: feishu-doc-orchestrator)
- [ ] `.archive/staging/skills/feishu-block-adder_SKILL.md` (Original: feishu-block-adder)
- [ ] `.archive/staging/skills/feishu-doc-creator-with-permission_SKILL.md` (Original: feishu-doc-creator-with-permission)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
