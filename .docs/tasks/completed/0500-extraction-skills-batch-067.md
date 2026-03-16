# Extraction Task: 0500-extraction-skills-batch-067

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-067` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/real-human_SKILL.md` (Original: real-human)
- [ ] `.archive/staging/skills/insurance-analyzer_SKILL.md` (Original: insurance-analyzer)
- [ ] `.archive/staging/skills/tencentcloud-vita_SKILL.md` (Original: tencentcloud-vita)
- [ ] `.archive/staging/skills/reddit-topic-insight_SKILL.md` (Original: reddit-topic-insight)
- [ ] `.archive/staging/skills/algorithm-solver_SKILL.md` (Original: algorithm-solver)
- [ ] `.archive/staging/skills/political-struggle_SKILL.md` (Original: political-struggle)
- [ ] `.archive/staging/skills/system-design-solver_SKILL.md` (Original: system-design-solver)
- [ ] `.archive/staging/skills/qqbot-persona_SKILL.md` (Original: qqbot-persona)
- [ ] `.archive/staging/skills/ruoxue_SKILL.md` (Original: ruoxue)
- [ ] `.archive/staging/skills/youtube-to-chinese_SKILL.md` (Original: youtube-to-chinese)
- [ ] `.archive/staging/skills/causal-graph_SKILL.md` (Original: causal-graph)
- [ ] `.archive/staging/skills/memory-dedup_SKILL.md` (Original: memory-dedup)
- [ ] `.archive/staging/skills/memory-health-score_SKILL.md` (Original: memory-health-score)
- [ ] `.archive/staging/skills/linkedin-human-warmup_SKILL.md` (Original: linkedin-human-warmup)
- [ ] `.archive/staging/skills/linkedin-warmup_SKILL.md` (Original: linkedin-warmup)
- [ ] `.archive/staging/skills/self-improving-agent-next_SKILL.md` (Original: self-improving-agent-next)
- [ ] `.archive/staging/skills/transition-design_SKILL.md` (Original: transition-design)
- [ ] `.archive/staging/skills/cc-coder_SKILL.md` (Original: cc-coder)
- [ ] `.archive/staging/skills/brand-monitor_SKILL.md` (Original: brand-monitor)
- [ ] `.archive/staging/skills/personal-review-report-chinese_SKILL.md` (Original: personal-review-report-chinese)
- [ ] `.archive/staging/skills/xiaolongxia-youtube-summarizer_SKILL.md` (Original: xiaolongxia-youtube-summarizer)
- [ ] `.archive/staging/skills/fortune-telling_SKILL.md` (Original: fortune-telling)
- [ ] `.archive/staging/skills/lightweight-kb_SKILL.md` (Original: lightweight-kb)
- [ ] `.archive/staging/skills/daily-evolution_SKILL.md` (Original: daily-evolution)
- [ ] `.archive/staging/skills/goal-heartbeat_SKILL.md` (Original: goal-heartbeat)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
