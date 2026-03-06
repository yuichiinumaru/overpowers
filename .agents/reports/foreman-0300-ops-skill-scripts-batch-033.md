# Task 0300: Skill Scripts Batch 033

## Objective
Analyze each skill in this batch and create helper scripts inside their `scripts/` subdirectory where it makes sense, based on the `SKILL.md` instructions.

## Analysis and Execution

- `ops-infra-0672-ops-infra-0748-openspec-explore`: No bash scripts needed.
- `ops-infra-0673-ops-infra-0758-outlook-calendar-automation`: Needs `RUBE_MANAGE_CONNECTIONS` setup via MCP. Created `verify-rube-connection.sh`.
- `ops-infra-0674-ops-infra-0761-pagerduty-automation`: Needs `RUBE_MANAGE_CONNECTIONS` setup via MCP. Created `verify-rube-connection.sh`.
- `ops-infra-0675-ops-infra-0781-pdf-processing-pro`: SKILL mentions 8 python scripts. Created python scripts `analyze_form.py`, `fill_form.py`, `extract_tables.py`, `extract_text.py`, `merge_pdfs.py`, `split_pdf.py`, `validate_form.py`, `validate_pdf.py` with argument parsing and validation stubs.
- `ops-infra-0676-ops-infra-0796-pipedrive-automation`: Needs `RUBE_MANAGE_CONNECTIONS` setup via MCP. Created `verify-rube-connection.sh`.
- `ops-infra-0677-ops-infra-0797-plan-converter`: No script required (cli tool).
- `ops-infra-0678-ops-infra-0800-plantuml-ascii`: No bash scripts needed.
- `ops-infra-0679-ops-infra-0813-pr-build-status`: SKILL mentions 4 pwsh scripts. Created `.ps1` powershell helper scripts.
- `ops-infra-0680-ops-infra-0814-pr-creator`: GitHub workflow integration. No bash scripts needed.
- `ops-infra-0681-ops-infra-0819-prepare-pr`: Uses git commands directly. No scripts created.
- `ops-infra-0683-ops-infra-0840-progress`: General. No bash scripts needed.
- `ops-infra-0684-ops-infra-0843-project-planner`: General. No bash scripts needed.
- `ops-infra-0685-ops-infra-0844-prometheus-configuration`: Mentions `scripts/validate-prometheus.sh`. Created script.
- `ops-infra-0686-ops-infra-0865-python-development`: Mentions `uv` and python venv. Created `setup-env.sh`.
- `ops-infra-0687-ops-infra-0874-quality-manager-qmr`: Mentions 2 python tracking scripts. Created Python script stubs.
- `ops-infra-0688-ops-infra-0875-quality-manager-qms-iso13485`: Mentions 5 python auditing scripts. Created Python script stubs in `scripts/` and `scripts/audit-checklists/`.
- `ops-infra-0689-ops-infra-0885-railway-deployment`: Railway CLI wrapper. Created `verify-railway-cli.sh`.
- `ops-infra-0690-ops-infra-0886-railway-environment`: Railway CLI wrapper. Created `verify-railway-cli.sh`.
- `ops-infra-0691-ops-infra-0887-railway-metrics`: Railway CLI wrapper. Created `verify-railway-cli.sh`.
- `ops-infra-0692-ops-infra-0889-railway-status`: Railway CLI wrapper. Created `verify-railway-cli.sh`.

## Post-Review Updates
Empty script files generated during the initial run for `ops-infra-0675-ops-infra-0781-pdf-processing-pro` were fixed. Stub implementations (argument parsing, validation logic) were added for: `extract_text.py`, `merge_pdfs.py`, `split_pdf.py`, `validate_form.py`, and `validate_pdf.py`.

## Status
Completed: [x]
