# Feature Plan: Skill Decision Trees Standardization

## 1. Overview
Standardize the "Decision Tree" pattern used in Overpowers skills. This research task aims to provide clear, consistent guidance for agents to select models, tools, and strategies based on the specific task and context.

## 2. Goals & Success Criteria
- **Goal:** Improve agent efficiency and accuracy by providing structured decision-making frameworks within skills.
- **Success Criteria:**
  - A canonical guide for building Skill Decision Trees is created.
  - A set of standard heuristics for Model Selection (Reasoning vs. Fast) is established.
  - A Markdown template for `## Decision Tree` sections is provided for skill authors.

## 3. Vertical Slices & Milestones

### Slice 1: Heuristic Definition
- **Objective:** Define clear rules for when to use specific models or strategies.
- **Deliverables:** A document listing "Overpowers Decision Heuristics".

### Slice 2: Template Creation
- **Objective:** Create standardized Markdown formats (Table and List) for decision trees.
- **Deliverables:** `templates/skill-decision-tree-template.md`.

### Slice 3: Meta-Skill Integration
- **Objective:** Integrate this guidance into the `skill-creator` or a new `decision-tree` skill.
- **Deliverables:** Updated `skill-creator` instructions or a new reference file in `.docs/`.

## 4. Risks & Mitigations
- **Context Bloat:** Large tables in `SKILL.md` can waste tokens. -> **Mitigation:** Recommend Progressive Disclosure (keeping trees in `references/` if they exceed 20 lines).
- **Stale Heuristics:** Model capabilities change over time. -> **Mitigation:** Centralize the core heuristics in one place so they can be updated globally.

## 5. Exit Conditions
- [x] Canonical guide `docs/guides/skill-decision-trees.md` created.
- [x] Template provided in `templates/`.
- [x] At least one existing skill updated to follow the new standard.
