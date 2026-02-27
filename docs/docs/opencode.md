<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# find as many possible FOSS alternatives to claude code. they MUST be cli (i DONT want ide or extensions to vscode like roocode vscode extension, if roocode has a CLI tool, bring me that), preferably support sub agents or parallel agents (even if plugins are necessary to do that).

Now I'll generate the comprehensive report.

## FOSS CLI Alternatives to Claude Code: Comprehensive Analysis

Based on extensive research of the current ecosystem, here are the FOSS CLI alternatives to Claude Code, organized by multi-agent capability level:

### **Tier 1: Native Multi-Agent/Parallel Execution Support**

#### **1. Goose** (by Block) – Best for Parallel Workflows[^1_1][^1_2][^1_3]

- **GitHub:** block/goose
- **CLI + Desktop GUI** with terminal integration mode (`@goose "do this"`)
- **Multi-agent architecture:** Subagents for parallel execution with recipes and orchestration
- **Key features:**
    - Parallel and sequential subagent execution
    - MCP (Model Context Protocol) support with first-class integration
    - Recipe system for reusable automation pipelines
    - Named sessions and skills for custom context
    - Terminal integration + full REPL mode
    - Extensible through plugins and custom recipes
- **Ecosystem:** Built by Square/Block in Rust + TypeScript
- **License:** Apache 2.0

**Why it stands out:** Goose is purpose-built for multi-agent workflows with explicit parallel execution primitives. You can spawn 4+ subagents simultaneously, each running in isolated sessions, and the recipes system orchestrates their work. This is the closest match to "parallel agents" in the FOSS space.

***

#### **2. OpenCode** – Purpose-Built Parallel Agents[^1_4][^1_5]

- **GitHub:** opencode-ai/opencode
- **Go-based CLI** with TUI interface
- **Multi-agent capability:** `Multi-session: Start multiple agents in parallel on the same project`
- **Key features:**
    - LSP (Language Server Protocol) support for code intelligence
    - Custom commands and project-level command organization
    - Git integration with intelligent context awareness
    - Sourcegraph integration for cross-repository search
    - Built-in agent tool for sub-task delegation
    - Session-based workflow isolation
- **Architecture:** Go backend with modular design
- **License:** FOSS (verified)

**Why it stands out:** OpenCode explicitly advertises parallel multi-session capability, meaning you can run multiple agents concurrently on the same project—exactly what you need for task distribution.

***

### **Tier 2: Multi-Agent via MCP Extension Ecosystem**

#### **3. Aider + MCP Servers** – Extensible Agent Orchestration[^1_6][^1_7][^1_8]

- **GitHub:** paul-gauthier/aider (core tool), plus community extensions
- **Pure CLI**, git-native workflow
- **Multi-agent capability:** NOT native, but achieved through MCP integrations
- **Recommended MCP bridges:**
    - **mcpm-aider** – Official MCP bridge for external tool integration
    - **AiderDesk** – Enhanced Aider with Agent Mode + MCP
    - **Aider Multi-Coder MCP Server** – Parallel execution of coding tasks
    - **aider-mcp-client** – Community-driven MCP client
- **Key features (base Aider):**
    - Codebase mapping and git-native commits
    - Multi-LLM support (Claude, DeepSeek, GPT-4, Gemini, Ollama local)
    - Voice coding support
    - Terminal integration
- **Multi-agent workflow example:** Fetch requirements from Jira MCP → Query database schema via MCP → Write API endpoint → Use GitHub MCP to create PR—all orchestrated by a single high-level prompt[^1_7]
- **License:** Apache 2.0

**Why it stands out:** Aider becomes a true orchestration engine when paired with MCP servers. The AiderDesk extension adds explicit Agent Mode that decomposes tasks, selects tools, and iterates—turning Aider into a multi-step automation platform.

***

#### **4. Continue CLI** – Modular, Rule-Based Agent Extension[^1_9][^1_10][^1_11]

- **GitHub:** continuedev/continue (fork: @continuedev/cli)
- **CLI tool** (npm i -g @continuedev/cli)
- **Multi-agent capability:** Modular agent loop extensible through MCP + custom rules
- **Key features:**
    - TUI (interactive) and headless (`-p`) modes
    - Session management with `--resume` functionality
    - Custom rules for team workflows
    - MCP support for tool expansion
    - File editing, terminal execution, git integration
    - CI/CD ready with API key authentication
    - Context engineering with `@` references and `/` commands
- **Configuration:** Same config.yaml as Continue IDE extension
- **License:** Open source

**Why it stands out:** Continue CLI's strength is **customization and rule-based workflows**. You can define custom agents (roles) via rules and chain them together. It's less about built-in parallelism and more about a battle-tested agent loop that's infinitely extensible.

***

### **Tier 3: Single-Agent Full Autonomy (Large Context)**

#### **5. Plandex** – Best for Large Codebases[^1_12][^1_13][^1_14][^1_15]

- **GitHub:** plandex-ai/plandex
- **CLI-first, REPL mode**
- **Multi-agent capability:** None (single agent, but with full autonomy across files)
- **Key features:**
    - 2M+ token effective context with 20M+ token indexing for massive repos
    - Diff-review sandbox (cumulative changes before commit)
    - Autonomous debugging: test execution, browser app debugging
    - Multi-model support (OpenAI, Anthropic, Google, OpenRouter)
    - Tree-sitter project mapping (30+ languages)
    - Full autonomy or step-by-step control modes
    - Git integration with commit message generation
- **Ideal for:** Complex cross-file refactoring in huge projects (e.g., SQLite, Redis, Git source)
- **License:** FOSS

**Why it stands out:** If you don't need multi-agent orchestration but need an agent that can handle million-line codebases without hallucinating, Plandex is unmatched. Its context management is engineered specifically for this problem.

***

### **Tier 4: Custom Agent Roles \& Extensibility**

#### **6. ForgeCode** – Customizable Agent Roles[^1_16][^1_17][^1_18]

- **GitHub:** antinomyhq/forge
- **CLI tool** (npx forgecode@latest)
- **Multi-agent capability:** Custom agents/roles system (`/muse` for planning, `/forge` for implementation)
- **Key features:**
    - Zero-config setup with just API key
    - Multi-provider support (OpenAI, Anthropic, Google Vertex, OpenRouter)
    - Terminal-native, integrates with existing workflows
    - Custom agent roles for specialized tasks (frontend, DevOps, etc.)
    - Secure by design: code stays on-premise
    - Open-source and fully customizable
    - Team-shareable custom agents
- **Use case:** "I can create custom 'agents' for specialized tasks (like one tailored to frontend work or DevOps scripts) and share them with my team"
- **License:** Open source

**Why it stands out:** ForgeCode's agent abstraction layer allows you to define team-specific agent personas. It's not true parallelism but functional composition of specialized agents.

***

### **Tier 5: Lightweight/Specialized CLI Tools**

#### **7. Gemini CLI** – Free, Official Google Tool[^1_19][^1_20][^1_21]

- **Official Google product**
- **CLI tool** bringing Gemini directly to terminal
- **Multi-agent capability:** Multi-step reasoning (not parallelizable subagents)
- **Key features:**
    - Free tier with highest usage limits in market
    - File manipulation, command execution
    - Dynamic troubleshooting
    - Works with Gemini Code Assist
    - Multi-step planning and auto-recovery
- **License:** Open source

***

#### **8. tlm (Terminal LLaMA)** – Local-First Alternative[^1_22][^1_23]

- **GitHub:** yusufcanb/tlm
- **CLI tool** using Ollama + CodeLLaMA
- **Multi-agent capability:** None
- **Key features:**
    - Completely self-hosted, runs offline
    - Shell command generation + explanation
    - Automatic shell detection (Bash/Zsh/Fish/PowerShell)
    - Response time: 2–4 seconds on Apple Silicon
- **License:** Open source

***

#### **9. Continue CLI** – Already listed above, but also includes basic multi-agent via rules

#### **10. Bito CLI** – Early Alpha[^1_24][^1_25]

- **GitHub:** gitbito/CLI
- **CLI interface** with chat functionality
- **Multi-agent capability:** Not found
- **Note:** Early alpha; not fully FOSS verified
- **License:** Early stage, unclear

***

#### **11. GPT-CLI** – Security-Focused Alternative[^1_26]

- **GitHub:** Visph/GPT-CLI
- **Open-source**, security-first design
- **Multi-agent capability:** None
- **Key features:**
    - Isolated child process execution
    - Built-in validator to prevent dangerous commands
    - Interactive conversations
    - Auto-execute mode available
    - Conversation history
- **License:** Open source

***

### **Comparison Matrix**

| Tool | Multi-Agent Native | Via MCP | CLI | Large Context | Local Model Support | License |
| :-- | :--: | :--: | :--: | :--: | :--: | :--: |
| **Goose** | ✅ Subagents | ✅ | ✅ | ✅ | ✅ | Apache 2.0 |
| **OpenCode** | ✅ Multi-session | - | ✅ | ✅ | ✅ | FOSS |
| **Aider + MCP** | ⚠️ Via extension | ✅ AiderDesk | ✅ | ✅ | ✅ | Apache 2.0 |
| **Continue CLI** | ⚠️ Via rules | ✅ | ✅ | ✅ | ✅ | Open source |
| **Plandex** | ❌ | - | ✅ | ✅✅ | ✅ | FOSS |
| **ForgeCode** | ⚠️ Custom roles | - | ✅ | ✅ | ✅ | Open source |
| **Gemini CLI** | ⚠️ Multi-step | - | ✅ | ✅ | ❌ | Open source |
| **tlm** | ❌ | - | ✅ | ⚠️ Limited | ✅✅ | Open source |


***

### **Recommendations by Use Case**

**You want parallel multi-agent workflows right now:**
→ **Goose** or **OpenCode** (native support)

**You want maximum extensibility via MCP:**
→ **Aider + AiderDesk MCP** or **Continue CLI** (infinite tool ecosystem)

**You're working with massive codebases (2M+ tokens):**
→ **Plandex** (single agent, perfect autonomy)

**You want custom team-specific agent roles:**
→ **ForgeCode** (role-based agents)

**You want fully offline/local execution:**
→ **tlm** (CodeLLaMA + Ollama) or **Goose** (local models via config)

**You want FOSS purity + simplicity:**
→ **Aider** (battle-tested, git-native, minimal dependencies)

***

### **Important Notes**

- **Roo Code** is NOT included because it's VS Code extension-only despite requests for CLI mode (GitHub issue \#3835 is open but unresolved)[^1_27][^1_28][^1_29]
- **Continue.dev IDE extension** has a CLI counterpart (**Continue CLI**), which is separate and fully CLI-native[^1_9]
- **MCP integration** (Model Context Protocol) is increasingly becoming the standard for extending agents with external tools and multi-agent capabilities
- All listed tools support multiple LLM providers (Anthropic, OpenAI, Google, local Ollama models) except Gemini CLI
<span style="display:none">[^1_30][^1_31][^1_32][^1_33][^1_34][^1_35][^1_36][^1_37][^1_38][^1_39][^1_40][^1_41][^1_42][^1_43][^1_44][^1_45][^1_46][^1_47][^1_48][^1_49][^1_50][^1_51][^1_52][^1_53][^1_54][^1_55][^1_56][^1_57][^1_58]</span>

<div align="center">⁂</div>

[^1_1]: https://www.nickyt.co/blog/what-makes-goose-different-from-other-ai-coding-agents-2edc/

[^1_2]: https://www.youtube.com/watch?v=KrFSaY-v-tE

[^1_3]: https://github.com/block/goose

[^1_4]: https://github.com/opencode-ai/opencode

[^1_5]: https://opencode.ai

[^1_6]: https://www.hotovo.com/blog/how-mcp-servers-gave-birth-to-aiderdesks-agent-mode

[^1_7]: https://skywork.ai/skypage/en/Mastering-Agentic-Coding-A-Deep-Dive-into-Integrating-Aider-with-the-Model-Context-Protocol-(MCP)/1972136065188859904

[^1_8]: https://skywork.ai/skypage/en/aider-multi-coder-server/1980832214269366272

[^1_9]: https://docs.continue.dev/guides/cli

[^1_10]: https://www.npmjs.com/package/@continuedev/cli

[^1_11]: https://docs.continue.dev/cli/overview

[^1_12]: https://www.youtube.com/watch?v=aj4vFEDr_qo

[^1_13]: https://github.com/cybernetics/plandex-ai

[^1_14]: https://github.com/plandex-ai/plandex?tab=readme-ov-file

[^1_15]: https://www.reddit.com/r/ChatGPTCoding/comments/1jgmbsa/plandex_v2_an_open_source_ai_coding_agent_with/

[^1_16]: https://www.npmjs.com/package/@antinomyhq/forge

[^1_17]: https://dev.to/forgecode/why-i-chose-forgecode-as-1-ai-coding-assistant-in-2025-325l

[^1_18]: https://forgecode.dev

[^1_19]: https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-cli-open-source-ai-agent/

[^1_20]: https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/

[^1_21]: https://codeassist.google

[^1_22]: https://www.reddit.com/r/selfhosted/comments/1b46p71/tlm_using_ollama_to_create_a_github_copilot_cli/

[^1_23]: https://www.youtube.com/watch?v=uAgRXQGCCyY

[^1_24]: https://www.youtube.com/watch?v=3dkg7oOSELQ

[^1_25]: https://docs.bito.ai/other-bito-ai-tools/bito-cli/overview

[^1_26]: https://www.reddit.com/r/opensource/comments/1myo0m0/i_built_a_securityfocused_opensource_ai_coding/

[^1_27]: https://github.com/RooCodeInc/Roo-Code

[^1_28]: https://www.reddit.com/r/RooCode/comments/1laswrx/roo_code_cli/

[^1_29]: https://github.com/RooCodeInc/Roo-Code/issues/3835

[^1_30]: https://getstream.io/blog/multiagent-ai-frameworks/

[^1_31]: https://replit.com/discover/claude-code-alternative

[^1_32]: https://aider.chat

[^1_33]: https://www.reddit.com/r/ClaudeAI/comments/1khc9dw/alternatives_for_claude_code_codex_that_i_can_use/

[^1_34]: https://dev.to/therealmrmumba/10-claude-code-alternatives-that-every-developer-must-use-4ffd

[^1_35]: https://www.reddit.com/r/ArtificialInteligence/comments/1bn97n2/i_built_a_foss_project_management_tool_with/

[^1_36]: https://www.reddit.com/r/ChatGPTCoding/comments/1n4resg/cli_alternatives_to_claude_code_and_codex/

[^1_37]: https://dev.to/forgecode/top-10-open-source-cli-coding-agents-you-should-be-using-in-2025-with-links-244m

[^1_38]: https://www.reddit.com/r/LocalLLM/comments/1macf0n/claude_code_alternative_recommendations/

[^1_39]: https://www.qodo.ai/blog/claude-code-alternatives/

[^1_40]: https://jimmysong.io/ai/goose/

[^1_41]: https://block.github.io/goose/docs/goose-architecture/

[^1_42]: https://www.reddit.com/r/ClaudeAI/comments/1j9p7uf/forge_a_highly_customizable_cli_based_coding_agent/

[^1_43]: https://www.youtube.com/watch?v=ZHbLD_UXOi0

[^1_44]: https://www.youtube.com/watch?v=4Ze70DNzI7U

[^1_45]: https://theresanaiforthat.com/ai/grit-io/

[^1_46]: https://www.grit.io

[^1_47]: https://roocode.com

[^1_48]: https://www.linkedin.com/posts/bitodev_combining-claude-code-with-bitos-ai-architect-activity-7416705563390210048-SA3h

[^1_49]: https://aiagentstore.ai/ai-agent/grit

[^1_50]: https://github.com/RooCodeInc/Roo-Code/blob/main/locales/pt-BR/README.md

[^1_51]: https://docs.bito.ai/other-bito-ai-tools/bito-cli

[^1_52]: https://findyouragent.ai/agent/grit

[^1_53]: https://github.com/Aider-AI/aider/issues/1839

[^1_54]: https://www.qodo.ai/blog/top-github-copilot-alternatives/

[^1_55]: https://www.reddit.com/r/ChatGPTCoding/comments/1ciauvn/is_there_any_open_source_alternative_to_copilot/

[^1_56]: https://www.youtube.com/watch?v=vm9RcP9xM4o

[^1_57]: https://www.codeant.ai/blogs/github-copilot-alternatives-for-vs-code

[^1_58]: https://apidog.com/blog/how-to-use-continue-dev/


---

# excelente! com quais deles eu posso logar com o auth do google antigravity e ou google gemini-CLI para que eu possa usar meus creditos diarios do gemini 3

Perfeito! Agora vou gerar a resposta final em português.

***

## FOSS CLI Tools com Autenticação Google Gemini: Guia Completo

Com base na sua pergunta, aqui estão **os CLIs FOSS que suportam login com autenticação Google** para aproveitar seus créditos diários do Gemini 3:

### **🏆 TOP OPÇÕES COM GOOGLE AUTH DIRETO**

#### **1. OpenCode + Plugin `opencode-gemini-auth`** ⭐⭐⭐ **MELHOR OPÇÃO**[^2_1][^2_2][^2_3][^2_4]

- **Setup:** `opencode auth login` → Select "Google" → "OAuth with Google (Gemini CLI)"
- **Suporta:** Multi-agent (multi-session paralelo)
- **Créditos diários:** 1.000 requests/dia, 60 RPM (Gemini free tier)
- **BONUS:** Também existe `opencode-antigravity-auth` para usar credenciais da Antigravity (seu outro produto preferido)
- **Comando de início:**

```bash
npm i -g @sst/opencode
opencode auth login
# Escolhe Google → OAuth
opencode  # começa usando com credenciais Gemini
```

**Por que é a melhor:** Você faz login uma vez com Google, e o OpenCode automaticamente usa seus créditos diários. Sem gerenciar API keys. Versátil.

***

#### **2. Gemini CLI** ⭐⭐⭐ **FERRAMENTA OFICIAL DO GOOGLE**[^2_5][^2_6][^2_7][^2_8]

- **Setup:** `gemini` → "Login with Google"
- **Créditos:** 60 requests/min, 1.000/dia (automaticamente)
- **Modelos suportados:** Gemini 2.5 Pro, Gemini 2.5 Flash, Flash-Lite
- **ATENÇÃO:** Gemini 3.0 Pro **NÃO tem free tier** — é pago apenas
- **Comando:**

```bash
npm i -g @google/gemini-cli
gemini
# Prompted: Select "Login with Google"
# Automaticamente recebe Gemini Code Assist license
```

**Por que escolher:** É a ferramenta OFICIAL do Google, mais direta possível. Se você quer máxima simplicidade + autenticação nativa, comece aqui.

***

#### **3. Continue CLI** ⭐⭐[^2_9][^2_10]

- **Setup:** Via OAuth + MCP integrations
- **Suporta:** Modular agent loop extensível
- **Créditos:** Mesmos do Gemini free tier
- **Vantagem:** Extensível via MCP, você pode criar agent rules customizadas

***

### **⚠️ OPÇÕES COM API KEY (NÃO OAuth "Login with Google")**

Se você preferir não fazer login interativo:

#### **4. Plandex**[^2_11][^2_12]

- **Requer:** `GEMINI_API_KEY` (obter em https://aistudio.google.com/apikey)
- **Não tem:** Direct "Login with Google" nativo
- **Mas:** Funciona com os mesmos créditos diários do Gemini free tier
- **Setup:**

```bash
export GEMINI_API_KEY="sua-chave-de-ai-studio"
plandex
# Seleciona Gemini model no REPL
```


#### **5. Aider**[^2_13][^2_14]

- **Requer:** `GEMINI_API_KEY` (mesmo caminho)
- **Não tem:** OAuth direto
- **Upgrade:** Pode usar MCP (mcpm-aider) para orchestration multi-agent
- **Setup:**

```bash
export GEMINI_API_KEY="sua-chave"
aider --model gemini-2.5-pro
```


#### **6. ForgeCode**[^2_15]

- **Suporta:** "Sign in with Google"
- **Mas:** Ainda precisa de API key para os modelos
- **Setup:** Browser auth + depois configurar Gemini key

***

### **❌ SEM SUPORTE GOOGLE AUTH**

- **Goose:** Apenas API Key (sem Google auth)
- **tlm:** Apenas modelos locais via Ollama
- **GPT-CLI:** Sem suporte a Google

***

### **📊 COMPARAÇÃO: GEMINI FREE TIER QUOTAS (Jan 2026)**[^2_7][^2_16][^2_17]

| Item | Limite |
| :-- | :-- |
| **Requests por minuto** | 60 RPM |
| **Requests por dia** | 1.000/dia |
| **Modelos free** | Gemini 2.5 Pro, Flash, Flash-Lite |
| **Gemini 3.0 Pro** | ❌ PAGO APENAS |
| **Context window** | 1M tokens |
| **Reset** | Meia-noite (Pacific Time) |


***

### **🎯 MINHA RECOMENDAÇÃO PARA VOCÊ**

Dado que você quer aproveitar os créditos diários do Gemini **E** tem interesse em Antigravity:

**1. Use `OpenCode + opencode-gemini-auth` (primeira escolha)**

- Login Google direto
- Multi-agent paralelo nativo
- Suporta Antigravity via `opencode-antigravity-auth`
- Sem gerenciar múltiplas chaves

**2. Como fallback: Gemini CLI direto**

- Mais simples possível
- Ferramenta oficial
- Apenas para testing/quick use

**3. Para Antigravity + Gemini 3 Pro:**

```bash
opencode auth login
# Seleciona: Google → OAuth with Google (Antigravity)
opencode
# Agora tem acesso ao tier Antigravity com Gemini 3 Pro
```


***

### **⚡ QUICK START (30 segundos)**

```bash
# Opção 1: OpenCode (recomendado)
npm i -g @sst/opencode
opencode auth login
# Escolhe Google
opencode

# Opção 2: Gemini CLI (mais direto)
npm i -g @google/gemini-cli
gemini
```

Isso é tudo! Você terá acesso automático aos seus 1.000 requests diários do Gemini.
<span style="display:none">[^2_18][^2_19][^2_20][^2_21][^2_22][^2_23][^2_24][^2_25][^2_26][^2_27][^2_28][^2_29][^2_30][^2_31][^2_32][^2_33][^2_34][^2_35][^2_36][^2_37][^2_38][^2_39][^2_40][^2_41]</span>

<div align="center">⁂</div>

[^2_1]: https://github.com/jenslys/opencode-gemini-auth

[^2_2]: https://libraries.io/npm/opencode-gemini-auth

[^2_3]: https://libraries.io/npm/@spmurrayzzz%2Fopencode-gemini-auth

[^2_4]: https://github.com/NoeFabris/opencode-antigravity-auth

[^2_5]: https://geminicli.com/docs/get-started/authentication/

[^2_6]: https://google-gemini.github.io/gemini-cli/docs/get-started/authentication.html

[^2_7]: https://codelabs.developers.google.com/gemini-cli-hands-on

[^2_8]: https://milvus.io/ai-quick-reference/how-do-i-authenticate-with-google-to-use-gemini-cli

[^2_9]: https://docs.continue.dev/guides/cli

[^2_10]: https://docs.continue.dev/cli/overview

[^2_11]: https://docs.plandex.ai/models/custom-models

[^2_12]: https://docs.plandex.ai/models/model-providers/

[^2_13]: https://aider.chat/docs/llms/gemini.html

[^2_14]: https://aider.chat/docs/config/api-keys.html

[^2_15]: https://forgecode.dev/blog/forge-v0.98.0-release-article/

[^2_16]: https://www.aifreeapi.com/en/posts/google-gemini-api-free-tier

[^2_17]: https://www.aifreeapi.com/en/posts/gemini-api-pricing-and-quotas

[^2_18]: https://gemini-cli-docs.pages.dev/cli/authentication

[^2_19]: https://ai.google.dev/gemini-api/docs/oauth

[^2_20]: https://www.youtube.com/watch?v=BKT1CyXrfks

[^2_21]: https://block.github.io/goose/docs/getting-started/providers/

[^2_22]: https://google-gemini.github.io/gemini-cli/docs/cli/authentication.html

[^2_23]: https://docs.n8n.io/integrations/builtin/credentials/googleai/

[^2_24]: https://docs.cloud.google.com/gemini/enterprise/docs/authentication

[^2_25]: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start/gcp-auth

[^2_26]: https://github.com/sst/opencode/issues/447

[^2_27]: https://ai.google.dev/gemini-api/docs/oauth?hl=ko

[^2_28]: https://github.com/aider-ai/aider/issues/4283

[^2_29]: https://www.reddit.com/r/Bard/comments/1o1mjde/question_about_oauth_access_token_with_gemini_ai/

[^2_30]: https://github.com/antinomyhq/forge

[^2_31]: https://git.doit.wisc.edu/czhao255/main/-/blob/main/aider_intro/Introduction%20To%20Aider.md

[^2_32]: https://docs.cloud.google.com/gemini/enterprise/docs/gcal/config

[^2_33]: https://developers.google.com/gemini-code-assist/auth/auth_success_gemini

[^2_34]: https://www.reddit.com/r/ChatGPTCoding/comments/1jrp1tj/a_simple_guide_to_setting_up_gemini_25_pro_free/

[^2_35]: https://www.reddit.com/r/Bard/comments/1p0geij/how_much_free_quota_a_user_get_for_gemini_30_pro/

[^2_36]: https://www.youtube.com/watch?v=FzpHJXYWonY

[^2_37]: https://www.glbgpt.com/hub/gemini-3-pro-preview-limits-the-ultimate-guide-to-quotas-tokens-hidden-caps-2025/

[^2_38]: https://docs.plandex.ai/cli-reference/

[^2_39]: https://www.gamsgo.com/blog/google-gemini-free

[^2_40]: https://docs.plandex.ai/cli-reference

[^2_41]: https://www.youtube.com/watch?v=lFPhOtelrkE


---

# show. me explique como instalar no opencode:

1 - plugin pra logar no gemini
2 - mcps
3 - skills
4 - subagents

Perfeito! Agora tenho todas as informações necessárias. Vou criar um guia completo de instalação.

## OpenCode: Guia Completo de Instalação e Configuração

Aqui está o passo a passo completo para instalar e configurar os 4 componentes no OpenCode:

***

### **1. PLUGIN PARA LOGAR NO GEMINI** 🔐

#### **Instalação do `opencode-gemini-auth`**[^3_1][^3_2]

**Passo 1:** Instale o OpenCode CLI

```bash
npm i -g @sst/opencode
```

**Passo 2:** Adicione o plugin ao arquivo de configuração

Edite o arquivo `~/.config/opencode/config.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": ["opencode-gemini-auth@latest"]
}
```

**Passo 3:** Execute o comando de autenticação

```bash
opencode auth login
```

**Passo 4:** Selecione as opções:

- Escolha: **Google**
- Depois: **OAuth with Google (Gemini CLI)**
- Uma janela do browser abrirá para você aprovar o acesso
- O plugin cria um servidor local temporário para capturar o callback
- Se falhar (porta ocupada ou ambiente headless), você pode colar manualmente a URL de callback ou o authorization code

**Passo 5:** Inicie o OpenCode

```bash
opencode
```

Agora você está usando seus créditos diários do Gemini!

#### **Atualização do Plugin**

OpenCode não atualiza plugins automaticamente. Para atualizar:

```bash
# Limpar cache do plugin específico
rm -rf ~/.cache/opencode/node_modules/opencode-gemini-auth

# Rodar OpenCode para reinstalar
opencode
```


***

### **2. MCPs (Model Context Protocol Servers)** 🔌

#### **Adicionar MCP Server via CLI**[^3_3][^3_4][^3_5]

**Comando interativo:**

```bash
opencode mcp add
```

O CLI vai guiar você através de perguntas:

**Exemplo 1: MCP Remoto (Svelte Docs)**

```bash
opencode mcp add

┌ Add MCP server
│
◇ Enter MCP server name
│ svelte
│
◇ Select MCP server type
│ Remote
│
◇ Enter MCP server URL
│ https://mcp.svelte.dev/mcp
```

**Exemplo 2: MCP Local (Context7 - Developer Docs)**

```bash
opencode mcp add context7 -- npx -y @upstash/context7-mcp
```

**Exemplo 3: MCP com variáveis de ambiente**

```bash
opencode mcp add <server-name> \
  --env VAR1=VALUE1 \
  --env VAR2=VALUE2 \
  -- <comando-do-servidor>
```


#### **Configuração Manual no Config File**[^3_4]

Edite `~/.config/opencode/config.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "svelte-docs": {
      "type": "remote",
      "url": "https://mcp.svelte.dev/mcp",
      "enabled": true
    },
    "context7": {
      "type": "local",
      "command": ["npx", "-y", "@upstash/context7-mcp"],
      "enabled": true,
      "timeout": 5000
    },
    "custom-mcp": {
      "type": "local",
      "command": ["node", "/path/to/mcp-server.js"],
      "environment": {
        "API_KEY": "your-key",
        "DEBUG": "true"
      },
      "enabled": true
    }
  }
}
```


#### **Opções de Configuração (Local MCP)**[^3_4]

| Opção | Tipo | Obrigatório | Descrição |
| :-- | :-- | :-- | :-- |
| `type` | String | ✅ | Tipo de conexão MCP, deve ser `"local"` |
| `command` | Array | ✅ | Comando e argumentos para rodar o servidor |
| `environment` | Object | ❌ | Variáveis de ambiente |
| `enabled` | Boolean | ❌ | Habilitar/desabilitar no startup |
| `timeout` | Number | ❌ | Timeout em ms (padrão: 5000) |

#### **Comandos úteis**

**Listar MCPs configurados:**

```bash
opencode mcp list
# ou versão curta
opencode mcp ls
```

**Autenticar com MCP OAuth:**

```bash
opencode mcp auth <server-name>
# ou sem nome para selecionar interativamente
opencode mcp auth
```

**Listar MCPs OAuth-capable:**

```bash
opencode mcp auth --list
```


***

### **3. SKILLS (Habilidades Reutilizáveis)** 🎯

#### **Sistema Nativo de Skills (Built-in)**[^3_6]

OpenCode tem suporte **nativo** para skills desde a versão mais recente. Skills são descobertos automaticamente via o tool `skill`.

**Estrutura de Diretórios:**

Skills podem estar em dois lugares:

1. **Global:** `~/.config/opencode/skill/*/SKILL.md`
2. **Projeto:** `.opencode/skill/*/SKILL.md` (no diretório do projeto)
3. **Claude-compatible:** `.claude/skills/*/SKILL.md`

#### **Criar uma Skill (Exemplo)**[^3_6]

**Passo 1:** Crie o diretório

```bash
mkdir -p .opencode/skill/git-release
```

**Passo 2:** Crie o arquivo `.opencode/skill/git-release/SKILL.md`

```markdown
---
name: git-release
description: Automate git release workflow with semantic versioning
---

# Git Release Skill

This skill helps create semantic version releases.

## Steps:
1. Check current version in package.json
2. Suggest next version (major/minor/patch)
3. Update package.json
4. Create git tag
5. Push tag to origin

## Usage:
Call this skill when user asks to "create a release" or "bump version"
```

**Passo 3:** Reinicie o OpenCode

```bash
opencode
```

**Passo 4:** Invocar a skill

O agente verá a skill disponível automaticamente e pode invocá-la:

```
"Can you load the git-release skill?"
```

Ou explicitamente via tool call:

```
skill tool → skill_name: "git-release"
```


#### **Plugin Alternativo: `opencode-skills`**[^3_7][^3_8]

Para compatibilidade **1:1 com Anthropic Skills** + nested skills:

**Instalação:**

```json
{
  "plugin": ["opencode-skills"]
}
```

**Estrutura:**

```bash
.opencode/skills/my-skill/SKILL.md
```

**Formato do SKILL.md:**

```markdown
---
name: my-skill
description: A custom skill that assists with specific tasks
---

# My Skill

Your skill instructions go here...
```

**Invocação:**

```
skills_my_skill  # formato: skills_<nome-da-skill>
```


***

### **4. SUBAGENTS (Agentes Paralelos)** 🤖🤖🤖

OpenCode tem suporte nativo para subagents via o **Task tool**.

#### **Como Funciona**[^3_9][^3_10][^3_11]

1. O agente principal usa o **Task tool** para spawnar subagents
2. Cada subagent roda em uma **session separada**
3. Subagents podem spawnar seus próprios subagents (nested)
4. Cada subagent tem seu próprio contexto, tools e system prompt

#### **Configurar Subagents**[^3_11]

**Opção 1: Definir via arquivo JSON**

Crie `.opencode/agents/code_reviewer.json`:

```json
{
  "name": "code_reviewer",
  "description": "Specialist in code review and best practices",
  "systemPrompt": "You are a senior code reviewer. Focus on: readability, performance, security, and maintainability.",
  "tools": ["read", "list", "search"],
  "permissions": {
    "write": false,
    "execute": false
  }
}
```

**Opção 2: Definir via Markdown (Claude-compatible)**

Crie `.opencode/agents/code_reviewer.md`:

```markdown
---
name: code-reviewer
description: Specialist in code review and best practices
tools: [read, list, search]
permissions:
  write: false
  execute: false
---

# Code Reviewer Agent

You are a senior code reviewer...
```


#### **Invocar Subagents**[^3_12][^3_13][^3_11]

**Método 1: Via Task Tool (Automático)**

O agente principal usa o Task tool internamente:

```
"Spawn 3 subagents: one for frontend, one for backend, one for testing"
```

OpenCode automaticamente:

- Cria 3 sessions paralelas
- Cada uma com seu próprio contexto
- Retorna resultados consolidados

**Método 2: Via @ Mention**

```
"@code-reviewer please review the latest PR"
```

**Método 3: Via Custom Command**

Crie `.opencode/commands/parallel-test.md`:

```markdown
---
name: parallel-test
description: Run parallel test implementation
---

Coordinate testing workflow using multiple parallel @test-writer subagents to implement test scripts.
```

Invocação:

```bash
opencode /parallel-test api endpoints
```


#### **Plugin: `op-sessions` (Multi-Agent Workflows)**[^3_13]

Para workflows multi-agent avançados:

**Instalação:**

```json
{
  "plugin": ["op-sessions"]
}
```

**4 modos de operação:**

1. **Fork Mode:** Spawna sessions paralelas para explorar diferentes abordagens
```
"Fork this conversation into 3 parallel sessions: one for microservices, one for serverless, one for modular monolith"
```

2. **Message Mode:** Handoff de trabalho entre agentes primários (ex: implementation → review)
3. **New Mode:** Inicia sessions frescas para transições de fase (research → planning → implementation)
4. **Compact Mode:** Comprime histórico de conversação quando atinge token limits

#### **Navegar entre Sessions de Subagents**[^3_9]

Quando subagents criam child sessions, navegue entre eles:

**Teclado:**

- `<Leader> + Right` (ou `session_child_cycle`): Avança parent → child1 → child2 → ... → parent
- `<Leader> + Left` (ou `session_child_cycle_reverse`): Volta parent ← child1 ← child2

**CLI:**

```bash
# Listar sessions ativas
opencode sessions list

# Trocar para session específica
opencode sessions switch <session-id>
```


#### **Best Practices para Subagents**[^3_14]

1. **Use um Manager Agent:**
    - Manager delega tarefas para specialists
    - Specialists recebem subset restrito de tools
2. **Restrinja Tools por Subagent:**
    - Code reviewers: apenas `read`, `list`, `search` (sem `write`)
    - Testers: `read`, `execute`, `write` em diretórios específicos
    - Implementers: full toolset
3. **Defina Papéis Claros:**
```json
{
  "agents": {
    "manager": {
      "tools": ["task", "read", "list"],
      "description": "Orchestrates work between specialists"
    },
    "frontend-dev": {
      "tools": ["read", "write", "execute"],
      "permissions": {
        "paths": ["src/frontend/**"]
      }
    },
    "backend-dev": {
      "tools": ["read", "write", "execute"],
      "permissions": {
        "paths": ["src/backend/**", "api/**"]
      }
    }
  }
}
```


***

## **RESUMO: Configuração Completa**

### **Arquivo `~/.config/opencode/config.json` Completo:**

```json
{
  "$schema": "https://opencode.ai/config.json",
  
  "plugin": [
    "opencode-gemini-auth@latest",
    "opencode-skills",
    "op-sessions"
  ],
  
  "mcp": {
    "context7": {
      "type": "local",
      "command": ["npx", "-y", "@upstash/context7-mcp"],
      "enabled": true
    },
    "svelte-docs": {
      "type": "remote",
      "url": "https://mcp.svelte.dev/mcp",
      "enabled": true
    }
  },
  
  "agents": {
    "code_reviewer": {
      "description": "Code review specialist",
      "tools": ["read", "list", "search"],
      "permissions": {
        "write": false
      }
    },
    "test-writer": {
      "description": "Test implementation specialist",
      "tools": ["read", "write", "execute"],
      "permissions": {
        "paths": ["tests/**", "src/**/*.test.ts"]
      }
    }
  }
}
```


### **Estrutura de Diretórios:**

```
~/.config/opencode/
├── config.json
├── skill/
│   ├── git-release/
│   │   └── SKILL.md
│   └── api-design/
│       └── SKILL.md
└── agents/
    ├── code_reviewer.json
    └── test-writer.json

projeto/
└── .opencode/
    ├── skill/
    │   └── project-specific/
    │       └── SKILL.md
    ├── agents/
    │   └── frontend-specialist.md
    └── commands/
        └── parallel-test.md
```


### **Quick Start (3 comandos):**

```bash
# 1. Instalar + configurar auth
npm i -g @sst/opencode
echo '{"plugin":["opencode-gemini-auth@latest"]}' > ~/.config/opencode/config.json
opencode auth login

# 2. Adicionar MCP
opencode mcp add context7 -- npx -y @upstash/context7-mcp

# 3. Criar primeira skill
mkdir -p .opencode/skill/my-skill
cat << 'EOF' > .opencode/skill/my-skill/SKILL.md
---
name: my-skill
description: My first skill
---
# My Skill
Instructions here...
EOF

# 4. Start!
opencode
```


***

Agora você tem:
✅ **Gemini auth** configurado (1.000 requests/dia grátis)
✅ **MCPs** para ferramentas externas
✅ **Skills** reutilizáveis
✅ **Subagents** para workflows paralelos
<span style="display:none">[^3_15][^3_16][^3_17][^3_18][^3_19][^3_20][^3_21][^3_22][^3_23][^3_24][^3_25][^3_26][^3_27][^3_28]</span>

<div align="center">⁂</div>

[^3_1]: https://github.com/jenslys/opencode-gemini-auth

[^3_2]: https://libraries.io/npm/opencode-gemini-auth

[^3_3]: https://opencode.ai/docs/cli/

[^3_4]: https://opencode.ai/docs/mcp-servers/

[^3_5]: https://svelte.dev/docs/mcp/remote-setup

[^3_6]: https://opencode.ai/docs/skills/

[^3_7]: https://www.reddit.com/r/opencodeCLI/comments/1ob1h4z/i_built_an_opencode_plugin_for_anthropicstyle/

[^3_8]: https://www.reddit.com/r/ClaudeAI/comments/1obb9fu/i_built_an_opencode_plugin_for_anthropicstyle/

[^3_9]: https://opencode.ai/docs/agents/

[^3_10]: https://cefboud.com/posts/coding-agents-internals-opencode-deepdive/

[^3_11]: https://github.com/sst/opencode/issues/1293

[^3_12]: https://github.com/sst/opencode/issues/6183

[^3_13]: https://www.reddit.com/r/opencodeCLI/comments/1ojlu01/i_built_an_opencode_plugin_for_multiagent/

[^3_14]: https://www.reddit.com/r/opencodeCLI/comments/1oyp9bi/opencode_agentsubagentcommand_best_practices/

[^3_15]: https://libraries.io/npm/opencode-gemini-cli-auth

[^3_16]: https://github.com/NoeFabris/opencode-antigravity-auth

[^3_17]: https://dev.opencode.ai/docs/cli/

[^3_18]: https://developers.openai.com/codex/mcp/

[^3_19]: https://github.com/sst/opencode/issues/1216

[^3_20]: https://github.com/anthropics/claude-code/issues/5032

[^3_21]: https://www.reddit.com/r/ClaudeAI/comments/1m00mhb/claudegeminicliopencode/

[^3_22]: https://github.com/sst/opencode/issues/6573

[^3_23]: https://docs.openhands.dev/sdk/guides/agent-delegation

[^3_24]: https://github.com/sst/opencode/issues/2352

[^3_25]: https://github.com/sst/opencode/issues/5734

[^3_26]: https://github.com/anomalyco/opencode/issues/1293

[^3_27]: https://github.com/awesome-opencode/awesome-opencode

[^3_28]: https://www.youtube.com/watch?v=EOIzFMdmox8


---

## ❌ PROBLEMAS ENCONTRADOS NO SEU CONFIG.JSON

### **1. ERRO CRÍTICO: Falta de vírgula após `"plugin"`**

```json
❌ ERRADO:
"plugin": ["opencode-gemini-auth@latest"]
"mcp": {

✅ CORRETO:
"plugin": ["opencode-gemini-auth@latest"],
"mcp": {
```

**Isso vai quebrar o parse JSON inteiro.**

***

### **2. FORMATO INCORRETO DOS MCPs**

Seu config usa um formato **antigo/incorreto**. O schema atual exige:

**❌ ERRADO (seu formato):**

```json
"deepwiki": {
  "serverUrl": "https://mcp.deepwiki.com/mcp"
}
```

**✅ CORRETO (novo formato):**

```json
"deepwiki": {
  "type": "remote",
  "url": "https://mcp.deepwiki.com/mcp",
  "enabled": true
}
```

**Problemas específicos:**


| Seu config | Correto |
| :-- | :-- |
| `serverUrl` → ❌ | `type` + `url` → ✅ |
| Sem `type` indicando se é local/remote | Precisa `"type": "local"` ou `"type": "remote"` |
| `command` e `args` separados | Precisa ser array único: `"command": ["npx", "-y", "pacote"]` |
| Falta `environment` como object | Precisa: `"environment": { "KEY": "value" }` |


***

### **3. SEU CONFIG REFORMATADO + PLUGINS**

Aqui está a versão **corrigida e com os plugins que sugeri**:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "plugin": [
    "opencode-gemini-auth@latest",
    "opencode-skills",
    "op-sessions"
  ],
  "mcp": {
    "context7": {
      "type": "local",
      "command": ["npx", "-y", "@upstash/context7-mcp"],
      "environment": {
        "CONTEXT7_API_KEY": "Yctx7sk-c7fd22ce-7547-41d2-87bd-b64a13239abe"
      },
      "enabled": true
    },
    "serena": {
      "type": "local",
      "command": [
        "uvx",
        "--from",
        "git+https://github.com/oraios/serena",
        "serena",
        "start-mcp-server",
        "--context",
        "ide-assistant"
      ],
      "enabled": true
    },
    "vibe-check": {
      "type": "local",
      "command": ["npx", "-y", "@pv-bhat/vibe-check-mcp", "start", "--stdio"],
      "environment": {
        "GEMINI_API_KEY": "AIzaSyB4xwJHUA2L7UaeipPAhzfks3MZ5zWVuK4"
      },
      "enabled": true
    },
    "think-tank": {
      "type": "local",
      "command": ["npx", "-y", "mcp-think-tank@2.0.7"],
      "environment": {
        "MEMORY_PATH": "/home/sephiroth/YUICHI/00-VIVI/.agents/memory.jsonl",
        "EXA_API_KEY": "7f184e67-1ba4-4952-b9d9-a096989880c6"
      },
      "enabled": true
    },
    "mult-fetch": {
      "type": "local",
      "command": ["npx", "-y", "@lmcc-dev/mult-fetch-mcp-server"],
      "enabled": true
    },
    "desktop-commander": {
      "type": "local",
      "command": ["npx", "-y", "@wonderwhy-er/desktop-commander@latest"],
      "enabled": true
    },
    "deepwiki": {
      "type": "remote",
      "url": "https://mcp.deepwiki.com/mcp",
      "enabled": true
    }
  },
  "agent": {
    "build": {
      "model": "google/gemini-2.5-pro"
    },
    "code_reviewer": {
      "mode": "subagent",
      "description": "Code review specialist"
    },
    "test-writer": {
      "mode": "subagent",
      "description": "Test implementation specialist"
    }
  }
}
```


***

## 📝 MUDANÇAS FEITAS

### **Plugins adicionados:**

```json
"plugin": [
  "opencode-gemini-auth@latest",      // ✅ Login com Google Gemini
  "opencode-skills",                   // ✅ Sistema de skills reutilizáveis
  "op-sessions"                        // ✅ Multi-agent parallel workflows
]
```


### **MCPs reformatados:**

| MCP | Antes | Depois |
| :-- | :-- | :-- |
| **context7** | Faltava `type` | Agora: `"type": "local"` + `"command"` array |
| **deepwiki** | `serverUrl` (❌) | Agora: `"type": "remote"` + `"url"` |
| **serena** | `args` separado | Agora: `"command"` com tudo junto |
| **vibe-check** | `--stdio` solto | Agora: dentro do array `command` |
| **think-tank** | ✅ Estrutura OK | Refatorado para novo formato |


***

## 🔧 COMO USAR O CONFIG CORRIGIDO

**Passo 1:** Abra o arquivo de config

```bash
nano ~/.config/opencode/config.json
```

**Passo 2:** Cole todo o JSON corrigido acima

**Passo 3:** Verifique com `opencode`

```bash
opencode
```

Se houver erro de sintaxe, ele vai avisar qual linha.

**Passo 4:** Verificar plugins instalados

```bash
opencode plugin list
```

**Passo 5:** Autenticar com Gemini

```bash
opencode auth login
# Seleciona: Google → OAuth with Google (Gemini CLI)
```


***

## ⚠️ OBSERVAÇÕES CRÍTICAS

### **API Keys no Config (PERIGO!)**

Você tem API keys expostas no JSON:

```json
"GEMINI_API_KEY": "AIzaSyB4xwJHUA2L7UaeipPAhzfks3MZ5zWVuK4"
"CONTEXT7_API_KEY": "Yctx7sk-c7fd22ce-7547-41d2-87bd-b64a13239abe"
"EXA_API_KEY": "7f184e67-1ba4-4952-b9d9-a096989880c6"
```

**Melhor abordagem:** Use variáveis de ambiente:

```bash
# ~/.bashrc ou ~/.zshrc
export GEMINI_API_KEY="AIzaSyB4xwJHUA2L7UaeipPAhzfks3MZ5zWVuK4"
export CONTEXT7_API_KEY="Yctx7sk-c7fd22ce-7547-41d2-87bd-b64a13239abe"
export EXA_API_KEY="7f184e67-1ba4-4952-b9d9-a096989880c6"
```

Depois no config:

```json
"environment": {
  "GEMINI_API_KEY": "$GEMINI_API_KEY"
}
```

E no terminal: `source ~/.bashrc && opencode`

***

## 📊 VALIDAÇÃO RÁPIDA

Para validar seu JSON antes de usar:

```bash
# Via jq
jq . ~/.config/opencode/config.json

# Via Python
python3 -m json.tool ~/.config/opencode/config.json
```

Se retornar sem erros, está tudo certo!

***

Pronto! Seu config agora está:
✅ Sintaxe corrigida
✅ Plugins para Gemini auth adicionados
✅ MCPs no formato correto
✅ Agents para subagents configurados
✅ Skills e sessions habilitadas
<span style="display:none">[^4_1]</span>

<div align="center">⁂</div>

[^4_1]: https://opencode.ai/config.json

