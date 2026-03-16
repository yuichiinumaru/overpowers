---
name: v2
description: "Intelligent Memory System v2.0 - Structured Memory + Knowledge Base + Heuristic Recall + AI Optimization"
metadata:
  openclaw:
    category: "utility"
    tags: []
    version: "1.0.0"
---

# starmemo v2.0 - Intelligent Memory System

## Core Features

| Feature | Description |
|:-----|:-----|
| 📝 **Structured Memory** | Cause → Change → To-do format, clear at a glance |
| 📚 **Knowledge Base** | Automatically extracts knowledge points for long-term accumulation |
| 🔍 **Heuristic Recall** | Intelligently determines when to recall, precise retrieval |
| 🧠 **AI Optimization** | Structured extraction, compression, knowledge extraction |
| 🌐 **Online Learning** | Can connect to the internet to supplement knowledge when insufficient |
| 🇨🇳 **Domestic LLMs** | Huoshan, Tongyi, Wenxin, DeepSeek, etc. |

---

## Workflow

```
User Message
    ↓
1. Heuristic Judgment → Need to recall?
    ↓ Yes                 ↓ No
2. Search Memory/Knowledge Base  3. AI Extract Structure
    ↓                        ↓
4. Memory Sufficient?        Save to daily/
    ↓ Yes       ↓ No         ↓
  Answer Directly Ask Clarifying Question Extract Knowledge Points to knowledge/
                             ↓
                         Update Index
```

---

## CLI Commands

### Save Memory

```bash
# Structured Save
python3 {baseDir}/v2/cli.py save --cause "Cause" --change "What was done" --todo "To-do"

# Text Save (Automatic Structure Extraction)
python3 {baseDir}/v2/cli.py save --text "Today I learned about Python decorators, which are used to modify function behavior"

# Read from stdin
echo "Content" | python3 {baseDir}/v2/cli.py save
```

### Search Memory

```bash
python3 {baseDir}/v2/cli.py search "Keywords"
```

### Show Memory

```bash
# Today's Memory
python3 {baseDir}/v2/cli.py show

# Knowledge Base
python3 {baseDir}/v2/cli.py show --knowledge
```

### Knowledge Base Management

```bash
# Add Knowledge
python3 {baseDir}/v2/cli.py knowledge --add "Title|Content"

# List Knowledge
python3 {baseDir}/v2/cli.py knowledge
```

### Configuration Management

```bash
# View Configuration
python3 {baseDir}/v2/cli.py config --show

# Set Model
python3 {baseDir}/v2/cli.py config --llm huoshan --key YOUR_API_KEY

# Enable Online Learning
python3 {baseDir}/v2/cli.py config --web true

# Enable Persistence
python3 {baseDir}/v2/cli.py config --persist true
```

---

## Storage Structure

```
memory/
├── daily/                  # Daily Memory (Structured)
│   └── 2026-03-10.md
├── knowledge/              # Knowledge Base
│   └── Python Decorators.md
├── archive/                # Archive
├── daily-index.md          # Daily Index
└── knowledge-index.md      # Knowledge Index
```

---

## Memory Format

```markdown
## [14:30] Learning
- **Cause**: User wanted to understand Python decorators
- **Change**: Learned basic usage and common patterns of decorators
- **To-do**: Practice decorators in a project
```

---

## Triggering Conditions

**Active Saving when:**
- User shares important information (preferences, decisions)
- A valuable task is completed
- New knowledge/skills are learned
- User says "Remember", "Save"

**Active Recall when:**
- User says "Before", "Last time", "That"
- User asks "What did I say before"
- Historical decisions need to be reviewed

---

## Supported LLMs

| Vendor | Identifier |
|:-----|:-----|
| Huoshan Ark | huoshan |
| Tongyi Qianwen | tongyi |
| Wenxin Yiyan | wenxin |
| DeepSeek | deepseek |
| Zhipu AI | zhipu |
| Xunfei Spark | xinghuo |
| Tencent Hunyuan | hunyuan |

---

## Examples

**User**: "Remember I like developing with TypeScript"

**Assistant Executes**:
```bash
python3 {baseDir}/v2/cli.py save --cause "User development preference" --change "Likes developing with TypeScript"
```

**User**: "What tech stack did I mention before?"

**Assistant Executes**:
```bash
python3 {baseDir}/v2/cli.py search "tech stack"
```

---

## Current Configuration

- Model: Huoshan Ark (doubao-seed-code-preview-251028)
- AI Optimization: ✅ Enabled
- Online Learning: ✅ Enabled
- Persistence: ✅ Enabled
