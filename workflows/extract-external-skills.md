---
description: Extract, analyze, and integrate agent skills from external GitHub repositories.
argument-hint: Space-separated list of GitHub Repo URLs or a path to a file containing URLs.
---

# /extract-external-skills

**Goal**: Automate the process of mining and extracting agent skills from external community repositories, comparing them against the internal `overpowers` repository, and selectively integrating them. Accommodates both direct skill repositories and "awesome list" repositories.

## Actions

1. **Input Parsing & Environment Setup**:
   - Parse the provided arguments (which may be a list of GitHub URLs or a path to a `.md`/`.txt` file containing URLs).
   - Create a temporary directory in the project root called `temp/` and a subdirectory `temp/extracted-skills/`.

2. **Primary Repository Cloning**:
   - Run `git clone` for each identified primary repository URL into `temp/`.

3. **Repository Triage (Direct Skills vs. Awesome Lists)**:
   - Analyze the structure of each cloned repository to determine its type:
     - **Type 1 (Direct Skills)**: If the repository contains actual skill files (e.g., directories containing `SKILL.md` or equivalent prompts), extract those skill folders/files and move them directly to `temp/extracted-skills/`.
     - **Type 2 (Awesome List)**: If the repository is an index (e.g., a `README.md` containing lists of links to other repositories):
       1. Extract all GitHub URLs pointing to external agent skill repositories.
       2. Run `git clone` on these extracted secondary repositories into `temp/`.
       3. Extract the skill files from these secondary repositories and move them to `temp/extracted-skills/`.

4. **Analyze & Categorize (Green/Yellow/Red)**:
   - Analyze the extracted skills in `temp/extracted-skills/` one by one.
   - Compare each extracted skill's functionality against the existing skills in the `overpowers/skills/` directory (focusing on actual logic and outcomes, not just names).
   - When similarities appear, **analyze carefully case by case and compare.** Do not skip this step, as it is crucial to provide a good analysis and recommendation to the user.
   - Generate a report for the User using the following color-coded system:
     - **🟢 Green (New)**: The skill has no equivalent in `overpowers`.
     - **🟡 Yellow (Overlap/Nuance)**: A similar skill exists, but there are differences in nuances, scripts, or depth.  After carefully assessing, offer the following options:
       - *a) Merge*: Enrich the existing `overpowers` skill with details, scripts, or guides from the new skill. Skills enriched this way should grow in size, complexity, and nuance, NEVER shrink, simplify, or become less detailed.
       - *b) Replace*: Substitute the existing `overpowers` skill with the new one.
       - *c) Skip*: Do not extract/integrate the new skill.
       - *d) Differentiate*: Rewrite the new skill to have a distinctly different function/focus than the existing one.
       - *Include your technical recommendation* (e.g., "For skill X, I recommend option A").
     - **🔴 Red (Duplicate/Inferior)**: The skill is a duplicate or accomplishes the same function but is inferior to the existing `overpowers` skill.

5. **Integration & Refinement**:
   - Present the report and wait for the User to provide feedback.
   - Based on the feedback, integrate the approved skills (Green and selected Yellows) into `overpowers/skills/`.
   - **Crucial**: Ensure all integrated skills obey the current folder naming convention (`type-subtype-nnnn-name`). Create or modify `SKILL.md` files as necessary to fit the `overpowers` standard format.

6. **Cleanup**:
   - Once extraction and integration are fully complete, delete the `temp/` directory completely.
