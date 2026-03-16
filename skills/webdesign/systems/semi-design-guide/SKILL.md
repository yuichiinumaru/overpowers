---
name: semi-design-guide
description: A comprehensive guide to using Semi Design components, including MCP tool usage flow, common patterns, and best practices. Use this skill when you need to query Semi Design components, generate component code, or resolve usage issues.
tags:
- design
- ux
version: 1.0.0
category: general
---

# Semi Design Usage Guide

This Skill helps you efficiently use the Semi Design component library to complete common development tasks.

## File Descriptions

This Skill consists of the following files, each focusing on guidance for a specific aspect:

### WORKFLOWS.md

**Content**: Complete workflows for using the Semi MCP tool.

**Includes**:
- MCP Tool Overview: Introduces the functions and usage scenarios of the four tools: `get_semi_document`, `get_component_file_list`, `get_file_code`, `get_function_code`.
- Basic Query Flow: A four-step process of finding a component → querying details → viewing source code → viewing function implementation.
- Complete Task Examples: Detailed steps for common scenarios such as Table filtering, form validation, cascader, drag and drop sorting, etc.
- Common Query Techniques: Specifying version queries, obtaining complete code, error troubleshooting process, etc.

**When to Use**: When you need to query component documentation, understand component APIs, or implement a specific feature but are unsure how to start.

### BEST_PRACTICES.md

**Content**: Best practices and considerations for using Semi Design components.

**Includes**:
- Component Import Method: Recommends directly importing components, icons, and styles.
- Theme Customization Guide: Guides the AI to consult the official customization documentation.
- React 19 Compatibility: Explains how to get component usage instructions related to React 19.
- Component Extension Methods: How to extend Semi components through inheritance and modify the internal UI of components when props are insufficient.

**When to Use**: When you need to ensure code adheres to best practices or to resolve difficult issues in component usage.

## Quick Navigation

| Requirement | View |
|------|------|
| How to use MCP tools to query components | [WORKFLOWS.md](WORKFLOWS.md) |
| Best practices for component usage | [BEST_PRACTICES.md](BEST_PRACTICES.md) |

## Overview

Semi Design is an enterprise-level UI component library launched by ByteDance. This Skill, used in conjunction with the [Semi MCP](/start/ai-mcp) tool, provides:

- **Workflows**: Complete processes for querying components and generating code using MCP tools.
- **Practices**: Best practices to avoid common pitfalls.

## Prerequisites

Before using this Skill, ensure that Semi MCP is configured:

```json
{
  "mcpServers": {
    "semi-mcp": {
      "command": "npx",
      "args": ["-y", "@douyinfe/semi-mcp"]
    }
  }
}
```
