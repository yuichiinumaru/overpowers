---
name: life-book
description: "Guides users to record their life stories, collect local and online materials, and generate a biographical life book. Use when: The user wants to record life experiences, create a personal biography, or organize life stories. NOT for: Diary entries, simple notes, temporary memos."
metadata:
  openclaw:
    category: "books"
    tags: ['books', 'reading', 'education']
    version: "1.0.0"
---

# Book of Life

## Core Principles

**Every conversation is an opportunity for sedimentation.** Every word the user says about their life should be recorded to continuously enrich the Book of Life.

## AI Guidance Rules

### 1. Conversation is Recording

Whenever the user shares any life experience, immediately:

1. Determine which chapter the content belongs to (see Chapter Mapping).
2. Append the content to the corresponding chapter file using the `exec` tool.
3. Continue the conversation, naturally asking for more details.

**Do not wait for the user to say "start recording"; sedimentation happens at all times.**

### 2. File Path Rules

```
~/.openclaw/workspace/life-books/[username]/chapters/[chapter_name].md
```

The default username is read from USER.md; if not set, use `default`.

Initialization directory (for first use):
```bash
mkdir -p ~/.openclaw/workspace/life-books/default/{chapters,materials,raw}
```

### 3. Chapter Mapping

| Keyword/Topic | Chapter File |
|---|---|
| Birth, childhood, when I was little, parents, hometown, old home | `Birth and Childhood.md` |
| Schooling, elementary school, middle school, high school, university, teachers, classmates | `Educational Experience.md` |
| Work, career, company, starting a business, career path, projects | `Professional Career.md` |
| Friends, dating, marriage, family, children, relationships | `Important Relationships.md` |
| Turning point, change, decision, crisis, opportunity, accident | `Life Turning Points.md` |
| Now, currently, future, dreams, plans, outlook | `Present and Outlook.md` |

### 4. Writing Format

When appending content, use the following format:

```markdown
### [Conversation Date Time]

[User's original words or summarized content]

---
```

Example:
```markdown
### 2026-03-07 14:00

I was born in Beijing in 1990 and grew up in a hutong. There were many friends in the hutong back then, and we played in the courtyard every day after school.

---
```

### 5. Follow-up Strategy

After recording the content, naturally ask one follow-up question to encourage the user to continue sharing:

- "What were the hutongs like back then?"
- "Who was your most unforgettable childhood playmate?"
- "What made you choose this job?"

**Ask only one question at a time; do not throw out multiple questions consecutively.**

### 6. Command Triggers

Users can also actively trigger the following operations:

| User Says | Action Executed |
|---|---|
| "Generate Book of Life" / "Generate Book" | Run `./life-book.sh generate` |
| "Check progress" / "See how much is written" | Run `./life-book.sh status` |
| "Add chapter XXX" | Run `./life-book.sh add-chapter XXX` |
| "Import materials [Path]" | Run `./life-book.sh import [Path]` |

### 7. Initialization Procedure

On first launch (if the chapters directory does not exist):

1. Run the initialization script to create the directory structure.
2. Greet the user and introduce the Book of Life.
3. Start with a relaxed question:

> "Let's start your Book of Life 📖 Let's begin at the very beginning—where are you from?"

### 8. Content Deduplication

Check the end of the file before appending to avoid writing the same content repeatedly. Each entry is distinguished by a timestamp.

### 9. Web Material Collection

When the user mentions a historical event, location, or person, use `web_search` to supplement background information, appended to a "Background Information" subsection in the corresponding chapter:

```markdown
#### Background Information

[Relevant historical background found via web search]
```

### 10. Periodic Summarization

After accumulating 5 entries, automatically generate a narrative summary and append it to the end of the chapter:

```markdown
#### Summary (Automatically Generated)

[Narrative summary paragraph based on the above content]
```

## Script Tools

The main script is located at: `~/.openclaw/workspace/skills/life-book/life-book.sh`

```bash
# Generate the book
~/.openclaw/workspace/skills/life-book/life-book.sh generate [username]

# Check status
~/.openclaw/workspace/skills/life-book/life-book.sh status [username]

# Add chapter
~/.openclaw/workspace/skills/life-book/life-book.sh add-chapter [username] [chapter_name]

# Import materials
~/.openclaw/workspace/skills/life-book/life-book.sh import [username] [Path|URL]
```

## Privacy Protection

- All data is stored locally at `~/.openclaw/workspace/life-books/`
- No content is uploaded to external servers.
- Sensitive content can be marked by the user as `[Private]`, and can be filtered during book generation.
