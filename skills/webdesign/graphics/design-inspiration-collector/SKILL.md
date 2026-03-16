---
name: design-ux-design-inspiration-collector
version: 1.0.0
description: Multi-platform design inspiration collector. Searches Behance, Dribbble, and Pinterest for design references, UI inspiration, and visual ideas, then compiles them into a structured Feishu document.
tags: [design, inspiration, ui, ux, behance, dribbble, pinterest, feishu]
category: design-ux
---

# Design Inspiration Collector

Helps users efficiently collect design inspiration from Behance, Dribbble, and Pinterest, and generates Lark documents.

## Features

1. **Multi-Platform Search**: Automatically searches Behance, Dribbble, and Pinterest.
2. **Lark Document**: Automatically generates a Lark document named in the format "keyword + date and time".
3. **Trend Analysis**: Extracts AI design trend summaries.
4. **Related Recommendations**: Recommends related design directions for further exploration.

## Workflow

### Step 1: Understand Requirements

When the user proposes a design direction, confirm:
- Specific domain (App type, design style, platform, etc.)
- Any specific requirements (e.g., "mobile only", "only Dashboards")

### Step 2: Multi-Platform Search

Use Tavily API to search the three platforms:

```python
# Pinterest
query = f"site:pinterest.com {topic} ui ux design 2026"

# Dribbble
query = f"site:dribbble.com {topic} ui design 2026"

# Behance
query = f"site:behance.net {topic} ui ux design 2026"
```

### Step 3: Generate Lark Document

Use the `feishu_doc` tool to create a Lark document:

```python
# 1. Create document, named: keyword + date and time
feishu_doc action=create title="{keyword}_{YYYYMMDD_HHMMSS}"

# 2. Write Markdown content
feishu_doc action=write doc_token=xxx content="markdown content"
```

**Document Naming Format**: `{keyword}_{YYYYMMDD_HHMMSS}`

Examples:
- `Healthcare App Design Inspiration_20260311_170245`
- `Finance Dashboard_20260311_143022`

### Step 4: Send Document Link

Send the Lark document link to the user in the following format:

```
# {Topic} Design Inspiration Collection

> Source: Behance, Dribbble, Pinterest

---

## 📊 Trend Overview

{AI analyzed design trends}

---

## 🎨 Pinterest Picks (5 items)

1. **{Title}** ⭐⭐⭐⭐⭐
   - Link: {URL}
   - Description: {Description}

2. **{Title}** ⭐⭐⭐⭐
   - Link: {URL}
   - Description: {Description}

... (Total 5 items)

---

## 🎯 Dribbble Picks (5 items)

...

---

## 💎 Behance Picks (5 items)

...

---

## 🔍 Search Keywords

- `{topic} ui design`
- `{topic} app ui`
- `{topic} dashboard`
- `{topic} mobile`

---

## 📌 Related Direction Recommendations

Shall I help you search for the following sub-topics?

1. **{Direction 1}** - {Brief Description}
2. **{Direction 2}** - {Brief Description}
3. **{Direction 3}** - {Brief Description}
```

---

**Lark Document Link**: https://feishu.cn/docx/xxx

---

## Dependencies

| Tool | Purpose | Installation |
|------|---------|--------------|
| Tavily API | Search three design platforms | `pip install tavily-python` |
| feishu_doc | Create Lark documents | Built-in |

## Configuration

### Tavily API Key

Set in the environment:
```bash
export TAVILY_API_KEY="tvly-your_key"
```

Or modify the default value in the script.

## Usage

### Basic Usage

When the user says "Help me collect design inspiration for XXX":

1. Use Tavily to search the three platforms.
2. Take the top 5 results from each platform.
3. Organize into Markdown format.
4. Send directly in the chat window.
5. Recommend related directions.

### Example Conversation

**User:** Help me collect design inspiration for a healthcare app.

**Execution:**
1. Search three platforms: `healthcare app ui design`
2. Organize 15 items (5 from each platform).
3. Create Lark document: `Healthcare App Design Inspiration_20260311_170245`
4. Send the document link to the user.
5. Recommend related directions: AI Consultation, Health Tracking, Telemedicine.

**Reply:**
```
✅ Lark document created!

**Document Name**: Healthcare App Design Inspiration_20260311_170245
**Document Link**: https://feishu.cn/docx/xxx

Collected 15 design inspirations (5 from Pinterest, 5 from Dribbble, 5 from Behance).

---

## 📌 Related Direction Recommendations

1. **AI Consultation Assistant** - Intelligent consultation, symptom analysis
2. **Health Tracking** - Exercise logging, sleep monitoring
3. **Telemedicine** - Video consultations, prescription management
```

## Search Tips

### Popular Design Directions

| Direction | Keywords |
|-----------|----------|
| Mobile App | mobile app, ios, android, app ui |
| Web Design | web design, landing page, website |
| Dashboard | dashboard, admin panel, data viz |
| E-commerce | ecommerce, shop, checkout |
| Finance | fintech, banking, crypto, payment |
| Health | health, medical, fitness, wellness |
| Style | glassmorphism, neumorphism, minimal |

## Notes

1. **Search all three platforms**: Pinterest, Dribbble, Behance, at least 5 items from each platform.
2. **Lark document naming**: Must follow the `{keyword}_{YYYYMMDD_HHMMSS}` format.
3. **Categorize by platform**: Clearly label Pinterest, Dribbble, and Behance in the document.
4. **Recommended content**: Recommend 3-5 related directions at the end (without links).
5. **Star rating**: Assign a 1-5 star rating based on relevance.
6. **Send link**: Must send the Lark document link to the user.
