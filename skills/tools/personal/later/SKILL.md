---
name: read-it-later
description: "Save and retrieve 'read it later' content - links, articles, notes, and ideas for future reference. Use when the user wants to (1) save a link, URL, article, or note to read later, (2) retrieve pre..."
metadata:
  openclaw:
    category: "utility"
    tags: []
    version: "1.0.0"
---

# Read It Later

Help users save and retrieve content for later reading.

## Core Features

### 1. Save Content

When the user wants to save content:

1. Read the `read-it-later.md` file (create if it doesn't exist)
2. Append the new content to the file in the specified format

**Storage Format:**
```markdown
## [Category Tag] Title/Summary

- **Source**: URL or source description
- **Added Time**: YYYY-MM-DD HH:mm
- **Status**: Unread / Read / Archived

Content summary or user notes...

---
```

**Supported Input Types:**
- URL/Link
- Article Title + Link
- Plain text notes/ideas
- Images/Files (saving path or description)

### 2. Retrieve Content

When the user wants to view saved content:

1. Read `read-it-later.md`
2. Filter based on user requirements:
   - Filter by status (Unread/Read/All)
   - Filter by tag
   - Filter by date range
   - Keyword search

### 3. Update Status

Supports marking content status:
- `Unread` → `Read`
- Move to `Archived`

## File Location

Default storage location: `~/read-it-later.md`

If `read-it-later.md` exists in the workspace, prioritize the file within the workspace.

## Usage Examples

**Saving:**
- "Help me save this link https://example.com/article"
- "Note this: read this article about AI later"
- "read it later: best practices for design systems"

**Retrieving:**
- "What links have I saved?"
- "Show me my read-it-later list"
- "Find content about [tag]"
- "Mark this article as read"

## Workflow

### Saving Content

1. Determine file path (workspace or user directory)
2. Read existing content
3. Parse user input, extracting:
   - URL (if present)
   - Title/Description
   - Tags (specified by the user or inferred automatically)
4. **If it is a URL: Automatically fetch content and apply tags**
   - Use kimi_fetch to get web content
   - Analyze content topic
   - Automatically select the most relevant tag (choose from predefined tags)
   - Extract or generate a title
5. Append the new entry in the specified format
6. Save the file
7. Confirm successful save, display automatically identified tags

### Automatic Tagging Rules

Predefined Tags:
- `#ai` - Content related to Artificial Intelligence, Machine Learning, Large Models
- `#yc-combinator` - Content related to YC, startups, financing
- `#podcast` - Podcasts, audio content
- `#技术` - Programming, development, tools
- `#设计` - UI/UX, visual design
- `#产品` - Product management, operations, growth
- `#商业` - Business analysis, industry trends
- `#待分类` - When the category cannot be determined

**Auto-Tagging Logic:**
- Analyze the topic after fetching URL content
- Select 1-2 most relevant tags
- If the content involves multiple domains, select the primary one
- Use `#待分类` if the category cannot be determined

### Retrieving Content

1. Determine file path
2. Read file content
3. Parse entries based on filtering criteria
4. Format output for the user

### Updating Status

1. Read the file
2. Locate the target entry
3. Modify the status field
4. Save the file
