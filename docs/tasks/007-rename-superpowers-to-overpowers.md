# Task: 007-rename-superpowers-to-overpowers

## Objective

Replace all references to "superpowers" with "overpowers" across the repository, except in `CHANGELOG.md` historical entries (immutable) and the "Based On" attribution link in `AGENTS.md`/`README.md`.

## Test Requirements

- `grep -ri "superpowers" . --include="*.md" --include="*.sh" --include="*.py" --include="*.json"` should only match CHANGELOG.md historical entries and the "Based On" attribution.
- No broken imports or links.

## Exit Conditions (GDD/TDD)

- [ ] All non-exempt files updated
- [ ] Skill directory `skills/using-superpowers/` renamed to `skills/using-overpowers/`
- [ ] Internal references to the renamed skill updated
- [ ] No broken links or imports

## Details

### What

This project is a heavily modified fork of "superpowers" but has its own identity as "overpowers". Some files still reference the old name.

Files to update (17 found):
- `install.sh`, `README.md`, `AGENTS.md`
- `skills/using-superpowers/SKILL.md` → rename directory
- `archives/references-cloned.sh`, `archives/references-list.md`
- `archives/26-dudqks0319-*`, `archives/skill-vs-agent-*.md`
- `docs/README.md`, `archives/EXTRACTION_MASTER_PLAN.md`
- `docs/architecture/003-arch-jules-digest.md`, `archives/004-archive-raw-analysis-notes.md`
- `docs/architecture/001-arch-project-structure-map.md`, `docs/architecture/002-arch-system-knowledge-graph.md`

Subtasks:
- [ ] Update text references in each file (not attribution links)
- [ ] Rename `skills/using-superpowers/` → `skills/using-overpowers/`
- [ ] Update all internal references to the renamed skill
- [ ] Verify no broken links

### Where

Root directory and `docs/` subdirectories.

### How

Use `sed` or manual edits. **Do NOT modify CHANGELOG.md entries** (immutable law). Keep the "Based On: Superpowers" attribution intact in README.md and AGENTS.md as a credit link only.

### Why

Brand consistency. The project has its own identity and should not confuse users or agents with stale references.
