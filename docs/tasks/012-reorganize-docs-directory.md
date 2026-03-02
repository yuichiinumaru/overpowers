# Task: 012-reorganize-docs-directory

## Objective

Reorganize the `docs/` directory into a clean, well-structured hierarchy. Classify all files, archive obsolete content, and ensure everything follows the `nnn-type` filename convention.

## Test Requirements

- No orphaned or misclassified files remain in `docs/` root
- All useful docs have been categorized and moved to the correct subdirectory
- File naming follows `nnn-type-name.md` convention
- Content references remain valid (or are updated)

## Exit Conditions (GDD/TDD)

- [x] Classify every file in `docs/` (excluding `tasks/` and `tasklist.md`)
- [x] Move obsolete/useless content → `archives/`
- [x] Move research/analysis/plans/reports about needed improvements → `docs/tasks/planning/`
- [x] Move specs/features/goals/architecture → `docs/architecture/`
- [x] Move usage guides → `docs/guides/`
- [x] Evaluate remaining files for potential agent/skill/workflow/hook reuse
- [x] Update outdated content to reflect current repo state
- [x] Rename files per `nnn-type-name.md` convention
- [x] Update any internal cross-references that break

## Details

### What

The `docs/` directory currently has ~80+ files scattered across root and 6 subdirectories with inconsistent naming. Files include:
- **Potentially obsolete:** Integration reports (Phase 1-3), raw analysis notes, old merge strategies, duplicate docs in `docs/docs/`
- **Guides:** hooks-guide.md, scripts-guide.md, workflows-guide.md, services-guide.md, skill_creation_guide.md
- **Architecture:** project_structure_map.md, SYSTEM_KNOWLEDGE_GRAPH.md, JULES_ARCHITECTURAL_DIGEST.md
- **Research/Planning:** model-fallback-system-design.md, oh-my-opencode-analysis.md, performance_analysis.md
- **Services:** entire `docs/services/` subtree
- **Knowledge:** `docs/knowledge/` subtree with testing patterns
- **YouTube:** mining results
- **Protocols:** intent-classification.md, sandbox-guidelines.md

### Where

- `docs/` (source) → `archives/`, `docs/architecture/`, `docs/guides/`, `docs/tasks/planning/`

### How

1. Inventory every file in `docs/` (excluding tasks/, tasklist.md)
2. Read each file to determine classification
3. Move files to appropriate subdirectories
4. Archive truly obsolete content
5. Update content that references old repo structure
6. Rename per convention

### Why

The current `docs/` structure is a historical accumulation of sessions by multiple agents (Jules, Gemini CLI, Antigravity). Without organization, agents waste context tokens reading irrelevant files or miss important ones.
