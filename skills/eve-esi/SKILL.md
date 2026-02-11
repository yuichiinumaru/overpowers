---
name: eve-esi
description: "Query and manage EVE Online characters via the ESI (EVE Swagger Interface) REST API. Use when the user asks about EVE Online character data, wallet balance, ISK transactions, assets, skill queue, skill points, clone locations, implants, fittings, contracts, market orders, mail, industry jobs, killmails, planetary interaction, loyalty points, or any other EVE account management task."
---

# EVE Online ESI

The ESI (EVE Swagger Interface) is the official REST API for EVE Online third-party development.

- Base URL: `https://esi.evetech.net/latest`
- Spec: `https://esi.evetech.net/latest/swagger.json`
- API Explorer: <https://developers.eveonline.com/api-explorer>

## Authentication

ESI uses OAuth 2.0 via EVE SSO. Most character endpoints require an access token with the correct scope.

Quick flow:
1. Register an app at <https://developers.eveonline.com/applications>
2. Redirect user to SSO authorize URL with required scopes
3. Exchange the auth code for access + refresh tokens
4. Pass `Authorization: Bearer <TOKEN>` on every ESI request

For full details (PKCE, token refresh, scope list): see [references/authentication.md](references/authentication.md).

## Public endpoints (no auth)

```bash
# Character public info
curl -s "https://esi.evetech.net/latest/characters/2114794365/" | python -m json.tool

# Portrait URLs
curl -s "https://esi.evetech.net/latest/characters/2114794365/portrait/"

# Corporation history
curl -s "https://esi.evetech.net/latest/characters/2114794365/corporationhistory/"

# Bulk affiliation lookup
curl -s -X POST "https://esi.evetech.net/latest/characters/affiliation/" \
  -H "Content-Type: application/json" \
  -d '[2114794365, 95538921]'
```

## Character info (authenticated)

```bash
TOKEN="<your_access_token>"
CHAR_ID="<your_character_id>"

# Online status (scope: esi-location.read_online.v1)
curl -s -H "Authorization: Bearer $TOKEN" \
  "https://esi.evetech.net/latest/characters/$CHAR_ID/online/"
```

## Wallet

```bash
# Balance (scope: esi-wallet.read_character_wallet.v1)
curl -s -H "Authorization: Bearer $TOKEN" \
  "https://esi.evetech.net/latest/characters/$CHAR_ID/wallet/"

# Journal (paginated)
curl -s -H "Authorization: Bearer $TOKEN" \
  "https://esi.evetech.net/latest/characters/$CHAR_ID/wallet/journal/?page=1"

# Transactions
curl -s -H "Authorization: Bearer $TOKEN" \
  "https://esi.evetech.net/latest/characters/$CHAR_ID/wallet/transactions/"
```

## Assets

```bash
# All assets (paginated; scope: esi-assets.read_assets.v1)
curl -s -H "Authorization: Bearer $TOKEN" \
  "https://esi.evetech.net/latest/characters/$CHAR_ID/assets/?page=1"

# Resolve item locations
curl -s -X POST -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '[1234567890, 9876543210]' \
  "https://esi.evetech.net/latest/characters/$CHAR_ID/assets/locations/"

# Resolve item names
curl -s -X POST -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '[1234567890]' \
  "https://esi.evetech.net/latest/characters/$CHAR_ID/assets/names/"
```

## Skills

```bash
# All trained skills + total SP (scope: esi-skills.read_skills.v1)
curl -s -H "Authorization: Bearer $TOKEN" \
  "https://esi.evetech.net/latest/characters/$CHAR_ID/skills/"

# Skill queue (scope: esi-skills.read_skillqueue.v1)
curl -s -H "Authorization: Bearer $TOKEN" \
  "https://esi.evetech.net/latest/characters/$CHAR_ID/skillqueue/"

# Attributes (intelligence, memory, etc.)
curl -s -H "Authorization: Bearer $TOKEN" \
  "https://esi.evetech.net/latest/characters/$CHAR_ID/attributes/"
```

## Location and ship

```bash
# Current location (scope: esi-location.read_location.v1)
curl -s -H "Authorization: Bearer $TOKEN" \
  "https://esi.evetech.net/latest/characters/$CHAR_ID/location/"

# Current ship (scope: esi-location.read_ship_type.v1)
curl -s -H "Authorization: Bearer $TOKEN" \
  "https://esi.evetech.net/latest/characters/$CHAR_ID/ship/"
```

## Clones and implants

```bash
# Jump clones + home station (scope: esi-clones.read_clones.v1)
curl -s -H "Authorization: Bearer $TOKEN" \
  "https://esi.evetech.net/latest/characters/$CHAR_ID/clones/"

# Active implants (scope: esi-clones.read_implants.v1)
curl -s -H "Authorization: Bearer $TOKEN" \
  "https://esi.evetech.net/latest/characters/$CHAR_ID/implants/"
```

## More endpoints

For contracts, fittings, mail, industry, killmails, market orders, mining, planetary interaction, loyalty points, notifications, blueprints, standings, and all other character endpoints, see [references/endpoints.md](references/endpoints.md).

## Dashboard Config

The skill supports a modular dashboard config for alerts, reports, and market tracking. Each user defines what they need in a JSON config file.

- **Schema**: [config/schema.json](config/schema.json) — full JSON Schema with all fields, types, and defaults
- **Example**: [config/example-config.json](config/example-config.json) — ready-to-use template

### Features

| Module | Description |
|--------|-------------|
| **Alerts** | Real-time polling for war decs, structure attacks, skill completions, wallet changes, industry jobs, PI extractors, killmails, contracts, clone jumps, mail |
| **Reports** | Cron-scheduled summaries: net worth, skill queue, industry, market orders, wallet, assets |
| **Market** | Price tracking with absolute thresholds and trend detection |

### Security

Tokens should **not** be stored in plain text. Use environment variable references:

```json
{
  "token": "$ENV:EVE_TOKEN_MAIN",
  "refresh_token": "$ENV:EVE_REFRESH_MAIN"
}
```

The config file should live outside the workspace (e.g. `~/.openclaw/eve-dashboard-config.json`).

### Validate a config

```bash
python scripts/validate_config.py path/to/config.json

# Show example config
python scripts/validate_config.py --example

# Show JSON schema
python scripts/validate_config.py --schema
```

## Using the query script

A reusable Python script is bundled at `scripts/esi_query.py`. It handles pagination, error limits, and caching headers.

```bash
# Simple query
python scripts/esi_query.py --token "$TOKEN" --endpoint "/characters/$CHAR_ID/wallet/" --pretty

# Fetch all pages of assets
python scripts/esi_query.py --token "$TOKEN" --endpoint "/characters/$CHAR_ID/assets/" --pages --pretty

# POST request (e.g. asset names)
python scripts/esi_query.py --token "$TOKEN" --endpoint "/characters/$CHAR_ID/assets/names/" \
  --method POST --body '[1234567890]' --pretty
```

## Best practices

- **Caching**: respect the `Expires` header; do not poll before it expires.
- **Error limits**: monitor `X-ESI-Error-Limit-Remain`; back off when low.
- **User-Agent**: always set a descriptive User-Agent with contact info.
- **Rate limits**: some endpoints (mail, contracts) have internal rate limits returning HTTP 520.
- **Pagination**: check the `X-Pages` response header; iterate with `?page=N`.
- **Versioning**: use `/latest/` for current stable routes. `/dev/` may change without notice.

## Resolving type IDs

ESI returns numeric type IDs (e.g. for ships, items, skills). Resolve names via:

```bash
# Single type
curl -s "https://esi.evetech.net/latest/universe/types/587/"

# Bulk names (up to 1000 IDs)
curl -s -X POST "https://esi.evetech.net/latest/universe/names/" \
  -H "Content-Type: application/json" \
  -d '[587, 638, 11393]'
```
