const results = []
const autoCloseable = []
const readyToMerge = []
const needsReview = []
const needsWork = []
const stale = []
const drafts = []

const completedPRs = new Set()
const totalPRs = taskMap.size

console.log(`\n📊 Streaming results for ${totalPRs} PRs...`)

// Stream results as each background task completes
while (completedPRs.size < totalPRs) {
  let newCompletions = 0

  for (const [prNumber, taskId] of taskMap) {
    if (completedPRs.has(prNumber)) continue

    // Non-blocking check for this specific task
    const output = await background_output(task_id=taskId, block=false)

    if (output && output.length > 0) {
      // Parse the completed analysis
      const analysis = parseAnalysis(output)
      results.push(analysis)
      completedPRs.add(prNumber)
      newCompletions++

      // REAL-TIME STREAMING REPORT
      console.log(`\n🔄 PR #${prNumber}: ${analysis.TITLE.substring(0, 60)}...`)

      // Immediate categorization & reporting
      if (analysis.CLOSE_ELIGIBLE === 'YES') {
        autoCloseable.push(analysis)
        console.log(`   ⚠️  AUTO-CLOSE CANDIDATE: ${analysis.CLOSE_REASON}`)
      } else if (analysis.MERGE_READY === 'YES') {
        readyToMerge.push(analysis)
        console.log(`   ✅ READY TO MERGE`)
      } else if (analysis.RECOMMENDATION === 'REVIEW') {
        needsReview.push(analysis)
        console.log(`   👀 NEEDS REVIEW`)
      } else if (analysis.RECOMMENDATION === 'WAIT') {
        needsWork.push(analysis)
        console.log(`   ⏳ WAITING FOR AUTHOR`)
      } else if (analysis.STALENESS === 'STALE' || analysis.STALENESS === 'ABANDONED') {
        stale.push(analysis)
        console.log(`   💤 ${analysis.STALENESS}`)
      } else {
        drafts.push(analysis)
        console.log(`   📝 DRAFT`)
      }

      console.log(`   📊 Action: ${analysis.ACTION_NEEDED}`)

      // Progress update every 5 completions
      if (completedPRs.size % 5 === 0) {
        console.log(`\n📈 PROGRESS: ${completedPRs.size}/${totalPRs} PRs analyzed`)
        console.log(`   Ready: ${readyToMerge.length} | Review: ${needsReview.length} | Wait: ${needsWork.length} | Stale: ${stale.length} | Draft: ${drafts.length} | Close-Candidate: ${autoCloseable.length}`)
      }
    }
  }

  // If no new completions, wait briefly before checking again
  if (newCompletions === 0 && completedPRs.size < totalPRs) {
    await new Promise(r => setTimeout(r, 2000))
  }
}

console.log(`\n✅ All ${totalPRs} PRs analyzed`)
