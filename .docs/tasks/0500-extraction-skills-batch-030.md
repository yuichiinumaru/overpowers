# Extraction Task: 0500-extraction-skills-batch-030

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-030` to execute this task or follow these manual steps for each item:

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

- [x] `.archive/staging/skills/weekly-report_SKILL.md` (Original: weekly-report) → `skills/weekly-report-generator/SKILL.md`
- [x] `.archive/staging/skills/org-learning-ops-skill_SKILL.md` (Original: org-learning-ops-skill) → `skills/org-learning-ops/SKILL.md`
- [x] `.archive/staging/skills/openclaw-feishu-optimizer_SKILL.md` (Original: openclaw-feishu-optimizer) → `skills/openclaw-feishu-optimizer/SKILL.md`
- [x] `.archive/staging/skills/filesystem-access_SKILL.md` (Original: filesystem-access) → `skills/filesystem-access/SKILL.md`
- [x] `.archive/staging/skills/conan-weekly-report_SKILL.md` (Original: conan-weekly-report) → `skills/conan-weekly-report/SKILL.md`
- [x] `.archive/staging/skills/radiation-data_SKILL.md` (Original: radiation-data) → `skills/medical-radiation-data/SKILL.md`
- [x] `.archive/staging/skills/rehabilitation_SKILL.md` (Original: rehabilitation) → `skills/rehabilitation-tracker/SKILL.md`
- [x] `.archive/staging/skills/report_SKILL.md` (Original: report) → `skills/health-report-generator/SKILL.md`
- [x] `.archive/staging/skills/save-report_SKILL.md` (Original: save-report) → `skills/medical-report-saver/SKILL.md`
- [x] `.archive/staging/skills/skin-health_SKILL.md` (Original: skin-health) → `skills/skin-health-tracker/SKILL.md`
- [x] `.archive/staging/skills/diankeyuan-contacts_SKILL.md` (Original: diankeyuan-contacts) → `skills/diankeyuan-contacts/SKILL.md`
- [x] `.archive/staging/skills/zsxq-fetch_SKILL.md` (Original: zsxq-fetch) → `skills/zsxq-fetch/SKILL.md`
- [x] `.archive/staging/skills/ai-contract-review-cn_SKILL.md` (Original: ai-contract-review-cn) → `skills/ai-contract-review-cn/SKILL.md`
- [x] `.archive/staging/skills/ai-data-analyst-cn_SKILL.md` (Original: ai-data-analyst-cn) → `skills/ai-data-analyst-cn/SKILL.md`
- [x] `.archive/staging/skills/ai-financial-report-cn-payment_SKILL.md` (Original: ai-financial-report-cn-payment) → `skills/ai-financial-report-cn-payment/SKILL.md`
- [x] `.archive/staging/skills/ai-financial-report-cn_SKILL.md` (Original: ai-financial-report-cn) → `skills/ai-financial-report-cn/SKILL.md`
- [x] `.archive/staging/skills/ai-fitness-coach-cn_SKILL.md` (Original: ai-fitness-coach-cn) → `skills/ai-fitness-coach-cn/SKILL.md`
- [x] `.archive/staging/skills/ai-food-recommendation-cn_SKILL.md` (Original: ai-food-recommendation-cn) → `skills/ai-food-recommendation-cn/SKILL.md`
- [x] `.archive/staging/skills/smart-resume-optimizer-cn-payment_SKILL.md` (Original: ai-learning-planner-cn-payment) → `skills/smart-resume-optimizer-cn-payment/SKILL.md`
- [x] `.archive/staging/skills/ai-learning-planner-cn_SKILL.md` (Original: ai-learning-planner-cn) → `skills/ai-learning-planner-cn/SKILL.md`
- [x] `.archive/staging/skills/ai-prompt-optimizer-cn-payment_SKILL.md` (Original: ai-prompt-optimizer-cn-payment) → `skills/ai-prompt-optimizer-cn-payment/SKILL.md`
- [x] `.archive/staging/skills/ai-prompt-optimizer-cn-v1-1_SKILL.md` (Original: ai-prompt-optimizer-cn-v1-1) → `skills/ai-prompt-optimizer-cn-v1-1/SKILL.md`
- [x] `.archive/staging/skills/ai-prompt-optimizer-cn_SKILL.md` (Original: ai-prompt-optimizer-cn) → `skills/ai-prompt-optimizer-cn/SKILL.md`
- [x] `.archive/staging/skills/ai-real-estate-cn_SKILL.md` (Original: ai-real-estate-cn) → `skills/ai-real-estate-cn/SKILL.md`
- [x] `.archive/staging/skills/ai-travel-planner-cn_SKILL.md` (Original: ai-travel-planner-cn) → `skills/ai-travel-planner-cn/SKILL.md`

**Processing Notes:**
- All 25 skills processed successfully
- Standardized frontmatter applied (name, description, tags, version, category)
- All descriptions are non-empty and clear
- Original files removed from staging directory


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
