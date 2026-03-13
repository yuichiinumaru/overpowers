---
description: Transform a macro project idea into a master project specification.
argument-hint: Project idea or path to a master planning document
---

# /01-specify-project (Master Project Specification)

**Context**: Use this workflow during the INCEPTION of a brand new project or a massive multi-epic phase. 

**Goal**: List all conceptualized features and transform them into a cohesive master plan using Specification-First Development (SDD).

## Actions

1. **Understand Input**: Review the raw idea or initial pitch document from the user.

2. **Interview User (Macro Level)**: Ask clarifying questions to extract:
   - **Core Value Proposition**: The overarching goal of the system.
   - **Major Epics/Modules**: Identify the big moving parts of the project.
   - **Minimum Viable Product (MVP)**: What must be included in v1.0 and what can be deferred.

3. **Format & Save**: 
   - Collate the information and create a master planning document, typically `0000-project-master-plan.md` or a comprehensive feature plan.
   - Outline the distinct features that will later require their own individual `01-specify-feature` workflows.
   - **CRITICAL**: No code is to be generated or modified during this stage.
