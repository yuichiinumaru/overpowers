# Extraction Task: 0500-extraction-skills-batch-028

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-028` to execute this task or follow these manual steps for each item:

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

- [x] `.archive/staging/skills/parse-video_SKILL.md` (Original: parse-video) - **Extracted to `skills/parse-video/`**
- [x] `.archive/staging/skills/points-recharge_SKILL.md` (Original: points-recharge) - **Extracted to `skills/points-recharge/`**
- [x] `.archive/staging/skills/pricing-test_SKILL.md` (Original: pricing-test) - **Extracted to `skills/pricing-test/`**
- [x] `.archive/staging/skills/prop-extractor_SKILL.md` (Original: prop-extractor) - **Extracted to `skills/prop-extractor/`**
- [x] `.archive/staging/skills/storyboard-generator_SKILL.md` (Original: storyboard-generator) - **Extracted to `skills/storyboard-generator/`**
- [x] `.archive/staging/skills/style-extractor_SKILL.md` (Original: style-extractor) - **Extracted to `skills/style-extractor/`**
- [x] `.archive/staging/skills/sutui-minimax-tts_SKILL.md` (Original: sutui-minimax-tts) - **Extracted to `skills/sutui-minimax-tts/`**
- [x] `.archive/staging/skills/upload-to-catbox_SKILL.md` (Original: upload-to-catbox) - **Extracted to `skills/upload-to-catbox/`**
- [x] `.archive/staging/skills/vidu-video_SKILL.md` (Original: vidu-video) - **Extracted to `skills/vidu-video/`**
- [x] `.archive/staging/skills/wan-video_SKILL.md` (Original: wan-video) - **Extracted to `skills/wan-video/`**
- [x] `.archive/staging/skills/conceive-short-drama-cn_SKILL.md` (Original: conceive-short-drama-cn) - **Extracted to `skills/conceive-short-drama-cn/`**
- [x] `.archive/staging/skills/shorts-builder-cn_SKILL.md` (Original: shorts-builder-cn) - **Extracted to `skills/shorts-builder-cn/`**
- [x] `.archive/staging/skills/easy-recruitment_SKILL.md` (Original: easy-recruitment) - **Extracted to `skills/easy-recruitment/`**
- [x] `.archive/staging/skills/prompt-learning-assistant_SKILL.md` (Original: prompt-learning-assistant) - **Extracted to `skills/prompt-learning-assistant/`**
- [x] `.archive/staging/skills/prompt-master_SKILL.md` (Original: prompt-master) - **Extracted to `skills/prompt-master/`**
- [x] `.archive/staging/skills/prompts-workflow_SKILL.md` (Original: prompts-workflow) - **Extracted to `skills/prompts-workflow/`**
- [x] `.archive/staging/skills/openclaw-backupgg_SKILL.md` (Original: openclaw-backupgg) - **Extracted to `skills/openclaw-backup/`**
- [x] `.archive/staging/skills/mcdonald-cn_SKILL.md` (Original: mcd) - **Extracted to `skills/mcdonald-cn/`**
- [x] `.archive/staging/skills/rednote_SKILL.md` (Original: rednote) - **Extracted to `skills/xiaohongshu/`**
- [x] `.archive/staging/skills/yahoo-auction-estimator_SKILL.md` (Original: yahoo-auction-estimator) - **Extracted to `skills/yahoo-auction-estimator/`**
- [x] `.archive/staging/skills/x-knowledge-base_SKILL.md` (Original: x-knowledge-base) - **Extracted to `skills/x-knowledge-base/`**
- [x] `.archive/staging/skills/qrcode-skills_SKILL.md` (Original: qrcode-skills) - **Extracted to `skills/qrcode-skills/`**
- [x] `.archive/staging/skills/limtdesign_SKILL.md` (Original: limtdesign) - **Extracted to `skills/visual-creative/`**
- [x] `.archive/staging/skills/crypto-learning_SKILL.md` (Original: crypto-learning) - **Extracted to `skills/crypto-learning/`**
- [x] `.archive/staging/skills/x-hot-topics-daily_SKILL.md` (Original: x-hot-topics-daily) - **Extracted to `skills/x-hot-topics-daily/`**


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
