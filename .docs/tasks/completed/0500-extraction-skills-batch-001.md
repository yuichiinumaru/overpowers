# Extraction Task: 0500-extraction-skills-batch-001

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-001` to execute this task or follow these manual steps for each item:

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

- [x] `.archive/staging/skills/sync-changelog_SKILL.md` (Original: sync-changelog)
- [x] `.archive/staging/skills/backend-patterns_SKILL.md` (Original: backend-patterns)
- [x] `.archive/staging/skills/coding-standards_SKILL.md` (Original: coding-standards)
- [x] `.archive/staging/skills/configure-ecc_SKILL.md` (Original: configure-ecc)
- [x] `.archive/staging/skills/continuous-learning-v2_SKILL.md` (Original: continuous-learning-v2)
- [x] `.archive/staging/skills/continuous-learning_SKILL.md` (Original: continuous-learning)
- [x] `.archive/staging/skills/cpp-testing_SKILL.md` (Original: cpp-testing)
- [x] `.archive/staging/skills/django-patterns_SKILL.md` (Original: django-patterns)
- [x] `.archive/staging/skills/django-security_SKILL.md` (Original: django-security)
- [x] `.archive/staging/skills/eval-harness_SKILL.md` (Original: eval-harness)
- [x] `.archive/staging/skills/golang-patterns_SKILL.md` (Original: golang-patterns)
- [x] `.archive/staging/skills/golang-testing_SKILL.md` (Original: golang-testing)
- [x] `.archive/staging/skills/iterative-retrieval_SKILL.md` (Original: iterative-retrieval)
- [x] `.archive/staging/skills/project-guidelines-example_SKILL.md` (Original: project-guidelines-example)
- [x] `.archive/staging/skills/python-testing_SKILL.md` (Original: python-testing)
- [x] `.archive/staging/skills/security-review_SKILL.md` (Original: security-review)
- [x] `.archive/staging/skills/security-scan_SKILL.md` (Original: security-scan)
- [x] `.archive/staging/skills/springboot-tdd_SKILL.md` (Original: springboot-tdd)
- [x] `.archive/staging/skills/strategic-compact_SKILL.md` (Original: strategic-compact)
- [x] `.archive/staging/skills/tdd-workflow_SKILL.md` (Original: tdd-workflow)
- [x] `.archive/staging/skills/verification-loop_SKILL.md` (Original: verification-loop)
- [x] `.archive/staging/skills/agent-harness-construction_SKILL.md` (Original: agent-harness-construction)
- [x] `.archive/staging/skills/agentic-engineering_SKILL.md` (Original: agentic-engineering)
- [x] `.archive/staging/skills/ai-first-engineering_SKILL.md` (Original: ai-first-engineering)
- [x] `.archive/staging/skills/article-writing_SKILL.md` (Original: article-writing)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
