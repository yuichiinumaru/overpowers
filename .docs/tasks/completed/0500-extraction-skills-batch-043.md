# Extraction Task: 0500-extraction-skills-batch-043

**Batch Type:** skills
**Total Items:** 25

## Objective
Process this batch of raw, deduplicated assets from `.archive/staging/skills/` and integrate them into the main repository (`skills/`, `agents/`, `workflows/`, `hooks/`).

## Workflow Instructions
Use the command `/ovp-extract-assets 0500-extraction-skills-batch-043` to execute this task or follow these manual steps for each item:

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

- [ ] `.archive/staging/skills/humanizer-zh_SKILL.md` (Original: humanizer-zh)
- [ ] `.archive/staging/skills/penguin-pet_SKILL.md` (Original: penguin-pet)
- [ ] `.archive/staging/skills/style-polisher_SKILL.md` (Original: style-polisher)
- [ ] `.archive/staging/skills/case-record-socialwork_SKILL.md` (Original: case-record-socialwork)
- [ ] `.archive/staging/skills/kid-tutor_SKILL.md` (Original: kid-tutor)
- [ ] `.archive/staging/skills/ai-ppt-maker_SKILL.md` (Original: ai-ppt-maker)
- [ ] `.archive/staging/skills/meeting-score_SKILL.md` (Original: meeting-score)
- [ ] `.archive/staging/skills/weather-of-beijing-with-almanac_SKILL.md` (Original: weather-of-beijing-with-almanac)
- [ ] `.archive/staging/skills/tencent-docs_SKILL.md` (Original: tencent-docs)
- [ ] `.archive/staging/skills/minimax-token-used-query_SKILL.md` (Original: minimax-token-used-query)
- [ ] `.archive/staging/skills/typecho-post-publisher_SKILL.md` (Original: typecho-post-publisher)
- [ ] `.archive/staging/skills/extract-pic-text_SKILL.md` (Original: extract-pic-text)
- [ ] `.archive/staging/skills/insurance-policy-parser_SKILL.md` (Original: insurance-policy-parser)
- [ ] `.archive/staging/skills/price-comparison-analyzer_SKILL.md` (Original: price-comparison-analyzer)
- [ ] `.archive/staging/skills/resume-optimization_SKILL.md` (Original: resume-optimization)
- [ ] `.archive/staging/skills/chinese-naming-master_SKILL.md` (Original: chinese-naming-master)
- [ ] `.archive/staging/skills/poe-chat_SKILL.md` (Original: poe-chat)
- [ ] `.archive/staging/skills/baidu-map-harmonyos-sdk_SKILL.md` (Original: baidu-map-harmonyos-sdk)
- [ ] `.archive/staging/skills/baidu-map-ios-sdk_SKILL.md` (Original: baidu-map-ios-sdk)
- [ ] `.archive/staging/skills/report-ppt-generator-pro_SKILL.md` (Original: report-ppt-generator-pro)
- [ ] `.archive/staging/skills/feishu-group-mention-responder_SKILL.md` (Original: feishu-group-mention-responder)
- [ ] `.archive/staging/skills/chat-ai_SKILL.md` (Original: chat-ai)
- [ ] `.archive/staging/skills/live-location-mapper_SKILL.md` (Original: live-location-mapper)
- [ ] `.archive/staging/skills/traffic-cam_SKILL.md` (Original: traffic-cam)
- [ ] `.archive/staging/skills/crypto-price-by-lpdawn_SKILL.md` (Original: crypto-price-by-lpdawn)


---
*Note: If an item turns out to be extremely low quality or a duplicate missed by the automated scripts, simply delete it from staging, note it as [Skipped], and move on.*
