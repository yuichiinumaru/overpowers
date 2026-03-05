# Planning: Skill Improvements & Standardization

## Overview
Based on the analysis of 1245 skills in the `skills/` directory, several opportunities for standardization and quality improvement have been identified.

## Identified Opportunities

### 1. Metadata Standardization
**Issue**: Inconsistent YAML frontmatter across `SKILL.md` files. Some have `name` and `description`, others only one or none.
**Goal**: Ensure all skills have a valid YAML block with:
- `name`: Human-readable name.
- `description`: Concise summary of the skill's purpose.
- `tags`: List of categories for better discovery.
- `version`: Version tracking for the skill.

### 2. Redundancy Consolidation
**Issue**: Multiple skills for the same tool or concept (e.g., several Mermaid diagramming skills, multiple news aggregators).
**Goal**: Merge redundant skills into single, parameter-aware skills or logical suites.

### 3. Localization & Translation
**Issue**: Some marketing and operational skills are written in Portuguese, while most are in English.
**Goal**: Translate all skills to English (the project's primary language) while maintaining bilingual support where relevant.

### 4. Workflow Section Template
**Issue**: The structure of "How to use" or "Workflow" sections varies wildly.
**Goal**: Implement a standard template for the 'Workflow' section:
- **Inputs**: What the skill needs.
- **Process**: Step-by-step agent actions.
- **Outputs**: Expected artifacts or results.

### 5. Execution Safety & Validation
**Issue**: Shell-based skills (using `nmap`, `ffmpeg`, etc.) often lack explicit safety checks or dependency verification.
**Goal**: Add mandatory 'Pre-flight Checks' to these skills to verify external binaries and provide diagnostic feedback.

### 6. Cross-Linking & Discovery
**Issue**: Related skills (e.g., scientific databases in the ToolUniverse suite) don't consistently link to each other.
**Goal**: Add a `Related Skills` section to all skills to improve agent navigation.

### 7. Memory Persistence Workflows
**Idea**: Update existing workflows to explicitly require reading "memory" (Memcord, Serena, etc.) at the start and updating it at the end.
**Goal**: Ensure continuity across multi-agent handoffs.

### 8. Memcord Sanitization Workflow
**Idea**: Create a workflow to identify project-related memory entries scattered across multiple Memcord slots, consolidate them into a single project slot (using multiple entries), and delete the redundant slots.
**Goal**: Prevent memory fragmentation.

## Proposed Action Plan
1. **Phase 1**: Execute the rename of skill folders based on the `type-subtype-nnnn-name` convention (Automated - DONE).
2. **Phase 2**: Apply metadata standardization across all `SKILL.md` files using a script.
3. **Phase 3**: Manual review and consolidation of redundant skills.
4. **Phase 4**: Translation and localization sweep.
5. **Phase 5**: Fix 82 invalid skills identified by the integrity check (Missing SKILL.md or invalid frontmatter).

## Next Steps
- Review and approve the naming mapping in `.agents/thoughts/skill_mapping.json`.
- Execute Phase 1 (Renaming).
- Initiate detailed planning for Phase 2.
