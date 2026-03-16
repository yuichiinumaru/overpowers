if (autoCloseable.length > 0) {
  console.log(`\n🚨 FOUND ${autoCloseable.length} PR(s) ELIGIBLE FOR AUTO-CLOSE:`)

  for (const pr of autoCloseable) {
    console.log(`   #${pr.PR}: ${pr.TITLE} (${pr.CLOSE_REASON})`)
  }

  // Close them one by one with progress
  for (const pr of autoCloseable) {
    console.log(`\n   Closing #${pr.PR}...`)

    await bash({
      command: `gh pr close ${pr.PR} --repo ${REPO} --comment "${pr.CLOSE_MESSAGE}"`,
      description: `Close PR #${pr.PR} with friendly message`
    })

    console.log(`   ✅ Closed #${pr.PR}`)
  }
}
