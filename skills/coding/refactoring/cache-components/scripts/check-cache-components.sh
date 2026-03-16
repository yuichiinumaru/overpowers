#!/bin/bash

# Check if cacheComponents is enabled in next.config.js or next.config.ts
if grep -r "cacheComponents" next.config.* 2>/dev/null; then
  echo "✅ Cache Components are enabled in this project."
else
  echo "❌ Cache Components are NOT enabled in this project."
  echo "To enable, add 'cacheComponents: true' to your next.config file."
fi
