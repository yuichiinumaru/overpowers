---
description: Clean and organize project memory
category: team-collaboration
---

# Memory Spring Cleaning

Clean and organize project memory

## Instructions

1. **Get Overview**
   - List all AGENTS.md and CLAUDE.local.md files in the project hierarchy

2. **Iterative Review**
   - Process each file systematically, starting with the root `AGENTS.md` file
   - Load the current content
   - Compare documented patterns against actual implementation
   - Identify outdated, incorrect, or missing information

3. **Update and Refactor**
   - For each memory file:
     - Verify all technical claims against the current codebase
     - Remove obsolete information
     - Consolidate duplicate entries
     - Ensure information is in the most appropriate file
   - When information belongs to a specific subcomponent, ensure it's placed correctly:
     - UI-specific patterns → `apps/myproject-ui/AGENTS.md`
     - API conventions → `apps/myproject-api/AGENTS.md`
     - Infrastructure details → `cdk/AGENTS.md` or `infrastructure/AGENTS.md`

4. **Focus on Quality**
   - Prioritize clarity, accuracy, and relevance
   - Remove any information that no longer serves the project
   - Ensure each piece of information is in its most logical location

## Credit

This command is based on the work of Thomas Landgraf: https://thomaslandgraf.substack.com/p/claude-codes-memory-working-with