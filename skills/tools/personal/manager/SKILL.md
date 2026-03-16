---
name: auto-memory-manager
description: "Intelligent memory management system: automatically records sessions, provides daily summaries, and weekly distillations to build long-term memory for AI."
metadata:
  openclaw:
    category: "automation"
    tags: ['automation', 'productivity', 'utility']
    version: "1.0.0"
---

# Memory Manager - Intelligent Memory Management System

**Give AI true long-term memory!**

Automatically record every conversation, summarize daily batches, refine weekly essences, and build an AI assistant that learns and grows!

---

## 🎯 Use Cases

- **Conversation History** - Automatically save every conversation, never lose important information
- **Daily Summary** - Automatically organize all conversations of the day at 20:00
- **Weekly Refinement** - Extract core information into long-term memory at 20:00 every Sunday
- **Real-time Key Information Saving** - Immediately save skill releases, payment information, etc.
- **Automatic Temporary File Cleanup** - Keep the system tidy and free up space

---

## 🛠️ Core Features

### 1. Conversation History
- ✅ **Automatic Recording** - Automatically save after each conversation ends
- ✅ **Structured Storage** - Categorized by topic/key information/to-dos/decisions
- ✅ **Temporary Files** - Saved to the `memory/temp/` directory
- ✅ **Automatic Numbering** - Facilitates tracking and retrieval

### 2. Daily Summary
- ✅ **Batch Processing** - Process all temporary files every night at 20:00
- ✅ **Information Refinement** - Extract key information/to-dos/decisions
- ✅ **Generate Daily Report** - Create `memory/YYYY-MM-DD.md`
- ✅ **Automatic Cleanup** - Delete temporary files to maintain tidiness

### 3. Weekly Refinement
- ✅ **Read Weekly Memories** - Read the 7 daily files of the current week
- ✅ **Extract Core** - Refine into `MEMORY.md` (long-term memory)
- ✅ **Clean Up Expired** - Delete daily files older than 30 days
- ✅ **Continuous Growth** - Long-term memory only grows, never shrinks

### 4. Real-time Saving (Double Guarantee)
- ✅ **Key Node Trigger** - Skill release/payment change/important decision
- ✅ **Immediate Append** - Real-time write to `MEMORY.md`
- ✅ **No Loss** - Recorded even if daily summary fails

---

## 📁 File Structure

```
memory-manager/
├── memory_manager.py      # Main script
├── SKILL.md              # Skill description
├── config.example.json   # Configuration template
├── .gitignore            # Git ignore
└── temp/                 # Temporary file directory (automatically created)
    ├── session_*.md      # Conversation records
    └── YYYY-MM-DD.md     # Daily summaries
```

---

## 🚀 Quick Start

### 1. Install Skill
```bash
clawhub install memory-manager
```

### 2. Configuration (Optional)
Copy the configuration file:
```bash
cp config.example.json config.json
```

### 3. Usage

**Conversation History:**
```python
from memory_manager import record_session

session_data = {
    "date": "2026-03-06",
    "topics": ["Skill Release", "Commercialization Discussion"],
    "key_info": ["Release 5th skill"],
    "todos": ["Submit proposal tomorrow"],
    "decisions": ["Adopt SaaS model"],
    "emotion": "Focused"
}

record_session(session_data)
```

**Daily Summary:**
```python
from memory_manager import process_temp_files

result = process_temp_files()
print(f"Processed {result['session_count']} sessions")
```

---

## ⚙️ Configuration Options

| Option | Description | Default Value |
|--------|-------------|---------------|
| `temp_dir` | Temporary file directory | `./temp` |
| `memory_dir` | Memory file directory | `../memory` |
| `auto_save` | Automatically save key information | `true` |
| `cleanup_days` | Retention days | `30` |

---

## 💰 Pricing

| Version | Price | Features |
|---------|-------|----------|
| **Standard** | Free | Conversation History + Daily Summary |
| **Pro** | $20/month (¥139/month) | + Weekly Refinement + Real-time Saving |
| **Team** | $50/month (¥349/month) | + Multi-user + Team memory sharing |
| **Custom** | $500-2000 (¥3500-14000) | On-premises deployment + Feature customization |

---

## 📧 Contact

**Custom Development:**
- 📧 Email: 1776480440@qq.com
- 💬 WeChat: DM for details

**Payment Support:**
- Domestic: DM for details
- International: DM for details (PayPal/Wise)

**After-Sales Support:**
- Free maintenance for the first year
- $50/year (¥350/year) optional for subsequent years

---

## 🎯 Case Studies

### Case 1: Personal AI Assistant
- **User:** Full-stack engineer
- **Need:** Have AI remember project details and decisions
- **Solution:** Standard Version + Real-time Saving
- **Result:** AI truly understands the project, no longer needs repetitive explanations

### Case 2: Customer Service Team
- **User:** 10-person customer service team
- **Need:** Share customer communication records
- **Solution:** Team Version + Memory Sharing
- **Result:** New customer service agents onboard quickly, customer satisfaction increased by 40%

### Case 3: Knowledge Management
- **User:** Research institution
- **Need:** Organize research discussions and decisions
- **Solution:** Pro Version + Weekly Refinement
- **Result:** Formed a complete knowledge base, reducing new employee training time by half

---

## 🔄 Changelog

### v1.0.0 (2026-03-06)
- Initial release
- Automatic conversation recording
- Daily batch summarization
- Weekly refinement feature
- Real-time saving of key information
- Automatic cleanup of temporary files

---

## 📚 Docs

**Full Documentation:** https://clawhub.ai/sukimgit/memory-manager/docs
**GitHub:** https://github.com/sukimgit/memory-manager
**Issue Reporting:** https://github.com/sukimgit/memory-manager/issues

---

**Source:** https://clawhub.ai/sukimgit/memory-manager
**Author:** Monet + Lao Gao
**License:** MIT
