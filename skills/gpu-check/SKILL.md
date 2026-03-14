---
name: gpu-check
description: Real-time GPU memory monitoring for distributed AI compute nodes on LAN. Displays VRAM usage with progress bars and monitors API service availability.
tags: [gpu, monitoring, lan, vram, ai-infrastructure]
version: "1.0.0"
---

# GPU 状态检查 (gpu_check)

Real-time GPU memory monitoring for distributed AI compute nodes on LAN.

## Features
* Automatically polls GPU status from 3090 (192.168.2.236) and 4090 (192.168.2.164)
* Outputs Markdown table with progress bars
* Monitors API service availability for each node

## Dependencies
* Node.js environment (built-in)
* axios library (requires installation)

## Installation
1. Install dependencies in skill directory:
   ```bash
   cd ~/.openclaw/workspace/skills/gpu-check
   npm init -y
   npm install axios
   ```
2. Ensure GPU node APIs are running (services supporting `/gpu` endpoint must be running on 192.168.2.236 and 192.168.2.164)

## Usage
Send in chat:
- `/gpu`
- `@bot GPU status`
- `Check GPU usage`
