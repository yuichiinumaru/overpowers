# Extraction Task: 0500-extraction-skills-batch-040

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-040` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/kim-msg-account_SKILL.md` (Original: kim-msg-account)
- [ ] `.archive/staging/skills/kim-msg_SKILL.md` (Original: kim-msg)
- [ ] `.archive/staging/skills/xhs-skill_SKILL.md` (Original: xhs-skill)
- [ ] `.archive/staging/skills/letundra_SKILL.md` (Original: letundra)
- [ ] `.archive/staging/skills/letundra-currency_SKILL.md` (Original: letundra-currency)
- [ ] `.archive/staging/skills/letundra-holidays_SKILL.md` (Original: letundra-holidays)
- [ ] `.archive/staging/skills/letundra-visa_SKILL.md` (Original: letundra-news)
- [ ] `.archive/staging/skills/abc_SKILL.md` (Original: abc)
- [ ] `.archive/staging/skills/alibaba_SKILL.md` (Original: alibaba)
- [ ] `.archive/staging/skills/bytedance_SKILL.md` (Original: bytedance)
- [ ] `.archive/staging/skills/wechat-intro_SKILL.md` (Original: chenlang)
- [ ] `.archive/staging/skills/clawopen_SKILL.md` (Original: clawopen)
- [ ] `.archive/staging/skills/digital-nomad_SKILL.md` (Original: digital-nomad)
- [ ] `.archive/staging/skills/jd_SKILL.md` (Original: jd)
- [ ] `.archive/staging/skills/leo_SKILL.md` (Original: leo)
- [ ] `.archive/staging/skills/money-knowledge_SKILL.md` (Original: money-knowledge)
- [ ] `.archive/staging/skills/shenzhen_SKILL.md` (Original: shenzhen)
- [ ] `.archive/staging/skills/zengming_SKILL.md` (Original: zengming)
- [ ] `.archive/staging/skills/yahoo-claw_SKILL.md` (Original: yahoo-claw)
- [ ] `.archive/staging/skills/image-translator_SKILL.md` (Original: image-translator)
- [ ] `.archive/staging/skills/tuniu-flight_SKILL.md` (Original: tuniu-flight)
- [ ] `.archive/staging/skills/programming_SKILL.md` (Original: programming)
- [ ] `.archive/staging/skills/fitness-personal-assistant_SKILL.md` (Original: fitness-personal-assistant)
- [ ] `.archive/staging/skills/ynote-news_SKILL.md` (Original: ynote-news)
- [ ] `.archive/staging/skills/youdaonote-clip_SKILL.md` (Original: youdaonote-clip)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
