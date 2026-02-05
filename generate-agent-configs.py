#!/usr/bin/env python3
"""
Generate modular agent configuration files from overpowers agents.

Usage:
    python3 generate-agent-configs.py

This script:
1. Scans overpowers/agents/ for all .md files
2. Extracts frontmatter (name, description, category)
3. Groups agents by category
4. Generates modular JSON files in overpowers/config/agents/
5. Generates a master agents.json with all agents
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict

AGENTS_DIR = Path(__file__).parent / "agents"
CONFIG_DIR = Path(__file__).parent / "config" / "agents"

def extract_frontmatter(file_path):
    """Extract YAML frontmatter from markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Match frontmatter between --- markers
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return {}
    
    frontmatter = {}
    for line in match.group(1).split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            val = value.strip()
            # Strip surrounding quotes if present
            if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                val = val[1:-1]
            frontmatter[key.strip()] = val
    
    return frontmatter

def get_prompt(file_path):
    """Extract the prompt content (everything after frontmatter)."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove frontmatter
    content = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)
    return content.strip()

def categorize_agent(name, frontmatter):
    """Determine agent category from frontmatter or name patterns."""
    # Use explicit category if present
    if 'category' in frontmatter:
        return frontmatter['category']
    
    # Infer from name patterns
    name_lower = name.lower()
    
    if any(x in name_lower for x in ['security', 'audit', 'penetration', 'owasp']):
        return 'security'
    if any(x in name_lower for x in ['test', 'qa', 'cypress', 'jest', 'playwright']):
        return 'testing'
    if any(x in name_lower for x in ['devops', 'deploy', 'ci', 'docker', 'kubernetes', 'terraform']):
        return 'devops'
    if any(x in name_lower for x in ['frontend', 'react', 'vue', 'angular', 'svelte', 'css', 'html']):
        return 'frontend'
    if any(x in name_lower for x in ['backend', 'api', 'database', 'sql', 'mongo', 'redis']):
        return 'backend'
    if any(x in name_lower for x in ['ml', 'ai', 'data', 'llm', 'nlp', 'tensor']):
        return 'ai-ml'
    if any(x in name_lower for x in ['research', 'analyst', 'synthesizer']):
        return 'research'
    if any(x in name_lower for x in ['architect', 'design', 'pattern']):
        return 'architecture'
    if any(x in name_lower for x in ['writer', 'document', 'content', 'technical']):
        return 'documentation'
    if any(x in name_lower for x in ['mobile', 'ios', 'android', 'flutter', 'react-native']):
        return 'mobile'
    if any(x in name_lower for x in ['crypto', 'blockchain', 'defi', 'web3']):
        return 'blockchain'
    if any(x in name_lower for x in ['product', 'manager', 'scrum', 'agile', 'sprint']):
        return 'product'
    if any(x in name_lower for x in ['marketing', 'seo', 'growth', 'social']):
        return 'marketing'
    if any(x in name_lower for x in ['expert', 'specialist', 'pro']):
        return 'specialists'
    
    return 'general'

def determine_mode(name, description):
    """Determine if agent should be primary or subagent."""
    name_lower = name.lower()
    desc_lower = (description or '').lower()
    
    # Orchestrators and coordinators are primary
    if any(x in name_lower for x in ['orchestrator', 'coordinator', 'manager', 'supervisor']):
        return 'primary'
    
    # Task decomposition and multi-agent are primary
    if any(x in name_lower for x in ['task-decomposition', 'multi-agent', 'swarm']):
        return 'primary'
    
    # Reviewers and checkers are subagents
    if any(x in name_lower for x in ['reviewer', 'checker', 'validator', 'auditor']):
        return 'subagent'
    
    # Specialists are subagents
    if any(x in name_lower for x in ['expert', 'specialist', 'pro']):
        return 'subagent'
    
    # Default to primary for flexibility
    return 'primary'

def main():
    # Create config directory
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    
    # Collect all agents
    agents_by_category = defaultdict(dict)
    all_agents = {}
    
    # Scan agents directory
    for md_file in AGENTS_DIR.glob('*.md'):
        name = md_file.stem
        frontmatter = extract_frontmatter(md_file)
        prompt = get_prompt(md_file)
        
        agent_name = frontmatter.get('name', name)
        description = frontmatter.get('description', '')
        category = categorize_agent(name, frontmatter)
        mode = determine_mode(name, description)
        model = frontmatter.get('model')
        model_fallback = frontmatter.get('model_fallback')
        
        agent_config = {
            "mode": mode,
            "description": description
        }

        if model:
            agent_config["model"] = model
        if model_fallback:
            agent_config["model_fallback"] = model_fallback
        
        # Only include prompt for subagents to save space in main config
        if mode == 'subagent':
            agent_config["prompt"] = prompt[:500] + "..." if len(prompt) > 500 else prompt
        
        agents_by_category[category][agent_name] = agent_config
        all_agents[agent_name] = agent_config
    
    # Generate category files
    for category, agents in agents_by_category.items():
        category_file = CONFIG_DIR / f"agents-{category}.json"
        with open(category_file, 'w', encoding='utf-8') as f:
            json.dump({"agent": agents}, f, indent=2, ensure_ascii=False)
        print(f"Generated: {category_file.name} ({len(agents)} agents)")
    
    # Generate master file
    master_file = CONFIG_DIR / "agents-all.json"
    with open(master_file, 'w', encoding='utf-8') as f:
        json.dump({"agent": all_agents}, f, indent=2, ensure_ascii=False)
    print(f"\nGenerated: {master_file.name} ({len(all_agents)} total agents)")
    
    # Generate summary
    print("\n=== Category Summary ===")
    for category in sorted(agents_by_category.keys()):
        count = len(agents_by_category[category])
        print(f"  {category}: {count} agents")
    
    # Generate index file for easy reference
    index = {
        "categories": list(sorted(agents_by_category.keys())),
        "total_agents": len(all_agents),
        "files": [f"agents-{cat}.json" for cat in sorted(agents_by_category.keys())]
    }
    index_file = CONFIG_DIR / "index.json"
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2)
    print(f"\nGenerated: {index_file.name}")

if __name__ == "__main__":
    main()
