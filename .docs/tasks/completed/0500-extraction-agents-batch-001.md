# Extraction Task: 0500-extraction-agents-batch-001

**Batch Type:** agents
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/agents/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-agents-batch-001` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/agents/default__context.md` (Original: _context)
- [ ] `.archive/staging/agents/agents_architect.md` (Original: architect)
- [ ] `.archive/staging/agents/agents_build-error-resolver.md` (Original: build-error-resolver)
- [ ] `.archive/staging/agents/agents_code-reviewer.md` (Original: code-reviewer)
- [ ] `.archive/staging/agents/agents_database-reviewer.md` (Original: database-reviewer)
- [ ] `.archive/staging/agents/agents_doc-updater.md` (Original: doc-updater)
- [ ] `.archive/staging/agents/agents_e2e-runner.md` (Original: e2e-runner)
- [ ] `.archive/staging/agents/agents_go-build-resolver.md` (Original: go-build-resolver)
- [ ] `.archive/staging/agents/agents_go-reviewer.md` (Original: go-reviewer)
- [ ] `.archive/staging/agents/agents_planner.md` (Original: planner)
- [ ] `.archive/staging/agents/agents_python-reviewer.md` (Original: python-reviewer)
- [ ] `.archive/staging/agents/agents_refactor-cleaner.md` (Original: refactor-cleaner)
- [ ] `.archive/staging/agents/agents_security-reviewer.md` (Original: security-reviewer)
- [ ] `.archive/staging/agents/agents_tdd-guide.md` (Original: tdd-guide)
- [ ] `.archive/staging/agents/agents_boss-qa.md` (Original: agents)
- [ ] `.archive/staging/agents/agents_chief-of-staff.md` (Original: chief-of-staff)
- [ ] `.archive/staging/agents/agents_harness-optimizer.md` (Original: harness-optimizer)
- [ ] `.archive/staging/agents/agents_loop-operator.md` (Original: loop-operator)
- [ ] `.archive/staging/agents/ui-designer.md` (Original: design)
- [ ] `.archive/staging/agents/engineering_frontend-developer.md` (Original: engineering)
- [ ] `.archive/staging/agents/marketing_growth-hacker.md` (Original: marketing)
- [ ] `.archive/staging/agents/product_sprint-prioritizer.md` (Original: product)
- [ ] `.archive/staging/agents/project-management_project-manager-senior.md` (Original: project-management)
- [ ] `.archive/staging/agents/specialized_sales-data-extraction-agent.md` (Original: specialized)
- [ ] `.archive/staging/agents/support_executive-summary-generator.md` (Original: support)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
