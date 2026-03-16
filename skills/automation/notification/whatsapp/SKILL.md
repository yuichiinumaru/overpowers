---
name: whatsapp
description: Send WhatsApp messages via connected provider.
tags:
- data
- sci
version: 1.0.0
category: general
---
# WhatsApp Actions

Use `whatsapp` to send messages.

## Actions

### Send Message
```json
{
  "action": "sendMessage",
  "to": "+1234567890",
  "content": "Hello via WhatsApp!"
}
```

*Note: Requires valid WhatsApp provider configuration.*
