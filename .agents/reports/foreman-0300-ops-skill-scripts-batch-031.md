# Task 0300: Skill Scripts Batch 031

**Status**: [x] Completed
**Type**: ops

## Summary
Analyzed the provided skills and created helper scripts inside their `scripts/` subdirectory where it made sense.

Specifically, added scripts for:
- `html2pptx`: created a script to generate PPTX from HTML template in `skills/ops-infra-0640-ops-infra-0532-html2pptx/scripts/generate_pptx.js`.
- `infographic-creator`: created a script to generate SVG infographics from HTML template in `skills/ops-infra-0643-ops-infra-0557-infographic-creator/scripts/generate-infographic.py`.
- `issue-triage`: created three scripts (`init-triage-session.ps1`, `query-issues.ps1`, `record-triage.ps1`) in `skills/ops-infra-0647-ops-infra-0576-issue-triage/scripts/`.

The rest of the skills (`github-issues`, `gitlab-automation`, `google-analytics-automation`, `google-calendar-automation`, `google-workspace`, `googlesheets-automation`, `grafana-dashboards`, `hubspot-automation`, `imsg`, `interactive-portfolio`, `intercom-automation`, `internal-comms`, `jira-automation`, `klaviyo-automation`, `knowledge-synthesis`, `kpi-dashboard-design`) had no clear use cases for additional helper scripts based on their `SKILL.md` definitions since they interact mostly with existing APIs via Composio without specifying bundled scripts.

All tasks marked as completed.
