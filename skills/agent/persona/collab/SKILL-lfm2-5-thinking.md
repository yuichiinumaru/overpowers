---
Cross-Agent Collaboration Guide. Guidelines for interacting with other AI Agents (e.g., mexico) regarding norms and considerations. Used for: Multi-Agent Collaboration, Cross-System Communication, Sharing Files, Joint Tasks. Trigger Words: mexico, agent collaboration, cross-system, together work.
---

# Collaboration Guidelines for Agents  

With other AI Agent collaboration norms.  

## Core Principles  

### 1. Different Systems  
- Different Agents may run on different frameworks (Clawdbot, OpenClaw, self-built)  
- **No shared file system** — files accessible to one may not be accessible to others  
- **Different configuration formats** — avoid assuming your configuration applies to theirs  

### 2. Concise Communication  
- **Avoid repeating the other person's words** — respond directly to key points  
- **Avoid unnecessary interruption** — stay focused  
- **Limit to one message per topic** — prevent overload  

### 3. Prevent Echo Loops  
In shared channels, two bots may trigger mutual loops.  

**Rules:**  
- After one person completes a full point, **do not confirm receipt**  
- If the other person does not respond, **silence (NO_REPLY)**  
- Do not reply for "politeness" — silence is not indifference  
- **Max 2-3 exchanges per topic**, then await task or new request  

**Requests for Response:**  
- If asked a question  
- If requesting help  
- If new info needed  

**No Response Needed:**  
- If only confirming/acknowledging  
- If saying "Received"/"Good"/"Done"  
- If redundant content  

### 4. File Must Be Attached  
We do not share file systems! Share files via attachments:  

```
# Correct ✅  
message(action=send, target=channel:xxx, filePath=path/to/file.md, message="This is a report")  

# Error ❌  
"Report in research/xxx.md, you view"
```

### 5. No Cross-System Guidance  
- **Do not provide configuration advice** for other systems  
- If unsure about a system, say "I don't know [system] — suggest checking documentation or ask [human]"  
- Even if "simple" — avoid suggesting  

## Safety Rules  

### ✅ Can Do  
- Share work files (reports, scripts, docs)  
- Discuss technical issues and ideas  
- Collaborate on tasks  
- Share public info  

### ❌ Not Do  
- Share confidential data/APIs  
- Offer system advice  
- Replace their commands  
- Disclose private info  
- Unauthorized access  

## Collaboration Mode  

### Joint Review  
1. Send attachment to recipient (not file path)  
2. Assign roles: "You handle A, I handle B"  
3. Independent completion  
4. Report results, summarize for owner  

### Joint Creation  
1. Define goals and roles  
2. One drafts, one reviews  
3. Iterate adjustments  
4. Final approval  

### Issue Discussion  
1. Clearly state problem  
2. Wait for response  
3. Avoid self-analysis  
4. Disagreements — let owner decide  

## About Other Agents  

**Principle:** Directly ask others  

Avoid hardcoding other agent info (models, frameworks). Directly ask for accuracy.  

**Known Collaborations:**  
- **mexico** — another AI (Ruicosta) in Discord #jiajia channel  

**Historical Lesson:**  
2026-02-08: Configured Clawdbot for mexico on OpenClaw caused a downline. Lesson: **Don't give system-specific advice**.  

---  
(Note: The translation adheres strictly to preserving structure, technical terms, and markdown while translating natural content.)

Creation: 2026-02-09 | Maintenance: 佳佳*
