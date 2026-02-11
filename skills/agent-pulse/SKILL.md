---
name: agent-pulse
description: >
  Send and verify on-chain liveness pulses for autonomous agents on Base via the
  Agent Pulse protocol. Use when you need to: (1) prove an agent is alive by sending
  a pulse, (2) check any agent's liveness status or streak, (3) monitor multiple
  agents, (4) view the global pulse feed, (5) auto-configure wallet and PULSE balance,
  (6) run scheduled heartbeat pulses, or (7) read protocol health and config.
  Supports both API and direct on-chain (cast) modes.
---

# Agent Pulse 💓

Liveness signaling for autonomous agents on Base. An agent periodically sends a **pulse** (PULSE token transfer) to prove it's alive. Observers query status via API or on-chain.

**Network:** Base (chainId 8453)

| Contract        | Address                                      |
|-----------------|----------------------------------------------|
| PulseToken      | `0x21111B39A502335aC7e45c4574Dd083A69258b07`  |
| PulseRegistry   | `0xe61C615743A02983A46aFF66Db035297e8a43846`  |
| API             | `https://agent-pulse-nine.vercel.app`         |

> **$PULSE is a utility token for pulse signals.** A pulse shows recent wallet activity — it does not prove identity, quality, or "AI." Avoid language suggesting financial upside.

## Decision Tree

1. **First time?** → Run `scripts/setup.sh` to auto-detect wallet, check balance, verify approval.
2. **Send a pulse?** → `scripts/pulse.sh --direct 1000000000000000000` (requires `PRIVATE_KEY`).
3. **Automated heartbeat?** → `scripts/auto-pulse.sh` (cron-safe; skips if TTL is healthy).
4. **Check one agent?** → `scripts/status.sh <address>` or `curl .../api/v2/agent/<addr>/alive`.
5. **Check many agents?** → `scripts/monitor.sh <addr1> <addr2> ...`
6. **View pulse feed?** → `scripts/monitor.sh --feed`
7. **Protocol config/health?** → `scripts/config.sh` / `scripts/health.sh`

## Scripts Reference

All scripts live in `scripts/`. Pass `-h` or `--help` for usage.

### setup.sh — Self-Configure

Auto-detects wallet from `PRIVATE_KEY`, checks PULSE balance, verifies registry approval, and queries agent status.

```bash
# Interactive setup
{baseDir}/scripts/setup.sh

# Auto-approve registry + JSON output
{baseDir}/scripts/setup.sh --auto-approve --quiet
```

**Env:** `PRIVATE_KEY` (required), `BASE_RPC_URL`, `API_BASE`
**Requires:** `cast`, `curl`, `jq`

### pulse.sh — Send Pulse

Send an on-chain pulse via direct `cast send`.

```bash
export PRIVATE_KEY="0x..."
{baseDir}/scripts/pulse.sh --direct 1000000000000000000
```

**Env:** `PRIVATE_KEY` (required), `BASE_RPC_URL`
**Requires:** `cast`

### auto-pulse.sh — Cron Heartbeat

Check if agent is alive; send pulse only when TTL is low or agent is dead. Safe to run on a schedule.

```bash
# Normal: pulse only if needed
{baseDir}/scripts/auto-pulse.sh

# Force pulse regardless of TTL
{baseDir}/scripts/auto-pulse.sh --force

# Check without sending
{baseDir}/scripts/auto-pulse.sh --dry-run
```

**Env:** `PRIVATE_KEY` (required), `BASE_RPC_URL`, `PULSE_AMOUNT` (default 1e18), `TTL_THRESHOLD` (default 21600s = 6h)
**Exit codes:** 0 = success or skipped, 1 = error

### status.sh — Agent Status

```bash
{baseDir}/scripts/status.sh 0xAgentAddress
```

### config.sh / health.sh — Protocol Info

```bash
{baseDir}/scripts/config.sh     # addresses, network, x402 config
{baseDir}/scripts/health.sh     # paused status, total agents, health
```

### monitor.sh — Multi-Agent Monitor

```bash
# Check specific agents
{baseDir}/scripts/monitor.sh 0xAddr1 0xAddr2 0xAddr3

# From file (one address per line)
{baseDir}/scripts/monitor.sh -f agents.txt

# JSON output
{baseDir}/scripts/monitor.sh --json 0xAddr1 0xAddr2

# Global pulse feed
{baseDir}/scripts/monitor.sh --feed
```

## API Quick Reference

| Endpoint                           | Method | Auth  | Description              |
|------------------------------------|--------|-------|--------------------------|
| `/api/v2/agent/{addr}/alive`       | GET    | None  | Alive check + TTL        |
| `/api/status/{addr}`               | GET    | None  | Full status + streak     |
| `/api/pulse-feed`                  | GET    | None  | Recent pulse activity    |
| `/api/config`                      | GET    | None  | Protocol configuration   |
| `/api/protocol-health`             | GET    | None  | Health and paused state  |
| `/api/pulse`                       | POST   | x402  | Send pulse via API       |

## Direct On-Chain (cast)

```bash
export BASE_RPC_URL="https://mainnet.base.org"

# Read: is agent alive?
cast call --rpc-url "$BASE_RPC_URL" \
  0xe61C615743A02983A46aFF66Db035297e8a43846 \
  "isAlive(address)(bool)" 0xAgent

# Read: full status tuple
cast call --rpc-url "$BASE_RPC_URL" \
  0xe61C615743A02983A46aFF66Db035297e8a43846 \
  "getAgentStatus(address)(bool,uint256,uint256,uint256)" 0xAgent

# Write: approve + pulse (requires PRIVATE_KEY)
cast send --rpc-url "$BASE_RPC_URL" --private-key "$PRIVATE_KEY" \
  0x21111B39A502335aC7e45c4574Dd083A69258b07 \
  "approve(address,uint256)(bool)" \
  0xe61C615743A02983A46aFF66Db035297e8a43846 1000000000000000000

cast send --rpc-url "$BASE_RPC_URL" --private-key "$PRIVATE_KEY" \
  0xe61C615743A02983A46aFF66Db035297e8a43846 \
  "pulse(uint256)" 1000000000000000000
```

## Error Handling

| Error                   | Cause                                    | Fix                          |
|-------------------------|------------------------------------------|------------------------------|
| `BelowMinimumPulse`    | Amount < `minPulseAmount` (default 1e18) | Use ≥ 1000000000000000000    |
| ERC20 transfer failure  | Missing approval or low PULSE balance    | Run `setup.sh --auto-approve`|
| `whenNotPaused`        | Registry paused                          | Wait; check `health.sh`     |
| 401/402/403             | Missing payment for paid endpoints       | Use direct on-chain mode     |
| 5xx                     | Transient API error                      | Retry with backoff           |

## Security

- **Never** log, print, or commit `PRIVATE_KEY`.
- Verify contract addresses and chainId before signing transactions.
- Test with small amounts first.

## References

- Action guide: `references/action_guide.md` — detailed API patterns and examples
- Contract ABI: `references/contract_abi.json` — PulseRegistry full ABI
