---
description: Mine GitHub repositories from the curated clone list, batch them into tasks, clone to references/, and extract useful assets, patterns, and ideas for integration.
argument-hint: Optional depth level (shallow|medium|deep) to skip the interactive prompt
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Objective

Transform the curated GitHub repository list into actionable mining tasks by:
1. Counting the repos in the list.
2. Letting the user choose a depth level that controls batch granularity.
3. Generating one task file per batch.
4. Each batch task: clone repos → analyze one by one → extract useful parts → create integration tasks.
5. Offering dispatch options (parallel sub-agents, Jules, or defer).

---

## Execution Flow

### Phase 1 — Superficial Analysis

1. Read `$OVERPOWERS_PATH/.agents/clone-list.md` (where `$OVERPOWERS_PATH` is the project root).
2. Count the total number of GitHub URLs (one per line, ignore blank lines, strip leading `[` or trailing `]` if present).
3. Present a summary to the user:

```
📦 GitHub Repo List Analysis
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total repositories found: {COUNT}
Top orgs/users:     {TOP_5_ORGS} (by frequency)
Estimated topics:   AI agents, OSINT, CLI tools, ... (inferred from repo names)
```

### Phase 2 — Depth Selection

If `$ARGUMENTS` already contains a valid depth level (`shallow`, `medium`, `deep`), use it directly. Otherwise, ask the user:

```
🔍 Select Mining Depth
━━━━━━━━━━━━━━━━━━━━━

┌──────────┬───────────────────┬───────────────┬──────────────────────────────────────┐
│ Level    │ Batch Size        │ Total Batches │ Description                          │
├──────────┼───────────────────┼───────────────┼──────────────────────────────────────┤
│ shallow  │ ~30 repos/batch   │ ~50 batches   │ Quick skim. README + structure only. │
│          │                   │               │ Fast first pass, broad overview.     │
├──────────┼───────────────────┼───────────────┼──────────────────────────────────────┤
│ medium   │ ~15 repos/batch   │ ~100 batches  │ Balanced. README + vertical slice    │
│          │                   │               │ of key modules per repo.             │
├──────────┼───────────────────┼───────────────┼──────────────────────────────────────┤
│ deep     │ ~5 repos/batch    │ ~300 batches  │ Full reverse engineering per repo.   │
│          │                   │               │ 5-step codebase analysis framework.  │
└──────────┴───────────────────┴───────────────┴──────────────────────────────────────┘

Which level do you prefer? (shallow / medium / deep)
```

**Wait for user response before proceeding.**

### Phase 3 — Batch Task Generation

Based on the chosen depth, split the repo list into sequential batches and create one task file per batch.

#### 3.1 Calculate batches

```python
# Pseudocode
BATCH_SIZES = { "shallow": 30, "medium": 15, "deep": 5 }
batch_size = BATCH_SIZES[chosen_level]
total_batches = ceil(total_repos / batch_size)
```

#### 3.2 Ensure task infrastructure

- Verify `docs/tasks/` exists. If not, reference `/ovp-06-scaffold-tasks` to scaffold it.
- Create `.agents/thoughts/repo-mining/` for intermediate reports.

#### 3.3 Create batch task files

For each batch `i` (1..total_batches), create:

**File:** `docs/tasks/planning/8{i:03d}-research-repo-mining-batch-{i}.md`

> **Naming:** Uses the `8xxx` prefix range to avoid collision with regular project tasks and `9xxx` arXiv tasks.

**Template per task file:**

```markdown
# Repo Mining — Batch {i}/{total_batches}

## Metadata
- **Type:** research
- **Subtype:** repo-mining
- **Depth Level:** {chosen_level}
- **Batch:** {i} of {total_batches}
- **Repos in batch:** {actual_count_in_this_batch}

## Objective

Clone, analyze, and extract useful assets from each GitHub repository listed below. For each repo, the goal is to identify:

1. **Reusable code** — functions, modules, components, scripts worth adopting or adapting.
2. **Architectural patterns** — design patterns, system architectures, project structures to learn from.
3. **Skills, agents, workflows, hooks** — any AI agent assets (AGENTS.md, skills/, workflows/) to scavenge.
4. **Ideas for new features** — capabilities or approaches that could enhance the current project.
5. **Dependencies & tools** — useful libraries, frameworks, or CLI tools discovered.

## Repositories

{numbered list of GitHub URLs for this batch}

## Instructions

### Per Repo (sequential within batch):

1. **Clone to references/:**
   ```bash
   git clone --depth 1 {repo_url} references/{repo_name}
   ```
   - Use shallow clone (depth 1) to save space.
   - If clone fails (private repo, deleted, etc.), log error and skip.

2. **Analyze the repo using the appropriate depth:**

   #### Shallow Analysis (depth = shallow):
   - Read `README.md`, `AGENTS.md`, `package.json`/`Cargo.toml`/`pyproject.toml`.
   - List directory structure (1 level).
   - Extract: purpose, tech stack, key features.

   #### Medium Analysis (depth = medium):
   - All of shallow, PLUS:
   - Read entry points (main files, CLI handlers, API routers).
   - Identify top 3 most interesting modules.
   - Read and summarize those modules.
   - Check for AI agent assets (skills/, workflows/, agents/, hooks/).

   #### Deep Analysis (depth = deep):
   - All of medium, PLUS:
   - Apply the **5-Step Vertical Slicing Framework** from `/ovp-codebase-analyzer`:
     1. Ecological Top-Down (dependencies, infra).
     2. Boundary Mapping (entry points).
     3. Vertical Slicing Trace (critical flow).
     4. Data-Oriented Analysis (state & mutations).
     5. Error Mesh & Control Flow.
   - Document complete architecture.
   - Identify ALL extractable assets.

3. **Extract useful assets:**
   - If skills/, agents/, workflows/, hooks/ are found:
     → Use `/ovp-batch-assets-extraction` patterns to stage them.
     → Copy to `.archive/staging/repo-mining/{repo_name}/`.
   - If reusable scripts or utilities are found:
     → Document them in the batch report for manual review.

4. **Log results and move to next repo.**

### After All Repos in Batch:

5. **Produce Batch Report** saved to `.agents/thoughts/repo-mining/batch-{i}-report.md`:

   ```markdown
   # Repo Mining Batch {i} Report

   ## Summary
   - Repos analyzed: {count}
   - Repos skipped (clone failed): {count}
   - Total extractable assets found: {count}
   - Top ideas: {brief list}

   ## Per-Repo Findings

   ### {repo_name_1}
   - **Purpose:** {what it does}
   - **Tech Stack:** {languages, frameworks}
   - **Relevance Score:** {1-5}
   - **Extractable Assets:** {list of skills/agents/workflows/scripts found}
   - **Key Ideas:** {ideas applicable to our codebase}
   - **Status:** analyzed / skipped / error

   ### {repo_name_2}
   ...

   ## Integration Tasks Created
   - [ ] {task description from high-relevance repos}

   ## Repos to Deep-Dive Later
   - {repos with relevance >= 4 that deserve focused analysis}
   ```

6. **Create integration sub-tasks** for high-relevance findings:
   - For each actionable idea with relevance >= 4, create a stub task in `docs/tasks/planning/`.
   - Reference the batch report and specific repo.

## Exit Conditions

- [ ] All {actual_count_in_this_batch} repos have been processed (cloned or skip-logged).
- [ ] Batch report saved to `.agents/thoughts/repo-mining/batch-{i}-report.md`.
- [ ] Extractable assets staged in `.archive/staging/repo-mining/` (if any found).
- [ ] Integration tasks created for high-relevance findings (if any).
```

#### 3.4 Summary

After creating all task files, present:

```
✅ Task Generation Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Level:         {chosen_level}
Batch size:    {batch_size} repos
Total batches: {total_batches}
Task files:    docs/tasks/planning/8001-research-repo-mining-batch-1.md
               ...
               docs/tasks/planning/8{total_batches:03d}-research-repo-mining-batch-{total_batches}.md
Clone target:  references/
Reports dir:   .agents/thoughts/repo-mining/
Staging dir:   .archive/staging/repo-mining/
```

### Phase 4 — Dispatch Options

Present the user with three options for executing the generated tasks:

```
🚀 How would you like to dispatch these {total_batches} tasks?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣  Parallel Sub-Agents (immediate, local)
    Uses /ovp-do-in-parallel to launch sub-agents that process
    batches concurrently. Each sub-agent clones its batch of repos
    to references/ and analyzes them sequentially within the batch.
    → Recommended for: shallow depth, quick survey.
    ⚠️ Disk space: ~{estimated_size} per batch for shallow clones.

2️⃣  Jules Dispatch (background, cloud)
    Uses /ovp-13-jules-dispatch to send batches to Jules agents
    running in their own cloud VMs. Ideal for deep analysis since
    Jules can take its time without blocking local compute.
    → Recommended for: medium/deep depth, large batch counts.

3️⃣  Defer (save for later)
    Tasks are already saved in docs/tasks/planning/.
    Pick them up manually or dispatch later.
    → Recommended for: reviewing tasks before execution.

Which option? (1 / 2 / 3)
```

**Wait for user response.**

#### Option 1 — Parallel Sub-Agents

1. Use the `/ovp-do-in-parallel` workflow.
2. Set `--targets` to the list of batch task file paths.
3. Task description: "Clone the repos listed in the batch task file to references/, analyze each with the specified depth, extract useful assets, and produce a batch report."
4. Model recommendation:
   - `haiku` for shallow (mainly README reading)
   - `sonnet` for medium (balanced analysis)
   - `opus` for deep (full reverse engineering)
5. Launch in groups of 5 batches at a time to avoid overwhelming disk/network.
6. **Important:** Ensure no two parallel agents clone to the same `references/` subdirectory.

#### Option 2 — Jules Dispatch

1. Use the `/ovp-13-jules-dispatch` workflow.
2. For each batch task, synthesize a Jules-compatible JSON prompt.
3. Include the clone step and analysis instructions in the prompt.
4. Dispatch sequentially (Jules handles its own parallelism in cloud).
5. Reference the skill at `skills/ai-llm-jules-dispatch/` for the JSON format.

#### Option 3 — Defer

1. Confirm tasks are saved.
2. Remind user they can dispatch later with:
   - `/ovp-do-in-parallel` for local parallel execution.
   - `/ovp-13-jules-dispatch` for cloud delegation.
3. End workflow.

---

## References

- **Repo list:** `.agents/clone-list.md`
- **Codebase analysis framework:** `/ovp-codebase-analyzer` — 5-step vertical slicing for deep analysis.
- **Deep scan:** `/ovp-07-deep-scan` — parallel codebase scanning with subagents.
- **Scavenge planner:** `prompts/scavenge-planner.md` — reverse engineering and asset extraction prompt.
- **Batch extraction pipeline:** `/ovp-batch-assets-extraction` — full pipeline for extracting skills, agents, workflows, hooks.
- **Clone script:** `skills/ovp-extract-assets/scripts/clone-github-repos.py` — shallow clone utility.
- **Scaffold tasks:** `/ovp-06-scaffold-tasks` — creates `docs/tasks/` structure if missing.
- **Parallel dispatch:** `/ovp-do-in-parallel` — launches sub-agents concurrently.
- **Jules dispatch:** `/ovp-13-jules-dispatch` — delegates to Jules cloud agents.
- **TOML conversion:** After creating this workflow, run `python3 scripts/generators/md-to-toml.py workflows/ workflows/toml/` to generate the Gemini-CLI TOML variant.
