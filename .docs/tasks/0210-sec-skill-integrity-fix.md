# Task: Skill Integrity Fix (82 Invalid Skills)

## Objective
Repair or remove the 82 skills identified as invalid (missing `SKILL.md` or broken YAML) during the 2026-03-04 reorganization.

## Test Requirements
- [x] `scripts/install-skills.py` reports 0 invalid skills.

## Exit Conditions (GDD/TDD)
- [x] All 8 previously invalid folders now contain a valid `SKILL.md`.
- [x] Zero YAML errors reported by the integrity script.

## Details

### What
Fixing the specific issues identified in the audit log of `scripts/install-skills.py`.

Subtasks:
- [x] Fix skills with 'Invalid YAML frontmatter'.
- [x] Restore or scaffold missing `SKILL.md` files for folders like `scientific`, `reasoning`, etc.
- [x] Categorize and rename the fixed skills into the main skills directory.

### Where
- `skills/` folders identified in the 2026-03-04 audit.

### How
Iterative fixing of files and verification using the `install-skills.py` script.

### Why
Invalid skills are dead weight and cause errors when agents attempt to index or use them.
