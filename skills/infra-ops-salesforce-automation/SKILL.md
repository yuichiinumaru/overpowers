---
name: salesforce-automation
description: 'Automate Salesforce tasks via Rube MCP (Composio): leads, contacts,
  accounts, opportunities, SOQL queries. Always search tools first for current schemas.'
tags:
- infra
- ops
version: 1.0.0
category: general
---
# Salesforce Automation

Automate Salesforce CRM operations through Composio's Salesforce toolkit via Rube MCP.

## When to Use

- User wants to create, search, update, or list leads.
- User needs to manage contacts and their associated accounts.
- User wants to track and manage sales opportunities.
- User wants to query Salesforce data with custom SOQL.
- User needs to create, search, update, or complete tasks.

## Prerequisites

- Rube MCP must be connected (RUBE_SEARCH_TOOLS available)
- Active Salesforce connection via `RUBE_MANAGE_CONNECTIONS` with toolkit `salesforce`
- Active Salesforce account with necessary permissions.

## Instructions

### Step 1: Setup
1. Verify Rube MCP is available by confirming `RUBE_SEARCH_TOOLS` responds.
2. Call `RUBE_MANAGE_CONNECTIONS` with toolkit `salesforce`.
3. If connection is not ACTIVE, follow the returned auth link to complete Salesforce OAuth.
4. Confirm connection status shows ACTIVE before running any workflows.

### Step 2: Execution
Depending on the task, use the appropriate tool sequence:

#### Manage Leads
1. `SALESFORCE_SEARCH_LEADS` - Search leads by criteria.
2. `SALESFORCE_CREATE_LEAD` - Create a new lead (LastName and Company are required).
3. `SALESFORCE_UPDATE_LEAD` - Update lead fields using `lead_id`.

#### Manage Contacts and Accounts
1. `SALESFORCE_CREATE_CONTACT` - Create a new contact.
2. `SALESFORCE_CREATE_ACCOUNT` - Create a new account.
3. `SALESFORCE_ASSOCIATE_CONTACT_TO_ACCOUNT` - Link contact to account.

#### Manage Opportunities
1. `SALESFORCE_CREATE_OPPORTUNITY` - Create new opportunity (Name, StageName, and CloseDate are required).
2. `SALESFORCE_GET_OPPORTUNITY` - Get opportunity details.

#### Run SOQL Queries
1. `SALESFORCE_RUN_SOQL_QUERY` or `SALESFORCE_QUERY` - Execute SOQL.
   - Example: `SELECT Id, Name, Email FROM Contact WHERE LastName = 'Smith'`

### Step 3: Verification
- Check the output of the tool call for success status.
- For queries, verify the returned data matches expectations.
- For record creation/updates, verify the record exists or has been modified in Salesforce.

## Examples

```sql
/* Basic SOQL Query */
SELECT Id, Name, Account.Name FROM Contact WHERE Account.Industry = 'Technology'
```

## Troubleshooting

| Problem | Solution |
|:--------|:---------|
| Connection not ACTIVE | Follow OAuth link via `RUBE_MANAGE_CONNECTIONS` |
| Missing required fields | Ensure LastName and Company are provided for leads |
| Invalid SOQL syntax | Use API names, not display labels (e.g., `Account.Name`) |
| Field not found | Custom fields end with `__c` suffix |
