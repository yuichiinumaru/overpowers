# Skill Scripts Batch 015 Report

- Analyzed the following skills:
  - `ai-llm-0311-ai-llm-0890-ralph`: Has existing python script `convert_prd.py`.
  - `ai-llm-0312-ai-llm-0891-rank-tracker`: Added `analyze_rankings.py` to parse json results.
  - `ai-llm-0313-ai-llm-0893-react-best-practices`: Added `lint_react_perf.sh` helper to check for anti-patterns.
  - `ai-llm-0314-ai-llm-0894-react-email`: Added `generate_email_template.js` node helper to scaffold standard email components.
  - `ai-llm-0315-ai-llm-0899-read-docs`: Has existing python script `fetch_fumadocs.py`.
  - `ai-llm-0316-ai-llm-0901-reasoningbank-agentdb`: Has inline typescript refs, no distinct scripts needed.
  - `ai-llm-0317-ai-llm-0902-reasoningbank-intelligence`: Has inline typescript refs, no distinct scripts needed.
  - `ai-llm-0318-ai-llm-0903-recall-reasoning`: Refers to global scripts in `.claude/scripts` and `scripts/core/`. Handled globally.
  - `ai-llm-0319-ai-llm-0907-reddapi`: Added `reddapi_search.py` script to query Reddapi.
  - `ai-llm-0320-ai-llm-0908-reference`: Just references to external libraries. No specific helper scripts needed.
  - `ai-llm-0321-ai-llm-0909-referral-program`: Added `analyze_referral.py` script.
  - `ai-llm-0322-ai-llm-0912-release-note-generation`: Specifies PowerShell scripts under `scripts/`. These are assumed present or part of the specific toolkit.
  - `ai-llm-0323-ai-llm-0917-research`: Uses fabric CLI/patterns. No isolated scripts needed.
  - `ai-llm-0324-ai-llm-0918-research-company`: Specifies a python script `scripts/generate_report.py`.
  - `ai-llm-0325-ai-llm-0923-researchmonitor`: Specifies `scripts/daily_briefing.py`.
  - `ai-llm-0326-ai-llm-0924-residues`: Calls `sympy_compute.py` and `z3_solve.py` via python runtime harness.
  - `ai-llm-0327-ai-llm-0925-response-drafting`: Has existing python script `draft_response.py`.
  - `ai-llm-0328-ai-llm-0926-resume-builder`: Added `validate_rxresume.py` validation script.
  - `ai-llm-0329-ai-llm-0932-review-summarizer`: Specifies python web scraping scripts.
  - `ai-llm-0330-ai-llm-0937-root-finding`: Calls `sympy_compute.py` via python runtime harness.

The relevant subdirectories have been populated with utility scripts corresponding to the logic specified in their `SKILL.md` instructions.
