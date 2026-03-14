# Extraction Task: 0500-extraction-hooks-batch-001

**Batch Type:** hooks
**Total Items:** 9

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/hooks/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-hooks-batch-001` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/hooks/hooks_index.ts` (Original: index)
- [ ] `.archive/staging/hooks/hooks___init__.py` (Original: __init__)
- [ ] `.archive/staging/hooks/hooks_stream-hook.mdx` (Original: stream-hook)
- [ ] `.archive/staging/hooks/pre-hooks.mdx` (Original: openai-moderation-guardrail)
- [ ] `.archive/staging/hooks/hooks.json` (Original: hooks)
- [ ] `.archive/staging/hooks/hooks_README.md` (Original: readme)
- [ ] `.archive/staging/hooks/hooks_auto-agent-setup.sh` (Original: auto-agent-setup)
- [ ] `.archive/staging/hooks/hooks_usePermission.ts` (Original: usepermission)
- [ ] `.archive/staging/hooks/scripts_session-start.sh` (Original: pre-compact)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
