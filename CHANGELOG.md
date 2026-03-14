---

## [2026-03-16] - Complete Uninstall System Implementation
### Added
- **Master Uninstaller** (`uninstall.sh`): Complete uninstall orchestration for all 10 platforms
  - Platform detection and selection (auto-detect or manual)
  - Multi-phase uninstall: MCPs → Platform symlinks → Plugins (optional) → Cleanup
  - Supports `--dry-run`, `--restore`, `--all`, `--platform`, `--no-mcp`, `--plugins` flags
  - Interactive platform selection with `gum` (falls back to auto-detect)
  - Comprehensive help text with examples
  - Backup management with retention policy (keeps last 5 backups per platform)
  - Restore capability from backups
  - Color-coded logging and comprehensive summaries

- **Platform Uninstall Scripts** (8 new scripts):
  - `scripts/uninstall-from-antigravity.sh`: Removes skills, global_workflows symlinks
  - `scripts/uninstall-from-kilo.sh`: Removes skills, workflows, rules, AGENTS.md symlinks
  - `scripts/uninstall-from-cursor.sh`: Removes skills symlink
  - `scripts/uninstall-from-windsurf.sh`: Removes skills symlink from ~/.agents/skills
  - `scripts/uninstall-from-claude-code.sh`: Removes skills, commands, CLAUDE.md symlinks
  - `scripts/uninstall-from-codex.sh`: Removes skills, AGENTS.MD symlinks (handles TOML)
  - `scripts/uninstall-from-factory.sh`: Removes skills, workflows/toml, AGENTS.md symlinks
  - `scripts/uninstall-from-qwen.sh`: Removes skills, AGENTS.md symlinks

- **Enhanced uninstall-utils.sh**: Complete utility library with:
  - Backup functions: `backup_before_remove()`, `init_backup_dir()`, `restore_from_backup()`
  - Removal functions: `remove_symlink()`, `remove_directory()`, `remove_file()`
  - MCP removal: `remove_mcp_entry()` (JSON), `remove_mcp_toml_entry()` (TOML)
  - Verification: `verify_removal()`, `validate_json()`, `validate_toml()`
  - Logging: `log_dry()`, `log_backup()`, `log_remove()`, `log_verify()`
  - Backup retention: `cleanup_old_backups()` (keeps last N backups)

### Changed
- All uninstall scripts follow consistent pattern and architecture
- Backups stored in `~/.overpowers/backups/<platform>/<timestamp>/`
- Comprehensive error handling with `set -euo pipefail`
- Dry-run mode supported across all scripts
- Verification of all removals before marking complete

### Documentation
- Created `.docs/tasks/0036-ops-uninstall-scripts.md` with full implementation plan
- Created `.docs/tasks/0037-ops-centralize-platform-paths.md` (follow-up task)
- Created `.docs/tasks/0038-ops-add-dry-run-support.md` (follow-up task)
- Created `.docs/tasks/0039-ops-standardize-error-handling.md` (follow-up task)
- Created `.docs/tasks/0040-ops-add-post-install-validation.md` (follow-up task)
- Created `.docs/tasks/planning/install-scripts-analysis.md` (comprehensive analysis)

**Author**: Omega Agent (with subagent delegation)

## [2026-03-16] - Unified MCP Uninstaller Script
### Added
- **Unified MCP Uninstaller** (`scripts/uninstall-mcps.sh`): Single script to remove Overpowers MCP servers from all 10 platforms
  - Supports all platforms: OpenCode, Gemini CLI, Antigravity, Cursor, Windsurf, Claude Code, Kilo Code, Factory, Qwen Code, Codex CLI
  - Removes ONLY Overpowers-installed MCPs (preserves user MCPs)
  - Overpowers MCPs removed: serena, vibe-check, desktop-commander, hyperbrowser, genkit, memcord, playwright-browser, context7, notebooklm
  - Supports `--dry-run` flag to preview changes
  - Supports `--platform <name>` flag to target specific platforms (can be used multiple times)
  - Supports `--all` flag to remove from all platforms (default behavior)
  - Supports `--list-platforms` to show available platforms and config paths
  - Creates timestamped backups before modifications in `~/.overpowers/backups/<platform>/`
  - Validates JSON/TOML configs after modifications
  - Prints comprehensive summary with removed/skipped counts
  - Handles both `mcpServers` and `mcp` config keys automatically
  - Handles TOML format for Codex CLI ([mcp_servers.NAME] blocks)
  - Automatic cleanup of old backups (keeps last 5 by default)
### Changed
- Replaces need for individual platform uninstall scripts for MCP removal
- Uses Python helpers for safe JSON/TOML manipulation with validation
- Comprehensive error handling with rollback capability via backups
**Author**: Frontend Developer

## [2026-03-16] - Uninstall Scripts Implementation (OpenCode & Gemini CLI)
### Added
- **Uninstall from OpenCode** (`scripts/uninstall-from-opencode.sh`): Removes all Overpowers symlinks from OpenCode configuration
  - Removes symlinks: agents, skills, commands, hooks, AGENTS.md, themes
  - Creates backups before removal in `~/.overpowers/backups/opencode/`
  - Supports `--dry-run` mode and `DRY_RUN` environment variable
  - Verifies all removals and prints summary
- **Uninstall from Gemini CLI** (`scripts/uninstall-from-gemini.sh`): Removes all Overpowers symlinks from Gemini CLI configuration
  - Removes symlinks: hooks, commands, GEMINI.md
  - Handles legacy skills directory backup/removal
  - Cleans up settings.json (removes experimental.enableAgents)
  - Creates backups before removal in `~/.overpowers/backups/gemini/`
  - Supports `--dry-run` mode and `DRY_RUN` environment variable
- **Enhanced uninstall-utils.sh**: Added `verify_removal()` function with dry-run awareness
### Changed
- Both scripts follow the architecture specified in `.docs/tasks/0036-ops-uninstall-scripts.md`
- Scripts source `uninstall-utils.sh` and `deploy-utils.sh` for shared functionality
- Proper error handling with `set -euo pipefail`
- Comprehensive logging with timestamps and color coding
**Author**: Frontend Developer

## [2026-03-16] - Extraction Task: Skills Batch 028 Completion
### Added
- Completed extraction of all 25 skills from batch `0500-extraction-skills-batch-028` using parallel subagents:
  - Video/Media: `parse-video`, `vidu-video`, `wan-video`, `storyboard-generator`, `style-extractor`
  - TTS/Audio: `sutui-minimax-tts`
  - Tools: `points-recharge`, `pricing-test`, `prop-extractor`, `upload-to-catbox`, `qrcode-skills`
  - Content Creation: `conceive-short-drama-cn`, `shorts-builder-cn`
  - Prompt Engineering: `prompt-learning-assistant`, `prompt-master`, `prompts-workflow`
  - OpenClaw: `openclaw-backup`
  - Lifestyle: `mcdonald-cn`, `yahoo-auction-estimator`, `crypto-learning`, `x-hot-topics-daily`
  - Social: `rednote` (xiaohongshu), `x-knowledge-base`
  - Recruitment: `easy-recruitment`
  - Design: `limtdesign` (visual-creative)
### Changed
- All 25 items in batch 0500-extraction-skills-batch-028 marked as completed [x]
- Used parallel subagent dispatch pattern (5 groups)
**Author**: Batch-28-Processor (Parallel Agents)

## [2026-03-16] - Extraction Task: Skills Batch 026 Completion
### Added
- Completed extraction of all 25 skills from batch `0500-extraction-skills-batch-026`:
  - OpenClaw Core: `wechat-mp-writer`, `openclaw-guardian-suite`, `semantic-router`, `subagent-isolation-guard`, `openclaw-parking-query`
  - AI/Methodology: `zhouyi-divination`, `complex-task-methodology`, `cursor-council`, `target-info-search-summarization`, `feedback-loop`, `skill-assessment`
  - Lifestyle: `yanjibus`, `meme-scanner`, `testa`, `zan-diary`, `health-manager`, `learning-planner`, `reading-buddy`, `reading-manager`, `study-buddy`, `trip`
  - Sulada Suite: `sulada-clawdchat`, `sulada-habit-tracker`, `sulada-knowledge-base`
  - Travel: `surf-query`
### Changed
- All 25 items in batch 0500-extraction-skills-batch-026 marked as completed [x]
**Author**: Batch-26-Processor (Parallel Agents)

## [2026-03-16] - Extraction Task: Skills Batch 024 Completion
### Added
- Completed extraction of all 25 skills from batch `0500-extraction-skills-batch-024` using parallel subagents:
  - Media/Content: `pexels-image-downloader`, `xhs-kit-publisher`, `clouddream-a-data`, `digital-human-training`, `openclaw-visual`, `image-generation`, `gif-maker`, `wechat-sticker-maker`
  - Productivity: `openclaw-expense-tracker`, `lark-wiki-writer`
  - Security: `daily-security-check`
  - Social: `douyin-publish`
  - Analysis: `tianlong-analyst`, `dianping-query`, `research-engine`
  - Hot Topics (CN): `36kr-hot-cn`, `weibo-hot-cn`, `douban-hot-cn`, `github-trending-cn`, `hackernews-cn`, `hot-aggregator-cn`
  - Finance: `chinese-ai-agent-guide`, `global-intel-summary`, `log-analyzer`, `finetune-service-cn`
### Changed
- All 25 items in batch 0500-extraction-skills-batch-024 marked as completed [x]
- Used parallel subagent dispatch pattern (5 groups of 5 agents each)
**Author**: Batch-24-Processor (Parallel Agents)

## [2026-03-16] - Batch Processing Infrastructure & Cleanup (gamma)
### Added
- **Batch Processing Script** (`scripts/generators/process-skill-batches.py`): Automated skill standardization and migration from staging to skills/
- **Cleanup Script** (`scripts/generators/clean-staging.py`): Safe staging cleanup with verification and audit logging
- **Sample Review Generator** (`scripts/generators/sample-review-generator.py`): 10% random sampling for quality verification
- **Processing Log** (`.docs/batch-processing-log.json`): Audit trail for all batch processing operations
### Changed
- Split batch processing into 2-phase workflow (process → verify → cleanup)
- Added verification step with 10% random sample review before cleanup
- All scripts support dry-run mode and detailed logging
### Fixed
- Batches 025-035 (126 skills) processed and verified
- 10% sample review (13 skills): 12 PASS, 1 WARNING, 0 FAIL
- Staging cleanup completed for batches 025-035
- 1293 files remaining in staging (batches 037+) preserved for other agents
**Author**: gamma

## [2026-03-16] - Batch Processing 031, 033, 035 (gamma)
### Added
- **Batch 031**: 25 skills processed - AI writing, PDF tools, customer service, expense tracking, recruitment, social media
  - AI writing assistants: ai-writing-assistant-cn (v1.1, payment versions)
  - PDF tools: pdf-smart-tool-cn (v1.1, payment versions)
  - Smart assistants: smart-customer-service-cn, smart-expense-tracker-cn, smart-resume-optimizer-cn, smart-marketing-copy-cn (payment versions)
  - Voice tools: voice-note-transcriber-cn (v1.1, payment versions)
  - Other: ozon-product-sourcing, bangai-recruit, weibo-fresh-posts, communication-mqtt, tencentcloud-faceid-detectaifakefaces, okx-trading-exe, kugou-mysterious-shop, brainhole-factory, safe-edit, quick-note
- **Batch 033**: 25 skills processed - Productivity, monitoring, finance, security, architecture
  - Content creation: nanobanana-ppt-skills, document-pro, video-learn, email-reader
  - Monitoring: bilibili-hot-monitor, a-stock-monitor, menews, x-engagement
  - Utilities: meihua-yishu, truth-check, validate-agent, zixun, openclaw-config-guide, xiaoye-voice, zxz-test, china-tax-calculator
  - Security & memory: jax-skill-security-scanner, smart-memory-system, folder-inspector
  - Specialized: lobster-radio-skill, amcjt-lottery, neo4j-cypher-query-analyze, chinese-daily-assistant, orchestrator, architecture-governance
- **Batch 035**: 25 skills processed - Jisu data APIs, cloud services, protocols
  - Jisu API skills: jisu-astro, jisu-baidu, jisu-baiduai, jisu-bazi, jisu-calendar, jisu-car, jisu-movie, jisu-news, jisu-stock
  - Data services: cell, epc, exchange, huangli, mobileempty, parts, stockhistory, vin
  - Cloud services: aliyun-asr, aliyun-oss, tencentcloud-tts
  - Agent tools: agent-onchain-watch, agent-trend-radar
  - Other: resume-project-summarizer, openclaw-work-protocol, coding-as-dressing
### Changed
- Enhanced batch processing script to handle 75 additional skills
- 6 skills had empty descriptions auto-generated
- All skills standardized with proper YAML frontmatter (kebab-case names, non-empty descriptions)
**Author**: gamma

## [2026-03-16] - Batch Processing 025, 027, 029 (gamma)
### Added
- **Batch 025**: 25 Chinese hot topics & news skills processed
  - Hot topics monitoring: hot-alert-cn, ithome-hot-cn, jike-hot-cn, product-hunt-cn, sspai-hot-cn, toutiao-hot-news-cn, v2ex-hot-cn, wechat-mp-cn, xueqiu-hot-cn
  - Finance & trading: market-analysis-cn, quant-trading-cn, skill-finder-cn
  - AI & productivity: mbti-agent, chat-with-l, feishu-doc-writing, feishu-readability, publish-checklist, ram-review, ai-meeting-room, openclaw-starter-kit, ai-news-research
  - Research & utilities: weather-query-ll, google-deep-research, sharkflow, ai-novel-chongshengfuchou
- **Batch 027**: 1 remaining skill verified (character-creator already completed)
- **Batch 029**: 25 utility skills processed
  - Dev tools: crypto-strategy-suite, code-flow-visualizer, error-message-decoder, performance-profiler, regex-generator
  - Productivity: focus-mind, snapdesign-rednote, minimax-opus-tune, ai-entrepreneur-guide, oceanbase-datapilot, prediction-market-reporter, huamu668-memos-cloud, huamu668-openclaw-security, tcn-diagnosis, writing-assistant-pro
  - Daily life OC: btceth-dulwin-engine, code-snippet-oc, currency-converter-zh, daily-reminder, email-draft-oc, expense-tracker-oc, file-organizer-zh, habit-tracker-oc, link-saver, meeting-notes-oc
### Changed
- Created automated batch processing script (`scripts/generators/process-skill-batches.py`)
- All skills standardized with proper YAML frontmatter (kebab-case names, non-empty descriptions)
- 8 skills had empty descriptions auto-generated
**Author**: gamma

## [2026-03-16] - Batch 027 Completion
### Added
- Agent profile initialization workflow execution for agent "gamma"
- Created continuity file `.agents/continuity-gamma.md` for session tracking
- Completed full context building:
  - Reviewed project memories (core identity, timeline, protocols, orchestration)
  - Analyzed codebase structure (482 agents, 1898 skills, 102+ scripts)
  - Absorbed operational laws (changelog, VCS, naming, archive protocols)
  - Studied orchestration system (CEO, Sisyphus, Prometheus)
- Memcord status: Not available (CLI/uvx unavailable), using `.agents/memories/` as alternative
**Author**: gamma
### Added
- 24 skills from batch 027:
  - `workspace-indexer` - Workspace indexer for code navigation
  - `wechat-article-parser` - Parse WeChat official account articles
  - `iflytek-asr` - iFlytek automatic speech recognition
  - `stockselectionmodel` - Stock selection model AI
  - `xhsredbook` - Xiaohongshu/RedBook content tool
  - `notion-sync-obsidian` - Sync Notion pages to Obsidian
  - `mac-camera-diary` - Use Mac camera as digital diary
  - `wechat-style-writer` - Write in WeChat official account style
  - `lunar-calendar` - Chinese lunar calendar converter
  - `spaces-group-assistant` - Group assistant for AI spaces
  - `weixin-xlog-analyzer` - WeChat Xlog file analyzer
  - `veadk-go-skills` - Veadk Go development skills
  - `qunar-travel-query` - Qunar travel search and booking
  - `free-girlfriend` - AI virtual girlfriend chatbot
  - `pinchtab-skills` - Pinchtab productivity skills
  - `feishu-deep-research` - Feishu deep research integration
  - `fal-consumption-audit` - FAL API consumption audit
  - `fal-llms-txt` - FAL llms.txt generator
  - `fashion-studio` - AI fashion design studio
  - `image-model-evaluation` - Image model evaluation framework
  - `minimax-audio` - MiniMax audio generation API
  - `nano-pro-shuihu` - Nano Pro Shuihuzhuan story generator
  - `novel-to-script` - Convert novels to video scripts
  - `omnihuman-video` - OmniHuman video generation
**Author**: Batch-Processor

## [2026-03-16] - Extraction Task: Skills Batch 024 (Items 16-20)
### Added
- Standardized and integrated 5 new skills from batch `0500-extraction-skills-batch-024`:
  - `tianlong-analyst` - 天龙需求分析专家 | Requirements analysis with critical thinking
  - `dianping-query` - 大众点评餐厅查询 | Dianping restaurant search and query
  - `research-engine` - 自动化研究引擎 | Automated research engine for trend analysis
  - `36kr-hot-cn` - 36 氪热门资讯监控 | 36kr trending tech news monitor
  - `weibo-hot-cn` - 微博热榜监控 | Weibo hot topics monitor
**Author**: Extraction-Agent

## [2026-03-16] - Extraction Task: Skills Batch 021 Completion
### Added
- Standardized and integrated 1 new skills from batch `0500-extraction-skills-batch-021`:
  - `feishu-wiki` - Feishu wiki operations
### Note
- 24 items already processed or missing from staging
**Author**: Batch-Processor (Parallel Agent)

## [2026-03-16] - Extraction Task: Skills Batch 017 Completion (Partial)
### Added
- Standardized and integrated 17 new skills from batch `0500-extraction-skills-batch-017`:
  - `amazon-product-scraper` - Scraping and analyzing Amazon product Listing information
  - `news-briefing` - Real-time AI news briefing with Chinese summaries
  - `engagelab-email` - Send emails via EngageLab REST API with templates
  - `juejin-publisher` - Automatically publish Markdown articles to Juejin platform
  - `money-idea-generator` - Automatically discover AI monetization opportunities
  - `zh` - Translation skill - Chinese-English mutual translation
  - `my-weather-query` - Weather query skill for any location
  - `melodylab-ai-song` - AI song generation and music creation
  - `zeelin-liberal-arts-paper` - Academic paper research for liberal arts
  - `zeelin-ai-detector` - AI content detection and analysis
  - `happycoding-aicoding` - Happy coding AI assistant for programming
  - `naver-search` - Search Korean news articles using Naver Search API
  - `meme-lord` - Generate memes using memegen.link API
  - `openclaw-installer` - Automated OpenClaw installation and configuration
  - `play-dumb` - AI persona skill for playing dumb strategically
  - `play-smart` - AI persona skill for playing smart strategically
  - `star-office-ui` - Star office UI design system and components
### Note
- 8 items already processed or missing from staging (likely duplicates)
**Author**: Batch-17-Processor (Parallel Agent)

## [2026-03-16] - Extraction Task: Skills Batch 015 Completion
### Added
- Standardized and integrated 19 new skills from batch `0500-extraction-skills-batch-015`:
  - `video-pro-cza` - Professional video processing and editing tool
  - `a-share-analysis` - A-share market analysis with technical indicators
  - `daily-game-news` - Daily gaming news aggregation and summaries
  - `daily-voice-quote` - Daily voice quotes and inspirational messages
  - `zhihu-to-wechat` - Convert Zhihu content to WeChat official account format
  - `task-management` - Personal task management and productivity tracking
  - `cn-video-gen` - Chinese video content generation tool
  - `hd-infoimage` - HD infographic and image generation tool
  - `ai-evolution-engine-v2` - AI self-evolution engine v2 for continuous improvement
  - `oc-cost-analyzer` - OpenClaw cost analyzer for API usage tracking
  - `easy-openclaw` - Easy OpenClaw setup and configuration helper
  - `docs-converter` - Document format converter for multiple file types
  - `ren-wu-shou-wei-qi` - Gomoku (Five in a Row) game implementation
  - `local-hub` - Local content aggregation hub
  - `vk-client-search-repetitor` - VKontakte client with search and tutor features
  - `create-agent-arch` - Create agent architecture and design patterns
  - `memory-system` - Memory system for AI agents with persistence
  - `qintianjian` - Financial data analysis tool
  - `openclaw-wecom-channel` - OpenClaw WeCom channel integration
**Author**: Batch-15-Processor (Parallel Agent)

## [2026-03-16] - Extraction Task: Skills Batch 022 Completion
### Added
- Completed extraction of all 25 skills from batch `0500-extraction-skills-batch-022` using parallel subagents:
  - Health analyzers: `social-hub`, `ai-analyzer`, `emergency-card`, `family-health-analyzer`, `fitness-analyzer`, `food-database-query`, `goal-analyzer`, `health-trend-analyzer`, `mental-health-analyzer`, `nutrition-analyzer`, `occupational-health-analyzer`, `oral-health-analyzer`, `rehabilitation-analyzer`, `sexual-health-analyzer`, `skin-health-analyzer`, `sleep-analyzer`, `tcm-constitution-analyzer`, `travel-health-analyzer`, `weightloss-analyzer`
  - Other: `noodle-create-writing`, `fund-report-processor`, `wecom-doc`, `ipo-alert`, `config-manager-evomap`, `yandex-calendar`
### Changed
- All 25 items in batch 0500-extraction-skills-batch-022 marked as completed [x]
- Used parallel subagent dispatch pattern (5 groups)
**Author**: Batch-22-Processor (Parallel Agents)

## [2026-03-16] - Extraction Task: Skills Batch 022 (5 items)
### Added
- Standardized and integrated 5 health analyzer skills from batch `0500-extraction-skills-batch-022`:
  - `occupational-health-analyzer` - Occupational health data analysis, workplace risk assessment, ergonomic evaluation
  - `oral-health-analyzer` - Oral health data analysis with nutrition and chronic disease correlation
  - `rehabilitation-analyzer` - Rehabilitation training data analysis, recovery progress tracking
  - `sexual-health-analyzer` - Sexual health data analysis with medication and chronic disease correlation
  - `skin-health-analyzer` - Skin health data analysis with nutrition and dermatology support
### Changed
- Updated `.docs/tasks/0500-extraction-skills-batch-022.md` - marked 5 items as completed [x]
- All skills already had proper YAML frontmatter and directory structure
**Author**: Batch-22-Processor

## [2026-03-16] - Extraction Task: Skills Batch 020 Completion
### Added
- Completed extraction of all 25 skills from batch `0500-extraction-skills-batch-020` using 5 parallel subagents:
  - `feishu-multi-agent`, `crypto-auto-progression`, `gpu-check`, `company-search-kimi`, `finance-accounting`
  - `voice-chat`, `139mail`, `voice-listener`, `tavern-card`, `shit-journal`
  - `wecom-channel-fix`, `social-persona-chloe`, `crypto-bot-factory`, `deep-research`, `jimeng-generator`
  - `v2ray-proxy`, `financial-content-writer`, `moment-writer`, `wechat-article-writer`, `fy`
  - `fenge-smart-search`, `china-demand-mining`, `china-hotel-comparison`, `tianyi-revenue-tracker`, `tianyi-self-upgrade`
### Changed
- All 25 items in batch 0500-extraction-skills-batch-020 marked as completed [x]
- Used parallel subagent dispatch pattern (5 groups of 5 agents each)
**Author**: Batch-20-Processor (Parallel Agents)

## [2026-03-16] - Extraction Task: Skills Batch 020 (5 items)
### Added
- Standardized and integrated 5 new skills from batch `0500-extraction-skills-batch-020`:
  - `v2ray-proxy` - V2Ray proxy management with automatic switching and system proxy configuration
  - `financial-content-writer` - Finance and tax audit content generator for WeChat public account articles
  - `moment-writer` - WeChat Moments copywriting generator based on McKinsey Trust Formula
  - `wechat-article-writer` - Complete WeChat public account writing assistant with 6-stage workflow and auto-image prompts
  - `fy` - Translation skill for Chinese-English mutual translation and multi-language to Chinese
**Author**: Batch-20-Processor

---

## [2026-03-16] - Extraction Task: Skills Batch 013 Completion
### Added
- Standardized and integrated 23 new skills from batch `0500-extraction-skills-batch-013`:
  - `mcp-zentao-pro` - ZenTao MCP capability extension with cross-project data aggregation
  - `a-stock-watcher` - A-share real-time monitoring with price alerts and technical analysis
  - `ck-rag-skill` - RAG skill for knowledge base queries
  - `sticker` - Generate and send stickers/emojis in chat
  - `skill-maker-chenxi` - Automated skill creation and generation tool
  - `28-day-goal-supervisor` - 28-day goal tracking and supervision system
  - `peter-bugfix-loop` - Automated bug fix loop with iterative testing
  - `peter-code-review` - Automated code review assistant
  - `peter-commit-ops` - Git commit operations and management
  - `safe` - Security and safety checks for code and operations
  - `terminal-executor` - Execute terminal commands safely with output capture
  - `kimi-file-transfer` - File transfer through Kimi workspace
  - `cryptofolio` - Cryptocurrency portfolio tracking and management
  - `irene-ai-news` - AI news aggregation and daily summaries
  - `alicloud-compute-swas-open` - Alibaba Cloud SWAS instance management
  - `baby-guide` - Parenting guide and baby care assistant
  - `bilibili-helper` - Bilibili video helper for downloading and interaction
  - `brand-namer` - Generate creative brand and product names
  - `fitness-plan` - Generate personalized fitness and workout plans
  - `fund-advisor-cn` - Chinese fund investment advisor
  - `live-stream-script` - Generate scripts for live streaming sessions
  - `name-generator` - Generate names for projects, products, and more
  - `test-publish-check` - Pre-publish testing and validation checks
**Author**: Batch-13-Processor (Parallel Agent)

---

## [2026-03-16] - Extraction Task: Skills Batch 010 Completion
### Added
- Completed extraction of 4 remaining skills from batch `0500-extraction-skills-batch-010` using parallel subagents:
  - `eatsth-by` - Personal health diet assistant with food inventory management
  - `myfood-by` - Food inventory management and diet recommendation tool
  - `yandex-tracker-cli` - Yandex Tracker CLI integration (bash + curl)
  - `cpskilltest123456` - Xiaohongshu long-form publishing skill (xiaohongshu-publish)
### Changed
- All 25 items in batch 0500-extraction-skills-batch-010 now marked as completed [x]
- Used parallel subagent dispatch pattern for efficient batch completion
**Author**: Batch-10-Processor (Parallel Agents)

## [2026-03-16] - Extraction Task: Skills Batch 011 Completion
  - `bazhuayu-rpa-webhook` - Trigger Bazhuayu (Octoparse) RPA tasks via webhook
  - `evomap-lite-client` - Lightweight EvoMap client with task loops and Swarm collaboration
  - `html-cn-render-fix` - Fix Chinese character rendering in Python-generated images
  - `stock-daily-report` - Generate daily A-share market reports with K-line charts
  - `polymarket-arbitrage-pro` - Professional Polymarket arbitrage detection tool
  - `async-programming` - Async programming patterns for concurrent task execution
  - `git-workflow` - OpenClaw Git workflow automation with auto-commit
  - `deepseek-chat` - DeepSeek API chat integration (free/cheap, Chinese support)
  - `feishu-article-collector` - Collect and organize articles from Feishu docs
  - `agent-memory-patterns` - Persistent memory patterns for AI agents using AgentDB
  - `agent-security-audit` - Autonomous security audit based on OpenFang 16-layer model
**Author**: Batch-11-Processor (Parallel Agent)

## [2026-03-12] - Consolidate Jules Skills
### Changed
- Consolidated `jules-harvest`, `jules-integrate`, and `jules-triage` skills into `ai-llm-jules-dispatch-login`.
- Renamed source `SKILL.md` files to `SKILL-harvest.md`, `SKILL-integrate.md`, and `SKILL-triage.md` during migration.
### Removed
- Archived `safety-sec-jules-dispatch` per Archive Protocol.
- Archived empty source directories for consolidated Jules skills.
**Author**: Overpowers Architect

## [2026-03-12] - Add Reference Repositories
### Added
- Cloned 42 reference repositories into references/ using usernamereponame naming convention.
- Created scripts/clone_references.sh for automated cloning.
**Author**: Overpowers Architect
## [2026-03-10] - Task 0300 Batch 058 Completion
### Added
- Created 9 new helper scripts for skills in Batch 058 (Web & Frontend domain).
- Populated empty `scripts/` directories for skills such as `linear`, `bluebubbles`, `pyzotero`, etc.
### Fixed
- Completed audit and cleanup of 20 skills in Batch 058, removing temporary `.o*` artifacts.
**Author**: gemini-engineer

## [2026-03-10] - Task 0300 Batch 057 Completion
### Added
- Created 10 new helper scripts for skills in Batch 057 (Design & Frontend domain).
- Populated empty `scripts/` directories for skills such as `wcag-audit`, `semi-design`, `figma-implement`, etc.
### Fixed
- Added missing `#!/usr/bin/env python3` shebangs to 7 existing Python scripts in Batch 057.
- Completed audit and cleanup of 20 skills in Batch 057, removing temporary `.o*` artifacts.
**Author**: gemini-engineer

## [2026-03-10] - Task 0300 Batch 056 Completion
### Added
- Created 11 new helper scripts for skills in Batch 056 (Design & UX domain).
- Populated empty `scripts/` directories for skills such as `gaming-ui`, `gedcom-explorer`, `gog`, `openhue`, `notion`, etc.
### Fixed
- Added missing `#!/usr/bin/env python3` shebangs to 7 existing Python scripts in Batch 056.
- Completed audit and cleanup of 20 skills in Batch 056, removing temporary `.o*` artifacts.
**Author**: gemini-engineer

## [2026-03-10] - Task 0300 Batch 025 Completion
### Added
- Created 18 new helper scripts for skills in Batch 025 (Media & Content domain) to replace missing implementations.
- Populated empty `scripts/` directories for skills such as `3d`, `accessibility`, `charts`, `canvas-design`, etc.
### Changed
- Verified and cleaned up existing scripts in Batch 025.
**Author**: gemini-engineer

## [2026-03-10] - Task 0300 Batch 017 Completion
### Added
- Created 10 new helper scripts for skills in Batch 017 (`strategy-advisor`, `task-plan`, `tavily-web`, `team-collaboration-standup-notes`, `technical-articles`, `transcribe-captions`, `steady-dancer-wan-ai-video`, `step-audio-editx-voice-cloning`, `subagent-driven-development`, `swarm-orchestration`).
- Initialized missing `scripts/` directories for 4 skills in Batch 017.
### Fixed
- Added missing `#!/usr/bin/env python3` shebang to `ai-llm-statistical-analysis` script.
- Completed audit and cleanup of 20 skills in Batch 017, removing temporary `.o*` artifacts.
### Changed
- Verified all scripts in Batch 017 follow best practices (shebang, main block, environment variables for keys).
**Author**: gemini-engineer

## [2026-03-10] - Task 0300 Batch 008 Completion
### Fixed
- Added missing `#!/usr/bin/env python3` shebangs to 3 scripts in Batch 008.
- Created missing `fred_query.py` and `fred_examples.py` for `ai-llm-fred-economic-data` skill.
### Changed
- Completed audit and cleanup of 20 skills in Batch 008, removing temporary `.o*` artifacts.
- Verified all scripts in Batch 008 follow best practices (shebang, main block, environment variables for keys).
**Author**: gemini-engineer

## [2026-03-08] - Semantic Namespacing and GraphRAG Migration
### Added
- Created Kùzu DB GraphRAG foundation (`.agents/skills_graph`) for autonomous skill clustering.
- Extracted 90 tags and 5,115 semantic concepts from 1,277 unique skills.
### Fixed
- Resolved 731 skill conflicts caused by duplicate folder names sharing the same internal skill name across multiple categories.
### Changed
- Migrated all 1,277 `skills/` folders from sequential numbering (`0001` - `1277`) to organic Semantic Namespacing (`[domain]-[subdomain]-[slug]`) derived directly from the Knowledge Graph.
- Re-synchronized the Gemini CLI global configuration via `scripts/deploy-to-gemini-cli.sh`.
- Archived 731 redundant skill folders into `.archive/skills/` to clear Gemini CLI discovery warnings and optimize context usage.
**Author**: Gemini CLI

## [2026-03-07] - Consolidated Parallel PRs for Jules Skill Scripts Batches
### Added
- Evaluated and verified parallel run outputs from Jules agents for the remaining `0300` skill batches.
- Merged and patched the most comprehensive version of scripts generated across 22 parallel batches directly into the main `development` bookmark via Jujutsu, avoiding snapshot corruption of immutable remote branches by using patch diffing.
- Auto-closed the corresponding Github Pull Requests associated with parallel Jules runs.
**Author**: Overpowers Architect (Antigravity)

## [2026-03-06] - Completed Tasks Archival
### Changed
- Extracted 37 completed tasks from `docs/tasklist.json` into a separate `docs/tasks/completed/tasklist-completed.json` manifest file to remove clutter.
- Refactored `docs/tasklist.json` schema to group arrays of payload tasks under a unified `prompt` directive, drastically minimizing repetitive structure.
- Moved the corresponding physical markdown task files from `docs/tasks/` to `docs/tasks/completed/`.
**Author**: Overpowers Architect (Antigravity)

## [2026-03-06] - CFA Helios Prompt Conversion
### Added
- Converted 17 Markdown prompts into structured JSON prompts adhering to the Cognitive Fusion Architecture (CFA) Helios standard.
- Implemented `task_profile`, `agent_profile`, `reasoning_config`, `directives`, and `pipeline` structures for: `architect`, `arxiv`, `doc-updater`, `gatekeeper`, `loom`, `mcps`, `nexus`, `refactor-cleaner`, `release-notes`, `reorganize-docs-agents`, `scout`, `security-reviewer`, `sort-scripts`, `tracker`, `update-memories`, `youtube-ripper`, and `scavenge-planner`.
### Changed
- Standardized naming in `prompts/` directory by removing underscores from Markdown files to match JSON counterparts.
- Aligned `scavenge-planner` naming across .md and .json versions.

## [2026-03-06] - Skill Naming Convention Enforcement
### Changed
- Renamed 13 unnumbered skill directories in `skills/` to follow the `type-subtype-nnnn-name` convention (IDs 1249-1261).
- Updated `name` field in `SKILL.md` for all renamed skills.
- Renamed script utilities in `skills/` and `scripts/utils/` to remove underscores (`consolidate-skills.py`, `consolidate-additional.py`, `skills-report.json`, `analyze-skill.sh`).
- Renamed documentation files in `docs/` to remove underscores (`agno-docs-links.txt`, `skill-creation-guide.md`).
- Moved `lista de skills.md` to `docs/skills-sources.md`.
### Removed
- Archived redundant skill folders (`compound-product-cycle`, `setup-codemap-cli`) and ZIP archives in `skills/` to `.archive/`.
**Author**: Overpowers Architect (Gemini CLI)

## [2026-03-06] - Skill Directory Cleanup & README Refresh
### Changed
- Executed mass rename of over 1223 skill folders in `skills/` to clean duplicated prefixes.
- Updated component inventory counts dynamically in `README.md`, now totaling 2600+ components (including 1280+ skills and 937+ agents).
- Re-aligned the MCP server documentation in `README.md` to perfectly match `opencode-example.json`.
### Removed
- Removed the `Jules Swarm Integration` section from `README.md` as its capabilities have graduated to native skill status.
**Author**: Overpowers Architect (Antigravity)

## [2026-03-06] - Consolidated Parallel PRs for Jules Skill Scripts Batches
### Added
- Evaluated and verified parallel run outputs from Jules agents for the remaining `0300` skill batches.
- Merged and patched the most comprehensive version of scripts generated across 43 parallel batches directly into the main `development` bookmark via Jujutsu, avoiding snapshot corruption of immutable remote branches by using patch diffing.
- Auto-closed the corresponding Github Pull Requests associated with parallel Jules runs.
**Author**: Overpowers Architect (Antigravity)

## [2026-03-05] - Repository Integrity Fix: Agent Syntax & Skill Conflicts
### Fixed
- Resolved YAML frontmatter syntax errors in `agents/jules-orchestrator.md` and `agents/team-claude--it-ops-orchestrator.md` (mismatched quotes and redundant tool entries).
- Resolved massive skill conflicts by archiving 772 legacy (non-prefixed) skill directories that had modern prefixed counterparts.
- Resolved agent duplication by archiving `agents/claude-it-ops-orchestrator.md` in favor of `agents/team-claude--it-ops-orchestrator.md`.
- Repaired merge conflicts and metadata inconsistencies in `continuity.md`.
**Author**: Overpowers Architect (Gemini CLI)

## [2026-03-05] - Skill Scripts Batch 039 Deployment
### Added
- Implemented and deployed helper scripts for 20 skills in Batch 039 (`sci-bio-0790` to `sci-chem-0810`).
- Created scripts for TCGA preprocessing, ToolUniverse multi-omics searches (expression, protein design, rare diseases, sequences), UniProt API queries, Venue template lookups, Baoyu slide deck initialization, Beads task management, ChEMBL queries, Clinical Decision Support scaffolding, ClinicalTrials.gov search, ClinPGx querying, COSMIC data downloads, Datamol structure analysis, DiffDock CSV generation, Drug Repurposing report scaffolding, DrugBank downloads, ESM model inference, and EDA for scientific formats.
**Author**: Overpowers Architect (Gemini CLI)

## [2026-03-05] - Skill Scripts Batch 055 Deployment
### Added
- Implemented and deployed helper scripts for 20 skills in Batch 055 (`sec-safety-1135` to `ux-design-1155`).
- Created specialized scripts for swarm validation, vibe-coding blueprints, worker-agent mappings, XSS payload generation, YARA-X syntax checking, YouTube transcript extraction, security stack detection, MVP scorecards, PREVC report scaffolding, binary information, track initialization, and accessibility audit checklists.
**Author**: Overpowers Architect (Gemini CLI)

## [2026-03-05] - Skill Scripts Batch 007 Deployment
### Added
- Implemented and deployed helper scripts for 20 skills in Batch 007 (`ai-llm-0133` to `ai-llm-0153`).

## [2026-03-05] - Skill Scripts Batch 006 Deployment
### Added
- Implemented and deployed helper scripts for 21 skills in Batch 006 (`ai-llm-0111` to `ai-llm-0132`).
- Created specialized scripts for daily updates (`claude_digest.py`), A/B testing (`ab_test_calculator.py`), ML drift monitoring (`semantic_drift_monitor.py`), decision making (`decision_frameworks.py`), deep research (`ddg.py`), automated research pipelines (`full_pipeline.py`, `init_research.py`), design tokens (`build_tokens.sh`, `generate_tokens.py`), repository exploration (`list_repos.sh`, `dig_repo.sh`), digital brain logging (`weekly_review.py`, `log_entry.py`), parallel agent dispatching (`task_generator.py`, `dispatch.py`), doc co-authoring (`init_scaffold.py`, `reader_test.py`), document parsing (`batch_convert.py`), changelog generation (`format_changelog.py`, `generate_highlights.py`), documentation seeking (`repomix_pack.sh`, `get_llms_txt.sh`), and various utilities for docstrings, watermarking, and domain name brainstorming.
**Author**: Overpowers Architect (Gemini CLI)
## [2026-03-05] - Skill Scripts Batch 036
### Added
- Helper scripts for 20 skills (`ops-infra-0735` to `sci-bio-0750`).
- New `check_deps.py` utility for dependency validation across multiple skills.
- Domain-specific scripts for Netlify, Render, GitHub CLI, and various Bioinformatics tools.
**Author**: Gemini CLI

- Created specialized scripts for outreach CSV preparation, Excalidraw diagram manipulation, Exa semantic search, Fal.ai API integration, and various domain-specific utilities for email sequences, prompt enhancement, and marketing campaign execution.
**Author**: Overpowers Architect (Gemini CLI)

## [2026-03-05] - Skill Scripts Batch 035 Deployment
### Added
- Implemented and deployed helper scripts for 20 skills in Batch 035 (`ops-infra-0714` to `ops-infra-0733`).
- Created specialized scripts for test failure grouping (`test_grouper.py`), Things 3 management (`things_helper.sh`), Three.js geometry reference (`threejs_geometry_list.py`), documentation mapping (`doc_mapper.py`), Expo upgrades (`expo_upgrade_helper.sh`), file summarization (`summarize_file.sh`), git worktree automation (`worktree_helper.sh`), web fetching/markdown conversion (`fetch.sh`, `web2md_helper.sh`), and Rube MCP automation helpers for Todoist, Trello, Webflow, WhatsApp, Wrike, Zoho CRM, and Zoom.
- Integrated Cloudflare deployment helper (`cloudflare_helper.sh`) and X article publishing guidance.
**Author**: Overpowers Architect (Gemini CLI)

## [2026-03-05] - Skill Scripts Batch 038
### Added
- Implemented helper scripts for 20 skills (sci-bio-0771 to sci-bio-0790) to improve operational efficiency.
**Author**: Overpowers Architect

# Changelog

All notable changes to this project will be documented in this file.

> [!CAUTION]
> **IMMUTABLE HISTORY**: Entries in this file must NEVER be deleted or modified (except typo fixes).
> New entries are ALWAYS added at the TOP in descending date order.

---

+++++++ Contents of side #1

## [2026-03-05] - Skill Scripts Batch 005 Deployment
### Added
- Implemented and deployed helper scripts for 20 skills in Batch 005 (`ai-llm-0086` to `ai-llm-0110`).
- Created specialized scripts for ComfyUI setup/utilities (AEP, Cache DiT, Wan 2.2, Z-Image), mathematical solving (Z3, Sympy), competitive research/intelligence (battlecards, research reporting), component analysis, Conductor track automation, content creation (brand voice, SEO optimization), strategy planning, copy editing (Seven Sweeps), and YAML handoff/plan generation.
- Synchronized internal skill mapping via `parse-skills.js`.
**Author**: Overpowers Architect (Gemini CLI)

## [2026-03-05] - Skill Scripts Batch 004 Deployment
### Added
- Implemented and deployed helper scripts for 20 skills in Batch 004 (`ai-llm-0066` to `ai-llm-0085`).
- Created specialized scripts for C4 component/context generation, cache component checking, campaign brief generation, OMC state clearing, CEO strategy/financial analysis, changelog updates, review alignment checking, Chroma DB utilities, CGD validation, health report generation, Ghostty Vim-nav setup, AGENTS.md scoring, research plan generation, Claude settings auditing, meta-skill creation/validation, skill syncing, README generation, execution runtime setup, and coding agent scratchpad initialization.
**Author**: Overpowers Architect (Gemini CLI)

## [2026-03-05] - Skill Scripts Batch 010 Deployment
### Added
- Implemented and deployed helper scripts for 20 skills in Batch 010 (`ai-llm-0198` to `ai-llm-0219`).
- Created specialized scripts for scientify installation, numerical interpolation, invoice organization, ISO 13485 gap analysis, asset sheet generation, Jira multi-backend handling, JSON Canvas building, Jules branch harvesting, Kagi API clients, knowledge base searching, LangSmith trace debugging, lead research reporting, LLM app scaffolding, RAG BI pipelines, Kubernetes LLM manifests, and batch markdown conversion.
**Author**: Overpowers Architect (Gemini CLI)

## [2026-03-05] - Skill Scripts Batch 011 Deployment
### Added
- Implemented and deployed helper scripts for 20 skills in Batch 011 (`ai-llm-0220` to `ai-llm-0241`).
- Created standardized Python and Bash utilities for market sizing, marketing CAC, A/B testing, MCP interactions, regulatory gap analysis, and more.
**Author**: Overpowers Architect (Gemini CLI)

## [2026-03-04] - Advanced Hooks Implementation
### Added
- Implemented robust `hooks/runtime/todo_enforcer.py` to auto-detect pending tasks from `tasklist.md` and `continuity.md`.
- Implemented intelligent `hooks/runtime/dir_injector.py` for automated context enrichment during directory navigation.
- Implemented `hooks/runtime/edit_guard.py` middleware providing actionable self-recovery hints for agent tool failures.
**Author**: Overpowers Architect (Gemini CLI)

## [2026-03-04] - External Skill Extraction and Integration

### Added
- Integrated 31 new 🟢 Green skills from external repositories (Anthropics, OpenAI, Vercel, Google Labs).
- Created `media-content-0571-media-content-1246-stitch-remotion-walkthrough` (Differentiated from Remotion hub).
- Created `ops-infra-0739-desktop-screenshot` (Differentiated from marketing screenshots).
- Created `ai-llm-1247-openai-imagegen` (Differentiated from Gemini imagegen).
- Created `ai-llm-1248-openai-speech` (Differentiated from Azure speech-to-text).
- New sequence of skills added to categories: `ai-llm` (1234-1246), `ops-infra` (0733-0738), `web-frontend` (1233-1238), `dev-code` (1144), `data-sci` (0481), `ux-design` (1194), `sec-safety` (1143-1144), `tool-general` (1154).

### Changed
- **Merged and Enriched**: `algorithmic-art`, `brand-guidelines`, `canvas-design`, `react-best-practices` (58 rules), `skill-creator`, `vercel-deploy`, and `web-design-guidelines` with superior official content.
- Updated `continuity.md` to reflect skill mining completion.
**Author**: Overpowers Architect (Gemini CLI)


### Added
- Created `scripts/utils/jj-commit-push.sh` to automate the local JuJutsu staging/commit/push lifecycle.
- Modified `workflows/00-setup.md` to establish global `$OVERPOWERS_PATH` capability to let users execute the setup sequence seamlessly anywhere.
- Added `10.4. Routine State Commits` requirement inside `AGENTS.md` (and template).

## [2026-03-04] - Constitution Template Hardening
### Changed
- Updated `AGENTS.md` and `templates/rules/AGENTS.md` Section 6 to formally enforce templates (`agent.md`, `skill-template/SKILL.md`, `workflow.md`) and mandate the `md-to-toml.py` conversion script for workflows.
- Renamed `docs/guides/` files to strictly follow the standard `type-[subtype]-nnnn-names.md` document convention.
**Author**: Antigravity

## [2026-03-04] - Massive Operation Framework Stress Test
### Added
- Created `.agents/thoughts/massive-operation-framework-stress-test.md` containing analysis and 30 stress-test questions for the universal transformation framework.
**Author**: Overpowers Architect (Gemini CLI)

## [2026-03-04] - Skill Reorganization
### Changed
- Created `scripts/install-skills.py` for skill integrity verification and local setup.
- Updated `AGENTS.md` and templates with memory management guidelines and terminology clarity.
- Renamed 1237 skill folders following the `type-subtype-nnnn-name` convention for better organization and discovery.
### Added
- Created `docs/tasks/planning/2026-03-04-skill-improvements-plan.md` for future standardization tasks.
**Author**: Overpowers Architect
## [2026-03-03] - System Recovery & Workflow Enhancements

### Added
- **Templates**: `prompts/scavengeplanner.md` template for blueprint assimilation and orchestration planning.
- **Workflows**: `workflows/task-grooming.md` for task extraction and decomposition.
- **Scripts**: `scripts/md-to-toml.py` markdown to TOML workflow parser for Gemini CLI.
- **Reports**: Post-mortem report `.agents/thoughts/jj-bookmark-regression.md` detailing the Jujutsu bookmark regression incident and the 5-stage safe restoration protocol.

### Changed
- **CLI Workflows**: Converted Markdown workflows successfully into TOML formatting for Gemini CLI.
- **System**: Restored repository integrity via Jujutsu operation log recovering lost workflows and tools.
- **System**: Deleted 10 stale/abandoned branches from GitHub and synchronized local repository.
- **Security**: Added `userenv` artifacts explicitly to `.gitignore` to prevent credential leakage.

**Author**: Overpowers Architect (Antigravity)


## [2026-05-24] - Browser Automation & Cleanup

### Added
- **Skills**: `browser-use`, `playwright-skill`, `web-research` (from Moltbot).
- **Agents**: `browser-automator.md` specialized in web interaction.
- **Workflows**: `workflows/web-research.md`.

### Changed
- **Config**: Updated `.gitignore` to exclude build artifacts and caches.
- **Agents**: Regenerated all agent configs.

**Author**: Jules (Agent)

## [2026-05-24] - BMAD Deepening Phase (Workflows)

### Added
- **Workflows**:
  - `workflows/game-dev/dev-story.md`: Full "Dev Story" workflow for Game Dev Agent.
  - `workflows/creative/problem-solving.md`: "Problem Solving" workflow for Creative Agent.
- **Agents**:
  - Updated `agents/game-dev-studio.md` with explicit workflow delegations.
  - Updated `agents/creative-problem-solver.md` with explicit workflow delegations.

### Changed
- **Agents**: `Link Freeman` and `Dr. Quinn` now have executable `workflow="..."` parameters in their prompts.

**Author**: Jules (Agent)

## [2026-05-24] - BMAD & Safety Integration

### Added
- **Safety**: `hooks/safety/destructive-command-blocker.ts` - Prevents catastrophic commands (`rm -rf`, `mkfs`, `circleci context delete`).
- **Agents**:
  - `agents/murat-test-architect.md`: Master Test Architect (from TEA).
  - `agents/game-dev-studio.md`: Game Development Specialist.
  - `agents/creative-problem-solver.md`: TRIZ/Systems Thinking Expert.
- **Knowledge Graph**: `docs/knowledge/testing/` - Massive import of testing patterns (Risk-based, ATDD, Flakiness).
- **Workflows**: `workflows/teach-me-testing.md`.
- **Skills**: `skills/playwright-skill/network-monitor.ts` - Network error monitoring fixture.

### Changed
- **Architecture**: Adopted "Knowledge Graph" pattern. Updated `JULES_ARCHITECTURAL_DIGEST.md`.

**Author**: Jules (Agent)

---

## [2026-05-24] - Bonus Round: Advanced Integration


## [2026-03-03] - Consolidated Generic AGENTS.md Template

### Added
- New `scripts/templates/AGENTS.md` — a comprehensive generic template (~550 lines) consolidating all rules from `AGENTS.md`, `AGENTS copy.md`, `AGENTS copy 2.md`, and all 14 `.agents/rules/` files.
- Template covers: session initialization, core philosophy, changelog protocol, knowledge routing, operational laws, security boundaries, conventions, task system, cognitive workflow & memory management, engineering standards, development practices (TDD, SDD, spec-first), multi-agent safety, VCS rules (Git + Jujutsu), Jules agent rules, delegation strategy, behavioral guidelines, forbidden actions, environment/tooling, and platform-specific rules.

**Author**: Overpowers Architect (Antigravity)

## [2026-03-02] - Merge PRs #45 and #46 via jj

### Added
- Integrated PR #46: feat: add skills extracted from Unsupervised Learning channel (Batch 1 & 2).
- Integrated PR #45: YouTube Ripper: Processes batch 7 for @fernandobrasao.

### Fixed
- Resolved merge conflicts in `CHANGELOG.md`, `.agents/reports/youtube-mining-notes.md`, and `docs/youtube/fernando-brasao.md`.

**Author**: Overpowers Architect (Gemini CLI)


## [2026-03-02] - YouTube Skill Mining: Unsupervised Learning Channel (Batch 1 & 2)

### Added
- **Skills**: `fabric-ai-evaluator` extracted from 'Using the Smartest AI to Rate Other AI' video.
- **Skills**: `nano-banana-art-generator` extracted from 'My Art Skill With Nano Banana 3' video.
- **Skills**: `claude-code-neovim-ghostty` extracted from 'Claude Code + Neovim via Ghostty Panes' video.
- **Skills**: `fabric-raycast-integration` extracted from 'Fabric New Integration with Raycast' video.
- **Reports**: Appended notes to `youtube-mining-notes.md` for batch 1 & 2 analysis.
- **Reports**: Added `docs/tasks/youtube-mining-video-analysis-report.md`.
- **Data**: Initial raw list of videos in `docs/youtube/unsupervised-learning.md`.
- **Data**: Subtitle and info files for processed videos in `docs/youtube/`.

**Author**: youtube-ripper

## [2026-03-02] - YouTube Ripper: Batch 6 & 7 (fernando-brasao)

### Changed
- Processed Batch 6 and 7 for @fernandobrasao.
- Handled HTTP 429 errors from YouTube during transcript extraction.
- Updated `docs/youtube/fernando-brasao.md` with processing status.
- Appended evaluation notes to `.agents/reports/youtube-mining-notes.md`.

**Author**: youtube-ripper

## [2026-03-02] - Docs Directory Reorganization

### Added
- New directory structure for `docs/`: `architecture/`, `guides/`, `tasks/planning/`.
- `archives/` directory for historical and obsolete documentation.
- Naming convention `nnn-type-name.md` applied to all core documentation files.

### Changed
- Reorganized `docs/` root into subdirectories.
- Moved testing patterns to `docs/guides/testing/`.
- Moved external service documentation to `docs/guides/services/`.
- Moved architectural concepts and codebase maps to `docs/architecture/`.
- Updated `docs/README.md` with new structure and fixed navigation links.
- Updated `docs/guides/004-guide-services.md` with correct internal paths.
- Updated `docs/architecture/codemaps/000-arch-index.md` with current file names.

### Fixed
- Resolved merge conflicts in `docs/README.md`.
- Completed documentation deduplication tasks (004, 005, 006).

**Author**: Overpowers Architect (Gemini CLI)

## [2026-03-02] - Second Pass Audit and Agent Standardization

### Added
- New audit report: "docs/architecture/016-second-audit-report.md".
- New maintenance script: "scripts/fix_agents.py" for standardizing agent frontmatter.

### Fixed
- **Critical**: Standardized frontmatter for all 938 agents. Fixed missing "tools" fields and corrupted YAML syntax across 832 files.
- Completed rebranding sweep from "superpowers" to "overpowers" in "README.md", "AGENTS.md", "install.sh", and core documentation.
- Ensured all agent "color" fields are double-quoted hex codes per constitutional rules.

### Changed
- Updated "docs/tasklist.md" marking Task 016 as complete.

**Author**: Overpowers Architect (Gemini CLI)

## [2026-03-02] - Enhanced Installation UX and Kilo Code Support

### Added
- New deployment script "scripts/deploy-to-kilo.sh" for Kilo Code support.
- Support for "OVERPOWERS_CONFLICT_POLICY" environment variable in all deployment scripts to allow merging assets instead of replacing them.
- Documentation for Kilo Code in "README.md" and "AGENTS.md".

### Changed
- Major UX improvements to "install.sh":
    - Added pre-install explanation of installation steps.
    - Added data handling disclaimer.
    - Implemented asset conflict detection for all platforms.
    - Added interactive prompts for conflict resolution (Replace vs Copy-Only).
    - Expanded platform selection to include Kilo Code.
    - Improved final installation summary.

**Author**: Overpowers Architect (Gemini CLI)

## [2026-03-02] - Fix Antigravity and Multi-Platform MCP Configurations

### Fixed
- Resolved unresolvable "{env:VAR}" and "${VAR}" patterns in "~/.gemini/antigravity/mcp_config.json".
- Standardized Antigravity, Gemini CLI ("settings.json"), and OpenCode ("opencode.json") MCP configurations with valid absolute paths.
- Updated "memcord" to use "uvx memcord server" instead of hardcoded virtualenv paths.
- Corrected "notebooklm" MCP command arguments to include the "run" subcommand.
- Fixed "semgrep" MCP configuration to use native "semgrep mcp" command.

### Changed
- Updated "scripts/templates/mcp-antigravity.json" with modern command patterns and Semgrep support.
- Synchronized "opencode-example.json" with the latest multi-platform configuration standards.

**Author**: Overpowers Architect (Gemini CLI)
%%%%%%% Changes from base to side #2
-## [2026-03-03] - Consolidated Generic AGENTS.md Template
-
-### Added
-- New `scripts/templates/AGENTS.md` — a comprehensive generic template (~550 lines) consolidating all rules from `AGENTS.md`, `AGENTS copy.md`, `AGENTS copy 2.md`, and all 14 `.agents/rules/` files.
-- Template covers: session initialization, core philosophy, changelog protocol, knowledge routing, operational laws, security boundaries, conventions, task system, cognitive workflow & memory management, engineering standards, development practices (TDD, SDD, spec-first), multi-agent safety, VCS rules (Git + Jujutsu), Jules agent rules, delegation strategy, behavioral guidelines, forbidden actions, environment/tooling, and platform-specific rules.
-
-**Author**: Overpowers Architect (Antigravity)
-
-## [2026-03-02] - Merge PRs #45 and #46 via jj
-
-### Added
-- Integrated PR #46: feat: add skills extracted from Unsupervised Learning channel (Batch 1 & 2).
-- Integrated PR #45: YouTube Ripper: Processes batch 7 for @fernandobrasao.
-
-### Fixed
-- Resolved merge conflicts in `CHANGELOG.md`, `.agents/reports/youtube-mining-notes.md`, and `docs/youtube/fernando-brasao.md`.
-
-**Author**: Overpowers Architect (Gemini CLI)
-
-
-## [2026-03-02] - YouTube Skill Mining: Unsupervised Learning Channel (Batch 1 & 2)
-
-### Added
-- **Skills**: `fabric-ai-evaluator` extracted from 'Using the Smartest AI to Rate Other AI' video.
-- **Skills**: `nano-banana-art-generator` extracted from 'My Art Skill With Nano Banana 3' video.
-- **Skills**: `claude-code-neovim-ghostty` extracted from 'Claude Code + Neovim via Ghostty Panes' video.
-- **Skills**: `fabric-raycast-integration` extracted from 'Fabric New Integration with Raycast' video.
-- **Reports**: Appended notes to `youtube-mining-notes.md` for batch 1 & 2 analysis.
-- **Reports**: Added `docs/tasks/youtube-mining-video-analysis-report.md`.
-- **Data**: Initial raw list of videos in `docs/youtube/unsupervised-learning.md`.
-- **Data**: Subtitle and info files for processed videos in `docs/youtube/`.
-
-**Author**: youtube-ripper
-
-## [2026-03-02] - YouTube Ripper: Batch 6 & 7 (fernando-brasao)
-
-### Changed
-- Processed Batch 6 and 7 for @fernandobrasao.
-- Handled HTTP 429 errors from YouTube during transcript extraction.
-- Updated `docs/youtube/fernando-brasao.md` with processing status.
-- Appended evaluation notes to `.agents/reports/youtube-mining-notes.md`.
-
-**Author**: youtube-ripper
-
-## [2026-03-02] - Docs Directory Reorganization
-
-### Added
-- New directory structure for `docs/`: `architecture/`, `guides/`, `tasks/planning/`.
-- `archives/` directory for historical and obsolete documentation.
-- Naming convention `nnn-type-name.md` applied to all core documentation files.
-
-### Changed
-- Reorganized `docs/` root into subdirectories.
-- Moved testing patterns to `docs/guides/testing/`.
-- Moved external service documentation to `docs/guides/services/`.
-- Moved architectural concepts and codebase maps to `docs/architecture/`.
-- Updated `docs/README.md` with new structure and fixed navigation links.
-- Updated `docs/guides/004-guide-services.md` with correct internal paths.
-- Updated `docs/architecture/codemaps/000-arch-index.md` with current file names.
-
-### Fixed
-- Resolved merge conflicts in `docs/README.md`.
-- Completed documentation deduplication tasks (004, 005, 006).
-
-**Author**: Overpowers Architect (Gemini CLI)
-
-## [2026-03-02] - Second Pass Audit and Agent Standardization
-
-### Added
-- New audit report: "docs/architecture/016-second-audit-report.md".
-- New maintenance script: "scripts/fix_agents.py" for standardizing agent frontmatter.
-
-### Fixed
-- **Critical**: Standardized frontmatter for all 938 agents. Fixed missing "tools" fields and corrupted YAML syntax across 832 files.
-- Completed rebranding sweep from "superpowers" to "overpowers" in "README.md", "AGENTS.md", "install.sh", and core documentation.
-- Ensured all agent "color" fields are double-quoted hex codes per constitutional rules.
-
-### Changed
-- Updated "docs/tasklist.md" marking Task 016 as complete.
-
-**Author**: Overpowers Architect (Gemini CLI)
-
-## [2026-03-02] - Enhanced Installation UX and Kilo Code Support
-
-### Added
-- New deployment script "scripts/deploy-to-kilo.sh" for Kilo Code support.
-- Support for "OVERPOWERS_CONFLICT_POLICY" environment variable in all deployment scripts to allow merging assets instead of replacing them.
-- Documentation for Kilo Code in "README.md" and "AGENTS.md".
-
-### Changed
-- Major UX improvements to "install.sh":
-    - Added pre-install explanation of installation steps.
-    - Added data handling disclaimer.
-    - Implemented asset conflict detection for all platforms.
-    - Added interactive prompts for conflict resolution (Replace vs Copy-Only).
-    - Expanded platform selection to include Kilo Code.
-    - Improved final installation summary.
-
-**Author**: Overpowers Architect (Gemini CLI)
-
-## [2026-03-02] - Fix Antigravity and Multi-Platform MCP Configurations
-
-### Fixed
-- Resolved unresolvable "{env:VAR}" and "${VAR}" patterns in "~/.gemini/antigravity/mcp_config.json".
-- Standardized Antigravity, Gemini CLI ("settings.json"), and OpenCode ("opencode.json") MCP configurations with valid absolute paths.
-- Updated "memcord" to use "uvx memcord server" instead of hardcoded virtualenv paths.
-- Corrected "notebooklm" MCP command arguments to include the "run" subcommand.
-- Fixed "semgrep" MCP configuration to use native "semgrep mcp" command.
-
-### Changed
-- Updated "scripts/templates/mcp-antigravity.json" with modern command patterns and Semgrep support.
-- Synchronized "opencode-example.json" with the latest multi-platform configuration standards.
-
-**Author**: Overpowers Architect (Gemini CLI)
+## [2026-03-05] - Skill Scripts Batch 002
+### Added
+- Implemented helper scripts for 20 skills (`ai-llm-0023` to `ai-llm-0045`).
+- Scripts include cost calculators, JSON validators, Brave search wrappers, Amazon ASIN and Product lookup templates, financial ratio calculators, Apify runner, ASO metadata optimizers, Argos URL builders, Art skill notification and generation wrappers, arXiv scanners, coordinate transformers, audio tool detectors and summarizers, and audit case RAG templates.
+- Established consistent directory structures and provided robust base implementations for all new scripts.
+**Author**: Overpowers Architect
+
+## [2026-03-05] - Skill Scripts Batch 001
+### Added
+- Implemented helper scripts for 20 skills (`ai-llm-0001` to `ai-llm-0022`).
+- Scripts include research queries, talking points, lyrics formatters, style analyzers, system monitors, load balancer simulators, board sync helpers, and more.
+- Consolidated repository utility scripts (detect-env, count-lines, search-knowledge) into relevant skill folders.
+**Author**: Overpowers Architect
+
+... [rest of file]
