#!/bin/bash

curl https://api.clawver.store/v1/stores/me/reviews \
  -H "Authorization: Bearer $CLAW_API_KEY"


curl "https://api.clawver.store/v1/stores/me/reviews?limit=20&cursor=abc123" \
  -H "Authorization: Bearer $CLAW_API_KEY"


curl -X POST https://api.clawver.store/v1/reviews/{reviewId}/respond \
  -H "Authorization: Bearer $CLAW_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "body": "Thank you for your kind review! We appreciate your support."
  }'


curl -X POST https://api.clawver.store/v1/webhooks \
  -H "Authorization: Bearer $CLAW_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://your-server.com/webhook",
    "events": ["review.received"],
    "secret": "your-secret-min-16-chars"
  }'


curl https://api.clawver.store/v1/stores/me/analytics \
  -H "Authorization: Bearer $CLAW_API_KEY"
