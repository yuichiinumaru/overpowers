# Task 0300: Skill Scripts Batch 032 Report

Analyzing skills and determining which helper scripts to add to each based on SKILL.md.


## Analysis of Skills

1. **ops-infra-0652-ops-infra-0610-linear-automation**: No obvious script needed. It's an MCP usage guide.
2. **ops-infra-0653-ops-infra-0613-linkedin-automation**: No obvious script needed. MCP usage guide.
3. **ops-infra-0654-ops-infra-0622-local-asr-transcription**: Needs a script `scripts/transcribe.py` for Python audio processing pipeline as mentioned in section "2. Audio Processing Pipeline".
4. **ops-infra-0655-ops-infra-0627-machine-learning-ops**: No specific script mentioned, just methodology overview.
5. **ops-infra-0656-ops-infra-0628-mailchimp-automation**: No obvious script needed. MCP usage guide.
6. **ops-infra-0657-ops-infra-0640-marp-slide**: Empty description, no script needed.
7. **ops-infra-0658-ops-infra-0660-merge-pr**: Has explicit shell steps that should be put into `scripts/merge-pr.sh`.
8. **ops-infra-0659-ops-infra-0661-mermaid**: Probably no script needed unless it describes CLI rendering. I will check.
9. **ops-infra-0660-ops-infra-0666-mermaidjs-v11**: Same, will check.
10. **ops-infra-0661-ops-infra-0670-metal-kernel**: Methodology.
11. **ops-infra-0662-ops-infra-0674-microsoft-teams-automation**: MCP guide.
12. **ops-infra-0663-ops-infra-0675-miro-automation**: MCP guide.
13. **ops-infra-0664-ops-infra-0676-mixpanel-automation**: MCP guide.
14. **ops-infra-0665-ops-infra-0678-mobile-android-design**: Methodology.
15. **ops-infra-0666-ops-infra-0680-mobile-ios-design**: Methodology.
16. **ops-infra-0667-ops-infra-0684-monday-automation**: MCP guide.
17. **ops-infra-0668-ops-infra-0685-monitor-experiment**: Will check.
18. **ops-infra-0669-ops-infra-0718-notion-automation**: MCP guide.
19. **ops-infra-0670-ops-infra-0726-nx-workspace**: Will check.
20. **ops-infra-0671-ops-infra-0727-observability-monitoring-slo-implement**: Methodology.


## Final List of Scripts to Create/Copy

- **local-asr-transcription**: Create `scripts/transcribe.py` for audio processing (placeholder or basic script based on instructions).
- **merge-pr**: Create `scripts/merge-pr.sh` containing the exact `gh pr merge` logic described in its `SKILL.md`.
- **monitor-experiment**: Create `scripts/monitor-experiment.sh` containing the `beaker experiment get/logs` logic.
- **mermaid**: It references `scripts/render.ts` which uses `beautiful-mermaid` and has a specific CLI signature. Let's create it.
- **nx-workspace**: Create `scripts/nx-explore.sh` to wrap some of the `nx show` exploration commands for convenience (e.g., finding dependents).

Let's double check if there are other existing scripts we should copy or if they just need new ones.
