# Scan Report: gmickel-sheets-cli

## Repository Overview
- **Source**: gmickel
- **Purpose**: Google Sheets CLI tool with agent skill
- **Type**: CLI tool + skill

## Contents Inventory

### Skills (1)
| Skill | Description |
|-------|-------------|
| sheets_cli | Read, write, and update Google Sheets via CLI |

### Commands
- sheets find (search by name)
- sheets list (list tabs)
- read table (get data with row numbers)
- update key (update by column value)
- update row (update by row index)
- append (add rows)
- batch (multiple operations)

### Features
- Key-based updates (preferred over row indices)
- Dry-run support
- JSON output
- Header auto-detection
- Column name case-insensitive matching

## Key Files
- SKILL.md
- .claude/skills/sheets_cli.md

## Quality Assessment
- **Structure**: Complete CLI with skill
- **Coverage**: Full Google Sheets CRUD operations
- **Documentation**: Excellent with examples
