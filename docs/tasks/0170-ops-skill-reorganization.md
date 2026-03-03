# Task: Skill Folder Reorganization

## Objective
Rename all skill folders in `skills/` to follow the `type-subtype-nnnn-name` convention for better organization and discoverability.

## Test Requirements
- [x] All 1237 folders follow the new naming convention.
- [x] Mapping file `.agents/thoughts/skill_mapping.json` exists and is unique.

## Exit Conditions (GDD/TDD)
- [x] Folders renamed correctly.
- [x] No duplicate folder names.
- [x] Original `SKILL.md` files preserved.

## Details

### What
Bulk rename of skill directories based on keyword heuristics from their `SKILL.md` content.

Subtasks:
- [x] List all skills.
- [x] Categorize skills using Python script heuristics.
- [x] Map skills to 4-digit unique IDs.
- [x] Perform `os.rename` on all valid skill folders.

### Where
- `skills/` directory.

### How
Using `scripts/categorize_skills.py` (temporary) to generate a JSON mapping and executing the renames via Python's `os.rename`.

### Why
The previous flat directory structure was becoming unmanageable with over 1200 items. Categorization improves agent search and human navigation.
