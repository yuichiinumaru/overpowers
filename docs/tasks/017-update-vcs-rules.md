# Task: 017-update-vcs-rules

## Objective

Consolidate and update VCS rules in `.agents/rules/` to reflect the new branching process, remove duplicates, and clean up Mothership-specific rules.

## Test Requirements

- No contradictory or duplicate rules across files
- VCS workflow rules are clear, actionable, and tested against edge cases
- Mothership-specific rules removed or generalized

## Exit Conditions (GDD/TDD)

- [x] Merge `jujutsu-rules.md` and `vcs-workflow.md` into a single unified rule
- [x] Remove Mothership-specific conda rules (conda-env.md, conda-mothership.md)
- [x] Update all rules for current repo state
- [x] Commit to `development` branch

## Details

### What

The `.agents/rules/` directory has overlapping VCS rules (`jujutsu-rules.md` and `vcs-workflow.md`) and Mothership-specific rules that don't apply to Overpowers. Need to consolidate.

### Where

- `.agents/rules/jujutsu-rules.md` [DELETE - merge into vcs-workflow.md]
- `.agents/rules/vcs-workflow.md` [MODIFY - absorb jujutsu-rules.md content]
- `.agents/rules/conda-env.md` [DELETE]
- `.agents/rules/conda-mothership.md` [DELETE]

### How

Merge the unique content from `jujutsu-rules.md` into `vcs-workflow.md`, remove conda rules, verify no references break.

### Why

Duplicate rules cause confusion for agents. Mothership rules are irrelevant to the Overpowers repo.
