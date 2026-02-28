# Task: 005-dedup-docs-analysis

## Objective

Deduplicate and consolidate the `docs/analysis/` directory (13 files). Contains overlapping extraction plans (V1 + V2), multiple harvest reports from the same date, and a massive 2.3MB diff file.

## Test Requirements

- No content loss: every unique detail from deleted files must be preserved.
- The 2.3MB `mega_harvest.diff` should be evaluated — if it is stale or already applied, it can be removed.

## Exit Conditions (GDD/TDD)

- [ ] Merge `EXTRACTION_MASTER_PLAN.md` and `EXTRACTION_MASTER_PLAN_V2.md` into one
- [ ] Consolidate same-date harvest reports into a single report per date
- [ ] Evaluate whether `mega_harvest.diff` and `integrate_references.diff` are still needed
- [ ] Delete redundant files

## Details

### What

The analysis directory has overlapping documents:
- `EXTRACTION_MASTER_PLAN.md` (2.4KB) + `EXTRACTION_MASTER_PLAN_V2.md` (1.7KB) — V2 is likely the evolution
- 5 `harvest_report_2026-01-19_*.md` files from the same date — can be consolidated into one
- `mega_harvest.diff` (2.3MB) — likely stale, needs evaluation
- `integrate_references.diff` (15KB) — may already be applied

Subtasks:
- [ ] Read both extraction plans, merge into one keeping all unique content
- [ ] Consolidate 5 same-date harvest reports into one comprehensive report
- [ ] Check if `mega_harvest.diff` has already been applied (compare with current tree)
- [ ] Check if `integrate_references.diff` has already been applied
- [ ] Delete stale/redundant files

### Where

`docs/analysis/`

### How

Diff-based comparison. For `.diff` files, attempt `git apply --check` to see if they are already applied. **NEVER simplify or remove unique details.** Merge and consolidate only.

### Why

Stale diffs and duplicate plans waste storage and confuse agents trying to understand the project history.
