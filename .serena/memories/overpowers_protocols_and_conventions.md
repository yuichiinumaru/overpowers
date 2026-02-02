# Overpowers: Protocols & Conventions

The Overpowers repository operates under strict protocols to ensure maintainability across its 900+ components.

## 1. The Immutable Changelog
*   **File**: `CHANGELOG.md`
*   **Rule**: Entries must **NEVER** be deleted or modified. History is sacred.
*   **Process**: New entries are always added at the top.

## 2. Protocol Zero: Continuity
*   **File**: `continuity.md`
*   **Rule**: Acts as a "Session Ledger".
*   **Process**: Must be read before starting work and updated before finishing to track "Current Focus" and "Next Actions".

## 3. Naming Conventions (The "Snake vs Kebab" War)
*   **Agents**: Use `snake_case` (e.g., `code_reviewer.md`) in recent sanitization efforts to avoid protocol errors (Gemini 400).
*   **Skills**: REQUIRE `kebab-case` for directories and the `name:` field in `SKILL.md` (e.g., `git-master`).
*   **Scripts**: Use `kebab-case.sh` (e.g., `quality-check.sh`).
*   **Recovery**: Scripts like `revert-skills-to-kebab.py` exist to fix accidental `snake_case` conversions in skills.

## 4. Operational Laws
*   **Explicit Declaration**: Agents must be registered in `opencode.json` (helper: `inject-agents-to-config.py`).
*   **Modular Extension**: usage of `generate-agent-configs.py` to maintain the registry.
