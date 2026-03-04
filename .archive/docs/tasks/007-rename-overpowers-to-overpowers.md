# Task: 007-rename-overpowers-to-overpowers

## Objective

Replace all references to the old toolkit name with "overpowers" across the repository, except in "CHANGELOG.md" historical entries (immutable) and the "Based On" attribution link in "AGENTS.md"/"README.md".

## Test Requirements

- No occurrences of the old name should exist outside of attribution links and historical changelog entries.
- No broken imports or links.

## Exit Conditions (GDD/TDD)

- [x] All non-exempt files updated
- [x] Skill directory "skills/using-overpowers/" renamed (Completed)
- [x] Internal references to the renamed skill updated
- [x] No broken links or imports

## Details

### What

This project is a heavily modified fork of the original toolkit but has its own identity as "overpowers". All remaining core references were updated during the second pass audit.

### Where

Root directory and "docs/" subdirectories.

### How

Broad sed sweep and manual verification of core files.

### Why

Brand consistency and to avoid confusing users or agents with stale references.
