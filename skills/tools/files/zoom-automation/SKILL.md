---
name: zoom-automation
description: Automate Zoom meeting creation, management, recordings, webinars, and
  participant tracking via Rube MCP (Composio). Always search tools first for current
  schemas.
tags:
- infra
- ops
version: 1.0.0
category: general
---
# Zoom Automation

Automate Zoom meeting scheduling, webinar management, cloud recording retrieval, and participant tracking through Composio's Zoom toolkit via Rube MCP.

## When to Use

- User wants to create, schedule, or manage Zoom meetings.
- User needs to list upcoming, live, or past meetings.
- User wants to manage cloud recordings (list, retrieve, delete).
- User needs to get meeting participant lists or usage reports.
- User wants to manage webinars or register participants for them.

## Prerequisites

- Rube MCP must be connected (RUBE_SEARCH_TOOLS available)
- Active Zoom connection via `RUBE_MANAGE_CONNECTIONS` with toolkit `zoom`.
- Paid Zoom account (Pro plan or higher) required for most features (recordings, participants).

## Instructions

### Step 1: Setup
1. Verify Rube MCP is available by confirming `RUBE_SEARCH_TOOLS` responds.
2. Call `RUBE_MANAGE_CONNECTIONS` with toolkit `zoom`.
3. If connection is not ACTIVE, follow the returned auth link to complete Zoom OAuth.
4. Confirm connection status shows ACTIVE before running any workflows.

### Step 2: Execution
Use the appropriate tool sequence based on the task:

#### Create and Schedule Meetings
1. `ZOOM_CREATE_A_MEETING` - Create meeting with topic, start_time, duration, and settings.
   - Note: Use `userId: "me"` for the authenticated user.
2. `ZOOM_GET_A_MEETING` to retrieve the `join_url` and `start_url`.

#### Manage Recordings
1. `ZOOM_LIST_ALL_RECORDINGS` to find recordings within a date range (max 1 month).
2. `ZOOM_GET_MEETING_RECORDINGS` for specific meeting files.

#### Participant Tracking
1. `ZOOM_GET_PAST_MEETING_PARTICIPANTS` to list attendees of a completed meeting.
   - Note: Always follow `next_page_token` for complete results.

### Step 3: Verification
- Check the tool output for success status and returned IDs.
- For meetings, verify the `join_url` is valid.
- For participants/reports, ensure the list is not empty (if expected).

## Examples

```json
/* Scheduling a meeting with specific timezone and auto-recording */
{
  "userId": "me",
  "topic": "Project Sync",
  "start_time": "2026-03-10T14:00:00Z",
  "duration": 45,
  "settings__auto_recording": "cloud"
}
```

## Troubleshooting

| Problem | Solution |
|:--------|:---------|
| Connection not ACTIVE | Follow OAuth link via `RUBE_MANAGE_CONNECTIONS` |
| 400 Error on Summary | AI Companion must be enabled on a paid plan |
| Empty participant list | Solo meetings return empty results; check if meeting was attended |
| UUID Error | Double URL-encode UUIDs starting with `/` or containing `//` |
