---
name: reading-list
description: "Reading List - 📚 Intelligent reading list management, efficient learning, track reading progress, intelligent recommendations."
metadata:
  openclaw:
    category: "reading"
    tags: ['reading', 'books', 'education']
    version: "1.0.0"
---

# Reading List Skill

📚 Intelligent reading list management, efficient learning, tracking reading progress, and smart recommendations.

## Features

### Core Features
- **Reading List Management** - Add, delete, archive articles
- **Reading Progress Tracking** - Record reading status and time
- **Smart Recommendations** - Recommend relevant content based on interests
- **Note Organization** - Automatically extract summaries and notes
- **Reading Statistics** - Visualize reading data

### Advanced Features
- **Multi-Source Support** - URL, PDF, Markdown
- **Tagging** - Categorize by topic/priority
- **Reading Reminders** - Timed reminders to read
- **Sharing Functionality** - Share reading lists
- **Export Functionality** - Export to Notion/Obsidian

## Usage

### Add Article
```
Add article to reading list: https://example.com/article
```

### Batch Add
```
Add the following articles to the reading list:
- https://blog.com/post1
- https://blog.com/post2
- https://blog.com/post3
```

### View List
```
View my reading list
```

### Update Progress
```
Mark "OpenClaw Complete Guide" as read
```

### Summarize Article
```
Summarize the key points of this article: https://example.com/article
```

### Smart Recommendations
```
Recommend some articles about AI programming
```

## Output Format

### Reading List
```
📚 Reading List

## 🔴 High Priority (5 articles)
1. [ ] OpenClaw Skills Development Guide - Estimated 15 minutes
2. [ ] Deep Dive into React Server Components - Estimated 20 minutes
3. [ ] Best Practices for AI Agent Workflows - Estimated 25 minutes

## 🟡 To Read (15 articles)
1. [ ] New Features in TypeScript 5.0 - Estimated 10 minutes
2. [ ] Node.js Performance Optimization Techniques - Estimated 15 minutes
3. [ ] Practical Guide to Docker Containerization - Estimated 20 minutes

## 🟢 In Progress (3 articles)
1. [⏳ 60%] Understanding TypeScript in Depth
2. [⏳ 30%] Node.js Performance Optimization
3. [⏳ 10%] Docker Practical Guide

## ✅ Completed (28 articles)
1. [✅] JavaScript Design Patterns - Read 3 days ago
2. [✅] Git Workflow Explained - Read 5 days ago
3. [✅] HTTP Protocol Complete Guide - Read 1 week ago

## 📊 Reading Statistics
- This week read: 8 articles
- This month read: 28 articles
- Total reading time: 12 hours
- Completion rate: 65%
```

### Article Summary
```
📄 Article Summary: OpenClaw Complete Guide

## Key Takeaways
1. OpenClaw is an open-source AI Agent platform
2. Supports multiple communication channels (Telegram/WhatsApp/WeChat)
3. The Skills system empowers Agents with custom capabilities
4. The heartbeat mechanism enables automated tasks

## Key Concepts
- Agent: AI assistant instance
- Skill: Extensible capability module
- Heartbeat: Scheduled task mechanism
- Memory: Persistent memory system

## Recommended Reading Time
Estimated 15 minutes

## Related Articles
- OpenClaw Skills Development Guide
- AI Agent Automation Workflows
```

## Use Cases

1. **Technical Learning** - Manage reading lists for technical articles
2. **Industry Research** - Collect industry reports and news
3. **Content Creation** - Organize materials and reference articles
4. **Knowledge Management** - Build a personal knowledge base
5. **Team Sharing** - Share team reading lists

## Best Practices

- Use tags to categorize articles (e.g., `#frontend` `#ai` `#business`)
- Set priorities to read important articles first
- Regularly clean up outdated articles
- Record notes promptly after reading
- Review reading statistics weekly

## Data Storage

The reading list is stored at `~/.openclaw/workspace/memory/reading-list.json`

---

Created: 2026-03-11
Author: ClawMart
Version: 1.0.0
