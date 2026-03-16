# Extraction Task: 0500-extraction-skills-batch-079

**Batch Type:** skills
**Total Items:** 17

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-079` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/tencentcloud-ocr-bizlicense_SKILL.md` (Original: tencentcloud-ocr-bizlicense)
- [ ] `.archive/staging/skills/tencentcloud-ocr-extractdocagent_SKILL.md` (Original: tencentcloud-ocr-extractdocagent)
- [ ] `.archive/staging/skills/tencentcloud-ocr-general_SKILL.md` (Original: tencentcloud-ocr-general)
- [ ] `.archive/staging/skills/tencentcloud-ocr-idcard_SKILL.md` (Original: tencentcloud-ocr-idcard)
- [ ] `.archive/staging/skills/tencentcloud-ocr-licenseplate_SKILL.md` (Original: tencentcloud-ocr-licenseplate)
- [ ] `.archive/staging/skills/tencentcloud-ocr-mlidpassport_SKILL.md` (Original: tencentcloud-ocr-mlidpassport)
- [ ] `.archive/staging/skills/tencentcloud-ocr-questionmarkagent_SKILL.md` (Original: tencentcloud-ocr-questionmarkagent)
- [ ] `.archive/staging/skills/tencentcloud-ocr-recognizetableaccurate_SKILL.md` (Original: tencentcloud-ocr-recognizetableaccurate)
- [ ] `.archive/staging/skills/tencentcloud-ocr-vatinvoice_SKILL.md` (Original: tencentcloud-ocr-vatinvoice)
- [ ] `.archive/staging/skills/tencentcloud-ocr-vehiclelicense_SKILL.md` (Original: tencentcloud-ocr-vehiclelicense)
- [ ] `.archive/staging/skills/tencentcloud-ocr_SKILL.md` (Original: tencentcloud-ocr)
- [ ] `.archive/staging/skills/wechat-html-publisher_SKILL.md` (Original: wechat-html-publisher)
- [ ] `.archive/staging/skills/feishu-operations_SKILL.md` (Original: feishu-operations)
- [ ] `.archive/staging/skills/fullstack-dev-engineer_SKILL.md` (Original: fullstack-dev-engineer)
- [ ] `.archive/staging/skills/sre-operator_SKILL.md` (Original: sre-operator)
- [ ] `.archive/staging/skills/auto-qa_SKILL.md` (Original: auto-qa)
- [ ] `.archive/staging/skills/lessons-learned_SKILL.md` (Original: lessons-learned)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
