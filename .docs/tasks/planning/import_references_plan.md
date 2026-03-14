# Import References Plan

**Date**: 2026-03-15
**Agent**: Nexus

## 1. Overview
After analyzing the `references` directory against the current `overpowers` repository, we found a large number of candidates out of 32,547 total files:
- **YES (New)**: 2,531 items
- **MAYBE (Similar)**: 7,368 items
- **NO (Duplicate)**: 22,545 items

A full report is available at `.agents/thoughts/references_analysis_report.md` and the raw JSON data is located at `.archive/temp/references_analysis.json`.

## 2. Strategy for Importing "YES" Candidates

We will not blindly copy 2,500+ items into the repo. We will apply a structured pipeline:

### Phase 1: Sub-Selection
1. **Filter by Quality & Size**: 
   - Skip files under 100 bytes (likely empty stubs).
   - Use our existing Python script `parse-skills.js` or `skill_standardizer.py` to identify well-formed `SKILL.md` files.
2. **Category Routing**:
   - `skills` (the majority of hits) go to a staging folder `.archive/temp/skills_staging/`.
   - `agents` go to `.archive/temp/agents_staging/`.
   - `workflows`/`commands` go to `.archive/temp/workflows_staging/`.

### Phase 2: Standardization
1. **Name Normalization**: Use an LLM or python script (`fix-skill-names.py`) to rename skills into our format (e.g. `domain-subdomain-skill-name`).
2. **Frontmatter Injection**: Ensure every agent and skill has the correct YAML frontmatter required by Overpowers.
3. **Deduplication Check**: Run a final quick comparison among the new candidates themselves to ensure we aren't adding 5 identical versions of the same skill from 5 different cloned repos.

### Phase 3: Integration
1. Move the processed and standardized items into `skills/`, `agents/`, and `workflows/`.
2. Run `python scripts/utils/audit_extracted_assets.py` to ensure no broken links or missing `SKILL.md` files.
3. Update `AGENTS.md` and `README.md` counts via `update_readme_counts.py`.

## 3. Strategy for "MAYBE" Candidates
1. "MAYBE" candidates have a similarity score between 0.60 and 0.85 with existing items. They often represent updated versions or alternative forks.
2. We will generate a "Merge Candidates" report for the top 100 "MAYBE" items.
3. We will selectively use an LLM diff-tool to compare the `MAYBE` file with our existing file, merging in any new instructions or features.

## 4. Next Steps
1. Await User Review of `.agents/thoughts/references_analysis_report.md`.
2. If approved, run an extraction script to move the top 500 "YES" candidates (ranked by file size and structural completeness) into the staging folders.
3. Execute Phase 2 (Standardization) on the staged files.
