# Task: 004-dedup-docs-docs

## Objective

Deduplicate and consolidate the `docs/docs/` directory (62 files). Many files are duplicate scan/compare reports from Jules harvest batches that exist in both short-form (`00026-*`) and long-form (`26-*`) versions.

## Test Requirements

- No content loss: every unique detail from a deleted file must exist in the surviving file.
- Directory should have significantly fewer files after consolidation.

## Exit Conditions (GDD/TDD)

- [ ] Identify all duplicate pairs (e.g., `00026-*-scan.md` vs `26-*-scan.md`)
- [ ] For each pair, diff the contents and keep the most complete version
- [ ] Merge any unique content from the less complete file into the kept file
- [ ] Delete the redundant file
- [ ] Update any internal cross-references

## Details

### What

The `docs/docs/` folder contains 62 files, many of which are duplicated scan/compare reports from different Jules harvesting runs. For example:
- `00026-dudqks0319-cpu-antigravity-skills-scan.md` (1.8KB)
- `26-dudqks0319-cpu-antigravity-skills-scan.md` (14KB)

The longer version is typically the complete one while the shorter is a summary.

Subtasks:
- [ ] List all file pairs sharing the same repo name but different prefixes
- [ ] For each pair, diff the two files
- [ ] Keep the more complete version, merge unique details from the other
- [ ] Delete the redundant file
- [ ] Verify no broken internal links

### Where

`docs/docs/`

### How

Use diff-based comparison. **NEVER simplify, synthesize, or remove unique details.** Only merge and deduplicate. The goal is consolidation without information loss.

### Why

Redundant files create confusion and bloat. Agents waste context reading duplicate information.
