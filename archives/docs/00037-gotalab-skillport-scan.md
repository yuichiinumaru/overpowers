# Scan Report: gotalab-skillport

## Repository Overview
- **Source**: gotalab
- **Purpose**: SkillOps Toolkit - validate, manage, and deliver skills at scale
- **Type**: Python CLI + MCP server

## Contents Inventory

### CLI Commands
| Command | Description |
|---------|-------------|
| skillport validate | Check skills against Agent Skills spec |
| skillport add | Add skills from GitHub, local, or zip |
| skillport update | Update all from original sources |
| skillport list | List installed skills |
| skillport remove | Uninstall skills |
| skillport meta get/set/unset | Manage skill metadata |
| skillport doc | Generate AGENTS.md with skill table |
| skillport show | Load full skill instructions |

### MCP Tools
| Tool | Description |
|------|-------------|
| search_skills | Find skills by description (full-text) |
| load_skill | Get full instructions + path |

### Experimental Skills
| Skill | Description |
|-------|-------------|
| git-branch-cleanup | Branch cleanup automation |
| opus-4-5-migration | Migration to Opus 4.5 |
| skill_evaluator | Evaluate skills against criteria |

### Features
- Tool Search Tool pattern (search first, load on demand)
- Category/tag organization
- Per-client filtering
- CLI and MCP modes

## Quality Assessment
- **Structure**: Excellent Python package
- **Coverage**: Complete skill management lifecycle
- **Documentation**: Very thorough
