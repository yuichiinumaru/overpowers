---
description: Comprehensive workflow for creating and publishing technical articles to CSDN.
---
# Workflow: CSDN Automated Publishing

This workflow covers the end-to-end process from ideation to live publication on CSDN.

## Steps

### 1. Information Gathering
- Confirm topic, technical angle, and source materials with the user.
- Define target article length and depth.

### 2. High-Quality Drafting
- Reference `style-guide-cn.md` for tone and structure.
- Incorporate code snippets and relevant links.
- Produce a Markdown draft for user approval.

### 3. Preparation for Launch
- Save final content to `/tmp/csdn-article-YYYY-MM-DD.md`.
- Ensure browser dependencies and Playwright are ready.

### 4. Authentication and Access
- Check `csdn-cookie.json` for validity.
- If needed, generate login QR code and send to user for scanning.

### 5. Automated Injection and Publishing
- Open CSDN Markdown editor via automated browser.
- Inject article title and body using the CDP injection script.
- Select appropriate tags and categories.
- Click 'Publish' and verify successful submission.

### 6. Post-Publication
- Provide the live article link to the user.
- Update local tracking logs.
