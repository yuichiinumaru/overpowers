#!/usr/bin/env python3
"""
model_selector.py - Stateful health monitor for model providers.
Reads and updates model status to track rate limits and cooldowns.
Supports returning fallback chains: Opus -> Sonnet -> Flash -> GLM.

Status file precedence:
1) OVERPOWERS_MODEL_STATUS_FILE (if set)
2) ~/.config/opencode/model_status.json
3) <project>/.agents/model_status.json
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

DEFAULT_STATUS_FILE = Path("~/.config/opencode/model_status.json").expanduser()


# Define our models and fallback chains based on complexity
MODELS = {
    "opus": "google/antigravity-claude-opus-4-5-thinking",
    "sonnet": "google/antigravity-claude-sonnet-4-5-thinking",
    "flash": "google/gemini-3-flash",
    "glm": "windsurf/glm-4.7",
}

CHAINS = {
    "high": ["opus", "sonnet", "flash", "glm"],
    "medium": ["sonnet", "flash", "glm", "opus"],
    "low": ["flash", "glm", "sonnet", "opus"],
}

DEFAULT_COOLDOWN_SECONDS = 300  # 5 minutes


def get_project_root() -> Path:
    return Path(os.getenv("OVERPOWERS_PATH", os.getcwd())).resolve()


def get_status_candidates() -> list[Path]:
    configured = os.getenv("OVERPOWERS_MODEL_STATUS_FILE")
    if configured:
        return [Path(configured).expanduser()]
    return [
        DEFAULT_STATUS_FILE,
        get_project_root() / ".agents" / "model_status.json",
    ]


def load_status() -> dict:
    for status_file in get_status_candidates():
        if not status_file.exists():
            continue
        try:
            with open(status_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            continue
    return {}


def save_status(status: dict) -> Path | None:
    for status_file in get_status_candidates():
        try:
            status_file.parent.mkdir(parents=True, exist_ok=True)
            with open(status_file, "w", encoding="utf-8") as f:
                json.dump(status, f, indent=2)
            return status_file
        except OSError:
            continue
    return None


def is_model_available(model_key: str, status: dict, current_time: float) -> bool:
    cooldown_until = status.get(model_key, {}).get("cooldown_until", 0)
    return current_time >= cooldown_until


def get_model(complexity: str, skip_models: list[str] | None = None) -> int:
    if skip_models is None:
        skip_models = []

    status = load_status()
    current_time = time.time()

    chain = CHAINS.get(complexity, CHAINS["medium"])

    for key in chain:
        if key in skip_models or MODELS[key] in skip_models:
            continue
        if is_model_available(key, status, current_time):
            print(MODELS[key])
            return 0

    for key in chain:
        if key not in skip_models and MODELS[key] not in skip_models:
            print(MODELS[key])
            return 0

    print(MODELS["glm"])
    return 0


def report_failure(model_name: str) -> None:
    model_key = None
    for k, v in MODELS.items():
        if v == model_name or k == model_name:
            model_key = k
            break

    if not model_key:
        model_key = model_name

    status = load_status()
    current_time = time.time()

    if model_key not in status:
        status[model_key] = {}

    status[model_key]["cooldown_until"] = current_time + DEFAULT_COOLDOWN_SECONDS
    status[model_key]["last_failure"] = current_time
    status[model_key]["failures"] = status[model_key].get("failures", 0) + 1

    saved_path = save_status(status)
    if saved_path:
        print(
            f"Reported failure for {model_key}. "
            f"Cooldown until {time.ctime(status[model_key]['cooldown_until'])} "
            f"(status: {saved_path})"
        )
    else:
        print("Warning: unable to persist model status.", file=sys.stderr)


def main() -> None:
    parser = argparse.ArgumentParser(description="Model Selector and Health Monitor")
    parser.add_argument("--get-model", choices=["high", "medium", "low"], help="Get best available model for complexity")
    parser.add_argument("--report-failure", metavar="MODEL", help="Report a rate limit/failure for a model")
    parser.add_argument("--skip", nargs="*", default=[], help="List of model keys to skip")

    args = parser.parse_args()

    if args.report_failure:
        report_failure(args.report_failure)
    elif args.get_model:
        sys.exit(get_model(args.get_model, args.skip))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
