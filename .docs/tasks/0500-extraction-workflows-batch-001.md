# Extraction Task: 0500-extraction-workflows-batch-001

**Batch Type:** workflows
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/workflows/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-workflows-batch-001` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/workflows/commands_README.md` (Original: readme)
- [ ] `.archive/staging/workflows/commands_build-fix.md` (Original: build-fix)
- [ ] `.archive/staging/workflows/commands_checkpoint.md` (Original: checkpoint)
- [ ] `.archive/staging/workflows/commands_code-review.md` (Original: code-review)
- [ ] `.archive/staging/workflows/commands_e2e.md` (Original: e2e)
- [ ] `.archive/staging/workflows/commands_eval.md` (Original: eval)
- [ ] `.archive/staging/workflows/commands_go-build.md` (Original: go-build)
- [ ] `.archive/staging/workflows/commands_go-review.md` (Original: go-review)
- [ ] `.archive/staging/workflows/commands_go-test.md` (Original: go-test)
- [ ] `.archive/staging/workflows/commands_instinct-export.md` (Original: instinct-export)
- [ ] `.archive/staging/workflows/commands_learn.md` (Original: learn)
- [ ] `.archive/staging/workflows/commands_multi-frontend.md` (Original: multi-backend)
- [ ] `.archive/staging/workflows/commands_multi-execute.md` (Original: multi-execute)
- [ ] `.archive/staging/workflows/commands_multi-plan.md` (Original: multi-plan)
- [ ] `.archive/staging/workflows/commands_multi-workflow.md` (Original: multi-workflow)
- [ ] `.archive/staging/workflows/commands_orchestrate.md` (Original: orchestrate)
- [ ] `.archive/staging/workflows/commands_pm2.md` (Original: pm2)
- [ ] `.archive/staging/workflows/commands_python-review.md` (Original: python-review)
- [ ] `.archive/staging/workflows/commands_refactor-clean.md` (Original: refactor-clean)
- [ ] `.archive/staging/workflows/commands_sessions.md` (Original: sessions)
- [ ] `.archive/staging/workflows/commands_setup-pm.md` (Original: setup-pm)
- [ ] `.archive/staging/workflows/commands_skill-create.md` (Original: skill-create)
- [ ] `.archive/staging/workflows/commands_tdd.md` (Original: tdd)
- [ ] `.archive/staging/workflows/commands_test-coverage.md` (Original: test-coverage)
- [ ] `.archive/staging/workflows/commands_update-codemaps.md` (Original: update-codemaps)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
