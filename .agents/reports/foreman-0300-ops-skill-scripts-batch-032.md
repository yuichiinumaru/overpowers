# Task Report: Skill Scripts Batch 032

## Goal
Implement helper scripts for 20 skills in Batch 032 (from `ops-infra-0652-ops-infra-0610-linear-automation` to `ops-infra-0671-ops-infra-0727-observability-monitoring-slo-implement`).

## Actions Taken
- Read `docs/tasks/0300-ops-skill-scripts-batch-032.md` to identify the target skills.
- Parsed the skills and checked their respective `SKILL.md` to identify patterns.
- Generated automation helper scripts tailored to each skill using Python parser script:
  - Created `linear-status.sh` for Linear.
  - Created `linkedin-status.sh` for LinkedIn.
  - Created `check-whisper.sh` for ASR.
  - Created `check-ml-tools.sh` for Machine Learning Ops.
  - Created `mailchimp-status.sh` for Mailchimp.
  - Created `build-slides.sh` for Marp Slides.
  - Created `merge-pr.sh` for PR Merging.
  - Created `render-mermaid.sh` for Mermaid.
  - Created `check-mermaid-v11.sh` for Mermaid v11.
  - Created `build-metal.sh` for Metal Kernel.
  - Created `teams-status.sh` for Microsoft Teams.
  - Created `miro-status.sh` for Miro.
  - Created `mixpanel-status.sh` for Mixpanel.
  - Created `check-android-env.sh` for Mobile Android Design.
  - Created `check-ios-env.sh` for Mobile iOS Design.
  - Created `monday-status.sh` for Monday Automation.
  - Created `monitor-experiment.sh` for Monitor Experiment.
  - Created `notion-status.sh` for Notion Automation.
  - Created `list-projects.sh` for Nx Workspace.
  - Created `check-slo-tools.sh` for SLO implementation.

## Results
- Successfully added useful scripts for all 20 skills.
- Marked task sub-items as completed `[x]` in `docs/tasks/0300-ops-skill-scripts-batch-032.md`.
- Updated `continuity.md` to reflect the completed state.
