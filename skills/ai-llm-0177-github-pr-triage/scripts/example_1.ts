// Create todos immediately
todowrite([
  { id: "1", content: "Fetch all open PRs with exhaustive pagination", status: "in_progress", priority: "high" },
  { id: "2", content: "Launch 1 background task per PR (1 PR = 1 task)", status: "pending", priority: "high" },
  { id: "3", content: "Stream-process results as each task completes", status: "pending", priority: "high" },
  { id: "4", content: "Execute conservative auto-close for eligible PRs", status: "pending", priority: "high" },
  { id: "5", content: "Generate final comprehensive report", status: "pending", priority: "high" }
])
