# Scan Report: feiskyer-claude-code-settings

**Repository**: https://github.com/feiskyer/claude-code-settings  
**Scan Date**: 2026-01-18  
**Recycler ID**: 30

## Overview

This repository is a comprehensive Claude Code configuration collection focused on "vibe coding" - a workflow-driven approach to development. It contains agents, custom commands, skills (as plugins), and various provider settings.

---

## Assets Inventory

### 1. AGENTS (7 total)

#### High Quality Agents

1. **pr-reviewer.md**
   - **Type**: Agent
   - **Quality**: ⭐⭐⭐⭐⭐ Excellent
   - **Description**: Expert code reviewer for GitHub PRs with thorough analysis workflow
   - **Features**:
     - Structured review process (selection → info gathering → analysis → feedback)
     - Focus areas: correctness, conventions, performance, tests, security
     - Uses GitHub API for posting line-specific comments
     - Clear output format (Critical/Important/Minor)
   - **Tools**: Write, Read, LS, Glob, Grep, Bash(gh:*), Bash(git:*)

2. **github-issue-fixer.md**
   - **Type**: Agent
   - **Quality**: ⭐⭐⭐⭐⭐ Excellent
   - **Description**: Complete GitHub issue resolution workflow specialist
   - **Features**:
     - 4-phase workflow: PLAN → CREATE → TEST → OPEN PR
     - Includes research and context gathering
     - Proper git branching and PR creation
     - Comprehensive testing (UI via Puppeteer, unit, full suite)
   - **Tools**: Write, Read, LS, Glob, Grep, Bash(gh:*), Bash(git:*)

3. **deep-reflector.md**
   - **Type**: Agent
   - **Quality**: ⭐⭐⭐⭐⭐ Excellent
   - **Description**: Session analysis and learning capture specialist
   - **Features**:
     - Comprehensive analysis framework (8 sections)
     - Extracts patterns, preferences, system understanding
     - Generates actionable items for CLAUDE.md updates
     - Builds cumulative knowledge
   - **Tools**: Not specified (general tools)

4. **ui-engineer.md**
   - **Type**: Agent
   - **Quality**: ⭐⭐⭐⭐ Very Good
   - **Description**: Expert frontend/UI developer agent
   - **Features**:
     - Modern frontend expertise (React, Vue, Angular, etc.)
     - Code quality standards (TypeScript, SOLID principles)
     - Backend-agnostic component design
     - Accessibility and performance focus
   - **Tools**: Read, Write, Edit, MultiEdit, LS, Glob, Grep, Bash, WebFetch

5. **instruction-reflector.md**
   - **Type**: Agent
   - **Quality**: ⭐⭐⭐⭐ Very Good
   - **Description**: Analyzes and improves Claude Code instructions
   - **Features**:
     - 5-phase process: Analysis → Documentation → Interaction → Implementation → Output
     - Uses TodoWrite for tracking improvements
     - Structured output with analysis/improvements/final instructions

6. **insight-documenter.md**
   - **Type**: Agent
   - **Quality**: ⭐⭐⭐ Good
   - **Description**: Technical breakthrough documentation specialist

7. **command-creator.md**
   - **Type**: Agent
   - **Quality**: ⭐⭐⭐⭐ Very Good
   - **Description**: Expert at creating new Claude Code custom commands
   - **Features**:
     - 4-step process: Analysis → Planning → Implementation → QA
     - Best practices enforcement
     - Proper YAML frontmatter validation

---

### 2. COMMANDS (11 total)

#### Analysis & Reflection Commands

1. **think-harder.md**
   - **Type**: Command
   - **Quality**: ⭐⭐⭐⭐⭐ Excellent
   - **Description**: Enhanced analytical thinking for complex problems
   - **Features**:
     - 4-phase methodology: Clarification → Multi-dimensional analysis → Critical evaluation → Synthesis
     - Structured output format (6 sections)
     - Focused on showing reasoning process

2. **think-ultra.md**
   - **Type**: Command
   - **Quality**: ⭐⭐⭐⭐ Very Good
   - **Description**: Ultra-comprehensive analysis (presumably extends think-harder)

3. **reflection.md**
   - **Type**: Command
   - **Quality**: ⭐⭐⭐⭐⭐ Excellent
   - **Description**: Analyze and improve Claude Code instructions
   - **Features**:
     - Analyzes chat history for instruction improvements
     - Interactive approval process
     - Updates CLAUDE.md with approved changes
   - **Tools**: Read, Edit, TodoWrite, Bash(git:*)

4. **reflection-harder.md**
   - **Type**: Command
   - **Quality**: ⭐⭐⭐⭐ Very Good
   - **Description**: Comprehensive session analysis (likely delegates to deep-reflector agent)

5. **eureka.md**
   - **Type**: Command
   - **Quality**: ⭐⭐⭐ Good
   - **Description**: Document technical breakthroughs

#### GitHub Integration Commands

6. **/gh/review-pr.md**
   - **Type**: Command
   - **Quality**: ⭐⭐⭐⭐ Very Good
   - **Description**: Comprehensive PR review with comments (likely delegates to pr-reviewer agent)

7. **/gh/fix-issue.md**
   - **Type**: Command
   - **Quality**: ⭐⭐⭐⭐ Very Good
   - **Description**: Complete issue resolution workflow (likely delegates to github-issue-fixer agent)

#### Documentation & Utilities

8. **/cc/create-command.md**
   - **Type**: Command
   - **Quality**: ⭐⭐⭐⭐ Very Good
   - **Description**: Create new Claude Code commands (likely delegates to command-creator agent)

9. **translate.md**
   - **Type**: Command
   - **Quality**: ⭐⭐⭐ Good
   - **Description**: Translate English/Japanese tech content to Chinese

---

### 3. SKILLS / PLUGINS (6 plugins)

#### Plugin 1: kiro-skill ⭐⭐⭐⭐⭐ EXCEPTIONAL

**Path**: `plugins/kiro-skill/`

**Description**: Interactive feature development workflow from idea to implementation. A comprehensive spec-driven development system.

**Quality Assessment**: This is a **gem** - extremely well-structured and comprehensive.

**Features**:
- **4-Phase Workflow**:
  1. **Requirements** (EARS format with user stories)
  2. **Design** (Architecture, components, data models)
  3. **Tasks** (Test-driven, incremental tasks)
  4. **Execute** (One task at a time with approval)
- Stores specs in `.kiro/specs/{feature-name}/`
- Explicit approval required between phases
- Minimal code philosophy
- Test-driven approach
- Kiro "personality" (warm, human, decisive)
- Research-driven design phase
- Task execution with strict one-at-a-time protocol

**Files**:
- `SKILL.md` (497 lines - comprehensive)
- `commands/kiro/design.md`
- `commands/kiro/execute.md`
- `commands/kiro/spec.md`
- `commands/kiro/task.md`
- `commands/kiro/vibe.md`
- `helpers/kiro-identity.md`
- `helpers/workflow-diagrams.md`

**Triggers**: "kiro", ".kiro/specs/", "feature spec", Chinese equivalents

---

#### Plugin 2: spec-kit-skill ⭐⭐⭐⭐⭐ EXCEPTIONAL

**Path**: `plugins/spec-kit-skill/`

**Description**: GitHub Spec-Kit integration for constitution-based spec-driven development with 7-phase workflow.

**Quality Assessment**: Another **gem** - official GitHub tooling integration with rigorous workflow.

**Features**:
- **7-Phase Workflow**:
  1. **Constitution** (governing principles)
  2. **Specify** (functional requirements)
  3. **Clarify** (max 5 questions to resolve ambiguities)
  4. **Plan** (technical strategy + data models + API contracts)
  5. **Tasks** (dependency-ordered, actionable)
  6. **Analyze** (consistency validation - read-only)
  7. **Implement** (test-driven execution)
- Integrates with GitHub Spec-Kit CLI (`specify` command)
- Stores specs in `.specify/specs/NNN-feature-name/`
- Constitution-driven decision making
- Numbered features (001, 002, etc.)
- Bash scripts for automation
- Principle: Technology-agnostic requirements

**Files**:
- `SKILL.md` (901 lines - extremely comprehensive)
- `helpers/detection-logic.md`
- `scripts/detect-phase.sh`

**Triggers**: "spec-kit", "speckit", "constitution", "specify", ".specify/"

**Prerequisites**: Python 3.11+, uv package manager, Git

---

#### Plugin 3: autonomous-skill ⭐⭐⭐⭐⭐ EXCEPTIONAL

**Path**: `plugins/autonomous-skill/`

**Description**: Long-running task automation across multiple sessions using dual-agent pattern (Initializer + Executor).

**Quality Assessment**: **Hidden gem** - sophisticated multi-session execution system.

**Features**:
- **Dual-Agent Pattern**:
  - **Initializer**: Creates task list for new tasks
  - **Executor**: Continues existing tasks
- Task isolation in `.autonomous/{task-name}/` directories
- Auto-continuation with 3-second delay
- Progress tracking via `task_list.md` and `progress.md`
- Headless Claude CLI execution
- Session-by-session progress notes
- Multiple parallel tasks supported

**Files**:
- `SKILL.md` (265 lines)
- `templates/executor-prompt.md`
- `templates/initializer-prompt.md`
- `templates/task-list-template.md`
- `scripts/run-session.sh`

**Triggers**: "autonomous", "long-running task", "multi-session", Chinese equivalents

**Requirements**: Claude CLI installed

---

#### Plugin 4: codex-skill ⭐⭐⭐⭐ VERY GOOD

**Path**: `plugins/codex-skill/`

**Description**: Leverage OpenAI Codex/GPT models for autonomous code implementation.

**Quality Assessment**: Well-documented delegation system for OpenAI models.

**Features**:
- Non-interactive automation mode
- 3 sandbox modes: read-only, workspace-write, danger-full-access
- Model selection (gpt-5, gpt-5.1, gpt-5.2, gpt-5.2-codex, etc.)
- Autonomous execution without approval prompts
- JSON output support
- Resumable sessions
- Comprehensive flag documentation

**Files**:
- `SKILL.md` (431 lines - very detailed)

**Triggers**: "codex", "use gpt", "gpt-5", "let openai", "full-auto", Chinese equivalents

**Requirements**: Codex CLI (`npm i -g @openai/codex` or `brew install codex`)

---

#### Plugin 5: nanobanana-skill ⭐⭐⭐⭐ VERY GOOD

**Path**: `plugins/nanobanana-skill/`

**Description**: Generate or edit images using Google Gemini API.

**Quality Assessment**: Useful image generation integration.

**Features**:
- Image generation with multiple aspect ratios
- Image editing capabilities
- Multiple models (gemini-3-pro-image-preview, gemini-2.5-flash-image)
- Resolution options (1K, 2K, 4K)
- Aspect ratios: square, portrait, landscape, ultra-wide

**Files**:
- `SKILL.md` (137 lines)
- `nanobanana.py` (Python script)
- `requirements.txt`

**Triggers**: "nanobanana", "generate image", "create image", "edit image", Chinese equivalents

**Requirements**: GEMINI_API_KEY, Python3 with google-genai, Pillow, python-dotenv

---

#### Plugin 6: youtube-transcribe-skill ⭐⭐⭐ GOOD

**Path**: `plugins/youtube-transcribe-skill/`

**Description**: Extract subtitles/transcripts from YouTube video links.

**Features**:
- Dual extraction methods: CLI (yt-dlp) and Browser Automation (chrome-devtools-mcp)
- Automatic subtitle language selection (zh-Hans, zh-Hant, en)
- DOM-based extraction for browser method

**Files**:
- `SKILL.md`

**Requirements**: `yt-dlp` or `chrome-devtools-mcp`

---

### 4. CONFIGURATION FILES

#### Settings Files (9 provider configurations)

Located in `settings/`:

1. **copilot-settings.json** - GitHub Copilot proxy (localhost:4141)
2. **litellm-settings.json** - LiteLLM gateway (localhost:4000)
3. **deepseek-settings.json** - DeepSeek v3.1 via Anthropic-compatible API
4. **qwen-settings.json** - Qwen models via Alibaba DashScope
5. **siliconflow-settings.json** - SiliconFlow API with Moonshot AI Kimi-K2-Instruct
6. **vertex-settings.json** - Google Cloud Vertex AI
7. **azure-settings.json** - Azure AI Anthropic-compatible endpoint
8. **azure-foundry-settings.json** - Azure AI Foundry native mode
9. **minimax.json** - MiniMax API with MiniMax-M2 model
10. **openrouter-settings.json** - OpenRouter unified API

**Quality**: ⭐⭐⭐⭐ Very Good - Comprehensive provider coverage

#### Core Config Files

1. **config.json** - Primary API key configuration
2. **.mcp.json** - MCP servers (chrome-devtools-mcp)
3. **settings.json** - Main settings file (root level)

#### Guidance Documents

Located in `guidances/`:

1. **github-copilot.md** - Guide for using Claude Code with GitHub Copilot
2. **llm-gateway-litellm.md** - Guide for LiteLLM proxy setup
3. **litellm_config.yaml** - LiteLLM proxy configuration

**Quality**: ⭐⭐⭐⭐ Very Good - Essential setup documentation

---

### 5. PLUGIN SYSTEM

**Plugin Definition Files**:
- `.claude-plugin/plugin.json` (main repo)
- `.claude-plugin/marketplace.json` (marketplace registration)
- Individual plugin.json files for each skill plugin

**Quality**: ⭐⭐⭐⭐ Very Good - Well-structured plugin architecture

---

### 6. OTHER NOTABLE FILES

1. **status-line.sh** - Status line script (likely for shell prompt)
2. **.github/copilot-instructions.md** - GitHub Copilot specific instructions
3. **README.md** - Comprehensive documentation (479 lines)
4. **LICENSE** - MIT License

---

## Hidden Gems 💎

### Top 3 Exceptional Assets:

1. **kiro-skill** (⭐⭐⭐⭐⭐)
   - Most comprehensive spec-driven workflow I've seen
   - Excellent phase separation with approval gates
   - Well-documented with personality/philosophy
   - EARS format for requirements is professional
   - Test-driven task execution

2. **spec-kit-skill** (⭐⭐⭐⭐⭐)
   - Official GitHub Spec-Kit integration
   - Constitution-based development (unique approach)
   - 7-phase rigorous workflow
   - CLI integration with bash scripts
   - Analyze phase for consistency validation

3. **autonomous-skill** (⭐⭐⭐⭐⭐)
   - Solves long-running task problem elegantly
   - Dual-agent pattern is sophisticated
   - Auto-continuation is brilliant
   - Task isolation prevents conflicts
   - Session-by-session progress tracking

### Other Notable Assets:

4. **pr-reviewer agent** - Best PR review workflow I've seen
5. **github-issue-fixer agent** - Complete issue → PR workflow
6. **deep-reflector agent** - Excellent learning capture system
7. **think-harder command** - Structured analytical thinking
8. **codex-skill** - Good OpenAI delegation pattern

---

## Code Quality Assessment

### Strengths:
- ✅ Exceptional documentation quality
- ✅ Clear workflow definitions
- ✅ Proper YAML frontmatter usage
- ✅ Comprehensive tool permissions
- ✅ Well-organized file structure
- ✅ Multiple provider support
- ✅ Plugin architecture for modularity
- ✅ Real-world use case focus

### Weaknesses:
- ⚠️ Some skills require external CLIs (codex, specify, yt-dlp)
- ⚠️ Heavy reliance on specific tools (Claude CLI for autonomous-skill)
- ⚠️ Settings files use non-standard model names (claude-sonnet-4.5, gpt-5-mini)
- ⚠️ Some Chinese language triggers/content (may not suit all users)

---

## Technical Debt / Issues

1. **Dependency on External CLIs**: Several skills require installation of external tools
2. **Claude Code Specific**: Heavily tailored to Claude Code, not easily portable
3. **Model Name Assumptions**: Settings reference models that may not exist (gpt-5-mini, claude-opus-4)
4. **API Key Management**: Multiple .env files and config locations

---

## Statistics

- **Total Agents**: 7
- **Total Commands**: 11
- **Total Skills/Plugins**: 6
- **Total Settings Files**: 10
- **Lines of Documentation**: ~2500+ lines in core skills
- **File Count**: ~90 files (excluding .git)

---

## Conclusion

This repository is a **treasure trove** of high-quality Claude Code assets, particularly the three exceptional skills (kiro, spec-kit, autonomous). The focus on workflow-driven development with proper phase separation and approval gates is professional and well-thought-out.

The repository demonstrates:
- Deep understanding of spec-driven development
- Excellent documentation practices
- Real-world workflow optimization
- Modular plugin architecture

**Recommendation**: Highly recommend adopting the core workflow skills (kiro, spec-kit, autonomous) and several agents (pr-reviewer, github-issue-fixer, deep-reflector).
