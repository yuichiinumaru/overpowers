---
name: wechat-article-writer
description: WeChat public account writing assistant - specialized in public account article creation, from topic selection to final draft + automatic image matching complete workflow. Trigger words: "write public account", "public account article", "push article", "/wechat"
tags: [wechat, article-writing, content-creation, public-account, copywriting, image-generation]
version: "1.0.0"
---

# WeChat Public Account Writing Assistant

## Trigger Methods

Activates when user says:
- "Write a public account article"
- "Help me write a push article"
- "Public account content creation"
- "/wechat" or "/public-account"

---

## Core Workflow

**Six Stages: Topic → Title → Framework → Draft → Save → Image Prompts → (Ask) Generate Images**

```
User proposes writing request
    │
    ↓
[Stage 01] Topic Positioning - Clarify article theme and positioning
    │
    ↓
[Stage 02] Title Optimization - Generate 5-10 viral title options for selection
    │
    ↓
[Stage 03] Framework Building - Design article structure
    │
    ↓
[Stage 04] Full Draft Writing - Complete 2500-3000 character article
    │
    ↓
[Stage 05] Save Article - Formatted MD saved to specified directory
    │
    ↓
[Stage 06] Auto-generate Image Prompts - Generate cover/infographic/CTA image prompts
    │
    ↓
[Ask] Generate images? - Only call API after user confirmation
```

---

## Workflow Overview

| Stage | Name | Goal | Detailed File |
|---|---|---|---|
| 01 | Topic Positioning | Clarify what to write, for whom, what problem to solve | `stages/01-topic.md` |
| 02 | Title Optimization | **Must provide 5-10 viral title options** | `stages/02-title.md` |
| 03 | Framework Building | Design article structure, ensure clear logic | `stages/03-framework.md` |
| 04 | Full Draft Writing | Complete 2500-3000 character article based on framework | `stages/04-writing.md` |
| 05 | Save Article | Formatted MD saved to specified directory | See below |
| 06 | Auto Image Prompts | **Auto-generate image prompts and save, ask user if generate images** | `image_templates/` |

---

## Dispatch Rules

**How to determine current stage:**

1. **Enter Stage 01** — User just starting, only has vague idea
2. **Enter Stage 02** — Topic confirmed, **must generate multiple viral titles for user selection**
3. **Enter Stage 03** — Title confirmed, need to design framework
4. **Enter Stage 04** — Framework confirmed, start writing full draft
5. **Enter Stage 05** — Article completed, **auto-save** to specified directory
6. **Enter Stage 06** — Article saved, **auto-generate image prompts and save, then ask user if generate images**

**At the start of each stage:**
- Tell user which stage they're in
- Read corresponding stage file to execute
- Clarify the goal of this stage

---

## Writing Style (Core Rules)

**Core Features (see `writing_style.md` for details):**

1. **Colloquial Expression** — Like chatting with friends
2. **Emotional Expression** — Directly express excitement, frustration
3. **Complete Sentence Expression** — **Use complete paragraphs, avoid excessive short fragmented sentences**
4. **Pragmatism** — Less nonsense, more useful content
5. **Real Experience** — Dare to complain, dare to admit shortcomings

**Important Rules:**
- ✅ Use complete paragraphs to express ideas
- ❌ Avoid excessive short fragmented sentences
- ✅ Have logical connections between paragraphs
- ✅ Maintain reading flow coherence

---

## Title Rules (Important)

**Stage 02 must execute:**

1. **Analyze viral title features**: Number type, Question type, Comparison type, Identity type, Time type, Emotion type
2. **Generate 5-10 title options**
3. **Provide recommendation reasons**
4. **Wait for user selection before continuing**

**Viral Title Formulas:**
- Number + Benefit: "4 techniques to help you XXX"
- Question + Pain point: "Why XXX still XXX?"
- Comparison + Contrast: "Others XXX, but you're XXX"
- Identity + Scenario: "To all XXX parents"
- Time + Urgency: "Before school starts, you must know"
- Emotional Resonance: "After reading this letter, I cried"

---

## Article Save Rules

**Stage 05 must execute:**

1. **File naming format**: `YYYYMMDD_Article title keywords.md`
2. **Save path**: `E:\Claude Code\claude\articles\Youth Learning Coach Public Account\`
3. **File format**: Formatted Markdown
4. **Save timing**: Auto-save after article completion

---

## Auto Image Matching Rules (Important)

**Stage 06 auto-executes:**

After article is saved, **auto-generate image prompts and save**, then **ask user** if they need to generate images.

1. **Auto-generate image prompts**:
   - Cover image + 2-3 infographics + Ending CTA image
   - Based on article content, use templates from `image_templates/`
   - Save format: Same name as article, add `_ImagePrompts.md`
   - Save path: Same directory as article

2. **Ask user if generate images**:
   - Display generated image prompts
   - Ask: "Do you need to call API to generate images?"
   - Only call `scripts/generate_images.py` to generate after user confirmation

**Image Prompt Templates:**
- Cover: `image_templates/cover.md`
- Infographic: `image_templates/infographic.md`
- CTA: `image_templates/cta.md`
- Style Baseline: `image_templates/style-block.md`

---

## File Structure

```
wechat-article-writer/
├── SKILL.md                    # Main file
├── writing_style.md            # Writing style guide (must read)
├── stages/
│   ├── 01-topic.md             # Topic positioning
│   ├── 02-title.md             # Title optimization (viral title formulas)
│   ├── 03-framework.md         # Framework building
│   └── 04-writing.md           # Full draft writing
├── templates/
│   ├── article-structure.md    # Article structure template
│   └── title-formulas.md       # Title formula library
├── image_templates/            # Image templates
│   ├── style-block.md          # Style baseline
│   ├── cover.md                # Cover image template
│   ├── infographic.md          # Body infographic template
│   └── cta.md                  # Ending CTA image template
├── scripts/                    # Image generation scripts
│   ├── image.env               # API configuration (key configured)
│   ├── image.env.example       # API configuration example
│   ├── generate_images.py      # Batch generation script
│   └── README.md               # Usage instructions
└── examples/
    └── sample-article.md       # Excellent article example
```

---

## Article Types

| Type | Features | Word Count | Use Case |
|---|---|---|---|
| Practical Tutorial | Clear steps, actionable | 2500-3000 | Skill sharing, tool introduction |
| Opinion Article | Clear viewpoint, well-supported | 2500-3000 | Industry analysis, thoughts |
| Story Case | Engaging plot, strong resonance | 2500-3000 | Personal experience, case sharing |
| List Roundup | High information density, easy to read | 2500-3000 | Resource recommendations, method summary |

**Unified Word Count Standard: 2500-3000 characters**

---

## Image API Configuration

**Current Configuration (`scripts/image.env`):**
```bash
API_KEY=88e6f80c14cb40e4ba6d5bfe702d6aac.74cOvJgmo1t48yrv
MODEL=glm-image
SIZE=900x383
```

**Supported Models:**
- glm-image: Standard image generation model (default)
- cogview-4: Advanced image generation model

**Image Size Rules:**
- **Default Size**: 900×383 pixels (recommended for headline cover)
- **Core Content Area**: Center approximately 383×383 pixel range (prevent information loss)

---

## Notes

- **User Control**: User can say "continue", "rewrite", "change direction" anytime
- **Maintain Style**: Write according to `writing_style.md` requirements
- **Complete Sentences**: Use complete paragraph expression, avoid short sentence fragmentation
- **Title Selection**: Must provide multiple viral title options for user selection
- **Auto Save**: Auto-save article + image prompts after completion
- **Auto Images**: Auto-generate image prompts after article save
- **Accurate Data**: When involving data, mark source or suggest verification
- **Avoid Clichés**: Less use of "shocking", "finally" and other overly exaggerated words
- **Word Count Control**: Target 2500-3000 characters
