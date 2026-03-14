# Extraction Task: 0500-extraction-skills-batch-047

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-047` to execute this task or follow these manual steps for each item:

1. **Read & Analyze**: Read the staged file to understand its purpose.
2. **Format & Standardize**: 
   - Inject the appropriate YAML frontmatter (name, description, tags, version: 1.0.0).
   - Ensure the name follows the standard convention (e.g., `domain-subdomain-name`).
   - Fix any broken internal links or outdated formatting.
3. **Move to Destination**: Save the formatted file to its final destination:
   - Skills -> `skills/<domain>-<subdomain>-<name>/SKILL.md`
   - Agents -> `agents/ovp-<name>.md`
   - Workflows -> `workflows/ovp-<name>.md`
4. **Clean Up**: Delete the file from the staging folder.
5. **Check off**: Mark the checkbox below.

## Batch Items

- [ ] `.archive/staging/skills/stock-technical-analysis_SKILL.md` (Original: stock-technical-analysis)
- [ ] `.archive/staging/skills/token-sniper-degen_SKILL.md` (Original: token-sniper-degen)
- [ ] `.archive/staging/skills/whale-alerts_SKILL.md` (Original: whale-alerts)
- [ ] `.archive/staging/skills/finance-agent_SKILL.md` (Original: finance-agent)
- [ ] `.archive/staging/skills/a-stock-data_SKILL.md` (Original: a-stock-data)
- [ ] `.archive/staging/skills/card-renderer_SKILL.md` (Original: card-renderer)
- [ ] `.archive/staging/skills/wechat-toolkit_SKILL.md` (Original: wechat-toolkit)
- [ ] `.archive/staging/skills/stock-board_SKILL.md` (Original: stock-board)
- [ ] `.archive/staging/skills/stock_SKILL.md` (Original: stock)
- [ ] `.archive/staging/skills/playwright-controller_SKILL.md` (Original: playwright-controller)
- [ ] `.archive/staging/skills/smart-money-v2_SKILL.md` (Original: smart-money-v2)
- [ ] `.archive/staging/skills/token-unlock-pro_SKILL.md` (Original: token-unlock-pro)
- [ ] `.archive/staging/skills/agent-advisor_SKILL.md` (Original: agent-advisor)
- [ ] `.archive/staging/skills/openclaw-ticket-assistant_SKILL.md` (Original: openclaw-ticket-assistant)
- [ ] `.archive/staging/skills/autonomy-gate_SKILL.md` (Original: autonomy-gate)
- [ ] `.archive/staging/skills/cs-autoresponder_SKILL.md` (Original: cs-autoresponder)
- [ ] `.archive/staging/skills/daily-sales-digest_SKILL.md` (Original: daily-sales-digest)
- [ ] `.archive/staging/skills/korean-invoice_SKILL.md` (Original: korean-invoice)
- [ ] `.archive/staging/skills/mufi-email-manager_SKILL.md` (Original: mufi-email-manager)
- [ ] `.archive/staging/skills/review-manager_SKILL.md` (Original: review-manager)
- [ ] `.archive/staging/skills/unified-invoice_SKILL.md` (Original: unified-invoice)
- [ ] `.archive/staging/skills/qweather_SKILL.md` (Original: qweather)
- [ ] `.archive/staging/skills/automation-tool_SKILL.md` (Original: automation-tool)
- [ ] `.archive/staging/skills/frontend-agent_SKILL.md` (Original: frontend-agent)
- [ ] `.archive/staging/skills/income-explorer_SKILL.md` (Original: income-explorer)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
