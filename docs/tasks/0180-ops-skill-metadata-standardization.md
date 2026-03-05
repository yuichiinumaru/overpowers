# Task: Skill Metadata Standardization

## Objective
Standardize the YAML frontmatter across all 1245 `SKILL.md` files to ensure consistent discovery and metadata parsing.

## Test Requirements
- [x] Script verifies all `SKILL.md` files have `name`, `description`, and `tags` fields.
- [x] YAML parsing passes for all files.

## Exit Conditions (GDD/TDD)
- [x] All `SKILL.md` files contain valid YAML frontmatter.
- [x] Mandatory fields (`name`, `description`) are present in every file.
- [x] `tags` are populated based on the new folder categorization.

## Details

### What
A systematic pass over all skills to fix inconsistent or missing metadata.

Subtasks:
- [x] Develop standardization script using `yaml.dump` for safety.
- [x] Extract current metadata and augment with missing fields.
- [x] Batch update `SKILL.md` files.
- [x] Verify with `scripts/install-skills.py`.

### Where
- `skills/*/SKILL.md`

### How
Using a Python script to read, parse, and rewrite `SKILL.md` files with a unified frontmatter template.

### Why
Inconsistent metadata hinders the ability of agents to accurately select and use skills.
