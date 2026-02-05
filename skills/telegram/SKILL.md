---
name: telegram
description: Send and manage Telegram messages, monitor channels, and handle bot interactions.
---

# Telegram Actions

Use `telegram` to interact with Telegram via a configured bot.

## Actions

### Send Message
```json
{
  "action": "sendMessage",
  "to": "user:123456789",
  "content": "Hello via Telegram!"
}
```

### List Updates
```json
{
  "action": "listUpdates",
  "limit": 10
}
```

### Get Me
```json
{
  "action": "getMe"
}
```

*Note: Requires valid Telegram Bot Token configured in environment.*
