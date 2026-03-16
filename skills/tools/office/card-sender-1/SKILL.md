---
name: communication-lark-card-sender
description: Professional Feishu/Lark interactive card message sender. Supports multiple templates (news, flight, tasks), automatic token management, and schema validation.
tags: communication, lark, feishu, card, bot
version: 1.0.0
---

# Lark Card Sender Skill

Feishu/Lark interactive card message sending solution.

## Functions

- **Full API Support**: Direct call to Lark OpenAPI, supports all card types.
- **Schema 2.0**: Strictly follows Lark interactive card specification.
- **Multiple Templates**: News briefs, flight deals, task management, and basic info.
- **Smart Error Handling**: Exception capture and error code processing.
- **Size Validation**: Detects 30KB limit automatically.
- **Token Management**: Auto-refresh and cache `tenant_access_token`.

## Usage

### Configuration
```bash
export FEISHU_APP_ID="your_app_id"
export FEISHU_APP_SECRET="your_app_secret"
```

### Basic Sending
```python
from feishu_card_sender_advanced import AdvancedFeishuCardSender

sender = AdvancedFeishuCardSender(app_id, app_secret)
result = sender.send_simple_card(
    receive_id="ou_xxx",
    receive_id_type="open_id", 
    title="🎯 Test Card",
    content="**Content** here"
)
```
