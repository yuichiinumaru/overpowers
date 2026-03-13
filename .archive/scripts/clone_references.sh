#!/bin/bash
REPOS=(
"https://github.com/sickn33/antigravity-awesome-skills"
"https://github.com/openclaw/skills"
"https://github.com/huggingface/skills"
"https://github.com/obra/superpowers"
"https://github.com/anthropics/skills"
"https://github.com/openai/skills"
"https://github.com/guipsamora/pandas_exercises"
"https://github.com/Chalarangelo/30-seconds-of-code"
"https://github.com/trailofbits/skills"
"https://github.com/antfu/skills"
"https://github.com/remotion-dev/skills"
"https://github.com/BankrBot/skills"
"https://github.com/vercel-labs/agent-skills"
"https://github.com/florinpop17/app-ideas"
"https://github.com/microsoft/skills"
"https://github.com/ComposioHQ/awesome-claude-skills"
"https://github.com/Dimillian/Skills"
"https://github.com/tsuirak/skills"
"https://github.com/NVIDIA-NeMo/Skills"
"https://github.com/agentskills/agentskills"
"https://github.com/vuejs-ai/skills"
"https://github.com/BehiSecc/awesome-claude-skills"
"https://github.com/norvig/pytudes"
"https://github.com/GuDaStudio/skills"
"https://github.com/moserware/Skills"
"https://github.com/git-game/git-game"
"https://github.com/mcollina/skills"
"https://github.com/phuryn/pm-skills"
"https://github.com/anthropics/claude-plugins-official"
"https://github.com/expo/skills"
"https://github.com/mattpocock/skills"
"https://github.com/VoltAgent/awesome-agent-skills"
"https://github.com/K-Dense-AI/claude-scientific-skills"
"https://github.com/xiaotianfotos/skills"
"https://github.com/itsmostafa/aws-agent-skills"
"https://github.com/refly-ai/refly"
"https://github.com/kepano/obsidian-skills"
"https://github.com/cloudflare/skills"
"https://github.com/github/awesome-copilot"
"https://github.com/affaan-m/everything-claude-code"
"https://github.com/trimstray/test-your-sysadmin-skills"
"https://github.com/mrgoonie/claudekit-skills"
)

mkdir -p references
cd references || exit

for repo in "${REPOS[@]}"; do
    # Extract USER/REPO from https://github.com/USER/REPO
    clean_url=${repo#*github.com/}
    username=${clean_url%/*}
    reponame=${clean_url#*/}
    
    # Combined name: usernamereponame
    dir_name="${username}${reponame}"
    
    if [ -d "$dir_name" ]; then
        echo "Skipping $dir_name (already exists)"
    else
        echo "Cloning $repo into $dir_name..."
        git clone --depth 1 "$repo" "$dir_name"
    fi
done
