---
description: Workflow for setting up and deploying an official QQ Bot with AI integration.
---
# Workflow: QQ Bot Deployment and AI Integration

This workflow guides the process of establishing a functional AI-powered QQ Bot from scratch.

## Steps

### 1. Platform Setup
- Register as a developer on the QQ Bot platform.
- Create a new bot and secure the AppID and AppSecret.

### 2. Network Authorization
- Identify the public IP of the host machine.
- Configure the IP whitelist in the bot console.

### 3. Software Configuration
- Enable the QQ channel in `openclaw.json`.
- Deploy the Python bot scripts to the workspace.

### 4. Process Launch
- Use the daemon script to start the bot process.
- Verify the WebSocket connection via logs.

### 5. AI Loop Verification
- Send a test message to the bot.
- Confirm the AI request is generated and the response is delivered back to QQ.
