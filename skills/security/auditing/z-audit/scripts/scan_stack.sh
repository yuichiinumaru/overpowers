#!/bin/bash
# Z-Audit Stack Detection and Secret Scan Helper

echo "--- Phase 0: Stack Detection ---"
ls -la | grep -E "package.json|requirements.txt|go.mod|Cargo.toml|wrangler.toml|vercel.json|netlify.toml|supabase|firebase"

if [ -f package.json ]; then
    echo "Framework detection from package.json:"
    grep -E '"(react|vue|svelte|next|nuxt|hono|express|fastify|elysia)"' package.json
    echo "Auth detection from package.json:"
    grep -E '"(@supabase|firebase|@clerk|@auth0|better-auth|lucia|next-auth)"' package.json
fi

echo "--- Phase 1: Secrets Scan (Basic Patterns) ---"
grep -rnE '(sk-[a-zA-Z0-9]{20,}|sk_live_[a-zA-Z0-9]+|AKIA[A-Z0-9]{16}|ghp_[a-zA-Z0-9]{36}|AIza[a-zA-Z0-9_-]{35}|eyJ[a-zA-Z0-9_-]*\.eyJ[a-zA-Z0-9_-]*\.[a-zA-Z0-9_-]*)' . \
     --exclude-dir=node_modules --exclude-dir=.git --exclude-dir=.agents 2>/dev/null | head -n 20
