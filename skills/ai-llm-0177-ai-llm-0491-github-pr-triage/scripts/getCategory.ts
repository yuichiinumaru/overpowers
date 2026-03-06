// Collection for tracking
const taskMap = new Map()  // prNumber -> taskId

// Category ratio: unspecified-low : writing : quick = 1:2:1
// Every 4 PRs: 1 unspecified-low, 2 writing, 1 quick
function getCategory(index) {
  const position = index % 4
  if (position === 0) return "unspecified-low"  // 25%
  if (position === 1 || position === 2) return "writing"  // 50%
  return "quick"  // 25%
}

// Launch 1 background task per PR
for (let i = 0; i < allPRs.length; i++) {
  const pr = allPRs[i]
  const category = getCategory(i)

  console.log(`🚀 Launching background task for PR #${pr.number} (${category})...`)

  const taskId = await task(
    category=category,
    load_skills=[],
    run_in_background=true,  // ← BACKGROUND TASK: Each PR runs independently
    prompt=`
## TASK
Analyze GitHub PR #${pr.number} for ${REPO}.

## PR DATA
- Number: #${pr.number}
- Title: ${pr.title}
- State: ${pr.state}
- Author: ${pr.author.login}
- Created: ${pr.createdAt}
- Updated: ${pr.updatedAt}
- Labels: ${pr.labels.map(l => l.name).join(', ')}
- Head Branch: ${pr.headRefName}
- Base Branch: ${pr.baseRefName}
- Is Draft: ${pr.isDraft}
- Mergeable: ${pr.mergeable}

## PR BODY
${pr.body}

## FETCH ADDITIONAL CONTEXT
1. Fetch PR comments: gh pr view ${pr.number} --repo ${REPO} --json comments
2. Fetch PR reviews: gh pr view ${pr.number} --repo ${REPO} --json reviews
3. Fetch PR files changed: gh pr view ${pr.number} --repo ${REPO} --json files
4. Check if branch exists: git ls-remote --heads origin ${pr.headRefName}
5. Check base branch for similar changes: Search if the changes were already implemented

## ANALYSIS CHECKLIST
1. **MERGE_READY**: Can this PR be merged? (approvals, CI passed, no conflicts, not draft)
2. **PROJECT_ALIGNED**: Does this PR align with current project direction?
3. **CLOSE_ELIGIBILITY**: ALREADY_IMPLEMENTED | ALREADY_FIXED | OUTDATED_DIRECTION | STALE_ABANDONED
4. **STALENESS**: ACTIVE (<30d) | STALE (30-180d) | ABANDONED (180d+)

## CONSERVATIVE CLOSE CRITERIA
MAY CLOSE ONLY IF:
- Exact same change already exists in main
- A merged PR already solved this differently
- Project explicitly deprecated the feature
- Author unresponsive for 6+ months despite requests

## RETURN FORMAT (STRICT)
\`\`\`
PR: #${pr.number}
TITLE: ${pr.title}
MERGE_READY: [YES|NO|NEEDS_WORK]
ALIGNED: [YES|NO|UNCLEAR]
CLOSE_ELIGIBLE: [YES|NO]
CLOSE_REASON: [ALREADY_IMPLEMENTED|ALREADY_FIXED|OUTDATED_DIRECTION|STALE_ABANDONED|N/A]
STALENESS: [ACTIVE|STALE|ABANDONED]
RECOMMENDATION: [MERGE|CLOSE|REVIEW|WAIT]
CLOSE_MESSAGE: [Friendly message if CLOSE_ELIGIBLE=YES, else "N/A"]
ACTION_NEEDED: [Specific action for maintainer]
\`\`\`
`
  )

  // Store task ID for this PR
  taskMap.set(pr.number, taskId)
}

console.log(`\n✅ Launched ${taskMap.size} background tasks (1 per PR)`)
