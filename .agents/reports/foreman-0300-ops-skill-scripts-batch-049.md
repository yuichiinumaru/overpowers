# Task Report: 0300-ops-skill-scripts-batch-049

## Overview
Analyzed skills from `sec-safety-1012-sec-safety-0554-incident-runbook-templates` to `sec-safety-1031-sec-safety-0629-manipulation-detector` to ensure they have relevant helper scripts in their `scripts/` directories based on `SKILL.md` content.

## Actions Taken
Many skills already had existing scripts, but missing scripts were added and tailored to the context provided in their `SKILL.md` files:

1. **`sec-safety-1012-sec-safety-0554-incident-runbook-templates`**: Added `validate-runbook.sh` to ensure structure requirements are met.
2. **`sec-safety-1013-sec-safety-0555-indirect-prompt-injection`**: Scripts already present (`run_tests.py`, `sanitize.py`).
3. **`sec-safety-1014-sec-safety-0572-ios-developer`**: Scripts already present (`check-ios-env.sh`, `clean-ios-project.sh`).
4. **`sec-safety-1015-sec-safety-0577-istio-traffic-management`**: Scripts already present (`istio-debug.sh`, `scaffold-istio.sh`).
5. **`sec-safety-1016-sec-safety-0578-it-operations`**: Scripts already present (`scaffold-incident-report.sh`, `scaffold-rfc.sh`).
6. **`sec-safety-1017-sec-safety-0580-jiang-irac-opposition`**: Scripts already present (`scaffold-irac-brief.sh`).
7. **`sec-safety-1018-sec-safety-0584-jira-issues`**: Scripts already present (`jira-tool.py`).
8. **`sec-safety-1019-sec-safety-0586-jules-dispatch`**: Scripts already present (`list-accounts.sh`, `prepare-dispatch.sh`).
9. **`sec-safety-1020-sec-safety-0589-jules-integrate`**: Scripts already present (`jules-cleanup.sh`, `scaffold-adaptation.sh`).
10. **`sec-safety-1021-sec-safety-0590-jules-triage`**: Scripts already present (`analyze-branch-prompt.sh`, `consolidate-triage.sh`).
11. **`sec-safety-1022-sec-safety-0591-k8s-manifest-generator`**: Created `validate-manifest.sh` to validate generated manifests with kubectl/yq.
12. **`sec-safety-1023-sec-safety-0592-k8s-security-policies`**: Created `validate-policy.sh` to check policy YAML syntax and optionally use kubescape.
13. **`sec-safety-1024-sec-safety-0599-kreuzberg`**: Created `extract-text.py` to extract text and metadata.
14. **`sec-safety-1025-sec-safety-0600-labarchive-integration`**: Created `api-check.sh` to test connection & token config.
15. **`sec-safety-1026-sec-safety-0601-lamindb`**: Created `init-lamin.py` to bootstrap db.
16. **`sec-safety-1027-sec-safety-0611-linear-claude-skill`**: Created `list-issues.sh` querying via GraphQL.
17. **`sec-safety-1028-sec-safety-0614-linkerd-patterns`**: Created `check-mesh.sh` using linkerd check.
18. **`sec-safety-1029-sec-safety-0615-linux-privilege-escalation`**: Created `enum-linux.sh` for standard enum checks.
19. **`sec-safety-1030-sec-safety-0620-llm-security`**: Created `audit-llm-app.sh` checking against OWASP Top 10 for LLM.
20. **`sec-safety-1031-sec-safety-0629-manipulation-detector`**: Scripts already present (`detect.py`).

Task list in `docs/tasks/0300-ops-skill-scripts-batch-049.md` was updated (all sub-tasks checked and status set to `[x]`).

## Conclusion
Batch 049 processed successfully. All skills now possess actionable helper scripts inside `scripts/`.
