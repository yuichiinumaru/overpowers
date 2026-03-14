# Extraction Task: 0500-extraction-workflows-batch-002

**Batch Type:** workflows
**Total Items:** 10

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/workflows/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-workflows-batch-002` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/workflows/commands_update-docs.md` (Original: update-docs)
- [ ] `.archive/staging/workflows/commands_verify.md` (Original: verify)
- [ ] `.archive/staging/workflows/commands_harness-audit.md` (Original: harness-audit)
- [ ] `.archive/staging/workflows/commands_learn-eval.md` (Original: learn-eval)
- [ ] `.archive/staging/workflows/commands_loop-start.md` (Original: loop-start)
- [ ] `.archive/staging/workflows/commands_loop-status.md` (Original: loop-status)
- [ ] `.archive/staging/workflows/commands_model-route.md` (Original: model-route)
- [ ] `.archive/staging/workflows/commands_multi-frontend.md` (Original: multi-frontend)
- [ ] `.archive/staging/workflows/commands_plan.md` (Original: plan)
- [ ] `.archive/staging/workflows/commands_quality-gate.md` (Original: quality-gate)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
