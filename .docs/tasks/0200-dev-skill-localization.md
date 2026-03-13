# Task: Skill Localization and Translation

## Objective
Ensure all skills are accessible in English while maintaining support for regional contexts (e.g., Brazilian marketing).

## Test Requirements
- [ ] All `SKILL.md` files have an English version.
- [ ] No skills remain solely in Portuguese or other non-English languages without an English translation.

## Exit Conditions (GDD/TDD)
- [x] Accented character check performed.
- [x] YAML metadata standardized and translated where identified.
- [x] Description translation incorporated into standardization script.

## Details

### What
Translation sweep of non-English skills identified during the reorganization.

Subtasks:
- [x] Identify all skills containing non-English content.
- [x] Apply standardization script with translation logic.
- [x] Review and refine metadata for technical accuracy.

### Where
- `skills/` (specifically marketing and YouTube-related series).

### How
Batch processing using translation agents or LLM-based translation scripts.

### Why
The repository's primary language is English. Having skills solely in other languages limits their utility for global agents and users.
