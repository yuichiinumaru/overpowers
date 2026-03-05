# Task: 006-dedup-docs-knowledge

## Objective

Deduplicate and consolidate the `docs/knowledge/` directory (36+ entries across `entries/` and `testing/` subdirs). Contains Jules-generated knowledge base entries that may have overlapping content.

## Test Requirements

- No content loss: every unique detail must be preserved.
- `index.json` must be updated to reflect any file changes.

## Exit Conditions (GDD/TDD)

- [ ] Audit all files in `docs/knowledge/testing/` (34 files)
- [ ] Identify entries covering the same topic or with heavily overlapping content
- [ ] Merge overlapping entries into the most complete version
- [ ] Update `docs/knowledge/index.json` to reflect final state
- [ ] Delete redundant files

## Details

### What

The knowledge directory has 34 testing entries and 1 main entry. Many testing entries may be iterations of the same knowledge, created during different Jules runs.

Subtasks:
- [ ] Read `index.json` to understand the cataloging structure
- [ ] List all `testing/` entries and group by topic similarity
- [ ] For each group, diff contents and identify the most complete version
- [ ] Merge unique content from less complete versions into the keeper
- [ ] Delete redundant entries
- [ ] Update `index.json` to remove references to deleted files

### Where

`docs/knowledge/` (especially `docs/knowledge/testing/`)

### How

Topic-based grouping followed by diff-based merging. **NEVER simplify, synthesize, or remove unique details.** Only consolidate duplicates.

### Why

Duplicate knowledge entries increase context noise and mislead agents who read them for project understanding.
