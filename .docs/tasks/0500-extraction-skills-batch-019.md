# Extraction Task: 0500-extraction-skills-batch-019

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-019` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/xtechhotnews_SKILL.md` (Original: xtechhotnews)
- [ ] `.archive/staging/skills/explain-code_SKILL.md` (Original: explain-code)
- [ ] `.archive/staging/skills/acg-rust-teacher_SKILL.md` (Original: acg-rust-teacher)
- [ ] `.archive/staging/skills/yan-learning-engine_SKILL.md` (Original: yan-learning-engine)
- [ ] `.archive/staging/skills/ceo-delegation_SKILL.md` (Original: ceo-delegation)
- [ ] `.archive/staging/skills/newspaper-brief_SKILL.md` (Original: newspaper-brief)
- [ ] `.archive/staging/skills/clawhub-intro-skill_SKILL.md` (Original: clawhub-intro-skill)
- [ ] `.archive/staging/skills/report-search_SKILL.md` (Original: report-search)
- [ ] `.archive/staging/skills/fortune-oracle_SKILL.md` (Original: fortune-oracle)
- [ ] `.archive/staging/skills/emily-web-fetch_SKILL.md` (Original: emily-web-fetch)
- [ ] `.archive/staging/skills/daily-gushiwen_SKILL.md` (Original: daily-gushiwen)
- [ ] `.archive/staging/skills/daily-trending_SKILL.md` (Original: daily-trending)
- [ ] `.archive/staging/skills/whu-campus_SKILL.md` (Original: whu-campus)
- [ ] `.archive/staging/skills/encrypted-file-writer_SKILL.md` (Original: encrypted-file-writer)
- [ ] `.archive/staging/skills/faithful-task-executor_SKILL.md` (Original: faithful-task-executor)
- [ ] `.archive/staging/skills/module-analyzer-generate-doc_SKILL.md` (Original: module-analyzer-generate-doc)
- [ ] `.archive/staging/skills/project-analyzer-generate-doc_SKILL.md` (Original: project-analyzer-generate-doc)
- [ ] `.archive/staging/skills/three-minds_SKILL.md` (Original: three-minds)
- [ ] `.archive/staging/skills/quant-stock-picker-pro_SKILL.md` (Original: quant-stock-picker-pro)
- [ ] `.archive/staging/skills/parallel-task-executor_SKILL.md` (Original: parallel-task-executor)
- [ ] `.archive/staging/skills/recursive-self-improvement_SKILL.md` (Original: recursive-self-improvement)
- [ ] `.archive/staging/skills/pro-zh-summary_SKILL.md` (Original: pro-zh-summary)
- [ ] `.archive/staging/skills/browser-relay-xiaohongshu_SKILL.md` (Original: browser-relay-xiaohongshu)
- [ ] `.archive/staging/skills/agent-batch-guard_SKILL.md` (Original: agent-batch-guard)
- [ ] `.archive/staging/skills/feishu-app-setup_SKILL.md` (Original: feishu-app-setup)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
