# Jujutsu (JJ) Version Control Workflow Rules
> **Context:** This rule prevents catastrophic state loss and snapshot desyncs caused by mixing raw Git commands with Jujutsu tracking, especially during dual-agent concurrent execution.

## 1. The Immutable Law of Mutation
**NEVER** use raw `git` commands to mutate repository state.
- 🔴 **FORBIDDEN:** `git commit`, `git add`, `git push`, `git checkout`, `git branch`, `git merge`, `git rebase`, `git reset`, `git restore`.
- 🟢 **ALLOWED (Read-Only):** `git log`, `git show`, `git diff`, `git status` (though `jj` equivalents are strictly preferred).

## 2. The Hierarchical Process (Sprint -> Task)
When managing the lifecycle of features and fixes, follow this strict mapped process using Jujutsu:

1. **Task Completa:** Snapshot the working copy.
   - `jj commit -m "feat/fix: task description"`
   - *(Note: `jj commit` is equivalent to `jj new` + adding a message to the previous revision).*

2. **Story Completa (Nova Branch):** Task is complete, assign it to a development branch.
   - `jj bookmark set development -r @` (marks current state as development)
   - `jj new development` (starts new work on top of it)

3. **Epic Completo (Merge para Staging):** Story is complete, merge into staging.
   - `jj new staging development -m "merge: epic complete into staging"`
   - `jj bookmark set staging -r @`

4. **Sprint/Fase Completa (Merge para Main):** Epic is complete, merge into main.
   - `jj new main staging -m "merge: sprint complete into main"`
   - `jj bookmark set main -r @`

5. **Backup Branch:**
   - The backup branch MUST remain completely untouched until explicit orders. Do not move or rebase its bookmark.

## 3. Merging & Sincronização Harmoniosa
- **Merge com o Jujutsu**: Sempre priorize utilizar a skill de `harmonious-jujutsu-merge` para resolução de conflitos originados dos múltiplos PRs dos agentes Jules.
- **Vantagem Concorrente**: O Jujutsu lida com ramificações simultâneas e modificações conflitantes de forma superior ao Git padrão.
- **PR Merges**: Em fluxos de Auto-Merge com `gh pr merge`, utilize apenas na Happy Path (sem conflitos). Se o GitHub alertar conflito, utilize a skill de merge harmoniosa via Jujutsu.

## 4. Prevenção e Cleanup
- Operações de merge devem ser seguidas de cleanup (exclusão de feature branches) para manter a repo limpa.
- Certifique-se de que nenhum artefato isolado nas workspaces virtuais do Jujutsu escape para o branch principal sem resolução.

## 5. Stress-Test & Vulnerabilities
While this process protects against raw Git conflicts, be aware of the following edge cases:

- **Vulnerability A (Concurrent Execution in Single Workspace):** If Antigravity and Gemini CLI are operating in the *same* working directory concurrently, the working copy is shared. When Agent A runs `jj commit`, it will unintentionally snapshot Agent B's partial work.
  - *Mitigation:* Concurrent agents must operate in completely separate `jj workspaces` (which use git worktrees under the hood).
- **Vulnerability B (Implicit Snapshots):** `jj` automatically snapshots on almost every `jj` command. If the working copy is broken mid-refactor and an agent runs `jj status`, the broken state is saved to the operation log.
- **Vulnerability C (Conflict Resolution Markers):** When merging via `jj new branch1 branch2`, if there are conflicts, `jj` tracks them without embedding `<<<<<<<` markers. An agent could push a conflicted commit if it doesn't verify with `jj status` or `jj resolve`.
