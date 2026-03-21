#!/usr/bin/env python3
"""
gemini-tool-selector.py — Interactive TUI for managing Gemini CLI tool budget.

Gemini CLI has a hard limit of 512 tools. This includes native tools, MCP server
tools, and agents (which count as tools). This script provides an interactive
checkbox-based interface to select which agents and MCP servers to deploy,
helping you stay within the budget.

Usage:
    python3 scripts/gemini-tool-selector.py [--profile <name>] [--list-profiles] [--dry-run]
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
GEMINI_DIR = Path.home() / ".gemini"
SETTINGS_JSON = GEMINI_DIR / "settings.json"
AGENTS_DIR = GEMINI_DIR / "agents"

# Resolve repo root relative to this script
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
REPO_AGENTS_DIR = REPO_ROOT / "agents"
CONFIG_DIR = SCRIPT_DIR / "config"
PROFILES_DIR = CONFIG_DIR / "gemini-profiles"
AGENTS_LIST = CONFIG_DIR / "gemini-cli-agents.txt"

# Tool budget
MAX_TOOLS = 512
# Rough estimate of native Gemini CLI tools (search_codebase, edit_file, etc.)
NATIVE_TOOL_ESTIMATE = 12

# Category classification rules (prefix -> category)
AGENT_CATEGORIES: dict[str, str] = {
    # Languages & Frameworks
    "rust": "🦀 Rust",
    "actix": "🦀 Rust",
    "go": "🐹 Go",
    "golang": "🐹 Go",
    "python": "🐍 Python",
    "django": "🐍 Python",
    "fastapi": "🐍 Python",
    "flask": "🐍 Python",
    "cpp": "⚙️ C/C++",
    "csharp": "🟦 C#/.NET",
    "dotnet": "🟦 C#/.NET",
    "java": "☕ Java",
    "kotlin": "☕ Java/Kotlin",
    "swift": "🍎 Swift/iOS",
    "dart": "🎯 Dart/Flutter",
    "flutter": "🎯 Dart/Flutter",
    "clojure": "λ Clojure",
    "bash": "🐚 Shell/Scripting",
    "typescript": "📘 TypeScript",
    "css": "🎨 CSS",

    # Frontend
    "angular": "🅰️ Frontend",
    "react": "⚛️ Frontend",
    "svelte": "🔶 Frontend",
    "astro": "🚀 Frontend",
    "frontend": "🖥️ Frontend",
    "docusaurus": "📝 Frontend",

    # Backend
    "backend": "🔧 Backend",
    "expressjs": "🔧 Backend",
    "nodejs": "🔧 Backend",
    "directus": "🔧 Backend",
    "drupal": "🔧 Backend",

    # Data & DB
    "data": "📊 Data",
    "database": "🗃️ Database",
    "elasticsearch": "🗃️ Database",
    "elk": "🗃️ Database",

    # DevOps & Infra
    "devops": "🏗️ DevOps",
    "docker": "🐳 DevOps",
    "cicd": "🏗️ DevOps",
    "cloud": "☁️ Cloud",
    "aws": "☁️ Cloud",
    "kubernetes": "☁️ Cloud",

    # Security
    "security": "🔒 Security",
    "fintech": "🔒 Security",
    "auth0": "🔒 Security",
    "owasp": "🔒 Security",

    # Code Quality
    "code_quality": "✅ Code Quality",
    "code_review": "✅ Code Quality",
    "clean_architecture": "✅ Code Quality",
    "design_patterns": "✅ Code Quality",
    "architect": "✅ Code Quality",
    "build-error": "✅ Code Quality",

    # Documentation
    "doc": "📚 Documentation",
    "documentation": "📚 Documentation",

    # Research & Analysis
    "research": "🔍 Research",
    "academic": "🔍 Research",
    "comprehensive": "🔍 Research",
    "explore": "🔍 Research",

    # Git & VCS
    "git": "🔀 Git/VCS",

    # AI & Blockchain
    "ai_engineer": "🤖 AI/ML",
    "llm": "🤖 AI/ML",
    "blockchain": "⛓️ Blockchain",
    "crypto": "⛓️ Blockchain",

    # Mobile
    "android": "📱 Mobile",
    "ios": "📱 Mobile",

    # Business & Marketing
    "content_marketer": "📣 Business",
    "customer": "📣 Business",
    "agile": "📣 Business",
    "scrum": "📣 Business",

    # Monitoring
    "claude-performance": "📈 Monitoring",
    "agents_md": "⚡ Meta/Tooling",
}

# MCP tool count estimates (will be refined if we can query)
MCP_TOOL_ESTIMATES: dict[str, int] = {
    "hyperbrowser": 12,
    "genkit-mcp-server": 8,
    "vibe_check": 4,
    "context7": 2,
    "playwright_browser": 16,
    "serena": 22,
    "notebooklm": 6,
    "desktop_commander": 45,
}


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------
@dataclass
class AgentInfo:
    filename: str
    category: str
    deployed: bool
    available: bool  # exists in repo


@dataclass
class McpServerInfo:
    name: str
    enabled: bool
    estimated_tools: int
    command: str


@dataclass
class ToolBudget:
    native: int = NATIVE_TOOL_ESTIMATE
    mcp_tools: int = 0
    agent_count: int = 0

    @property
    def total(self) -> int:
        return self.native + self.mcp_tools + self.agent_count

    @property
    def remaining(self) -> int:
        return MAX_TOOLS - self.total


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def classify_agent(filename: str) -> str:
    """Classify an agent filename into a category."""
    # Strip prefix and extension
    name = filename.removeprefix("ovp-").removesuffix(".md").lower()

    # Try longest prefix match
    for prefix, category in sorted(
        AGENT_CATEGORIES.items(), key=lambda x: len(x[0]), reverse=True
    ):
        if name.startswith(prefix) or prefix in name:
            return category

    return "🔮 Other"


def load_settings() -> dict[str, Any]:
    """Load Gemini CLI settings.json."""
    if SETTINGS_JSON.exists():
        return json.loads(SETTINGS_JSON.read_text())
    return {}


def save_settings(settings: dict[str, Any]) -> None:
    """Save Gemini CLI settings.json."""
    SETTINGS_JSON.write_text(json.dumps(settings, indent=2) + "\n")


def get_mcp_servers(settings: dict) -> list[McpServerInfo]:
    """Extract MCP server info from settings."""
    servers = []
    mcp_config = settings.get("mcpServers", {})
    for name, config in mcp_config.items():
        cmd = config.get("command", "unknown")
        est = MCP_TOOL_ESTIMATES.get(name, 10)
        servers.append(McpServerInfo(name=name, enabled=True, estimated_tools=est, command=cmd))
    return servers


def get_deployed_agents() -> set[str]:
    """Get set of agent filenames currently deployed."""
    if not AGENTS_DIR.exists():
        return set()
    return {f.name for f in AGENTS_DIR.iterdir() if f.suffix == ".md"}


def get_available_agents() -> set[str]:
    """Get set of all agent filenames available in the repo."""
    if not REPO_AGENTS_DIR.exists():
        return set()
    return {f.name for f in REPO_AGENTS_DIR.iterdir() if f.suffix == ".md"}


def build_agent_registry() -> list[AgentInfo]:
    """Build registry of all known agents with status."""
    deployed = get_deployed_agents()
    available = get_available_agents()
    all_agents = sorted(deployed | available)

    return [
        AgentInfo(
            filename=name,
            category=classify_agent(name),
            deployed=name in deployed,
            available=name in available,
        )
        for name in all_agents
    ]


def group_by_category(agents: list[AgentInfo]) -> dict[str, list[AgentInfo]]:
    """Group agents by category, sorted by category name."""
    groups: dict[str, list[AgentInfo]] = {}
    for agent in agents:
        groups.setdefault(agent.category, []).append(agent)
    return dict(sorted(groups.items()))


def load_profile(name: str) -> dict[str, Any] | None:
    """Load a saved profile."""
    path = PROFILES_DIR / f"{name}.json"
    if path.exists():
        return json.loads(path.read_text())
    return None


def save_profile(name: str, data: dict[str, Any]) -> None:
    """Save a profile."""
    PROFILES_DIR.mkdir(parents=True, exist_ok=True)
    path = PROFILES_DIR / f"{name}.json"
    path.write_text(json.dumps(data, indent=2) + "\n")


def list_profiles() -> list[str]:
    """List available profiles."""
    if not PROFILES_DIR.exists():
        return []
    return sorted(f.stem for f in PROFILES_DIR.glob("*.json"))


# ---------------------------------------------------------------------------
# Budget display
# ---------------------------------------------------------------------------
def print_budget(budget: ToolBudget) -> None:
    """Print the current tool budget."""
    bar_width = 40
    used_ratio = min(budget.total / MAX_TOOLS, 1.0)
    filled = int(bar_width * used_ratio)
    empty = bar_width - filled

    if used_ratio < 0.6:
        color = "\033[32m"  # green
    elif used_ratio < 0.85:
        color = "\033[33m"  # yellow
    else:
        color = "\033[31m"  # red

    reset = "\033[0m"
    bold = "\033[1m"
    dim = "\033[2m"

    print(f"\n{bold}═══ Gemini CLI Tool Budget ═══{reset}")
    print(f"  {color}{'█' * filled}{'░' * empty}{reset}  {budget.total}/{MAX_TOOLS}")
    print(f"  {dim}Native: {budget.native}  │  MCP: {budget.mcp_tools}  │  Agents: {budget.agent_count}{reset}")
    print(f"  Remaining: {bold}{budget.remaining}{reset} tools\n")


# ---------------------------------------------------------------------------
# Interactive TUI
# ---------------------------------------------------------------------------
def run_interactive(args: argparse.Namespace) -> None:
    """Run the interactive tool selector."""
    try:
        from InquirerPy import inquirer
        from InquirerPy.separator import Separator
    except ImportError:
        print("\033[31m[✗]\033[0m InquirerPy not installed. Install with:")
        print("    pip install InquirerPy")
        print("    # or: uv pip install InquirerPy")
        sys.exit(1)

    settings = load_settings()
    mcp_servers = get_mcp_servers(settings)
    agents = build_agent_registry()
    categories = group_by_category(agents)
    deployed = get_deployed_agents()

    # --- Calculate initial budget ---
    budget = ToolBudget(
        mcp_tools=sum(s.estimated_tools for s in mcp_servers if s.enabled),
        agent_count=len(deployed),
    )
    print_budget(budget)

    # --- Load profile if specified ---
    pre_selected_agents: set[str] | None = None
    disabled_mcps: set[str] | None = None

    if args.profile:
        profile = load_profile(args.profile)
        if profile:
            pre_selected_agents = set(profile.get("agents", []))
            disabled_mcps = set(profile.get("disabled_mcps", []))
            print(f"\033[36m[~]\033[0m Loaded profile: {args.profile}\n")
        else:
            print(f"\033[33m[!]\033[0m Profile '{args.profile}' not found. Starting fresh.\n")

    # --- Step 1: MCP Server Selection ---
    print("\033[1m── Step 1: MCP Servers ──\033[0m\n")

    mcp_choices = []
    mcp_defaults = []
    for server in mcp_servers:
        label = f"{server.name} (~{server.estimated_tools} tools)"
        mcp_choices.append({"name": label, "value": server.name})
        if disabled_mcps and server.name not in disabled_mcps:
            mcp_defaults.append(server.name)
        elif not disabled_mcps:
            mcp_defaults.append(server.name)

    selected_mcps = inquirer.checkbox(
        message="Select MCP servers to enable:",
        choices=mcp_choices,
        default=mcp_defaults,
        instruction="(Space to toggle, Enter to confirm)",
    ).execute()

    # Recalculate MCP budget
    mcp_tool_count = sum(
        s.estimated_tools for s in mcp_servers if s.name in selected_mcps
    )

    # --- Step 2: Agent Category Selection ---
    print(f"\n\033[1m── Step 2: Agent Categories ──\033[0m")
    print(f"\033[2m   Budget after MCPs: {NATIVE_TOOL_ESTIMATE + mcp_tool_count}/{MAX_TOOLS}\033[0m\n")

    cat_choices = []
    cat_defaults = []
    for cat_name, cat_agents in categories.items():
        deployed_count = sum(1 for a in cat_agents if a.deployed)
        total_count = len(cat_agents)
        label = f"{cat_name} ({total_count} agents, {deployed_count} deployed)"
        cat_choices.append({"name": label, "value": cat_name})
        if deployed_count > 0:
            cat_defaults.append(cat_name)

    selected_categories = inquirer.checkbox(
        message="Select agent categories to include:",
        choices=cat_choices,
        default=cat_defaults,
        instruction="(Space to toggle, Enter to confirm)",
    ).execute()

    # --- Step 3: Fine-grained agent selection within chosen categories ---
    print(f"\n\033[1m── Step 3: Fine-tune Agents ──\033[0m\n")

    final_agents: list[str] = []

    for cat_name in selected_categories:
        cat_agents = categories[cat_name]
        if len(cat_agents) == 0:
            continue

        agent_choices = []
        agent_defaults = []
        for agent in cat_agents:
            status = ""
            if agent.deployed and agent.available:
                status = " ✓ deployed"
            elif agent.deployed and not agent.available:
                status = " ⚠ deployed (not in repo)"
            elif not agent.deployed and agent.available:
                status = " ○ available"

            label = f"{agent.filename}{status}"
            agent_choices.append({"name": label, "value": agent.filename})

            # Default: keep deployed, add from profile
            if pre_selected_agents is not None:
                if agent.filename in pre_selected_agents:
                    agent_defaults.append(agent.filename)
            elif agent.deployed:
                agent_defaults.append(agent.filename)

        selected = inquirer.checkbox(
            message=f"{cat_name}:",
            choices=agent_choices,
            default=agent_defaults,
            instruction="(Space to toggle, Enter to confirm)",
        ).execute()

        final_agents.extend(selected)

    # --- Budget check ---
    new_budget = ToolBudget(
        mcp_tools=mcp_tool_count,
        agent_count=len(final_agents),
    )

    print_budget(new_budget)

    if new_budget.total > MAX_TOOLS:
        print(f"\033[31m[✗]\033[0m Over budget by {new_budget.total - MAX_TOOLS} tools!")
        proceed = inquirer.confirm(
            message="Proceed anyway? (May cause Gemini CLI errors)",
            default=False,
        ).execute()
        if not proceed:
            print("Aborted.")
            return

    # --- Summary ---
    to_add = set(final_agents) - deployed
    to_remove = deployed - set(final_agents)

    print("\033[1m── Summary ──\033[0m\n")
    if to_add:
        print(f"  \033[32m+ Add {len(to_add)} agents:\033[0m")
        for a in sorted(to_add):
            print(f"    + {a}")
    if to_remove:
        print(f"  \033[31m- Remove {len(to_remove)} agents:\033[0m")
        for a in sorted(to_remove):
            print(f"    - {a}")

    disabled_mcp_set = {s.name for s in mcp_servers} - set(selected_mcps)
    if disabled_mcp_set:
        print(f"  \033[33m~ Disable {len(disabled_mcp_set)} MCPs:\033[0m")
        for m in sorted(disabled_mcp_set):
            print(f"    ~ {m}")

    if not to_add and not to_remove and not disabled_mcp_set:
        print("  No changes needed.")
        return

    if args.dry_run:
        print("\n\033[33m[!]\033[0m Dry run — no changes applied.")
        return

    # --- Confirm & Apply ---
    confirm = inquirer.confirm(
        message="Apply these changes?",
        default=True,
    ).execute()

    if not confirm:
        print("Aborted.")
        return

    # Apply agent changes
    AGENTS_DIR.mkdir(parents=True, exist_ok=True)
    for agent_file in to_add:
        src = REPO_AGENTS_DIR / agent_file
        dst = AGENTS_DIR / agent_file
        if src.exists():
            shutil.copy2(src, dst)
            print(f"\033[32m[✓]\033[0m Copied {agent_file}")
        else:
            print(f"\033[33m[!]\033[0m {agent_file} not found in repo — skipping")

    for agent_file in to_remove:
        dst = AGENTS_DIR / agent_file
        if dst.exists():
            # Move to .archive instead of deleting (per Art. 6)
            archive = AGENTS_DIR / ".archive"
            archive.mkdir(exist_ok=True)
            shutil.move(str(dst), str(archive / agent_file))
            print(f"\033[31m[-]\033[0m Archived {agent_file}")

    # Apply MCP changes (comment-out disabled servers in settings.json)
    if disabled_mcp_set:
        current_mcps = settings.get("mcpServers", {})
        # Store disabled server configs separately
        settings.setdefault("_disabledMcpServers", {})
        for mcp_name in disabled_mcp_set:
            if mcp_name in current_mcps:
                settings["_disabledMcpServers"][mcp_name] = current_mcps.pop(mcp_name)
                print(f"\033[33m[~]\033[0m Disabled MCP: {mcp_name}")

        # Re-enable previously disabled servers that are now selected
        for mcp_name in selected_mcps:
            if mcp_name in settings.get("_disabledMcpServers", {}):
                current_mcps[mcp_name] = settings["_disabledMcpServers"].pop(mcp_name)
                print(f"\033[32m[✓]\033[0m Re-enabled MCP: {mcp_name}")

        save_settings(settings)

    # --- Save profile prompt ---
    save_as = inquirer.text(
        message="Save as profile? (Enter name or leave blank to skip):",
        default="",
    ).execute()

    if save_as.strip():
        profile_data = {
            "agents": final_agents,
            "disabled_mcps": sorted(disabled_mcp_set),
            "selected_mcps": sorted(selected_mcps),
            "budget": {
                "total": new_budget.total,
                "native": new_budget.native,
                "mcp_tools": new_budget.mcp_tools,
                "agent_count": new_budget.agent_count,
            },
        }
        save_profile(save_as.strip(), profile_data)
        print(f"\033[32m[✓]\033[0m Profile saved: {save_as.strip()}")

    # Update the config/gemini-cli-agents.txt to reflect new list
    AGENTS_LIST.parent.mkdir(parents=True, exist_ok=True)
    AGENTS_LIST.write_text("\n".join(sorted(final_agents)) + "\n")
    print(f"\033[32m[✓]\033[0m Updated {AGENTS_LIST.relative_to(REPO_ROOT)}")

    print(f"\n\033[32m═══ Done! Restart Gemini CLI to apply changes. ═══\033[0m")


# ---------------------------------------------------------------------------
# Non-interactive: list profiles
# ---------------------------------------------------------------------------
def cmd_list_profiles() -> None:
    """List available profiles."""
    profiles = list_profiles()
    if not profiles:
        print("No profiles saved yet.")
        return
    print("\033[1mSaved profiles:\033[0m")
    for name in profiles:
        profile = load_profile(name)
        if profile:
            b = profile.get("budget", {})
            print(f"  • {name}  ({b.get('agent_count', '?')} agents, {b.get('total', '?')}/{MAX_TOOLS} tools)")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Interactive Gemini CLI tool budget manager.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                      # Start interactive selector
  %(prog)s --profile rust-dev   # Load a saved profile
  %(prog)s --list-profiles      # Show saved profiles
  %(prog)s --dry-run            # Preview changes without applying
        """,
    )
    parser.add_argument(
        "--profile", "-p",
        help="Load a saved profile as starting point.",
    )
    parser.add_argument(
        "--list-profiles", "-l",
        action="store_true",
        help="List saved profiles and exit.",
    )
    parser.add_argument(
        "--dry-run", "-n",
        action="store_true",
        help="Show what would change without applying.",
    )

    args = parser.parse_args()

    if args.list_profiles:
        cmd_list_profiles()
        return

    run_interactive(args)


if __name__ == "__main__":
    main()
