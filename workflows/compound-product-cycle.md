# Compound Product Cycle Workflow

## 1. Overview
This workflow automates the cycle of turning product reports into code.

**Cycle Steps:**
1.  **Ingest**: Reads the latest markdown report from `reports/`.
2.  **Analyze**: Uses an LLM to identify the #1 actionable priority (no DB migrations, low effort).
3.  **Plan**: Creates a feature branch and a Product Requirement Document (PRD).
4.  **Task**: Breaks the PRD into atomic tasks (`prd.json`).
5.  **Execute**: Runs a loop to implement tasks one by one, verifying each step.
6.  **Submit**: Creates a Pull Request with a summary of changes.

---

## 2. Setup

### Configuration
Create `compound.config.json` in the project root:

```json
{
  "tool": "claude",
  "reportsDir": "./reports",
  "outputDir": "./scripts/compound",
  "qualityChecks": ["npm test", "npm run lint"],
  "maxIterations": 10,
  "branchPrefix": "compound/"
}
```

### Environment Variables
Ensure you have API keys set for the analysis step (in `.env.local` or environment):
- `ANTHROPIC_API_KEY` (or `OPENAI_API_KEY`, `OPENROUTER_API_KEY`)

---

## 3. Usage

### Full Automation
Run the pipeline to process the latest report:

```bash
./scripts/compound/auto-compound.sh
```

### Dry Run
See what the agent would pick without creating branches or code:

```bash
./scripts/compound/auto-compound.sh --dry-run
```

---

## 4. Reports Directory
Place your daily/weekly reports in `reports/` as markdown files (e.g., `reports/2023-10-27-user-feedback.md`).

The agent prefers:
- Specific bug reports
- clear UX improvements
- Configuration tweaks
```
