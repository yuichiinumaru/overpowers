---
name: agent-memory-on-demand
description: On-demand memory retrieval. Automatically searches memory and QMD for relevant information when the user asks history-related questions. Supports dual insurance of QMD search and Memory search.
tags: [agent, memory, retrieval, on-demand]
version: 1.0.0
---

# Memory On Demand - On-Demand Memory Retrieval

## Trigger Conditions

Automatically triggered when the user's question contains the following keywords:
- "before", "previously", "last time"
- "history", "record"
- "that time", "that time"
- "do you remember"
- "I previously"
- "we previously"
- "back then"

## Execution Flow

### 1. Determine if Retrieval is Needed
Check if the user's question is related to historical records.

### 2. Select Retrieval Method

**Preferred: QMD Search** (Faster, More Accurate)
```bash
qmd search "keywords" --limit 5
```

**Alternative: Memory Search**
```bash
# Search memory files
grep -r "keywords" ~/.openclaw/workspace/memory/

# Or use memory_search
```

### 3. Return Results
Organize and return the search results to the user.

## Usage Example

User asks: "What was the record from that previous fitness training session?"

Automatic Execution:
1. Detects the keyword "previously"
2. Executes `qmd search "fitness training"`
3. Returns relevant records

## Advantages

- **On-Demand Loading**: Searches only when needed, saving context.
- **Automatic Trigger**: No manual specification required.
- **Multi-Source Retrieval**: QMD + Memory for double assurance.

## Configuration

- QMD Index: Configured with workspace + butler + researcher + sessions
- Memory Files: Automatically reads memory/*.md

---
*Automatic Memory Retrieval Skill*
