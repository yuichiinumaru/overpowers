#!/usr/bin/env python3
"""
Sync OpenCode agents to HyperTool personas.

Generates consolidated personas from 396+ agent profiles with automatic
MCP tool assignment based on role categories.
"""

import os
import re
import json
import yaml
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# Paths
AGENTS_DIR = Path("/home/sephiroth/.config/opencode/Overpowers/agents")
PERSONAS_DIR = Path("/home/sephiroth/.config/opencode/Overpowers/personas")
OPENCODE_JSON = Path("/home/sephiroth/.config/opencode/opencode.json")

# Essential MCPs (always included)
ESSENTIAL_MCPS = {
    "serena": {
        "type": "local",
        "command": ["uvx", "--from", "git+https://github.com/oraios/serena", "serena", "start-mcp-server", "--context", "ide-assistant"],
        "enabled": True
    },
    "vibe-check": {
        "type": "local",
        "command": ["npx", "-y", "@pv-bhat/vibe-check-mcp", "start", "--stdio"],
        "environment": {"GEMINI_API_KEY": "<YOUR_GEMINI_API_KEY>"},
        "enabled": True
    }
}

# Role-specific MCPs (YAAMCPL Winners integrated 2026-01-19)
ROLE_MCPS = {
    "developer": {
        "context7": {
            "type": "local",
            "command": ["npx", "-y", "@upstash/context7-mcp"],
            "environment": {"CONTEXT7_API_KEY": "<YOUR_CONTEXT7_API_KEY>"},
            "enabled": True
        },
        "deepwiki": {
            "type": "remote",
            "url": "https://mcp.deepwiki.com/mcp",
            "enabled": True
        },
        "github": {
            "type": "local",
            "command": ["npx", "-y", "github-repos-manager-mcp"],
            "environment": {"GH_TOKEN": "${GH_TOKEN}"},
            "enabled": True,
            "note": "YAAMCPL Winner: Full GitHub management (89 tools)"
        },
        "filesystem": {
            "type": "local",
            "command": ["uvx", "mcp-filesystem-server"],
            "enabled": True,
            "note": "YAAMCPL Winner: mark3labs/mcp-filesystem-server"
        }
    },
    "researcher": {
        "mult-fetch": {
            "type": "local",
            "command": ["npx", "-y", "@lmcc-dev/mult-fetch-mcp-server"],
            "enabled": True
        },
        "think-tank": {
            "type": "local",
            "command": ["npx", "-y", "mcp-think-tank@2.0.7"],
            "environment": {"MEMORY_PATH": "/home/sephiroth/.config/opencode/memory.jsonl"},
            "enabled": True
        },
        "memory": {
            "type": "local",
            "command": ["uvx", "chroma-mcp", "--client-type", "persistent", "--data-dir", "./chroma-data"],
            "enabled": True,
            "note": "YAAMCPL Winner: chroma-core/chroma-mcp (local vector DB)"
        },
        "browser": {
            "type": "local",
            "command": ["npx", "-y", "@playwright/mcp@latest"],
            "enabled": True,
            "note": "YAAMCPL Winner: microsoft/playwright-mcp"
        }
    },
    "security": {
        "hyperbrowser": {
            "type": "local",
            "command": ["npx", "-y", "@google/antigravity-hyperbrowser-mcp"],
            "enabled": True
        },
        "terminal": {
            "type": "local",
            "command": ["mcp-shell"],
            "environment": {"MCP_SHELL_LOG_LEVEL": "info"},
            "enabled": True,
            "note": "YAAMCPL Winner: sonirico/mcp-shell (secure shell with audit)"
        }
    },
    "devops": {
        "context7": {
            "type": "local",
            "command": ["npx", "-y", "@upstash/context7-mcp"],
            "environment": {"CONTEXT7_API_KEY": "<YOUR_CONTEXT7_API_KEY>"},
            "enabled": True
        },
        "terminal": {
            "type": "local",
            "command": ["mcp-shell"],
            "environment": {"MCP_SHELL_LOG_LEVEL": "info"},
            "enabled": True,
            "note": "YAAMCPL Winner: sonirico/mcp-shell"
        },
        "docker": {
            "type": "local",
            "command": ["uvx", "mcp-server-docker"],
            "enabled": True,
            "note": "YAAMCPL Winner: ckreiling/mcp-server-docker"
        },
        "kubernetes": {
            "type": "local",
            "command": ["k8s-mcp-server"],
            "enabled": True,
            "note": "YAAMCPL Winner: manusa/kubernetes-mcp-server"
        },
        "grafana": {
            "type": "local",
            "command": ["npx", "@grafana/mcp-grafana"],
            "environment": {"GRAFANA_URL": "${GRAFANA_URL}", "GRAFANA_API_KEY": "${GRAFANA_API_KEY}"},
            "enabled": True,
            "note": "YAAMCPL Winner: grafana/mcp-grafana"
        }
    },
    "ai-ml": {
        "deepwiki": {
            "type": "remote",
            "url": "https://mcp.deepwiki.com/mcp",
            "enabled": True
        },
        "think-tank": {
            "type": "local",
            "command": ["npx", "-y", "mcp-think-tank@2.0.7"],
            "environment": {"MEMORY_PATH": "/home/sephiroth/.config/opencode/memory.jsonl"},
            "enabled": True
        },
        "memory": {
            "type": "local",
            "command": ["uvx", "chroma-mcp", "--client-type", "persistent", "--data-dir", "./chroma-data"],
            "enabled": True,
            "note": "YAAMCPL Winner: chroma-core/chroma-mcp"
        }
    },
    "database": {
        "mysql": {
            "type": "local",
            "command": ["node", "/path/to/mcp-mysql-server/build/index.js"],
            "enabled": True,
            "note": "YAAMCPL Winner: f4ww4z/mcp-mysql-server (dynamic connect)"
        },
        "gateway": {
            "type": "local",
            "command": ["docker", "run", "-i", "--rm", "ghcr.io/centralmind/gateway:latest", "start", "--connection-string", "${DATABASE_URL}", "mcp-stdio"],
            "enabled": True,
            "note": "YAAMCPL Winner: centralmind/gateway (universal DB)"
        },
        "redis": {
            "type": "local",
            "command": ["uvx", "mcp-redis"],
            "enabled": True,
            "note": "YAAMCPL Winner: redis/mcp-redis"
        }
    }
}

# Persona categories with agent patterns
PERSONA_CATEGORIES = {
    "security_auditor": {
        "patterns": ["security", "penetration", "audit", "vulnerability", "incident"],
        "role_mcps": ["security"],
        "description": "Security testing, vulnerability assessment, and incident response",
        "toolsets": [
            {"name": "scanning", "tools": ["serena.search_for_pattern", "serena.find_symbol", "vibe-check.analyze_deviation"]},
            {"name": "testing", "tools": ["hyperbrowser.browser_use_agent", "serena.read_memory"]},
            {"name": "reporting", "tools": ["serena.write_memory", "serena.list_memories"]}
        ]
    },
    "fullstack_developer": {
        "patterns": ["developer", "frontend", "backend", "fullstack", "web", "react", "vue", "angular", "nextjs"],
        "role_mcps": ["developer"],
        "description": "Full-stack web development across frontend and backend technologies",
        "toolsets": [
            {"name": "coding", "tools": ["serena.find_symbol", "serena.get_symbols_overview", "serena.replace_symbol_body", "context7.query-docs"]},
            {"name": "debugging", "tools": ["serena.search_for_pattern", "serena.find_referencing_symbols"]},
            {"name": "docs", "tools": ["deepwiki.query", "context7.resolve-library-id"]}
        ]
    },
    "comprehensive_researcher": {
        "patterns": ["research", "analyst", "synthesizer", "knowledge"],
        "role_mcps": ["researcher"],
        "description": "Research, analysis, and knowledge synthesis across domains",
        "toolsets": [
            {"name": "discovery", "tools": ["mult-fetch.fetch_markdown", "think-tank.search"]},
            {"name": "analysis", "tools": ["serena.search_for_pattern", "serena.think_about_collected_information"]},
            {"name": "synthesis", "tools": ["serena.write_memory", "think-tank.remember"]}
        ]
    },
    "devops_engineer": {
        "patterns": ["devops", "sre", "infrastructure", "kubernetes", "docker", "terraform", "cicd", "deployment"],
        "role_mcps": ["devops"],
        "description": "Infrastructure, CI/CD, and deployment automation",
        "toolsets": [
            {"name": "infra", "tools": ["serena.find_file", "serena.search_for_pattern", "context7.query-docs"]},
            {"name": "deployment", "tools": ["serena.list_dir", "serena.get_symbols_overview"]},
            {"name": "monitoring", "tools": ["serena.read_memory", "vibe-check.check_status"]}
        ]
    },
    "system-architect": {
        "patterns": ["architect", "design", "microservices", "cloud"],
        "role_mcps": ["developer"],
        "description": "System design, architecture review, and technical leadership",
        "toolsets": [
            {"name": "design", "tools": ["serena.get_symbols_overview", "serena.find_referencing_symbols", "deepwiki.query"]},
            {"name": "review", "tools": ["serena.search_for_pattern", "vibe-check.analyze_deviation"]},
            {"name": "docs", "tools": ["serena.write_memory", "context7.query-docs"]}
        ]
    },
    "ai-ml-engineer": {
        "patterns": ["ai", "ml", "machine-learning", "llm", "nlp", "data-scien"],
        "role_mcps": ["ai-ml"],
        "description": "AI/ML engineering, model development, and data science",
        "toolsets": [
            {"name": "development", "tools": ["serena.find_symbol", "serena.replace_symbol_body", "deepwiki.query"]},
            {"name": "research", "tools": ["think-tank.search", "think-tank.remember"]},
            {"name": "analysis", "tools": ["serena.search_for_pattern", "serena.get_symbols_overview"]}
        ]
    },
    "qa-engineer": {
        "patterns": ["test", "qa", "quality", "automation"],
        "role_mcps": ["developer"],
        "description": "Quality assurance, test automation, and coverage analysis",
        "toolsets": [
            {"name": "testing", "tools": ["serena.find_symbol", "serena.search_for_pattern"]},
            {"name": "coverage", "tools": ["serena.get_symbols_overview", "serena.find_referencing_symbols"]},
            {"name": "reporting", "tools": ["serena.write_memory", "vibe-check.check_status"]}
        ]
    },
    "documentation-writer": {
        "patterns": ["document", "writer", "technical_writer", "api-doc"],
        "role_mcps": ["researcher"],
        "description": "Technical documentation and API documentation creation",
        "toolsets": [
            {"name": "research", "tools": ["serena.get_symbols_overview", "serena.find_symbol", "mult-fetch.fetch_markdown"]},
            {"name": "writing", "tools": ["serena.write_memory", "serena.search_for_pattern"]},
            {"name": "review", "tools": ["vibe-check.analyze_deviation", "serena.read_memory"]}
        ]
    },
    "database-specialist": {
        "patterns": ["database", "sql", "postgres", "mysql", "mongo", "redis", "data_engineer", "etl"],
        "role_mcps": ["database"],
        "description": "Database administration, optimization, and data modeling",
        "toolsets": [
            {"name": "querying", "tools": ["mysql.query", "mysql.list_tables", "gateway.query"]},
            {"name": "analysis", "tools": ["serena.search_for_pattern", "serena.find_symbol"]},
            {"name": "optimization", "tools": ["serena.get_symbols_overview", "context7.query-docs"]},
            {"name": "docs", "tools": ["serena.write_memory", "deepwiki.query"]}
        ]
    },
    "mobile_developer": {
        "patterns": ["mobile", "ios", "android", "flutter", "react-native", "swift", "kotlin"],
        "role_mcps": ["developer"],
        "description": "Mobile app development for iOS and Android platforms",
        "toolsets": [
            {"name": "coding", "tools": ["serena.find_symbol", "serena.replace_symbol_body", "context7.query-docs"]},
            {"name": "debugging", "tools": ["serena.search_for_pattern", "serena.find_referencing_symbols"]},
            {"name": "docs", "tools": ["deepwiki.query", "serena.get_symbols_overview"]}
        ]
    },
    "product_manager": {
        "patterns": ["product", "project", "scrum", "agile", "sprint"],
        "role_mcps": ["researcher"],
        "description": "Product management, project planning, and agile methodologies",
        "toolsets": [
            {"name": "planning", "tools": ["serena.list_memories", "serena.read_memory", "think-tank.search"]},
            {"name": "analysis", "tools": ["mult-fetch.fetch_markdown", "serena.search_for_pattern"]},
            {"name": "reporting", "tools": ["serena.write_memory", "think-tank.remember"]}
        ]
    },
    "language-specialist": {
        "patterns": ["python", "java", "golang", "rust", "typescript", "javascript", "php", "ruby", "csharp", "cpp"],
        "role_mcps": ["developer"],
        "description": "Language-specific development expertise",
        "toolsets": [
            {"name": "coding", "tools": ["serena.find_symbol", "serena.replace_symbol_body", "context7.query-docs"]},
            {"name": "refactoring", "tools": ["serena.rename_symbol", "serena.find_referencing_symbols"]},
            {"name": "analysis", "tools": ["serena.get_symbols_overview", "serena.search_for_pattern"]}
        ]
    }
}


def load_agents():
    """Load all agent files and extract metadata."""
    agents = []
    for agent_file in AGENTS_DIR.glob("*.md"):
        name = agent_file.stem
        content = agent_file.read_text(encoding='utf-8')
        agents.append({
            "name": name,
            "file": str(agent_file),
            "content": content[:500]  # First 500 chars for description matching
        })
    return agents


def categorize_agent(agent_name: str) -> str:
    """Determine which persona category an agent belongs to."""
    name_lower = agent_name.lower()
    for persona, config in PERSONA_CATEGORIES.items():
        for pattern in config["patterns"]:
            if pattern in name_lower:
                return persona
    return "general-assistant"  # Default fallback


def generate_persona(persona_name: str, agents: list) -> dict:
    """Generate a persona configuration."""
    config = PERSONA_CATEGORIES.get(persona_name, {
        "description": "General-purpose assistant",
        "role_mcps": [],
        "toolsets": [{"name": "default", "tools": ["serena.search_for_pattern", "serena.find_symbol"]}]
    })
    
    return {
        "name": persona_name,
        "description": config["description"],
        "version": "1.0",
        "toolsets": [
            {"name": ts["name"], "toolIds": ts["tools"]}
            for ts in config["toolsets"]
        ],
        "defaultToolset": config["toolsets"][0]["name"] if config["toolsets"] else "default",
        "metadata": {
            "author": "Overpowers",
            "tags": [persona_name.split("-")[0], "auto-generated"],
            "created": datetime.now().isoformat() + "Z",
            "agents": [a["name"] for a in agents[:10]]  # List first 10 agents
        }
    }


def generate_mcp_json(persona_name: str) -> dict:
    """Generate MCP server configuration for a persona."""
    config = PERSONA_CATEGORIES.get(persona_name, {"role_mcps": []})
    
    servers = dict(ESSENTIAL_MCPS)
    for role in config.get("role_mcps", []):
        if role in ROLE_MCPS:
            servers.update(ROLE_MCPS[role])
    
    return {"mcpServers": servers}


def generate_readme(persona_name: str, agents: list) -> str:
    """Generate README for a persona."""
    config = PERSONA_CATEGORIES.get(persona_name, {"description": "General assistant"})
    
    agent_list = "\n".join([f"- `{a['name']}`" for a in agents[:20]])
    if len(agents) > 20:
        agent_list += f"\n- ... and {len(agents) - 20} more"
    
    return f"""# {persona_name.replace('-', ' ').title()}

{config['description']}

## Included Agents ({len(agents)})

{agent_list}

## Toolsets

| Toolset | Purpose |
|---------|---------|
{chr(10).join([f"| `{ts['name']}` | {ts['name'].replace('-', ' ').title()} workflow |" for ts in config.get('toolsets', [])])}

## Usage

### With HyperTool

```bash
npx -y @toolprint/hypertool-mcp mcp run --persona {persona_name}
```

### Quick Start

```bash
cp personas/{persona_name}/mcp.json ~/.config/opencode/.mcp.json
```
"""


def main():
    """Generate all personas from agents."""
    print("=" * 60)
    print("Agent-to-Persona Sync")
    print("=" * 60)
    
    # Load agents
    agents = load_agents()
    print(f"\nFound {len(agents)} agents")
    
    # Categorize agents
    categorized = defaultdict(list)
    for agent in agents:
        category = categorize_agent(agent["name"])
        categorized[category].append(agent)
    
    # Show distribution
    print("\nAgent distribution:")
    for category, agent_list in sorted(categorized.items(), key=lambda x: -len(x[1])):
        print(f"  {category}: {len(agent_list)} agents")
    
    # Generate personas
    print("\nGenerating personas...")
    generated = 0
    for persona_name, agent_list in categorized.items():
        if persona_name == "general-assistant" and len(agent_list) < 5:
            continue  # Skip small general bucket
        
        persona_dir = PERSONAS_DIR / persona_name
        persona_dir.mkdir(exist_ok=True)
        
        # Generate persona.yaml
        persona_config = generate_persona(persona_name, agent_list)
        with open(persona_dir / "persona.yaml", 'w') as f:
            yaml.dump(persona_config, f, default_flow_style=False, sort_keys=False)
        
        # Generate mcp.json
        mcp_config = generate_mcp_json(persona_name)
        with open(persona_dir / "mcp.json", 'w') as f:
            json.dump(mcp_config, f, indent=2)
        
        # Generate README.md
        readme = generate_readme(persona_name, agent_list)
        with open(persona_dir / "README.md", 'w') as f:
            f.write(readme)
        
        print(f"  ✅ {persona_name} ({len(agent_list)} agents)")
        generated += 1
    
    print("\n" + "=" * 60)
    print(f"Generated {generated} personas in {PERSONAS_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()
