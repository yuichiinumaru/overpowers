---
name: git-master
description: "Git expert for atomic commits, rebase/squash, and history search. Use when you need to commit changes, clean up history, or find who wrote code/when bugs were introduced."
---

# Git Master Skill

This skill provides expert-level Git capabilities for atomic commits, history rewriting, and deep search.

## 1. Commit Mode

### Principles
- **Atomic Commits**: One logical change per commit.
- **Semantic Messages**: `feat:`, `fix:`, `chore:`, `refactor:`, `docs:`, `test:`, `style:`.
- **Verification**: Tests must pass before commit (unless explicitly WIP).

### Workflow
1. **Status Check**: `git status`
2. **Diff Review**: `git diff`
3. **Atomic Staging**: `git add <file>` (group related files)
4. **Commit**: `git commit -m "type(scope): description"`
5. **Verify**: `git log -1`

## 2. Rebase Mode

### Workflow
1. **Fetch**: `git fetch origin`
2. **Rebase**: `git rebase origin/main` (or `origin/master`)
3. **Conflict Resolution**:
   - `git status` (identify conflicts)
   - Edit files to resolve markers (`<<<<`, `====`, `>>>>`)
   - `git add <file>`
   - `git rebase --continue`
4. **Push**: `git push --force-with-lease`

## 3. History Search Mode

### Techniques

| Goal | Command |
|------|---------|
| **When was X added/removed?** | `git log -S "X" --oneline` (Pickaxe) |
| **Who changed this line?** | `git blame -L N,N file.py` |
| **Commit history of file** | `git log --follow -- path/file.py` |
| **Find deleted file** | `git log --all --full-history -- "**/filename"` |
| **Changes matching regex** | `git log -G "pattern" --oneline` |

### Bisect (Bug Hunting)
1. `git bisect start`
2. `git bisect bad` (Current HEAD is broken)
3. `git bisect good <commit-hash>` (Last known working version)
4. Git checks out a middle commit.
5. Test it. Run `git bisect good` or `git bisect bad`.
6. Repeat until culprit found.
7. `git bisect reset`

## Anti-Patterns
- Using `git push --force` (always use `--force-with-lease`).
- Committing unrelated changes together.
- Rebasing shared branches (unless coordinated).
- Assuming the first search result is the answer (verify with context).
