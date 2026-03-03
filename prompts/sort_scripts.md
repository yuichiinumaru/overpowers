# Task: Scripts Directory Triage and Reorganization

## Background
The `scripts/` directory has grown excessively large due to bulk extraction from other repositories. Many of the scripts located there (e.g., `*-helper.sh`, `*-cli.sh`) are highly specific to individual skills or workflows and do not belong in a global scripts folder. The root `scripts/` folder should only contain globally applicable repository maintenance or utility scripts.

## Your Mission
Analyze the `scripts/` directory in the root of the repository. Your goal is to systematically evaluate each script and decide its correct home. Many of these should be moved into specific skill directories under `skills/<skill-name>/scripts/`.

### Steps:
1. **Analyze**: Read the contents of the `scripts/` directory. Look out for `*-helper.sh`, `*-cli.sh`, and other specialized tool wrappers.
2. **Determine Belonging**: For each specialized script, figure out which skill in `skills/` it belongs to. For example, `pandoc-helper.sh` likely belongs to a document conversion skill, `stagehand-helper.sh` belongs to a stagehand/browser automation skill, etc.
3. **Move**: Move the script to the corresponding `skills/<skill_name>/scripts/` directory. Create the `scripts/` subdirectory inside the skill if it does not exist.
4. **Update References**: If the script is referenced by any `SKILL.md` or workflow, ensure the paths are updated to reflect the new location.
5. **Keep Globals**: Leave globally applicable scripts (like `install.sh`, `generate-inventory.py`, codebase linters, etc.) in the root `scripts/` directory.
6. **Commit**: Make atomic commits for clusters of related scripts being moved. Let the commit messages clearly state why the scripts were grouped and moved.

## Success Criteria
- The global `scripts/` directory only contains truly global utilities.
- Highly specialized wrapper scripts are placed inside their respective skill directories.
- No workflows or `SKILL.md` documents are broken due to bad paths.
