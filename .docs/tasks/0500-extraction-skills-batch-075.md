# Extraction Task: 0500-extraction-skills-batch-075

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-075` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/openclaw-x-article-cover-generator_SKILL.md` (Original: openclaw-x-article-cover-generator)
- [ ] `.archive/staging/skills/kailas-copywriting_SKILL.md` (Original: kailas-copywriting)
- [ ] `.archive/staging/skills/voice-memo_SKILL.md` (Original: voice-memo)
- [ ] `.archive/staging/skills/pmbuysell_SKILL.md` (Original: pmbuysell)
- [ ] `.archive/staging/skills/sister-soul_SKILL.md` (Original: sister-soul)
- [ ] `.archive/staging/skills/resume-screening_SKILL.md` (Original: resume-screening)
- [ ] `.archive/staging/skills/ponzu-ethereum_SKILL.md` (Original: ponzu-ethereum)
- [ ] `.archive/staging/skills/agent-existence-protocol_SKILL.md` (Original: agent-existence-protocol)
- [ ] `.archive/staging/skills/deep-reading_SKILL.md` (Original: deep-reading)
- [ ] `.archive/staging/skills/receipt-assistant_SKILL.md` (Original: receipt-assistant)
- [ ] `.archive/staging/skills/high-repeat-small-goods-ops_SKILL.md` (Original: high-repeat-small-goods-ops)
- [ ] `.archive/staging/skills/hot-topic-ideator_SKILL.md` (Original: hot-topic-ideator)
- [ ] `.archive/staging/skills/social-media-title-insight_SKILL.md` (Original: social-media-title-insight)
- [ ] `.archive/staging/skills/cat-therapy_SKILL.md` (Original: cat-therapy)
- [ ] `.archive/staging/skills/openclaw-docs-cn_SKILL.md` (Original: openclaw-docs-cn)
- [ ] `.archive/staging/skills/mind-layer_SKILL.md` (Original: mind-layer)
- [ ] `.archive/staging/skills/buffett-analysis_SKILL.md` (Original: buffett-analysis)
- [ ] `.archive/staging/skills/finstep-tools_SKILL.md` (Original: finstep-tools)
- [ ] `.archive/staging/skills/dingtalk-bot-publish_SKILL.md` (Original: dingtalk-bot-publish)
- [ ] `.archive/staging/skills/wechat-moments-post_SKILL.md` (Original: wechat-moments-post)
- [ ] `.archive/staging/skills/dsp_SKILL.md` (Original: dsp)
- [ ] `.archive/staging/skills/code-security-auditor_SKILL.md` (Original: code-security-auditor)
- [ ] `.archive/staging/skills/continuous-evolution_SKILL.md` (Original: continuous-evolution)
- [ ] `.archive/staging/skills/progress-reporter_SKILL.md` (Original: progress-reporter)
- [ ] `.archive/staging/skills/task-auditor_SKILL.md` (Original: task-auditor)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
