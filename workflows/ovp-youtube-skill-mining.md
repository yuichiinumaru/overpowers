# YouTube Skill Mining (Cyclic Agent Workflow)

Maximize procedural knowledge acquisition by pointing the `youtube-ripper` agent to a YouTube channel or a list of videos, looping indefinitely to transform unstructured tech videos into documented executable Skills.

## Overview

This workflow leverages the `youtube-ripper` agent combined with two specialized skills to perform an end-to-end "rip and build" loop:
1. Extract all canonical URLs from a target source.
2. Batch-analyze these URLs.
3. Automatically forge valid `SKILL.md` files or update existing knowledge.

## Prerequisites

- Agent: `@youtube-ripper`
- Tools/Skills available:
  - `youtube-link-extractor`
  - `youtube-skill-creator`

## Workflow Steps

### 1. Preparation & Targets
```
/invoke youtube-ripper

Define the target list of videos. You may start with testing references already available in the repo:
- skills/youtube-skill-creator/references/benji-ai-playground.md
- skills/youtube-skill-creator/references/ibm-channels.md
```

### 2. Extraction Phase (If needed)
If the user only provided a channel URL (e.g., `https://youtube.com/@techchannel`), the agent must execute:
```
/skill youtube-link-extractor

1. Launch browser to the channel's /videos, /shorts, or /streams tab.
2. Inject extraction scripts to harvest all canonical URLs.
3. Compile deduplicated links into a temporary markdown ledger (e.g., `youtube-mining-queue.md`).
```

### 3. The Cyclic Engine (Non-Stop Loop & Context Management)
Once a list is established, run the batch consumption loop recursively to prevent context rot.

**For every chunk of 2 to 5 videos (Recursive Loop):**
```
/skill youtube-skill-creator

1. Watch/transcribe the videos in the batch. (Tip: Use `scripts/helpers/youtube_audio_transcriber.js` locally if yt-dlp faces IP blocks).
2. Take notes: If a video does not have enough context on its own to form a full skill, take notes of the problems, edge cases, and solutions presented.
3. Evaluate Accumulation:
   - If the accumulated notes provide enough context for a robust procedure, proceed to step 4.
   - If NOT, save the notes to `.agents/reports/youtube-mining-notes.md` and immediately loop to the next batch of videos.
4. Apply the scorecard calculation (`skill_scorecard.md`) to filter noise from actual procedures.
5. Draft a `video_analysis_report.md` outlining the precise steps seen.
6. Translate viable reports into fully functional agent skills, ensuring they follow:
   - Proper folder structure: `skills/extracted-topic-name/SKILL.md`
   - YAML Frontmatter (name, description, etc).
7. Cross-check `skills/` directory to avoid duplicate overlap; prefer updating existing skills if heavily redundant, utilizing the accumulated notes.
```

### 4. Progress Persistence & Auto-Continue
After a batch is processed and skills are written to the repository:
1. The agent marks those URLs as `[x] DONE` in the mining queue ledger.
2. The agent commits the newly created skills to the project repository if tracking is active.
3. The internal prompt requests permission (or uses auto-continue loops) to proceed directly to the **next batch of 5 videos**.

## Success Metrics

| Metric | Target |
|--------|--------|
| Target Efficiency | 1 new/updated Skill every ~5 videos |
| Noise Reduction | 0 vlogs/podcasts formalized as skills |
| Skill Structure | 100% adherence to `skills/<name>/SKILL.md` |
