# Extraction Task: 0500-extraction-skills-batch-010

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-010` to execute this task or follow these manual steps for each item:

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

- [x] `.archive/staging/skills/security-audit-tools_SKILL.md` (Original: naruto-multi-agent-cn)
- [x] `.archive/staging/skills/self-evolve_SKILL.md` (Original: self-evolve)
- [x] `.archive/staging/skills/volcengine-config_SKILL.md` (Original: volcengine-config)
- [x] `.archive/staging/skills/design-inspiration-collector_SKILL.md` (Original: design-inspiration-collector)
- [x] `.archive/staging/skills/claw-asset-privacy-guardian_SKILL.md` (Original: claw-asset-privacy-guardian)
- [x] `.archive/staging/skills/claw-ethics-checker_SKILL.md` (Original: claw-ethics-checker)
- [x] `.archive/staging/skills/claw-memory-guardian_SKILL.md` (Original: claw-memory-guardian)
- [x] `.archive/staging/skills/claw-problem-diagnoser_SKILL.md` (Original: claw-problem-diagnoser)
- [x] `.archive/staging/skills/claw-security-scanner_SKILL.md` (Original: claw-security-scanner)
- [x] `.archive/staging/skills/smart-agent-memory_SKILL.md` (Original: smart-agent-memory)
- [x] `.archive/staging/skills/qqbot-media-sender_SKILL.md` (Original: qqbot-media-sender)
- [x] `.archive/staging/skills/email-reply_SKILL.md` (Original: email-reply)
- [x] `.archive/staging/skills/xiaohongshu-publish-skill_SKILL.md` (Original: xiaohongshu-publish-skill)
- [x] `.archive/staging/skills/qichacha_SKILL.md` (Original: qichacha)
- [x] `.archive/staging/skills/auto-install-openclaw_SKILL.md` (Original: auto-install-openclaw)
- [x] `.archive/staging/skills/im-social-insurance-backpay_SKILL.md` (Original: im-social-insurance-backpay)
- [x] `.archive/staging/skills/software-copyright-cn_SKILL.md` (Original: software-copyright-cn)
- [x] `.archive/staging/skills/batch-processing-patterns_SKILL.md` (Original: batch-processing-patterns)
- [x] `.archive/staging/skills/ecommerce-price-comparison_SKILL.md` (Original: ecommerce-price-comparison)
- [x] `.archive/staging/skills/macclaw-copilot-cli_SKILL.md` (Original: macclaw-copilot-cli)
- [x] `.archive/staging/skills/eatsth-by_SKILL.md` (Original: eatsth-by)
- [x] `.archive/staging/skills/myfood-by_SKILL.md` (Original: myfood-by)
- [x] `.archive/staging/skills/yandex-tracker-cli_SKILL.md` (Original: yandex-tracker-cli)
- [x] `.archive/staging/skills/cpskilltest123456_SKILL.md` (Original: cpskilltest123456)
- [x] `.archive/staging/skills/crypto-daily-report_SKILL.md` (Original: crypto-daily-report)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
