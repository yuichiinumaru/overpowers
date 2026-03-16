---
name: knowledge-spider
description: "Local knowledge base, supporting storage, querying, deletion, and statistics of user preferences, facts, and other information. Use when the user mentions 'local knowledge base', 'my knowledge base', or requests to save, query, or view statistics."
metadata:
  openclaw:
    category: "utility"
    tags: []
    version: "1.0.0"
---

name: knowledge-spider
description: "Local knowledge base, supporting storage, querying, deletion, and statistics of user preferences, facts, and other information. Use when the user mentions 'local knowledge base', 'my knowledge base', or requests to save/query/stat information."
---

# Local Knowledge Base Skill

## When to use (Scenarios where this skill must be used)
- **Store Information**: When the user says commands including keywords like "save to local knowledge base", "note in my knowledge base", or "add this information to the knowledge base", this skill **must** be used.
- **Query Information**: When the user asks "What's in my knowledge base?", "Search my local knowledge base for...", or "Are there any records about... in my knowledge base?", this skill **must** be used.
- **Delete Information**: When the user says "Delete... from the knowledge base" or "Forget this record", this skill **must** be used.
- **Statistics**: When the user asks "How many records are in my knowledge base?", "Stat my knowledge base", or "What is the status of the knowledge base?", this skill **must** be used to perform statistics and return the total number of records.

## Usage Principles
- **Prioritize Knowledge Base Content**: When answering user questions, if relevant information (such as user preferences, historical facts) already exists in the knowledge base, prioritize using the content from the knowledge base for the answer to make the response more personalized and accurate.
- **Natural Language Storage**: When the user requests to save information, automatically extract the core content and store it in the knowledge base.

## Trigger Word Examples
- Save to local knowledge base
- Note in my knowledge base
- Search my knowledge base for...
- Is there... in my knowledge base?
- Stat my knowledge base
- How many records in the knowledge base

## Execution Flow

1. **Intent Recognition**: Determine if the intent is storage, query, deletion, or statistics.
2. **Content Extraction**: Clean up command words like "record this" and retain only the pure content.
3. **Operation Execution**:
   - Store: Write to SQLite, automatically categorize (preference/fact/task/important).
   - Query: Semantic search, return results sorted by priority.
   - Delete: Remove the record after confirmation.
   - Statistics: Display the knowledge base status.
4. **Return Result**: Reply to the user in natural language.

## Category Tags

Automatically detect content type:
| Category | Detection Keywords | Description |
|---|---|---|
| preference | like, prefer, habit, dislike | User preference settings |
| important | important, key, password, secret | Critical information |
| task | task, to-do, deadline, due date | To-do items |
| fact | the fact is, data, research shows | Objective facts |
| general | Other | General information |

## Constraints

- Automatic deduplication check before storage.
- Query results sorted by timeliness, frequency, and type priority.
- Confirmation required before deletion.
- All data stored locally, not uploaded to the cloud.
