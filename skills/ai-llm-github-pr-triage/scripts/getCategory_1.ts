// CORRECT: Launch all as background tasks, stream results
const taskIds = []

// Category ratio: unspecified-low : writing : quick = 1:2:1
// Every 4 PRs: 1 unspecified-low, 2 writing, 1 quick
function getCategory(index) {
  const position = index % 4
  if (position === 0) return "unspecified-low"  // 25%
  if (position === 1 || position === 2) return "writing"  // 50%
  return "quick"  // 25%
}

// PHASE 1: Launch 1 background task per PR
for (let i = 0; i < allPRs.length; i++) {
  const pr = allPRs[i]
  const category = getCategory(i)

  const taskId = await task(
    category=category,
    load_skills=[],
    run_in_background=true,  // ← CRITICAL: Each PR is independent background task
    prompt=`Analyze PR #${pr.number}...`
  )
  taskIds.push({ pr: pr.number, taskId, category })
  console.log(`🚀 Launched background task for PR #${pr.number} (${category})`)
}

// PHASE 2: Stream results as they complete
console.log(`\n📊 Streaming results for ${taskIds.length} PRs...`)

const completed = new Set()
while (completed.size < taskIds.length) {
  for (const { pr, taskId } of taskIds) {
    if (completed.has(pr)) continue

    // Check if this specific PR's task is done
    const result = await background_output(taskId=taskId, block=false)

    if (result && result.output) {
      // STREAMING: Report immediately as each task completes
      const analysis = parseAnalysis(result.output)
      reportRealtime(analysis)
      completed.add(pr)

      console.log(`\n✅ PR #${pr} analysis complete (${completed.size}/${taskIds.length})`)
    }
  }

  // Small delay to prevent hammering
  if (completed.size < taskIds.length) {
    await new Promise(r => setTimeout(r, 1000))
  }
}
