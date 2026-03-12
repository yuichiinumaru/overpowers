---
name: api-fuzzing
type: skill
domain: Security
description: Performs automated fuzz testing against REST and GraphQL APIs to find edge cases and vulnerabilities.
requires:
  - security-researcher
---
# API Fuzzing Skill
Use this skill to send malformed data to API endpoints.
1. Run `ffuf` against the target.
2. Analyze the HTTP 500s.
