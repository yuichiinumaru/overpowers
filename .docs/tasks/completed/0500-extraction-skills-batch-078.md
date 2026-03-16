# Extraction Task: 0500-extraction-skills-batch-078

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-078` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/feishu-doc-verifier_SKILL.md` (Original: feishu-doc-verifier)
- [ ] `.archive/staging/skills/feishu-logger_SKILL.md` (Original: feishu-logger)
- [ ] `.archive/staging/skills/feishu-md-parser_SKILL.md` (Original: feishu-md-parser)
- [ ] `.archive/staging/skills/insurance-broker_SKILL.md` (Original: insurance-broker)
- [ ] `.archive/staging/skills/ai-drama-prompt-factory_SKILL.md` (Original: ai-drama-prompt-factory)
- [ ] `.archive/staging/skills/python-code-test_SKILL.md` (Original: python-code-test)
- [ ] `.archive/staging/skills/local-file_SKILL.md` (Original: local-file)
- [ ] `.archive/staging/skills/read-it-later_SKILL.md` (Original: read-it-later)
- [ ] `.archive/staging/skills/address-extractor_SKILL.md` (Original: address-extractor)
- [ ] `.archive/staging/skills/ket_SKILL.md` (Original: ket)
- [ ] `.archive/staging/skills/feishu-cache-guardian_SKILL.md` (Original: feishu-cache-guardian)
- [ ] `.archive/staging/skills/desearch_SKILL.md` (Original: desearch)
- [ ] `.archive/staging/skills/astock-research_SKILL.md` (Original: astock-research)
- [ ] `.archive/staging/skills/certificate-analysis_SKILL.md` (Original: certificate-analysis)
- [ ] `.archive/staging/skills/literature-report_SKILL.md` (Original: literature-report)
- [ ] `.archive/staging/skills/localspeechrecognition_SKILL.md` (Original: localspeechrecognition)
- [ ] `.archive/staging/skills/agent-training_SKILL.md` (Original: agent-training)
- [ ] `.archive/staging/skills/email-marketing-3_SKILL.md` (Original: email-marketing-3)
- [ ] `.archive/staging/skills/email-marketing-faq_SKILL.md` (Original: email-marketing-faq)
- [ ] `.archive/staging/skills/chaogu_SKILL.md` (Original: chaogu)
- [ ] `.archive/staging/skills/multi-agent-hybrid-architecture_SKILL.md` (Original: multi-agent-hybrid-architecture)
- [ ] `.archive/staging/skills/openclaw-config-center_SKILL.md` (Original: openclaw-config-center)
- [ ] `.archive/staging/skills/openclaw-sandbox_SKILL.md` (Original: openclaw-sandbox)
- [ ] `.archive/staging/skills/xiaomi-home-assistant-skill_SKILL.md` (Original: xiaomi-home-assistant-skill)
- [ ] `.archive/staging/skills/pdf-watermark_SKILL.md` (Original: pdf-watermark)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
