---
name: agent-im-manager-v100
description: "Multi-Agent conversation management platform with Gemini-style UI. Manage all your OpenClaw agents in one place with image upload, chat history, and message isolation."
metadata:
  openclaw:
    category: "agent"
    tags: ['agent', 'automation', 'monitoring']
    version: "1.0.0"
---

# Agent Manager - Multi-Agent Conversation Management Platform

A unified platform for managing conversations with multiple OpenClaw Agents, supporting text + image input and automatic conversation history saving.

## 🎯 Feature Highlights

- **Multi-Agent Management** - Unified management of all Agents
- **Gemini Style Interface** - Modern left-right split design
- **Image Input** - Supports drag-and-drop upload and button selection
- **Conversation History** - Auto-saved, no loss when switching Agents
- **Message Isolation** - Independent conversation history for each Agent
- **Local Storage** - Data saved in the browser

## 🔒 Security Notice

**Resources accessed by this skill:**
- `~/.openclaw/agents` - Agent configuration directory
- `~/.openclaw/workspace-*` - Agent workspace directory
- `~/.openclaw/devices/paired.json` - Reads Operator Token

**Security Commitment:**
- ✅ No hardcoded credentials (Token configured by the user)
- ✅ No external API calls (All data processed locally)
- ✅ No data exfiltration (Conversation history stored in browser localStorage)
- ✅ Fully open-source code for review

**Please review the code before use to ensure trust in the author.**

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd agent-manager
npm install
```

### 2. Configure Token

```bash
# Copy example configuration
cp config.example.json config.json

# Get your Operator Token
cat ~/.openclaw/devices/paired.json | jq '.[].tokens.operator.token'

# Edit config.json and fill in the Token
nano config.json
```

### 3. Start the Service

```bash
node server-gemini.js
```

### 4. Access the Interface

Open your browser and visit:
```
http://localhost:3000
```

## 📋 Usage Instructions

### Chatting with an Agent

1. Select an Agent on the left (e.g., Judy/MNK/Fly)
2. Type your message in the input box on the right
3. Press Enter or click send
4. Wait for the Agent's reply

### Uploading Images

1. Click the 📎 button to select an image
2. Or drag and drop an image directly into the input box
3. You can add a text description
4. Click send

### Viewing History

1. Switch to another Agent
2. Switch back
3. The complete conversation record will load automatically

## 📁 File Structure

```
agent-manager/
├── server-gemini.js      # Main server
├── index.html            # Frontend interface
├── package.json          # Dependency configuration
├── config.json           # Configuration file (requires Token)
├── config.example.json   # Configuration example
├── cli.js                # Command-line tool
├── README.md             # Detailed documentation
└── SKILL.md              # This file
```

## ⚙️ Configuration Instructions

### config.json

```json
{
  "openclawGateway": "http://127.0.0.1:18789",
  "openclawToken": "Your Operator Token"
}
```

| Field | Description | Default Value |
|------|------|--------|
| openclawGateway | OpenClaw Gateway address | http://127.0.0.1:18789 |
| openclawToken | Operator Token (Required) | Must be obtained by the user |

### Getting the Operator Token

```bash
# Method 1: Using jq
cat ~/.openclaw/devices/paired.json | jq '.[].tokens.operator.token'

# Method 2: Manual inspection
cat ~/.openclaw/devices/paired.json
```

## 🎨 Interface Features

- **Gemini Style** - Inspired by Google Gemini design
- **Left-Right Split** - Agent list on the left, conversation area on the right
- **Responsive Design** - Adapts to window size
- **Modern Color Scheme** - Purple gradient theme
- **Smooth Animations** - Message fade-in effect

## 📊 Supported Agents

| Agent | Responsibility | Model |
|-------|------|------|
| Judy | Marketing Outreach | qwen3.5-plus |
| MNK | Technical Architecture | glm-5 |
| Fly | Schedule Management | qwen3.5-plus |
| Dav | Data Analysis | qwen3.5-plus |
| Zhou | User Operations | qwen3.5-plus |
| PNews | News Broadcasting | qwen3.5-plus |

## ⚠️ Important Notes

1. **Gateway Must Be Running** - Ensure `openclaw gateway status` shows running
2. **Browser Isolation** - History is not shared between different browsers
3. **Incognito Mode** - History will be lost upon closing the browser in incognito mode
4. **Image Size** - Recommended within 5MB
5. **Token Security** - Do not share your config.json file

## 🆘 Troubleshooting

**Interface not loading?**
```bash
# Check if the service is running
ps aux | grep "node server"

# Check port usage
lsof -i :3000

# Restart the service
node server-gemini.js
```

**Agent not loading?**
```bash
# Check OpenClaw Gateway
openclaw gateway status

# Refresh the browser Ctrl+Shift+R

# Check if the Token is correct
cat config.json
```

**Cannot chat with Agent?**
```bash
# Check Gateway logs
tail -f ~/.openclaw/logs/gateway.log

# Check if Agent is paired
openclaw devices list
```

## 💰 Pricing Information

**Price:** $10 USD (One-time purchase)

**Payment:** PayPal (396554498@qq.com)

**Includes:**
- ✅ Full source code
- ✅ Permanent usage license
- ✅ Basic technical support
- ✅ Future minor version updates

**Purchase Process:**
1. Purchase through ClawHub
2. Automatically receive a download link
3. Install and use according to this guide

## 📄 License

**Usage Rights:**
- ✅ Personal use
- ✅ Commercial use
- ❌ Resale of the skill itself
- ❌ Public distribution of source code

**Disclaimer:**
This skill is provided "as is" without any warranties, express or implied. Use of this skill is at your own risk.

---

**For detailed documentation, please refer to README.md and CLAWHUB.md**

**Enjoy efficient conversations with your Agents!** 🚀
