---
name: asset-extraction
description: System for mass extraction, semantic deduplication, and standardization of agents, skills, and workflows from external repositories into the Overpowers ecosystem.
tags:
- automation
- ingestion
- deduplication
- python
source: overpowers/scripts
license: MIT
version: 1.0.0
category: ai-llm
---

# Asset Extraction System

This skill provides a pipeline for ingesting hundreds or thousands of agent assets (skills, prompts, workflows, hooks) from cloned repositories, analyzing them for novelty, and standardizing them into the Overpowers format.

## The Pipeline Workflow

### 1. Discovery & Cross-Reference Analysis
Finds all potential candidate files in a target directory and compares them against the existing Overpowers repository using semantic text similarity.

**Script:** `scripts/analyze_references.py`
- Scans target directory for `.md` files, `SKILL.md`, and hooks.
- Compares candidates against existing assets to prevent regressions or exact duplicates.
- Outputs `YES` (new), `MAYBE` (similar/updates), and `NO` (exact duplicates) lists to `.archive/temp/`.

### 2. Categorization
Determines the functional type of each new candidate (Agent, Skill, Workflow, Hook) using content heuristics and structural markers.

**Script:** `scripts/categorize_candidates.py`
- Analyzes file content for YAML frontmatter, specific headers (`# command:`), and keywords (`Role:`, `<skill>`).
- Splits the `YES` list into category-specific JSON manifests.

### 3. Intra-Candidate Deduplication
Because candidates often come from multiple forked repositories, the `YES` list itself contains internal duplicates. This step clusters the candidates by similarity and picks a single representative file per cluster to move to staging.

**Script:** `scripts/deduplicate_candidates.py`
- Compares candidates within each category (Skills, Agents, Workflows, Hooks).
- Chooses the richest/longest version of duplicates.
- Copies the final unique files to `.archive/staging/{category}/`.
- Generates `.archive/staging/manifest.json`.

### 4. Task Generation & Execution
Instead of processing thousands of files in a single pass, this system generates bite-sized task lists (25 items per batch) and updates the global `.docs/tasklist.json`.

**Script:** `scripts/generate_extraction_tasks.py`
- Reads `.archive/staging/manifest.json`.
- Uses the `000-template-extraction-task.md` to generate batch tasks (e.g., `0500-extraction-skills-batch-001.md`).
- Appends the new tasks to `.docs/tasklist.json`.

**Workflow:** `workflows/ovp-extract-assets.md`
- Agents use the command `/ovp-extract-assets <task-file>` to pick up a batch.
- They read the staged file, apply the Overpowers standards (YAML frontmatter, naming conventions), move it to the final directory, delete it from staging, and check off the box in the task file.

## Usage

When you need to ingest a new folder of cloned repositories (e.g., `~/Work/references`):

1. **Run Analysis:**
   ```bash
   python3 skills/ai-llm-asset-extraction/scripts/analyze_references.py
   ```

2. **Run Categorization:**
   ```bash
   python3 skills/ai-llm-asset-extraction/scripts/categorize_candidates.py
   ```

3. **Run Deduplication:**
   ```bash
   python3 skills/ai-llm-asset-extraction/scripts/deduplicate_candidates.py
   ```

4. **Generate Tasks:**
   ```bash
   python3 skills/ai-llm-asset-extraction/scripts/generate_extraction_tasks.py
   ```

5. **Start Extracting (Parallel execution):**
   Open multiple sessions and assign each a different batch:
   ```text
   /ovp-extract-assets 0500-extraction-skills-batch-001.md
   ```
