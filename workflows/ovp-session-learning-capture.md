---
description: Capture and document session learnings
category: team-collaboration
allowed-tools: Glob
---

# Session Learning Capture

Capture and document session learnings

## Instructions

1. **Identify Session Learnings**
   - Review if during your session:
     - You learned something new about the project
     - I corrected you on a specific implementation detail
     - I corrected source code you generated
     - You struggled to find specific information and had to infer details about the project
     - You lost track of the project structure and had to look up information in the source code

2. **Determine Appropriate File**
   - Choose the right file for the information:
     - `AGENTS.md` for shared context that should be version controlled
     - `CLAUDE.local.md` for private notes and developer-specific settings
     - Subdirectory `AGENTS.md` for component-specific information

3. **Memory File Types Summary**
   - **Shared Project Memory (`AGENTS.md`):**
     - Located in the repository root or any working directory
     - Checked into version control for team-wide context sharing
     - Loaded recursively from the current directory up to the root
   - **Local, Non-Shared Memory (`CLAUDE.local.md`):**
     - Placed alongside or above working files, excluded from version control
     - Stores private, developer-specific notes and settings
     - Loaded recursively like `AGENTS.md`
   - **On-Demand Subdirectory Loading:**
     - `AGENTS.md` files in child folders are loaded only when editing files in those subfolders
     - Prevents unnecessary context bloat
   - **Global User Memory (`~/.claude/AGENTS.md`):**
     - Acts as a personal, cross-project memory
     - Automatically merged into sessions under your home directory

4. **Update Memory Files**
   - Add relevant, non-obvious information that should be persisted
   - Ensure proper placement based on component relevance:
     - UI-specific information → `apps/[project]-ui/AGENTS.md`
     - API-specific information → `apps/[project]-api/AGENTS.md`
     - Infrastructure information → `cdk/AGENTS.md` or `infrastructure/AGENTS.md`
   - This ensures important knowledge is retained and available in future sessions

## Credit

This command is based on the work of Thomas Landgraf: https://thomaslandgraf.substack.com/p/claude-codes-memory-working-with