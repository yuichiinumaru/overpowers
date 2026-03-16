---
name: lessons-learned
description: "Lessons Learned - > OpenClaw Skill - Error Learning and Long-Term Memory System"
metadata:
  openclaw:
    category: "utility"
    tags: []
    version: "1.0.0"
---

# lessons_learned Skill

> OpenClaw Skill - Error Learning and Long-Term Memory System

---

## Trigger Conditions

### Automatic Triggers
- User expresses preference: "I like..." / "Do not..." / "Remember..."
- When an operation fails
- When executing high-risk operations
- When user input contains prohibited words
- When user input contains emergency stop words

### Manual Triggers
```
/lessons_learned learn <error_description>    # Record error
/lessons_learned check <operation>         # Check operation
/lessons_learned memory <content>       # Persist information
```

---

## Execution Flow

### 1. Prohibited Word Check (Highest Priority)

When the following words are detected, **stop immediately** without executing any operation:

```
delete / clear / format / rm -rf
send email / send message / commit code
execute command / sudo / chmod 777
```

**Reaction**:
```
Stop operation immediately
Output: "This operation is risky, please confirm execution"
Wait for user confirmation
```

### 2. Emergency Stop Check

When user input contains the following words, **immediately stop all operations**:
- Stop / stop / halt
- Cancel / cancel / abort
- Hold on / hold on / wait

### 3. User Habit Matching

Execute automatically based on user habits:
- User speaks Chinese $\rightarrow$ Reply in Chinese
- User speaks English $\rightarrow$ Reply in English
- User provides a file path $\rightarrow$ Read content first
- User provides a URL $\rightarrow$ Fetch content first

### 4. Error Logging

When an operation fails:
1. Log to `memory/lessons/MISTAKES.md`
2. Analyze the cause of failure
3. Generate avoidance rules
4. Write to `memory/lessons/LESSONS_LEARNED.md`

### 5. Information Persistence

When the user expresses a preference:
1. Write immediately to `MEMORY.md`
2. Record the habit in `memory/lessons/HABITS.md`
3. Update `memory/lessons/PROHIBITED.md` if necessary

---

## Core Rules

### Prohibited
- ❌ Repeating known failed operations
- ❌ Ignoring recorded user preferences
- ❌ Skipping prohibited word checks
- ❌ Ignoring emergency stop words

### Must
- ✅ Prohibited words $\rightarrow$ Stop immediately
- ✅ Emergency stop words $\rightarrow$ Stop immediately
- ✅ Preferences $\rightarrow$ MEMORY.md
- ✅ Failure $\rightarrow$ MISTAKES.md
- ✅ Habits $\rightarrow$ HABITS.md
- ✅ Risky operations $\rightarrow$ Confirmation

---

## File Locations

| File | Purpose |
|------|------|
| memory/lessons/MISTAKES.md | Error log |
| memory/lessons/LESSONS_LEARNED.md | Enforced guidelines |
| memory/lessons/PROHIBITED.md | List of prohibited words |
| memory/lessons/HABITS.md | User habits |
| memory/lessons/SYSTEM_PROMPT.md | Injection template |
| MEMORY.md | Long-term memory |

---

## Error Levels

| Level | Definition | Handling |
|------|------|------|
| P0 | Critical | Stop immediately |
| P1 | Severe | Log and recover |
| P2 | General | Log and continue |
| P3 | Minor | Log only |

---

## Examples

### Prohibited Word Trigger
```
User: "Help me delete this directory"
Agent: "This operation is risky, please confirm execution"
```

### Emergency Stop
```
User: "Stop the current operation"
Agent: (Stop all operations immediately)
```

### Recording an Error
```
/lessons_learned learn "Did not check permissions when deleting file"
```

### Persisting a Preference
```
User: "I prefer to reply in Chinese"
→ Automatically written to MEMORY.md
→ Automatically written to HABITS.md
```

---

> **Version**: 2.0.0 | **Updated**: 2026-02-26
