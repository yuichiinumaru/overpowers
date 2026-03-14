"""Trading client for the simulation platform API with HMAC authentication."""

import hashlib
import hmac
import json
import os
import secrets
import time
import urllib.request
import urllib.parse


BASE_URL = os.environ.get("TRADE_API_URL", "http://54.255.3.5:8088")
API_PREFIX = "/api/v1/moss/agent"


class TradingClient:
    def __init__(self, api_key: str = "", api_secret: str = "", agent_id: str = ""):
        self.api_key = api_key
        self.api_secret = api_secret
        self.agent_id = agent_id
        self.base_url = BASE_URL

    def _sign(self, method: str, path: str, query: str, body: str) -> tuple[str, str, str]:
        ts = str(int(time.time()))
        nonce = secrets.token_hex(12)
        payload = f"{method}\n{path}\n{query}\n{body}\n{ts}\n{nonce}"
        signature = hmac.new(
            self.api_secret.encode(), payload.encode(), hashlib.sha256
        ).hexdigest()
        return ts, nonce, signature

    def _request(self, method: str, path: str, body: dict = None,
                 query: dict = None, need_auth: bool = True,
                 custom_prefix: str = None) -> dict:
        prefix = custom_prefix if custom_prefix is not None else API_PREFIX
        full_path = f"{prefix}{path}"
        url = f"{self.base_url}{full_path}"

        canonical_query = ""
        if query:
            sorted_params = sorted(query.items())
            canonical_query = urllib.parse.urlencode(sorted_params)
            url = f"{url}?{canonical_query}"

        raw_body = ""
        if body is not None:
            raw_body = json.dumps(body, separators=(",", ":"))

        headers = {"Content-Type": "application/json"}

        if need_auth and self.api_key:
            ts, nonce, sig = self._sign(method, full_path, canonical_query, raw_body)
            headers["X-API-KEY"] = self.api_key
            headers["X-TS"] = ts
            headers["X-NONCE"] = nonce
            headers["X-SIGNATURE"] = sig

        req = urllib.request.Request(
            url,
            data=raw_body.encode() if raw_body else None,
            headers=headers,
            method=method,
        )

        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                resp_body = resp.read()
                if not resp_body:
                    return {"status": "ok"}
                return json.loads(resp_body)
        except urllib.error.HTTPError as e:
            error_body = e.read().decode()
            try:
                return json.loads(error_body)
            except json.JSONDecodeError:
                return {"code": "HTTP_ERROR", "message": f"{e.code}: {error_body}"}

    # ── Binding ──

    def create_pair_code(self, user_uuid: str) -> dict:
        return self._request("POST", "/pair-codes", query={"user_uuid": user_uuid}, need_auth=False)

    def bind(self, pair_code: str, display_name: str = "Bot",
             persona: str = "", description: str = "",
             fingerprint: str = "") -> dict:
        if not fingerprint:
            fingerprint = f"sha256:{secrets.token_hex(16)}"
        body = {
            "pair_code": pair_code,
            "display_name": display_name,
            "persona": persona or display_name,
            "description": description or f"{display_name} trading bot",
            "agent_fingerprint": fingerprint,
        }
        return self._request("POST", "/agents/bind", body, need_auth=False)

    def unbind(self, agent_id: str, user_uuid: str) -> dict:
        return self._request("POST", f"/agents/{agent_id}/unbind",
                             query={"user_uuid": user_uuid}, need_auth=False)

    # ── Profile (HMAC) ──

    def update_profile(self, display_name: str = "", persona: str = "", description: str = "") -> dict:
        body = {}
        if display_name:
            body["display_name"] = display_name
        if persona:
            body["persona"] = persona
        if description:
            body["description"] = description
        return self._request("PATCH", "/profile", body)

    # ── Trading (HMAC) ──

    def get_price(self) -> dict:
        return self._request("GET", "/market/price")

    def get_account(self) -> dict:
        return self._request("GET", "/account")

    def get_positions(self) -> list:
        return self._request("GET", "/positions")

    def get_orders(self, limit: int = 100) -> list:
        return self._request("GET", "/orders", query={"limit": str(limit)})

    def get_trades(self, limit: int = 100) -> list:
        return self._request("GET", "/trades", query={"limit": str(limit)})

    def open_long(self, notional_usdt: str, leverage: int, client_order_id: str = "") -> dict:
        body = {
            "symbol": "BTCUSDT",
            "side": "BUY",
            "position_side": "LONG",
            "notional_usdt": notional_usdt,
            "leverage": leverage,
        }
        if self.agent_id:
            body["agent_id"] = self.agent_id
        if client_order_id:
            body["client_order_id"] = client_order_id
        return self._request("POST", "/orders/market", body)

    def open_short(self, notional_usdt: str, leverage: int, client_order_id: str = "") -> dict:
        body = {
            "symbol": "BTCUSDT",
            "side": "SELL",
            "position_side": "SHORT",
            "notional_usdt": notional_usdt,
            "leverage": leverage,
        }
        if self.agent_id:
            body["agent_id"] = self.agent_id
        if client_order_id:
            body["client_order_id"] = client_order_id
        return self._request("POST", "/orders/market", body)

    def close_position(self, position_side: str, close_qty_btc: str = "") -> dict:
        body = {
            "symbol": "BTCUSDT",
            "position_side": position_side,
        }
        if self.agent_id:
            body["agent_id"] = self.agent_id
        if close_qty_btc:
            body["close_qty_btc"] = close_qty_btc
        return self._request("POST", "/positions/close", body)

    # ── Public display (no auth) ──

    def get_discover_leaderboard(self, mode: str = "realtime") -> dict:
        return self._request("GET", "/trader/discover/leaderboard",
                             query={"mode": mode}, need_auth=False)

    def get_bots_public(self, mode: str = "hell", sort_by: str = "pnl",
                        sort_order: str = "desc", page: int = 1, page_size: int = 20) -> dict:
        return self._request("GET", "/trader/bots", query={
            "mode": mode, "sort_by": sort_by, "sort_order": sort_order,
            "page": str(page), "page_size": str(page_size),
        }, need_auth=False)

    def get_bot_detail_public(self, bot_id: str) -> dict:
        return self._request("GET", f"/trader/bots/{bot_id}", need_auth=False)

    # ── User-scoped display (no auth, needs user_uuid) ──

    def get_overview(self, user_uuid: str) -> dict:
        return self._request("GET", "/trader/overview",
                             query={"user_uuid": user_uuid}, need_auth=False)

    # ── Backtest (all under /api/v1/moss/agent/backtest/) ──

    def verify_backtest(self, user_uuid: str, package: dict) -> dict:
        """Submit verify job (async). Returns job_id, poll with get_verify_job()."""
        return self._request("POST", "/backtest/verify", body=package,
                             query={"user_uuid": user_uuid}, need_auth=False)

    def get_verify_job(self, user_uuid: str, job_id: str) -> dict:
        """Poll verify job status. Terminal states: verified/rejected/failed."""
        return self._request("GET", f"/backtest/jobs/{job_id}",
                             query={"user_uuid": user_uuid}, need_auth=False)

    def verify_backtest_and_wait(self, user_uuid: str, package: dict,
                                  poll_interval: int = 3, max_wait: int = 120) -> dict:
        """Submit + poll until terminal state."""
        import time as _time
        job = self.verify_backtest(user_uuid, package)
        job_id = job.get("job_id", "")
        if not job_id:
            return job

        elapsed = 0
        while elapsed < max_wait:
            _time.sleep(poll_interval)
            elapsed += poll_interval
            status = self.get_verify_job(user_uuid, job_id)
            st = status.get("status", "")
            if st in ("verified", "rejected", "failed"):
                return status.get("result", status)
        return {"code": "TIMEOUT", "message": f"Job {job_id} not done after {max_wait}s"}

    def get_backtest_bots(self, user_uuid: str, page: int = 1, page_size: int = 20) -> dict:
        return self._request("GET", "/backtest/bots", query={
            "user_uuid": user_uuid, "page": str(page), "page_size": str(page_size),
        }, need_auth=False)

    def get_backtest_bot_detail(self, user_uuid: str, bot_id: str) -> dict:
        return self._request("GET", f"/backtest/bots/{bot_id}",
                             query={"user_uuid": user_uuid}, need_auth=False)

    def delete_backtest_bot(self, user_uuid: str, bot_id: str) -> dict:
        return self._request("DELETE", f"/backtest/bots/{bot_id}",
                             query={"user_uuid": user_uuid}, need_auth=False)

    def get_backtest_leaderboard(self, sort_by: str = "return", page: int = 1, page_size: int = 20) -> dict:
        return self._request("GET", "/backtest/leaderboard", query={
            "sort_by": sort_by, "page": str(page), "page_size": str(page_size),
        }, need_auth=False)
