---
name: ai-learning-journal
description: "AI learning record and growth tracking tool. Used to record AI/LLM learning notes, usage experiences, Prompt techniques, tool evaluations, etc., and provide learning guidance and planning. This skill should be used whenever the user mentions any of the following topics: AI learning records, learning notes, AI usage experiences, Prompt engineering learning, model comparison experiences, AI tool usage records, LLM learning, RAG learning, Agent learning, MCP learning, AI fine-tuning practice, AI learning planning, how to learn AI, AI getting started, ..."
metadata:
  openclaw:
    category: "ai"
    tags: ['ai', 'automation', 'generation']
    version: "1.0.0"
---

# AI Learning Record and Growth Tracker

Helps users systematically record their AI learning journey, providing guidance and planning suggestions. All records are persistently stored as Markdown files, supporting review and knowledge summarization.

## Storage Specification

All learning records are saved in the `records/` folder within this skill's directory.

```
records/
├── index.md                    # Global Index (Automatically updated after every new/modified record)
├── plans/                      # Learning plan files
│   └── YYYY-MM-DD-plan-topic.md
├── summaries/                  # Knowledge summary reports
│   └── YYYY-MM-monthly-summary.md
└── YYYY-MM/                    # Learning records organized by year and month
    └── YYYY-MM-DD-topic-keywords.md
```

Path Explanation:
- The root directory of this skill is located at the user's `~/.copilot/skills/ai-learning-journal/`
- The absolute path for `records/` is `~/.copilot/skills/ai-learning-journal/records/`
- Use `create_file` to create new records, and use `replace_string_in_file` to update existing records and `index.md`

---

## Feature 1: Structured Recording

### Trigger Scenarios

The user describes an AI-related learning experience or usage insight, such as:
- "Learned about RAG principles today."
- "Tried Claude's MCP, it feels very powerful."
- "Documenting my experience using Cursor for coding."
- "Sharing my comparison thoughts on GPT-4o and Claude."

### Interaction Flow

1. **Understand User Input**: The user might describe the learning content in a colloquial, fragmented manner; patiently extract key information.
2. **Supplementary Questions** (Only if information is clearly insufficient): Ask 1-2 key questions lightly; do not turn it into a survey. For example:
   - "In what scenario did you use it? How was the result?"
   - "Did you encounter any pitfalls or unexpected discoveries?"
3. **Generate Structured Record**: Organize the user input into the following template format.
4. **Save File**: Write to the `records/YYYY-MM/` directory.
5. **Update Index**: Append a new entry to the table in `records/index.md`.

### Record Template

```markdown
# 学习记录: [主题]

- **日期**: YYYY-MM-DD
- **领域**: [See domain classifications below]
- **标签**: [关键词1, 关键词2, ...]
- **难度**: [入门 / 进阶 / 高阶]

## 学习内容

[What the user learned, core concepts and key points]

## 使用场景

[The scenario/project where it was used or learned]

## 关键发现与心得

[Personal reflections, comparative thinking, best practices]

## 遇到的问题

[Confusion encountered during learning, pitfalls, unresolved questions]

## 参考资源

[Related links, documents, tutorials, papers, etc.]
```

### Domain Classification

Select from the following categories for the record (multiple selections allowed):
- **Prompt Engineering**: Prompt design, techniques, patterns
- **RAG**: Retrieval-Augmented Generation, vector databases, Embedding
- **Agent & Tool Use**: AI Agents, MCP, Function Calling, tool integration
- **模型使用与对比** (Model Usage & Comparison): Usage experience with ChatGPT, Claude, Gemini, open-source models, etc.
- **AI 编程工具** (AI Coding Tools): Cursor, Copilot, Windsurf, etc.
- **Fine-tuning**: Model fine-tuning, LoRA, data preparation
- **AI 基础理论** (AI Fundamentals): Machine Learning, Deep Learning, Transformer, Attention Mechanism
- **多模态** (Multimodal): Image generation, speech recognition, video understanding
- **AI 安全与对齐** (AI Safety & Alignment): Security, alignment issues, ethics
- **生产部署** (Production Deployment): Model inference optimization, API integration, cost control
- **AI 产品与设计** (AI Product & Design): AI product thinking, user experience, commercialization

### Index Update

After adding a new record, append a line to the record table in `records/index.md`:

```
| YYYY-MM-DD | [主题] | [领域] | [标签] | [一句话摘要] |
```

---

## Feature 2: Historical Review

### Trigger Scenarios

- "Review my learning records."
- "What have I learned before?"
- "What did I study last month?"
- "What did I record previously about RAG?"

### Interaction Flow

1. Read `records/index.md` to get a global view.
2. Filter based on user requirements:
   - **By Time**: Read files in the corresponding month's directory.
   - **By Domain**: Filter records matching the domain from the index.
   - **By Tag/Keyword**: Search for matching records.
3. Present the learning timeline: Display matching record summaries in a clear list or table format.
4. Deep Dive as needed: If the user wants details of a specific record, read and display the full content.

### Output Format

```
📚 你的 AI 学习历程

期间：YYYY-MM 至 YYYY-MM
共 N 条记录，覆盖 X 个领域

| 日期 | 主题 | 领域 | 关键收获 |
|------|------|------|----------|
| ...  | ...  | ...  | ...      |

最活跃领域：[领域名] (N 条记录)
最近关注：[最近几条记录的主题]
```

---

## Feature 3: Learning Guidance

### Trigger Scenarios

- "How is this best used?" (Follow-up question after recording a specific technology)
- "Are there any best practices?"
- "Give me some advanced suggestions."
- When the "Challenges & Questions" section in the user's record has unresolved queries.

### Interaction Flow

1. Based on the content just recorded by the user, or by reading specified historical records.
2. Provide specific advice regarding the technology/tool:
   - **Usage Suggestions**: Best practices, common patterns, efficiency tips.
   - **Pitfall Avoidance**: Common misconceptions, performance traps, security considerations.
   - **Advanced Directions**: Extension learning paths for the current knowledge point.
3. If the user mentioned a problem in their record, proactively offer a solution approach.
4. Guidance content is presented directly in the conversation, not stored separately as a file (unless the user requests saving).

---

## Feature 4: Learning Planning

### Trigger Scenarios

- "Based on my records, what should I study next?"
- "Help me create a study plan."
- "Which direction should I delve deeper into next?"

### Interaction Flow

1. Read `records/index.md` and recent records to analyze the knowledge the user has already mastered.
2. Refer to the "AI Knowledge Domain Map" below to locate the user's current stage.
3. Identify knowledge gaps and natural next steps.
4. Generate a personalized learning plan.
5. Save the plan to `records/plans/YYYY-MM-DD-规划主题.md`.

### Plan Template

```markdown
# AI 学习规划

- **生成日期**: YYYY-MM-DD
- **用户当前阶段**: [Assessment based on existing records]
- **推荐路线**: [应用者 / 开发者 / 产品运营]

## 已掌握的知识领域

[Extracted from historical records, noting proficiency level]

## 阶段一：[主题]（预计 X 周）

### 学习目标
[Specific, measurable goals]

### 推荐资源
[Courses/docs/projects, noting difficulty and estimated time]

### 实战项目
[A small hands-on project]

### 学习方法建议
[Study methods specific to this phase]

## 阶段二：[主题]（预计 X 周）
...

## 长期方向建议
[3-6 month outlook]
```

---

## Feature 5: Knowledge Summarization

### Trigger Scenarios

- "Summarize my learning this month."
- "Generate a study report."
- "Review my AI knowledge system."

### Interaction Flow

1. Read all records for the specified time period (defaulting to the last month).
2. Analyze learning patterns: frequency, domain distribution, depth changes.
3. Extract core takeaways and knowledge connections.
4. Generate a structured summary report.
5. Save to `records/summaries/YYYY-MM-总结主题.md`.

### Summary Template

```markdown
# AI 学习总结

- **期间**: YYYY-MM-DD 至 YYYY-MM-DD
- **记录数**: N 条
- **覆盖领域**: [Domain list]

## 学习概览

[Time distribution, frequency analysis, domain percentage]

## 核心收获

[Top 3-5 most important knowledge points or insights extracted]

## 知识图谱进展

[Coverage and growth path within the user's AI knowledge system]

## 待深入领域

[Identified knowledge gaps and recommended areas for reinforcement]

## 下一步建议

[Short-term study suggestions based on the summary]
```

---

## Feature 6: Proactive Learning Consultation

### Trigger Scenarios

The user actively asks about AI learning directions, usable without relying on existing records:
- "I want to learn AI, where should I start?"
- "How to systematically learn AI?"
- "AI learning roadmap recommendation."
- "Can I learn AI with zero background?"
- "What are good methods for learning AI?"
- "I want to switch careers to AI, how do I start?"

### Interaction Flow

1. **Understand User Background** (Brief conversation, 2-3 questions suffice):
   - Technical foundation: Any programming experience? Which languages are familiar? Math foundation?
   - Learning Goal: Interest exploration / Work efficiency improvement / Career transition / Building AI products?
   - Available Time: Approximately how many hours per week?
2. **Recommend a Matching Learning Route** (Select from the three routes below).
3. **Output Structured Learning Plan** (Using the planning template).
4. **Provide Specific Study Method Suggestions**.
5. **If the user has historical records**, read them to mark already mastered parts and avoid redundant recommendations.

### Three Learning Routes

#### Route A: AI Practitioner (Non-technical background or aiming for quick adoption)

Suitable for: Product Managers, Operations, Designers, Students, non-technical roles aiming to use AI for efficiency.

```
Phase 1: AI Cognition & Basic Tools (2-3 Weeks)
├── Understand basic principles of AI/LLM (conceptual level, no math needed)
├── Proficiently use conversational AIs like ChatGPT / Claude
├── Learn basic Prompt writing techniques
└── Practical: Use AI to complete a real work task

Phase 2: Advanced Prompt Engineering (3-4 Weeks)
├── Systematically study Prompt design patterns (Role setting, Few-shot, CoT, etc.)
├── Learn to build complex Prompt workflows
├── Understand the characteristics and applicable scenarios of different models
└── Practical: Design a set of Prompt templates for a specific work scenario

Phase 3: AI Tool Ecosystem (3-4 Weeks)
├── AI Coding Tools: Cursor / Copilot (usable even by non-programmers)
├── AI Image Tools: Midjourney / DALL-E / Stable Diffusion
├── AI Writing & Document Tools
├── AI Automation Tools: Zapier AI / Make
└── Practical: Build an AI-assisted personal workflow

Phase 4: Agents & Advanced Applications (4-6 Weeks)
├── Understand the concept and architecture of AI Agents
├── Learn MCP (Model Context Protocol)
├── Understand RAG application scenarios (as a user, not a developer)
├── Explore industry implementation cases of AI
└── Practical: Design or build an AI Agent workflow
```

#### Route B: AI Developer (With programming background)

Suitable for: Software Engineers, Data Analysts, technical personnel with Python foundation.

```
Phase 1: AI/ML Fundamentals (4-6 Weeks)
├── Python Data Science Stack (NumPy, Pandas, Matplotlib)
├── Basic Machine Learning concepts (Supervised/Unsupervised/Reinforcement Learning)
├── Classic ML algorithm practice (sklearn)
├── Deep Learning Introduction (Neural Networks, Backpropagation)
└── Practical: Complete an ML classification or regression project

Phase 2: NLP & LLMs (4-6 Weeks)
├── NLP Basics (Text processing, Word Embeddings, Sequence Models)
├── Transformer Architecture principles
├── LLM Working Principles (Pre-training, RLHF, Inference)
├── API Calling practice (OpenAI API / Anthropic API)
├── Prompt Engineering (Developer perspective)
└── Practical: Build an application based on LLM APIs

Phase 3: RAG & Agent Development (4-6 Weeks)
├── Embedding & Vector Databases (Pinecone / Chroma / FAISS)
├── RAG architecture design and optimization
├── Function Calling / Tool Use
├── Agent Frameworks (LangChain / LlamaIndex / CrewAI)
├── MCP protocol development
└── Practical: Build a RAG application or AI Agent

Phase 4: Fine-tuning & Deployment (6-8 Weeks)
├── Fine-tuning methodologies (LoRA / QLoRA / Full Fine-tuning)
├── Training data preparation and cleaning
├── Model evaluation and benchmarking
├── Inference optimization (Quantization, Distillation)
├── Production deployment (API serving, cost optimization)
└── Practical: Fine-tune a model and deploy it live
```

#### Route C: AI Product & Operations

Suitable for: Product Managers, Project Managers, Entrepreneurs, Operations personnel.

```
Phase 1: AI Product Cognition (2-3 Weeks)
├── AI Technology Landscape (What can it do, what can't it do)
├── AI product forms and business models
├── Experience mainstream AI products to build product sense
└── Practical: Analyze the core competitiveness of 3 AI products

Phase 2: AI Product Design (3-4 Weeks)
├── AI-Native product design thinking
├── Matching user needs with AI capabilities
├── Prompt strategy design (Product perspective)
├── AI product user experience design
└── Practical: Design an AI product PRD

Phase 3: AI Product Practice (4-6 Weeks)
├── Building AI prototypes using no-code/low-code tools
├── AI product data metrics system
├── User feedback and model iteration
├── AI content operation strategy
└── Practical: Build an AI product prototype and conduct user testing

Phase 4: AI Strategy & Commercialization (4-6 Weeks)
├── AI industry trend analysis
├── AI product cost and ROI analysis
├── AI compliance and ethics
├── Building internal AI capabilities within a team
└── Practical: Write an AI product commercialization plan
```

### Specific Study Method Suggestions

Select suitable recommendations from the following methods based on the user's situation:

1. **Project-Driven Learning**: Don't just watch tutorials; build a small project for every stage. Even if it's simple or rough, going through the process is more effective than watching ten tutorials. If you lack project inspiration, start by solving a real problem in your work or life.

2. **Feynman Learning Technique**: After learning a concept, write it down in your own words (this perfectly utilizes this skill's structured recording feature). If you can't explain it clearly, you haven't truly understood it; go back and study more. These records accumulate into your personal knowledge base.

3. **Comparative Learning**: When learning AI tools and models, test different tools/models on the same task and record the differences (use this skill's recording feature). Understanding the strengths and weaknesses of each tool is more important than memorizing parameters.

4. **Spaced Repetition**: Spend 15 minutes every week using this skill's "Historical Review" feature to look back at recent learning records. Reviewing your old notes after some time will lead to new insights.

5. **Community Integration**: Participate in AI-related community discussions (GitHub, Twitter/X, Reddit r/LocalLLaMA, Zhihu AI topics, various Discord servers). See how others use AI to gain inspiration, and outputting to the community reinforces your learning.

6. **Fragmented Learning + Systematic Organization**: Use fragmented time for reading articles, watching videos, and trying tools, but set aside a dedicated block of time weekly for systematic organization (using this skill's "Knowledge Summarization" feature). Acquire information in fragments, build knowledge systematically.

---

## AI Knowledge Domain Map

Used to locate the user's current stage and recommend the next steps during learning planning. Each node is annotated with prerequisites and difficulty.

```
AI Knowledge System
│
├── 🟢 Foundational Cognition Layer (Beginner, no prerequisites)
│   ├── AI/ML Basic Concepts
│   ├── LLM Working Principles (Conceptual level)
│   └── AI Product Form Cognition
│
├── 🟡 Application Practice Layer (Beginner → Intermediate)
│   ├── Prompt Engineering ← Foundational Cognition
│   ├── AI Tool Usage (ChatGPT/Claude/Cursor, etc.) ← Foundational Cognition
│   ├── AI Image/Audio/Video Tools ← Foundational Cognition
│   └── Building AI-Assisted Workflows ← Prompt Engineering + Tool Usage
│
├── 🟠 Technical Development Layer (Intermediate, requires programming foundation)
│   ├── Python Data Science ← Programming Foundation
│   ├── ML/DL Algorithm Practice ← Python Data Science + Math Foundation
│   ├── NLP Basics ← ML/DL Foundation
│   ├── LLM API Development ← Programming Foundation + Prompt Engineering
│   ├── RAG System Development ← LLM API + Vector Databases
│   ├── Agent Development ← LLM API + Tool Use
│   ├── MCP Development ← Agent Development
│   └── Fine-tuning ← ML/DL Foundation + LLM Principles
│
├── 🔴 Advanced Professional Layer (Advanced)
│   ├── Model Architecture Design ← Deep Learning
│   ├── Training Optimization ← Fine-tuning + Algorithm Foundation
│   ├── Inference Optimization & Deployment ← Model Principles + Engineering Skills
│   ├── Multimodal Systems ← NLP + CV Foundation
│   └── AI Safety & Alignment ← LLM Principles
│
└── 💼 Product & Strategy Layer (Intermediate, no technical prerequisites)
    ├── AI Product Design ← Foundational Cognition + Product Thinking
    ├── AI Commercialization ← AI Product Design
    └── Building Internal AI Capabilities ← AI Product Experience
```

---

## 使用语言 / Language

This skill fully supports bilingual interaction in Chinese and English.

**Language Auto-Adaptation Principle:**
- Always interact using the same language as the user. If the user speaks Chinese, use Chinese throughout; if the user speaks English, use English throughout.
- The title and body content of record files follow the user's input language.
- File names use keywords in the user's language (Chinese characters or Pinyin for Chinese, English for English), but fixed parts in the directory structure (`records/`, `plans/`, `summaries/`) remain in English.
- Field labels in the record templates also switch language, for example:
  - Chinese template: `日期`、`领域`、`标签`、`学习内容`、`关键发现与心得`
  - English template: `Date`, `Domain`, `Tags`, `What I Learned`, `Key Insights`
- The table headers in `index.md` maintain bilingual compatibility: `日期/Date | 主题/Topic | 领域/Domain | 标签/Tags | 摘要/Summary`

**English record template:**

```markdown
# Learning Note: [Topic]

- **Date**: YYYY-MM-DD
- **Domain**: [see domain categories]
- **Tags**: [keyword1, keyword2, ...]
- **Level**: [Beginner / Intermediate / Advanced]

## What I Learned

[Core concepts and key points]

## Use Case / Context

[Where and how this was applied or discovered]

## Key Insights

[Personal reflections, comparisons, best practices]

## Challenges & Questions

[Difficulties encountered, unresolved questions]

## References

[Links, docs, tutorials, papers]
```

**English learning plan template:**

```markdown
# AI Learning Plan

- **Generated**: YYYY-MM-DD
- **Current Level**: [assessment based on history]
- **Recommended Track**: [Practitioner / Developer / Product & Strategy]

## Knowledge Already Covered

[Extracted from history, with proficiency notes]

## Phase 1: [Topic] (Est. X weeks)

### Learning Goals
### Recommended Resources
### Hands-on Project
### Study Tips

## Phase 2: ...

## Long-term Direction
```

**English summary template:**

```markdown
# AI Learning Summary

- **Period**: YYYY-MM-DD to YYYY-MM-DD
- **Records**: N entries
- **Domains Covered**: [list]

## Overview
## Key Takeaways
## Knowledge Map Progress
## Gaps to Fill
## Next Steps
```

## Interaction Principles

1. **Low Barrier to Entry**: Help record even casual remarks; avoid turning interactions into surveys.
2. **High Value**: After every interaction, the user should receive a structured record file or useful guidance suggestions.
3. **Continuity**: Actively link to historical records to help the user see their learning trajectory and growth.
4. **Practice Focus**: When giving advice, prioritize recommendations that involve "doing" over "passive learning."
5. **Conciseness**: Maintain appropriate information density; explain key information thoroughly, and touch upon secondary information briefly.
