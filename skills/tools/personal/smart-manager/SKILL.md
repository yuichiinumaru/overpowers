---
name: system-memory-smart-manager
description: Intelligent memory management for agents with short/long-term memory layering, semantic search, auto summarization, and RAG enhancement.
tags: [memory, system, rag, summarization]
version: 1.0.0
---

# 🧠 Smart Memory Manager

## Key Highlights
1. 📚 **Hierarchical Memory System**: Three-layer architecture (short-term/long-term/important), automatically cleans expired memories to solve context overflow issues.
2. 🔍 **Multi-Mode Retrieval**: Supports keyword, semantic, and hybrid retrieval modes for fast memory recall and improved RAG accuracy.
3. 📝 **Auto-Summarization**: One-click memory summary generation, supporting long-session context compression, reducing token usage by up to 70%.
4. 💾 **Persistence Support**: Supports memory and disk persistence, ensuring memories are not lost after a restart.

## 🎯 Use Cases
- Long-session agents and chatbots.
- Memory layer for RAG applications.
- Task-oriented agents requiring long-term memory.
- Context management for customer service and assistant agents.

## 📝 Parameter Description
| Parameter | Type | Required | Description |
|------|------|------|------|
| action | string | Yes | Operation type: add/search/summarize/clear/list/load/save |
| content | string | No | Required for 'add', the content of the memory. |
| type | string | No | Optional for 'add', memory type: short-term/long-term/important (default: short-term). |
| query | string | No | Required for 'search', search keywords. |
| limit | number | No | Optional for 'search/list', number of results to return (default: 5/20). |
| typeFilter | string | No | Optional for all, filter by memory type (default: all). |
| persist | boolean | No | Optional for 'add', whether to persist storage (default: false). |
| persistPath | string | No | Optional for 'load/save', persistence file path (default: ./memory-store.json). |

## 💡 Out-of-the-Box Examples
### Adding Memory
```typescript
// Add long-term memory
await skills.smartMemoryManager({
  action: "add",
  content: "User likes coffee, no sugar, and drinks milk tea every Wednesday afternoon",
  type: "long-term",
  persist: true
});
```

### Searching Memory
```typescript
const result = await skills.smartMemoryManager({
  action: "search",
  query: "User preferences",
  limit: 3,
  searchMode: "hybrid" // Keyword + semantic hybrid search
});
```

### Generating Session Summary
```typescript
const summary = await skills.smartMemoryManager({
  action: "summarize",
  typeFilter: "short-term",
  maxTokens: 500
});
```

### Persistence and Loading
```typescript
// Save all memories to disk
await skills.smartMemoryManager({
  action: "save",
  persistPath: "./my-memory.json"
});

// Load memories from disk
await skills.smartMemoryManager({
  action: "load",
  persistPath: "./my-memory.json"
});
```

## 🔧 Technical Implementation Notes
- Built-in automatic cleanup mechanism; short-term memory retains a maximum of 100 entries to avoid memory overflow.
- Modular design allows for easy integration with vector databases for semantic retrieval.
- End-to-end type safety with automatic parameter validation.
- Lightweight with no external dependencies, ready to use, and supports custom extensions.
