# Browser Use Integration

This document details the integration of the `browser-use` library into the overpowers repository.

## Overview
`browser-use` allows AI agents to control a web browser, navigate websites, and interact with page elements. We have integrated it as a **Skill** and an **Agent**.

## Components

### 1. Browser Automator Agent (`agents/browser-automator.md`)
This agent is specialized in using the browser to complete tasks. It has a specific system prompt that guides it on how to interact with the DOM, handle page state changes, and use the filesystem.

**Key Features:**
- Navigation & Interaction
- Form Filling
- Data Extraction
- Session Management

### 2. Browser Use Skill (`skills/browser-use/`)
This skill provides the CLI interface for the `browser-use` library. It exposes commands to open URLs, inspect state, click elements, type text, and take screenshots.

**Commands:**
- `browser-use open <url>`
- `browser-use state`
- `browser-use click <index>`
- `browser-use input <index> <text>`
- `browser-use screenshot`

## Setup
To use the browser automation features, you must first install the dependencies:

```bash
./scripts/setup-browser-use.sh
```

This script will install `browser-use` and the necessary Playwright browsers (Chromium).

## Usage
You can use the `Browser Automator Agent` for complex tasks or the `browser-use` skill directly for simpler, step-by-step control.

**Example with Agent:**
"Use the Browser Automator to find the cheapest flight from NY to London on Expedia."

**Example with Skill:**
```bash
browser-use open https://google.com
browser-use input 0 "Browser Use"
browser-use keys "Enter"
```
