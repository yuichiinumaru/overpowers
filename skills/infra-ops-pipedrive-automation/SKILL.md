---
name: pipedrive-automation
description: Automate Pipedrive CRM operations including deals, contacts, organizations, activities, notes, and pipeline management via Rube MCP (Composio). Always search tools first for current schemas.
tags:
- infra
- ops
---
# Pipedrive Automation

Automate Pipedrive CRM workflows through Composio's Pipedrive toolkit via Rube MCP.

## When to Use

- User wants to create or manage deals in the sales pipeline.
- User needs to manage contacts (persons and organizations).
- User wants to schedule and track activities (calls, meetings, tasks).
- User needs to add and manage notes attached to entities.
- User wants to query pipelines, stages, or deals within them.

## Prerequisites

- Rube MCP must be connected (RUBE_SEARCH_TOOLS available)
- Active Pipedrive connection via `RUBE_MANAGE_CONNECTIONS` with toolkit `pipedrive`.
- Active Pipedrive account with necessary permissions.

## Instructions

### Step 1: Setup
1. Verify Rube MCP is available by confirming `RUBE_SEARCH_TOOLS` responds.
2. Call `RUBE_MANAGE_CONNECTIONS` with toolkit `pipedrive`.
3. If connection is not ACTIVE, follow the returned auth link to complete Pipedrive OAuth.
4. Confirm connection status shows ACTIVE before running any workflows.

### Step 2: Execution
Always resolve display names to numeric IDs before operations:

#### Manage Deals
1. `PIPEDRIVE_GET_ALL_PIPELINES` and `PIPEDRIVE_GET_ALL_STAGES` to resolve IDs.
2. `PIPEDRIVE_ADD_A_DEAL` - Create deal with title, value, org_id, person_id, and stage_id.
3. `PIPEDRIVE_UPDATE_A_DEAL` - Modify deal properties using numeric ID.

#### Manage Contacts
1. `PIPEDRIVE_SEARCH_PERSONS` or `PIPEDRIVE_SEARCH_ORGANIZATIONS` to find existing entities.
2. `PIPEDRIVE_ADD_A_PERSON` or `PIPEDRIVE_ADD_AN_ORGANIZATION` to create new contacts.
   - Note: Email and phone fields are arrays of objects (e.g., `[{"value": "test@example.com", "label": "work", "primary": true}]`).

#### Schedule Activities
1. `PIPEDRIVE_ADD_AN_ACTIVITY` - Create activity with subject, type, and due_date.
2. `PIPEDRIVE_UPDATE_AN_ACTIVITY` - Modify activity details or mark as done (`done: 1`).

#### Add Notes
1. `PIPEDRIVE_ADD_A_NOTE` - Create note with HTML content linked to an entity ID.

### Step 3: Verification
- Check the output of the tool call for success status.
- Verify IDs return in the response for created entities.
- Use `PIPEDRIVE_GET_DETAILS_OF_A_DEAL` (or other entities) to verify the state.

## Examples

```json
/* Adding a person with formatted email/phone */
{
  "name": "John Doe",
  "email": [{"value": "john@example.com", "label": "work", "primary": true}],
  "phone": [{"value": "+123456789", "label": "mobile", "primary": true}]
}
```

## Troubleshooting

| Problem | Solution |
|:--------|:---------|
| Connection not ACTIVE | Follow OAuth link via `RUBE_MANAGE_CONNECTIONS` |
| Invalid ID format | Ensure IDs are numeric integers (except Leads which are UUIDs) |
| Missing required fields | `subject` and `type` are mandatory for activities |
| done field ignored | Use integer `0` or `1`, not boolean `true/false` |
