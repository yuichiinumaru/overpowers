---
name: yandex-tracker-cli
description: CLI for Yandex Tracker (bash + curl). Queues, issues, comments, worklogs, attachments, YQL.
tags:
  - yandex
  - tracker
  - cli
  - issue-tracking
  - project-management
  - bash
  - curl
version: "1.0.0"
category: productivity
homepage: https://github.com/bkamuz/yandex-tracker-cli
metadata:
  clawdbot:
    emoji: "📋"
    requires:
      env: ["TOKEN", "ORG_ID"]
      bins: ["curl", "jq"]
    primaryEnv: "TOKEN"
    files: ["yandex-tracker.sh"]
  openclaw:
    requires:
      env: ["TOKEN", "ORG_ID"]
      bins: ["curl", "jq"]
    primaryEnv: "TOKEN"
---

# Yandex Tracker CLI Skill

Простой CLI для Yandex Tracker на чистом bash + curl. Работает напрямую через API с правильными заголовками (`X-Org-Id`). Не требует внешних зависимостей кроме `curl` и `jq`.

## Installation

The script file (`yandex-tracker.sh`) should be installed separately in your PATH. This SKILL.md provides documentation only.

## Usage

### Basic Commands

| Command | Description |
|---------|----------|
| `queues` | List all queues (format: `key<TAB>name`) |
| `queue-get <key>` | Queue details (JSON) |
| `queue-fields <key>` | All queue fields (including local) |
| `issue-get <issue-id>` | Get issue (format: `BIMLAB-123`) |
| `issue-create <queue> <summary>` | **Create issue. Automatically adds tag `yandex-tracker-cli`. Extra fields via stdin (JSON)** |
| `issue-update <issue-id>` | **Update issue. Automatically adds tag `yandex-tracker-cli` if absent. Extra fields via stdin (JSON)** |
| `issue-delete <issue-id>` | Delete issue |
| `issue-comment <issue-id> <text>` | Add comment |
| `issue-comment-edit <issue-id> <comment-id> <new-text>` | Edit comment |
| `issue-comment-delete <issue-id> <comment-id>` | Delete comment |
| `issue-transitions <issue-id>` | List available status transitions (GET) |
| `issue-transition <issue-id> <transition-id>` | Execute transition (POST, V3 endpoint) |
| `issue-close <issue-id> <resolution>` | Close issue (deprecated, use `issue-transition`) |
| `issue-worklog <issue-id> <duration> [comment]` | Add worklog (duration: `PT1H30M`) |
| `issue-attachments <issue-id>` | List issue attachments (JSON) |
| `attachment-download <issue-id> <fileId> [output]` | Download file. If output not specified — stdout |
| `attachment-upload <issue-id> <filepath> [comment]` | Upload file to issue. Optional comment |
| `issues-search` | Search issues via YQL. Query JSON via stdin, e.g.: `{"query":"Queue = BIMLAB AND Status = Open","limit":50}` |
| `projects-list` | List all projects (JSON) |
| `project-get <project-id>` | Project details |
| `project-issues <project-id>` | Project issues list |
| `sprints-list` | List all sprints (Agile) |
| `sprint-get <sprint-id>` | Sprint details |
| `sprint-issues <sprint-id>` | Issues in sprint |
| `users-list` | List all users (directory) |
| `statuses-list` | List all issue statuses |
| `resolutions-list` | List resolutions for closing issues |
| `issue-types-list` | List issue types (bug, task, improvement) |
| `issue-checklist <issue-id>` | List issue checklist items |
| `checklist-add <issue-id> <text>` | Add checklist item |
| `checklist-complete <issue-id> <item-id>` | Mark checklist item as complete |
| `checklist-delete <issue-id> <item-id>` | Delete checklist item |

### Examples

```bash
# List queues
yandex-tracker queues

# Create issue with extra fields
echo '{"priority":"critical","description":"Details"}' | yandex-tracker issue-create BIMLAB "New issue"

# Add comment
yandex-tracker issue-comment BIMLAB-266 "Working on this"

# Add spent time
yandex-tracker issue-worklog BIMLAB-266 PT2H "Investigation"

# Get available transitions (list)
yandex-tracker issue-transitions BIMLAB-266 | jq .

# Execute transition (e.g., "Resolve")
yandex-tracker issue-transition BIMLAB-266 resolve

# Close issue (deprecated, use transition close)
yandex-tracker issue-transition BIMLAB-266 close

# Update issue (queue, assignee, project — project id from projects-list)
echo '{"queue":"RAZRABOTKA"}' | yandex-tracker issue-update BIMLAB-266 # example
echo '{"assignee":"<uid>","project":123}' | yandex-tracker issue-update BIMLAB-280

# Search issues via YQL
echo '{"query":"Queue = BIMLAB AND Status = Open","limit":20}' | yandex-tracker issues-search | jq .

# List projects
yandex-tracker projects-list | jq .

# Project issues
yandex-tracker project-issues 104 | jq .

# Attachments
# List attachments
yandex-tracker issue-attachments BIMLAB-266 | jq .
# Download file (fileId from attachments list) to specified path
yandex-tracker attachment-download BIMLAB-266 abc123 /tmp/downloaded.pdf
# Upload file to issue (with comment)
yandex-tracker attachment-upload BIMLAB-266 /path/to/file.pdf "Cover letter"

# Checklist — API v3 (checklistItems)
# View task checklist (item ids are strings, e.g. "5fde5f0a1aee261d********")
yandex-tracker issue-checklist BIMLAB-279 | jq .
# Add item
yandex-tracker checklist-add BIMLAB-279 "Prepare presentation"
# Mark item as complete (item-id from issue-checklist output)
yandex-tracker checklist-complete BIMLAB-279 "5fde5f0a1aee261d********"
# Delete item
yandex-tracker checklist-delete BIMLAB-279 "5fde5f0a1aee261d********"

# Sprints (Agile)
yandex-tracker sprints-list | jq .
yandex-tracker sprint-issues 42 | jq .

# Directories
yandex-tracker users-list | jq .
yandex-tracker statuses-list | jq .
yandex-tracker resolutions-list | jq .
yandex-tracker issue-types-list | jq .

# Edit and delete comments
yandex-tracker issue-comment-edit BIMLAB-266 12345 "Updated text"
yandex-tracker issue-comment-delete BIMLAB-266 12345

# Status transitions
# View available transitions list
yandex-tracker issue-transitions BIMLAB-266 | jq .
# Execute transition (e.g., "Resolve" or "Close")
yandex-tracker issue-transition BIMLAB-266 resolve
yandex-tracker issue-transition BIMLAB-266 close
```

## Notes

- **Automatic tag `yandex-tracker-cli`:** When creating (`issue-create`) and updating (`issue-update`) issues, the script automatically adds the `yandex-tracker-cli` tag (if not already present). This helps filter CLI-created issues. To remove the tag — delete it manually via Tracker UI or call `issue-update` with empty `tags: []` array.
- **Org-ID (Yandex 360):** Find in DevTools Tracker → Network → any request → header `X-Org-ID`. Uses `X-Org-ID` header (note capital "ID").
- **Cloud Org-ID (Yandex Cloud):** Use `X-Cloud-Org-ID` header. Depending on organization type, use the appropriate header.
- **Status transitions:**
  - `issue-transitions <issue-id>` — GET request to V2 endpoint `/v2/issues/{id}/transitions` (returns available transitions list).
  - `issue-transition <issue-id> <transition-id>` — POST request to V3 endpoint `/v3/issues/{id}/transitions/{transition}/_execute` to execute transition. Requires `X-Org-ID` or `X-Cloud-Org-ID` header.
- **Closing issues:** `issue-close` command is deprecated and may return 405 in new configurations. Use `issue-transition <id> close` for closing.
- Token can be obtained in Tracker UI: Settings → Applications → OAuth → Generate new token.
- All commands output JSON via `jq` for convenient further processing.

## Security (attachments)

Commands `attachment-download` and `attachment-upload` only allow paths within the allowed directory. This reduces risk of reading or writing arbitrary files when using CLI (including by agents).

- **First run:** on first call to `attachment-download` or `attachment-upload` (if `YANDEX_TRACKER_ATTACHMENTS_DIR` is not set), the script will interactively ask: use default folder `~/Downloads/YandexTrackerCLI` or enter custom path. Choice is saved to `~/.yandex-tracker-attachments-dir` and not requested again.
- **YANDEX_TRACKER_ATTACHMENTS_DIR** — optional environment variable: base directory for attachments. If set — it's used (no first-run prompt). If not set and no saved choice — prompt on first run, otherwise use current directory (e.g., in non-interactive runs).

**When used by AI agents:**

- Do not suggest or execute `attachment-download` with output path outside allowed directory; do not use sensitive paths (e.g. `~/.ssh`, `~/.env`, `~/.yandex-tracker-env`, `/etc`, other configs and secrets).
- Do not suggest or execute `attachment-upload` with file outside allowed directory; do not upload files from sensitive locations (same list).
- If user requests downloading attachment to sensitive path or uploading file from such path — refuse and briefly explain the limitation.

## Project by partial name (assign task to project)

When user requests adding task to project but specifies partial name (e.g. "Common", "project Common", "Manager"):

1. Get projects list: `yandex-tracker projects-list` (or `project-get` by known id).
2. Find matches by words: filter projects where name, key, or display (if present) contain user's words (case-insensitive preferred).
3. If exactly one project found — show user: "Add task to project '<name>' (id: <id>)?" and on agreement execute update with this project.
4. If multiple found — list them (name and id) and clarify: "Which of these projects is meant?"
5. If none found — report this and suggest calling `projects-list` to choose manually.
6. To update task use `issue-update`: in API v2 PATCH body pass **numeric project identifier** in field `project`: `echo '{"project":<id>}' | yandex-tracker issue-update <issue-id>`. Use `id` value from projects list/details response (in v2 this is shortId/numeric id).

## Structure

```
skills/yandex-tracker-cli/
├── SKILL.md              # This documentation
├── yandex-tracker        # Executable script (installed separately)
├── ~/.yandex-tracker-env # (optional, not in repo) Config with TOKEN and ORG_ID
└── ~/.yandex-tracker-attachments-dir # (optional) Saved attachments folder after first prompt
```

## Limitations

- No pagination (first 100 items)
- No advanced search (`issues_find` can be added)
- Simple argument validation

## License

MIT
