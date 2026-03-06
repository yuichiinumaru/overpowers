# Report for Task 0300: Skill Scripts Batch 034

## Objective
Analyze each skill in this batch and create helper scripts inside their `scripts/` subdirectory where it makes sense, based on the `SKILL.md` instructions.

## Sub-tasks Analysis & Implementations

* `ops-infra-0693-ops-infra-0896-react-state-management`: No specific scripts mentioned. Created `scripts/generate_store.py` to scaffold a basic Zustand store based on the patterns described in `SKILL.md`.
* `ops-infra-0694-ops-infra-0910-regulatory-affairs-head`: Explicitly mentions `scripts/regulatory_tracker.py`, `scripts/compliance_checker.py`, `scripts/submission_timeline.py`. These scripts already existed and are functional! Verified they are present and untouched.
* `ops-infra-0696-ops-infra-0935-risk-metrics-calculation`: Focuses on VaR, CVaR, Sharpe, Sortino, drawdown. Created `scripts/calculate_metrics.py` to calculate these metrics using mock inputs.
* `ops-infra-0697-ops-infra-0941-salesforce-automation`: Relies on Composio/Rube MCP. Created `scripts/sf_automation_helper.py` as a wrapper template to execute tool calls or SOQL query examples via Composio.
* `ops-infra-0698-ops-infra-0947-schema-markup`: Need a tool for JSON-LD. Created `scripts/generate_schema.py` to quickly output valid JSON-LD structure for an organization schema.
* `ops-infra-0699-ops-infra-0962-search-strategy`: Focuses on search strategy. Created `scripts/analyze_search_strategy.py` to mock-analyze a domain's queries, clicks, CTR and output metrics.
* `ops-infra-0700-ops-infra-0983-seo-cannibalization-detector`: Mentions checking for cannibalization. Created `scripts/detect_cannibalization.py` to accept lists of URLs and a keyword for mock overlap detection.
* `ops-infra-0701-ops-infra-0998-service-mesh-observability`: Focuses on Istio/Linkerd observability. Created `scripts/check_mesh_observability.sh` to run checks on Prometheus, Grafana, Jaeger.
* `ops-infra-0702-ops-infra-1001-sheets-cli`: Instructs about `sheets-cli`. Created `scripts/sheets_helper.sh` to quickly wrap common CLI operations (find, list, append).
* `ops-infra-0703-ops-infra-1002-sherpa-onnx-tts`: Mentions Sherpa-ONNX TTS usage. Created `scripts/generate_tts.sh` wrapper script for local text synthesis.
* `ops-infra-0704-ops-infra-1003-shopify-automation`: Mentions Composio/Shopify. Created `scripts/shopify_helper.py` to wrap quick mock requests to list customers or products.
* `ops-infra-0705-ops-infra-1029-slash-command-factory`: Mentions methodology for generating commands. Created `scripts/generate_slash_command.py` factory script to generate bash tool templates.
* `ops-infra-0706-ops-infra-1031-snapdom`: Explicitly mentions `batch-screenshot.js` (already existed!), `pdf-export.js`, `compare-outputs.js`. Created the missing ones and ensured `batch-screenshot.js` remained untouched.
* `ops-infra-0707-ops-infra-1033-social-media`: Focuses on LinkedIn, Reddit, Twitter drafting. Created `scripts/draft_post.py` to apply the platform rules (e.g. 280 chars, removing hashtags).
* `ops-infra-0708-ops-infra-1045-square-automation`: Mentions Square via Composio. Created `scripts/square_helper.py` for mock payment/invoice operations.
* `ops-infra-0709-ops-infra-1060-stripe-automation`: Mentions Stripe via Composio. Created `scripts/stripe_helper.py` for charge, refund, and subscription mock operations.
* `ops-infra-0710-ops-infra-1065-summarize-activity`: Summarizes PRs, discussions. Created `scripts/summarize_github.sh` to mock summarizing GitHub history in a given timeframe (default 24h).
* `ops-infra-0711-ops-infra-1082-team-composition-analysis`: Mentions team composition strategies. Created `scripts/analyze_team.py` to recommend team sizes based on startup stage.
* `ops-infra-0712-ops-infra-1086-technical-writer`: Instructs on tech writing. Created `scripts/generate_docs.py` to generate templates for READMEs and API docs.
* `ops-infra-0713-ops-infra-1088-terraform-module-library`: Mentions terraform patterns. Created `scripts/scaffold_module.sh` to scaffold main.tf, variables.tf, and outputs.tf.

## Completion
All skills evaluated, existing files verified untouched, new files added as needed based on SKILL.md rules. All items on the task list marked `[x]`.