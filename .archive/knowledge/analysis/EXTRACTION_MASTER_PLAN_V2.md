# Extraction Master Plan V2: Deep Iterative Refinement

**Goal**: Extract remaining value from `AntigravityManager`, `antigravity-tools-linux`, and `antigravity-skills`.

## Iteration 1: Candidate Identification
- `antigravity-skills`: Found `algorithmic-art`, `brand-guidelines`, `canvas-design` (Check if already present, if not, grab them).
- `AntigravityManager`: It's an Electron app. Extracting "Agents" is hard as they might be compiled.
- `antigravity-tools-linux`: Scripts are likely simple helpers.

## Iteration 2: Gap Analysis (Skills)
Comparing `antigravity-skills` vs `skills/`:
- `algorithmic-art`: Present in source? Yes.
- `brand-guidelines`: Present? Yes.
- `canvas-design`: Present? Yes.
- `slack-gif-creator`: Present? Yes.
- `web-artifacts-builder`: Present? Yes.
*Wait, I need to check if I missed any.*

Let's do a rigorous diff in execution.

## Iteration 3: Knowledge Management Refinement
- We have `save-knowledge.py`.
- We can add `benchmark-scripts.py` and `sync-agents-stats.py` from `andy-universal-agent-rules` if they are useful.

## Iteration 4: Docker/Sandbox Refinement
- We already adapted `sanity-gravity`.
- Can we extract `sanity-cli`? It might be a useful wrapper.

## Final Plan
1. **Skills**: Re-run the copy for *all* folders in `antigravity-skills/skills/` to ensuring nothing was missed (using `rsync -av --ignore-existing`).
2. **Scripts**:
   - Extract `sanity-cli` from `sanity-gravity` -> `scripts/sandbox-cli`.
   - Extract any useful bash scripts from `antigravity-tools-linux`.

## Execution Steps
1. `rsync` all skills from external to internal (no overwrite).
2. Copy `sanity-cli` to `scripts/`.
3. Check `antigravity-tools-linux` for `setup.sh` or similar.
