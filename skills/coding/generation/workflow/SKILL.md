---
name: sdd-dev-workflow
description: "规范驱动开发工作流（SDD + Speckit + Claude Code）。用于复杂软件开发项目，包含完整的规范驱动开发流程、Claude Code 交互式操作、开发最佳实践。当用户需要开发复杂应用、进行多迭代开发项目时使用此 skill。"
metadata:
  openclaw:
    category: "development"
    tags: ['development', 'devops', 'tools']
    version: "1.0.0"
---

# SDD 开发工作流 Skill

## ⚠️ 安装前必读

**安全警告**：
- 本 skill 包含 `bypassPermissions` 模式，会跳过 Claude Code 权限检查
- 脚本会执行全局 npm 安装和 `curl | sh` 安装器
- 需要 GitHub Token 和智谱 API Key（建议使用最小权限）

**安装前检查清单**：
- [ ] 检查 `scripts/` 目录下的脚本内容
- [ ] 确认不需要在敏感环境中运行
- [ ] 准备最小权限的 GITHUB_TOKEN
- [ ] 准备智谱 API Key

---

本 skill 整合了**规范驱动开发（SDD）**、**Speckit 工作流**和**Claude Code 交互式操作**，用于复杂软件项目的开发。

## 🎯 核心理念

> **用规范驱动开发（SDD）把需求变成结构化的"规范文档"，让大语言模型在相对准确且完整的上下文中，收敛注意力，提供更符合预期的输出。**

### 三大原则

1. **规范优先（Spec First）**：开发前先编写规范，确保方向一致
2. **规范锚定（Spec Anchored）**：规范持续演进，作为长期资产
3. **规范作为源（Spec as Source）**：规范是主要源文件，代码由规范驱动生成

---

## ⚠️ 工具链协作方式（必读）

### Specify CLI 的角色

```
Specify CLI         →       Claude Code          →      完成开发
（仅用于初始化）           （执行 /speckit 命令）        （代码实现）
```

**Specify CLI 仅用于初始化**：
- ✅ `specify init` 初始化项目结构
- ✅ 生成 `.specify/` 配置和模板
- ❌ **不支持** clarify/plan/tasks/analyze/implement

**后续工作在 Claude Code 中执行**：
- ✅ `/speckit.constitution` 定义项目宪法
- ✅ `/speckit.specify` 创建功能规范
- ✅ `/speckit.clarify` 需求澄清
- ✅ `/speckit.plan` 实现计划
- ✅ `/speckit.tasks` 任务拆分
- ✅ `/speckit.analyze` 一致性分析
- ✅ `/speckit.implement` **代码实现（最终目标）**

### 最终目标

| ❌ 错误理解 | ✅ 正确理解 |
|------------|------------|
| 生成 spec.md | 完成代码实现 |
| 生成 plan.md | 通过测试验证 |
| 生成 tasks.md | 功能可以运行 |

**任务完成的标志**：
- ✅ 代码已实现（不是文档）
- ✅ 测试已通过
- ✅ 功能可运行

---

## 🏛️ 公共宪法模板

### 为什么需要公共宪法？

宪法是项目的通用工程原则，不应该每次新项目都从零开始。我们提供了一套公共宪法模板，可以在新项目中直接引用。

### 宪法模板位置

```
~/.openclaw/skills/sdd-dev-workflow/templates/
├── constitution-template.md      # 基础模板（精简版）
└── constitution-aigc-ops.md      # AIGC-OPS 完整模板（推荐）
```

### 使用方式

#### 方式 1：通过 Speckit 命令引用（推荐）

在 Claude Code 中执行：

```bash
/speckit.constitution 阅读并使用公共宪法模板 ~/.openclaw/skills/sdd-dev-workflow/templates/constitution-aigc-ops.md 作为当前项目的宪法
```

#### 方式 2：手动复制

```bash
# 复制公共宪法到新项目
cp ~/.openclaw/skills/sdd-dev-workflow/templates/constitution-aigc-ops.md \
   /path/to/project/.specify/memory/constitution.md
```

#### 方式 3：使用辅助脚本

```bash
# 初始化项目时指定宪法模板
~/.openclaw/skills/sdd-dev-workflow/scripts/init-project.sh my-project --constitution=aigc-ops
```

### 宪法模板说明

| 模板 | 文件 | 适用场景 |
|------|------|----------|
| **enterprise**（推荐） | `constitution-enterprise.md` | 企业级项目，完整严格 |
| **lite** | `constitution-lite.md` | 小型项目，精简灵活 |

> 💡 你也可以添加自己的宪法模板到 `templates/` 目录，然后在初始化时指定。

### 宪法版本管理

- 宪法使用语义化版本号：`MAJOR.MINOR.PATCH`
- 更新公共宪法模板后，所有新项目自动使用新版本
- 已有项目可选择性升级宪法

---

## 📁 项目路径规范

### 标准目录结构

```
~/openclaw/workspace/
├── projects/                    # 正式开发项目（长期维护）
│   └── <project-name>/         # 项目目录
│
├── tmp/                         # 临时项目（验证、测试，可随时清理）
│   └── <temp-project>/         # 临时目录
│
├── docs/                        # 文档（可选，按需创建）
│   └── <any-docs>/             # 任意文档
│
├── research/                    # 深度研究报告
│   └── <topic>/
│
├── memory/                      # 日期日记
├── .learnings/                  # 学习记录
└── [配置文件]                   # AGENTS.md, SOUL.md, etc.
```

### 目录用途

| 目录 | 用途 | 生命周期 |
|------|------|----------|
| `projects/` | 正式开发项目 | 长期维护 |
| `tmp/` | 临时验证、测试项目 | 短期，可清理 |
| `docs/` | 通用文档 | 按需创建 |
| `research/` | 研究报告 | 长期保存 |

### 路径规则

| 类型 | 路径 | 示例 |
|------|------|------|
| **正式项目** | `projects/<name>/` | `projects/my-app/` |
| **临时项目** | `tmp/<name>/` | `tmp/test-workflow/` |
| **研究报告** | `research/<topic>/` | `research/ai-sovereignty/` |
| **文档** | `docs/<name>/` | `docs/api-specs/`（可选） |

### 新项目创建规范

```bash
# ✅ 正式项目：创建于 projects/
~/.openclaw/skills/sdd-dev-workflow/scripts/init-project.sh my-project

# ✅ 临时项目：创建于 tmp/
~/.openclaw/skills/sdd-dev-workflow/scripts/init-project.sh test-xyz --tmp

# ❌ 错误：不要在 workspace 根目录创建项目
cd ~/openclaw/workspace
specify init my-project  # 错误！
```

---

## 🔧 环境检查与初始化

### 自动环境检查

在开始开发前，系统会自动检查以下依赖：

| 依赖 | 要求 | 检查命令 |
|------|------|----------|
| **Python** | 3.11+ | `python3.11 --version` |
| **Git** | 任意 | `git --version` |
| **UV** | 任意 | `uv --version` |
| **specify-cli** | 最新 | `specify --help` |
| **Claude Code** | 最新 | `claude --version` |
| **tmux** | 3.0+ | `tmux -V` |

### 手动安装依赖

```bash
# 1. 安装 Python 3.11+（如果需要）
# Ubuntu/Debian:
sudo apt-get install python3.11 python3.11-venv python3.11-dev

# macOS:
brew install python@3.11

# 2. 安装 UV 包管理器
curl -LsSf https://astral.sh/uv/install.sh | sh

# 3. 安装 specify-cli
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

# 4. 安装 Claude Code（智谱 Coding Plan 方案）
npm install -g @anthropic-ai/claude-code
npm install -g @z_ai/coding-helper
coding-helper auth glm_coding_plan_china "YOUR_API_KEY"
coding-helper auth reload claude

# 5. 配置 GLM-5 模型
# 编辑 ~/.claude/settings.json，添加：
{
  "env": {
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "glm-5",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "glm-5",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "glm-5"
  }
}
```

### 初始化新项目

```bash
# 方式 1：创建全新项目
specify init my-project
cd my-project

# 方式 2：在现有项目中初始化
cd existing-project
specify init .
```

**初始化产物**：
```
project/
├── .specify/
│   ├── memory/
│   │   └── constitution.md    # 项目宪法（待填写）
│   ├── scripts/               # 辅助脚本
│   │   └── bash/
│   │       ├── create-new-feature.sh
│   │       └── setup-plan.sh
│   └── templates/             # 规范模板
│       ├── spec-template.md
│       ├── plan-template.md
│       └── tasks-template.md
├── .cursor/                   # Cursor IDE 命令（如使用 Cursor）
│   └── commands/
│       ├── speckit.constitution.md
│       ├── speckit.specify.md
│       ├── speckit.clarify.md
│       ├── speckit.plan.md
│       ├── speckit.tasks.md
│       ├── speckit.analyze.md
│       └── speckit.implement.md
└── specs/                     # 规范文档目录（待创建）
```

---

## 🔧 工具链

### tmux vs sessions_spawn 定位说明

| 工具 | 用途 | 场景 |
|------|------|------|
| **sessions_spawn** | Autonomous agent | 自动化任务、开发工作流、研究任务 |
| **tmux** | 交互式操作 | 人类手动调试、紧急干预、实时测试 |

**推荐优先级**：
1. ✅ **优先使用 sessions_spawn**（真正 autonomous，无需监控）
2. ⚠️ **tmux 仅用于手动交互**（需要人类实时参与）

### 1. Claude Code 交互式操作（tmux 手动模式）

> **⚠️ 注意**：tmux 用于人类手动交互，autonomous 任务使用 sessions_spawn

Claude Code 是一个终端 AI 编码工具，通过 tmux 可以实现交互式操作。

#### 基础配置

```bash
# Socket 路径约定
SOCKET_DIR="${TMPDIR:-/tmp}/openclaw-tmux-sockets"
mkdir -p "$SOCKET_DIR"
SOCKET="$SOCKET_DIR/claude-code.sock"
```

#### 启动 Claude Code 会话

```bash
# 创建新会话
SESSION="claude-dev"
tmux -S "$SOCKET" new-session -d -s "$SESSION" -x 120 -y 40

# 进入工作目录
tmux -S "$SOCKET" send-keys -t "$SESSION" "cd /path/to/project" Enter

# 启动 Claude Code
tmux -S "$SOCKET" send-keys -t "$SESSION" "claude" Enter

# 等待启动（首次需要确认信任目录）
sleep 5

# 确认信任目录（按 Enter 选择默认选项）
tmux -S "$SOCKET" send-keys -t "$SESSION" Enter
```

#### 发送命令

```bash
# 发送自然语言指令（使用 -l 避免特殊字符问题）
tmux -S "$SOCKET" send-keys -t "$SESSION" -l -- "你的指令内容"
tmux -S "$SOCKET" send-keys -t "$SESSION" Enter
```

#### 捕获输出

```bash
# 捕获最近 100 行输出
tmux -S "$SOCKET" capture-pane -p -t "$SESSION" -S -100
```

#### 等待完成

```bash
# 等待 Claude Code 完成任务（检测 shell prompt）
for i in {1..60}; do
  if tmux -S "$SOCKET" capture-pane -p -t "$SESSION" -S -3 | grep -q "❯"; then
    echo "任务完成"
    break
  fi
  sleep 2
done
```

#### 处理交互式确认

```bash
# 方案 A：启动时使用 --permission-mode acceptEdits（推荐）
tmux -S "$SOCKET" send-keys -t "$SESSION" "claude --permission-mode acceptEdits" Enter

# 方案 B：手动确认每个命令
# Claude Code 会询问是否执行命令
# 选项格式：1. Yes  2. Yes, don't ask again  3. No

# 选择选项
tmux -S "$SOCKET" send-keys -t "$SESSION" "1" Enter  # 选择 Yes
# 或
tmux -S "$SOCKET" send-keys -t "$SESSION" "2" Enter  # 选择 Yes, don't ask again
```

> 💡 **推荐使用 `--permission-mode acceptEdits`**，可自动接受编辑操作，避免每个命令都需要手动确认。

#### 清理会话

```bash
# 终止特定会话
tmux -S "$SOCKET" kill-session -t "$SESSION"

# 终止所有会话
tmux -S "$SOCKET" kill-server
```

### 2. 并行 Agent 模式

对于大型项目，可以同时运行多个 Claude Code 实例：

```bash
# 创建多个会话（使用 acceptEdits 自动接受编辑）
for i in 1 2 3; do
  tmux -S "$SOCKET" new-session -d -s "agent-$i" -x 120 -y 40
  tmux -S "$SOCKET" send-keys -t "agent-$i" "cd /path/to/project/worktree-$i" Enter
  tmux -S "$SOCKET" send-keys -t "agent-$i" "claude --permission-mode acceptEdits" Enter
done

# 并行发送任务
tmux -S "$SOCKET" send-keys -t agent-1 -l -- "实现用户认证模块" Enter
tmux -S "$SOCKET" send-keys -t agent-2 -l -- "实现数据访问层" Enter
tmux -S "$SOCKET" send-keys -t agent-3 -l -- "编写单元测试" Enter

# 轮询检查状态
for sess in agent-1 agent-2 agent-3; do
  if tmux -S "$SOCKET" capture-pane -p -t "$sess" -S -3 | grep -q "❯"; then
    echo "$sess: 完成"
  else
    echo "$sess: 运行中..."
  fi
done
```

---

## 📋 Speckit 工作流

### 工作流概览

```
┌─────────────────────────────────────────────────────────────┐
│                    Speckit 工作流                            │
├─────────────────────────────────────────────────────────────┤
│  1. init          → 初始化项目结构                           │
│  2. constitution  → 建立项目宪法（工程原则）                  │
│  3. specify       → 编写功能规范（what & why）               │
│  4. clarify       → 需求澄清（消除歧义）⚠️ 强制执行 ≥1 次    │
│  5. plan          → 生成实现计划（how）                      │
│  6. tasks         → 拆分任务（可执行单元）                   │
│  7. analyze       → 一致性分析（质量门禁）⚠️ 强制执行 ≥1 次  │
│  8. implement     → 自动实施（代码生成）                     │
└─────────────────────────────────────────────────────────────┘
```

**⚠️ 强制阶段（不可跳过）**：
- **clarify**：必须执行至少 1 次（推荐 2 次）
- **analyze**：必须执行至少 1 次（推荐 2 次）

即使内容看起来完整/一致，也必须由 AI 主动验证。

### 🤝 人类介入点（Human Checkpoints）

SDD 工作流中，以下阶段**必须**等待人类确认：

| 阶段 | 介入原因 | 介入方式 |
|------|----------|----------|
| **clarify** | 需求歧义需要澄清 | 发送问题 → 等待回复 |
| **analyze** | 一致性问题需要决策 | 发送报告 → 等待确认 |
| **implement** | 大规模代码变更 | 可选：发送摘要 → 等待确认 |

#### 介入机制

```
┌─────────────────────────────────────────────────────────────┐
│                    人类介入流程                              │
├─────────────────────────────────────────────────────────────┤
│  1. Agent 到达介入点                                         │
│  2. 暂停工作流                                               │
│  3. 通过 Feishu 发送问题/报告                                │
│  4. 等待用户回复                                             │
│  5. 收到回复后继续执行                                       │
└─────────────────────────────────────────────────────────────┘
```

#### 示例：clarify 阶段交互

```
【Agent → 用户】
📋 Speckit 澄清阶段发现问题：

1. 天气查询工具是否需要支持多语言？
   - A: 仅支持中文城市名
   - B: 支持中英文城市名

2. 是否需要缓存天气数据以减少 API 调用？
   - A: 不缓存，每次实时查询
   - B: 缓存 5 分钟

请回复选项（如：1B 2A）或提供详细说明。

【用户 → Agent】
1B 2A

【Agent → 用户】
收到，继续执行 /speckit.plan...
```

#### 自动继续条件

以下情况可以**自动继续**，无需人工确认：
- clarify 连续 2 次无问题
- analyze 连续 2 次无问题
- 用户明确表示"全部自动执行"

#### 配置介入级别

在项目宪法中可以配置介入级别：

```markdown
## Development Workflow

### 人类介入配置
- **严格模式**：每个 clarify/analyze 都等待确认
- **平衡模式**：连续 2 次无问题后自动继续（默认）
- **自动模式**：仅在发现问题时通知，不等待
```

#### 介入判断逻辑

```
┌─────────────────────────────────────────────────────────────┐
│                    是否需要人类介入？                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  clarify/analyze 发现问题                                    │
│         │                                                    │
│         ▼                                                    │
│  ┌─────────────────────┐                                     │
│  │ 信息是否完整？       │                                     │
│  └─────────────────────┘                                     │
│      │         │                                             │
│     完整      不完整/疑义                                     │
│      │         │                                             │
│      ▼         ▼                                             │
│  ┌────────┐  ┌──────────────┐                                │
│  │ 自己决策 │  │ 转发用户确认 │                                │
│  │ 补充规范 │  │ 等待回复     │                                │
│  │ 继续执行 │  │ 收到后继续   │                                │
│  └────────┘  └──────────────┘                                │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

#### 自动决策条件（无需介入）

| 情况 | 我的处理 |
|------|----------|
| 信息完整，只是细节缺失 | 基于最佳实践自行补充 |
| 常规技术选择（如用 requests 还是 httpx） | 选择主流方案，记录理由 |
| 宪法已有明确规定 | 直接遵循宪法执行 |
| clarify 连续 2 次无问题 | 自动进入下一阶段 |
| 简单项目，需求明确 | 全程自动化 |

#### 需要介入的条件

| 情况 | 原因 |
|------|------|
| 多个方案各有优劣，需要业务决策 | 我无法判断业务优先级 |
| 需求有明显矛盾或冲突 | 需要澄清真实意图 |
| 涉及外部依赖或资源 | 需要确认可用性 |
| 超出宪法规定的边界 | 需要明确约束 |
| analyze 发现严重一致性问题 | 需要决定修复方向 |

#### 示例

**场景 1：自动决策**
```
发现：spec 未指定 HTTP 库
判断：这是技术细节，requests 是主流方案
处理：选择 requests，在 plan.md 中记录理由
结果：继续执行，不中断
```

**场景 2：需要介入**
```
发现：spec 说"支持多语言"，但未指定哪些语言
判断：这是业务决策，影响范围大
处理：暂停，发送问题给用户
消息：📋 需要确认支持哪些语言？
      A: 中英文
      B: 中英日韩
      C: 其他（请说明）
```

### 阶段详解

> **⚠️ 重要**：以下阶段 2-8 的命令（`/speckit.*`）都在 **Claude Code** 中执行，不是 Specify CLI 命令

#### 阶段 1：初始化（specify init）

```bash
# 安装 Speckit
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git

# 初始化新项目
specify init <项目名称>

# 在现有项目中初始化
specify init .
```

**产物**：
- `.specify/` 目录：配置和模板
- `templates/` 目录：规范文档模板
- `scripts/` 目录：辅助脚本
- Agent 配置文件（CLAUDE.md/CURSOR.md）

#### 阶段 2：建立宪法（/speckit.constitution）

定义项目的工程原则和质量标准。

**示例指令**：
```bash
/speckit.constitution 创建项目宪法，要求：
1. 测试覆盖率 ≥ 80%
2. 使用 TypeScript 严格模式
3. 遵循 RESTful API 设计原则
4. 所有 API 必须进行身份验证
5. 敏感数据必须加密存储
```

**产物**：`.specify/memory/constitution.md`

#### 阶段 3：功能规范（/speckit.specify）

描述"要做什么"和"为什么做"，**专注于业务需求**。

**示例指令**：
```bash
/speckit.specify 构建一个用户认证系统：
- 支持邮箱+密码登录
- 支持 OAuth 第三方登录（Google、GitHub）
- 支持 JWT 令牌刷新
- 支持账户锁定和解锁
- 记录登录日志
```

**产物**：`specs/001-<特性名>/spec.md`

#### 阶段 4：需求澄清（/speckit.clarify）

**最关键的阶段**，消除需求歧义。

⚠️ **强制要求**：
- **必须至少执行 1 次** `/speckit.clarify`
- 即使 spec 看起来完整，也必须由 AI 检查
- 第一次无问题 → 执行第二次确认
- 第二次仍无问题 → 才能进入 plan 阶段

```bash
# 主动澄清
/speckit.clarify 目标是轻量化实现：
1. 不需要记住历史登录
2. 锁定时间固定 30 分钟

# 模糊性扫描（推荐连续执行直到无问题）
/speckit.clarify
```

**关键点**：连续两次 `/speckit.clarify` 无问题才进入下一阶段。

#### 阶段 5：实现计划（/speckit.plan）

确定"怎么做"，**需要明确技术栈**。

```bash
/speckit.plan 使用技术栈：
- 后端：Go 1.21+ 标准库
- 数据库：PostgreSQL
- 缓存：Redis
- 认证：JWT
- 遵循宪法规范
```

**产物**：
- `plan.md`：技术实现计划
- `data-model.md`：数据模型
- `research.md`：技术调研
- `contracts/`：API 契约

#### 阶段 6：任务拆分（/speckit.tasks）

将计划拆分为可执行任务。

```bash
/speckit.tasks
```

**产物**：`tasks.md`，包含：
- 任务描述
- 目标文件路径
- 依赖关系
- 并行标记 `[P]`
- 实现指导

#### 阶段 7：一致性分析（/speckit.analyze）

**质量门禁**，确保规范完整一致。

⚠️ **强制要求**：
- **必须至少执行 1 次** `/speckit.analyze`
- 即使实现看起来一致，也必须由 AI 检查
- 第一次无问题 → 执行第二次确认
- 第二次仍无问题 → 才能进入 implement 阶段

```bash
/speckit.analyze

# 发现问题时修复
# 修复所有问题
```

**关键点**：连续两次分析无问题才能进入实施。

#### 阶段 8：自动实施（/speckit.implement）

**🎯 最终目标**：完成代码实现，不是写文档

按任务顺序生成代码。

```bash
# 开始实施
/speckit.implement 严格遵循宪法规范 @.specify/memory/constitution.md

# 继续实施（Agent 暂停时）
/speckit.implement 继续实现剩余阶段
```

**完成标准**：
- ✅ 代码已实现（不是文档）
- ✅ 测试已通过
- ✅ 功能可运行

**🚨 强制验收检查点（必须执行）**：

```bash
# 1. 语法检查（必须通过）
python3 -m py_compile <项目目录>/app/main.py

# 2. 核心功能测试（至少 1 个通过）
cd <项目目录> && poetry run pytest tests/ -v

# 3. 服务启动验证（至少能启动）
cd <项目目录> && timeout 5 poetry run uvicorn app.main:app || true
```

**验收失败处理**：
- ❌ 语法错误 → 修复后才能标记完成
- ❌ 测试失败 → 至少修复核心测试
- ❌ 服务无法启动 → 调试基础依赖问题

**核心原则**：
> **可运行 > 完整性**
>
> 一个能跑通的核心功能，胜过 10 个未验证的完整模块。

**禁止行为**：
- ❌ 配置未使用的外部服务（MinIO、SendGrid 等）
- ❌ 生成空测试文件假装有测试
- ❌ 只写代码不验证可运行性

---

## 📐 开发最佳实践

### 1. 需求表达原则

| 原则 | 说明 | 示例 |
|------|------|------|
| **结构化** | 使用规范文档而非散落 prompt | spec.md > 对话记录 |
| **可追溯** | 需求有明确来源和理由 | "因为 X，所以需要 Y" |
| **可验证** | 有明确的验收标准 | "支持 100 并发请求" |

### 2. 质量控制

```
┌─────────────────────────────────────────┐
│              质量门禁                    │
├─────────────────────────────────────────┤
│  clarify → 连续2次无问题                 │
│  analyze → 连续2次无问题                 │
│  implement → 每阶段测试通过              │
└─────────────────────────────────────────┘
```

### 3. 迭代管理

| 场景 | 处理方式 |
|------|----------|
| **需求变更** | 开启新迭代周期，新建分支 |
| **Bug 修复** | Agent 实现导致的 → 直接 prompt 修复<br>规范问题 → 新迭代 |
| **功能扩展** | 新迭代，MVP 先行 |
| **上下文丢失** | 规范文档是锚点，不依赖对话 |

### 4. 成本优化

| 策略 | 效果 |
|------|------|
| 使用规范文档 | 效率提升 10-30 倍 |
| 国产模型组合 | 成本显著降低 |
| 并行 Agent | 时间节省 |
| 质量前置 | 减少返工 |

### 5. 会话管理

```
┌─────────────────────────────────────────┐
│           会话分工建议                    │
├─────────────────────────────────────────┤
│  咨询会话：需求分析、架构设计             │
│  开发会话：Speckit + Agent 实现          │
│  一个迭代周期 = 一个会话                  │
└─────────────────────────────────────────┘
```

---

## 🚀 快速开始模板

### 场景 A：全新项目

```bash
# 1. 初始化项目
specify init my-project
cd my-project

# 2. 通过 Claude Code 执行 Speckit 工作流
# （使用上述 tmux 命令启动 Claude Code）

# 3. 在 Claude Code 中依次执行：
/speckit.constitution [宪法内容]
/speckit.specify [功能描述]
/speckit.clarify
/speckit.plan [技术栈]
/speckit.tasks
/speckit.analyze
/speckit.implement 严格遵循宪法规范
```

### 场景 B：复杂需求分阶段

```bash
# 迭代 1：MVP
/speckit.specify 实现核心功能 A

# 迭代 2：扩展
/speckit.specify 添加功能 B

# 迭代 3：优化
/speckit.specify 性能优化和 Bug 修复
```

### 场景 C：并行开发

```bash
# 使用 git worktree 创建多个工作目录
git worktree add ../project-feature-a feature-a
git worktree add ../project-feature-b feature-b

# 启动多个 Claude Code 实例
# 每个 worktree 一个 Agent
```

---

## 📁 目录结构

```
project-root/
├── .specify/
│   ├── memory/
│   │   └── constitution.md    # 项目宪法
│   ├── scripts/               # 辅助脚本
│   └── templates/             # 规范模板
├── specs/
│   └── 001-<feature>/
│       ├── spec.md            # 功能规范
│       ├── plan.md            # 技术方案
│       ├── tasks.md           # 任务拆分
│       ├── data-model.md      # 数据模型
│       ├── research.md        # 技术调研
│       ├── contracts/         # API 契约
│       └── checklists/        # 检查清单
├── src/                       # 源代码
└── tests/                     # 测试代码
```

---

## ⚠️ 常见问题

### Q1: specify init 失败？
**原因**：网络问题或 GitHub 限流
**解决方案**：
1. 使用 `--force` 跳过确认
2. 设置 GitHub Token：`export GH_TOKEN=xxx`
3. 使用代理或更换网络

### Q2: specify init 卡住？
**原因**：交互式确认等待输入
**解决方案**：
```bash
# 使用 --here --force 跳过确认
specify init . --here --force --ai claude --no-git
```

### Q3: 需求澄清不完怎么办？
采用**分阶段、小粒度**拆分，每个迭代只做 MVP。

### Q4: 上下文丢失怎么办？
规范文档是锚点，不依赖对话历史。重要阶段提醒关键约束。

### Q5: 实现一半发现需求错了？
放弃当前迭代，git 回滚，重新开始。

### Q6: 前端开发怎么做？
借助组件库（shadcn、heroui），让 Agent 使用现成组件。

### Q7: Claude Code 连接失败？
**错误**：`Unhandled stop reason: network_error`
**原因**：Gateway 网络问题
**解决方案**：
```bash
# 检查 gateway 状态
openclaw gateway status

# 重启 gateway
openclaw gateway restart
```

### Q8: 项目初始化超时？
**原因**：Speckit 模板下载慢
**解决方案**：脚本已内置 60 秒超时和降级方案

### Q9: `python` vs `python3` 问题？
**原因**：Claude Code 生成的代码使用 `python3`，但系统只有 `python3`
**解决方案**：
1. 在测试时使用 `python3` 而非 `python`
2. 或在代码中添加 shebang：`#!/usr/bin/env python3`

### Q10: 外部 API 网络不可达？
**原因**：某些 API（如 wttr.in）国内被 GFW 限制
**解决方案**：设置代理环境变量
```bash
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
python3 src/weather.py 北京
```

### Q11: 交互式确认太多？
**原因**：Claude Code 默认每个命令都需要确认
**解决方案**：使用 `--permission-mode` 参数
```bash
# 方案 A：自动接受编辑操作（推荐）
claude --permission-mode acceptEdits

# 方案 B：跳过所有权限检查（仅限沙箱环境）
claude --dangerously-skip-permissions

# 在脚本中使用
./claude-code-helper.sh start my-project /path/to/project acceptEdits
```

---

## 🔧 问题排查清单

遇到问题时按此顺序检查：

```
1. [ ] Gateway 是否正常运行？
   → openclaw gateway status

2. [ ] 大模型 API 是否可用？
   → 测试简单对话

3. [ ] 环境依赖是否满足？
   → ~/.openclaw/skills/sdd-dev-workflow/scripts/check-environment.sh

4. [ ] Speckit 是否可用？
   → specify --help

5. [ ] 网络是否通畅？
   → curl -s https://api.github.com | head -5

6. [ ] tmux 会话是否正常？
   → tmux -S /tmp/openclaw-tmux-sockets/claude-code.sock ls
```

---

## 🔄 长时间运行 Agent

> **✅ 所有项目默认支持断点续传**，无需额外配置。`init-project.sh` 会自动创建 `.task-context/` 目录。

### 核心问题

长时间运行 Agent 面临的挑战：

| 挑战 | 说明 |
|------|------|
| **上下文丢失** | Context window 溢出，忘记之前的工作 |
| **进度中断** | 网络断开、服务重启导致任务中断 |
| **状态不可知** | 不知道任务执行到哪一步 |
| **无法恢复** | 中断后无法从断点继续 |

---

### 解决方案：断点续传机制

```
┌─────────────────────────────────────────┐
│         长时间运行工作流                 │
├─────────────────────────────────────────┤
│                                          │
│  Initializer Agent（首次）               │
│    ↓ 创建                                │
│  .task-context/                          │
│    ├── progress.json     # 进度跟踪      │
│    ├── checkpoint.md     # 检查点快照    │
│    └── session-log.md    # 会话日志      │
│                                          │
│  Coding Agent（多次运行）                │
│    ↓ 读取                                │
│  progress.json → 恢复上下文              │
│    ↓ 执行                                │
│  增量任务 → 更新进度                     │
│    ↓ 保存                                │
│  checkpoint.md → 断点续传                │
│                                          │
└─────────────────────────────────────────┘
```

---

### 进度跟踪文件

#### progress.json（进度状态）

```json
{
  "projectId": "my-app",
  "projectName": "用户认证系统",
  "status": "in_progress",
  "currentPhase": "implement",
  "phases": {
    "constitution": "completed",
    "specify": "completed",
    "clarify": "completed",
    "plan": "completed",
    "tasks": "completed",
    "analyze": "completed",
    "implement": "in_progress"
  },
  "currentTask": {
    "index": 3,
    "total": 10,
    "description": "实现用户认证 API",
    "file": "src/auth/api.py"
  },
  "artifacts": {
    "constitution": ".specify/memory/constitution.md",
    "spec": "specs/001-auth/spec.md",
    "plan": "specs/001-auth/plan.md",
    "tasks": "specs/001-auth/tasks.md"
  },
  "startTime": "2026-03-10T08:00:00Z",
  "lastUpdate": "2026-03-10T09:45:00Z",
  "estimatedCompletion": "2026-03-10T12:00:00Z",
  "checkpoints": [
    {
      "timestamp": "2026-03-10T08:30:00Z",
      "phase": "specify",
      "summary": "完成需求规范"
    },
    {
      "timestamp": "2026-03-10T09:00:00Z",
      "phase": "plan",
      "summary": "完成技术方案设计"
    }
  ]
}
```

#### checkpoint.md（检查点快照）

```markdown
# 检查点 - 2026-03-10 09:45

## 📍 当前位置
- 阶段：implement（代码实施）
- 任务：3/10（实现用户认证 API）
- 文件：src/auth/api.py

## ✅ 已完成
- [x] 项目初始化
- [x] 需求规范（spec.md）
- [x] 技术方案（plan.md）
- [x] 任务拆分（tasks.md）
- [x] 任务1：项目结构搭建
- [x] 任务2：数据库模型定义

## 🔄 进行中
- [ ] 任务3：用户认证 API
  - [x] POST /auth/register
  - [x] POST /auth/login
  - [ ] POST /auth/refresh（当前）
  - [ ] POST /auth/logout

## 📋 待办
- [ ] 任务4：JWT 令牌生成
- [ ] 任务5：登录日志记录
- [ ] 任务6：单元测试
- [ ] 任务7：集成测试
- [ ] 任务8：API 文档
- [ ] 任务9：性能优化
- [ ] 任务10：部署配置

## 🚨 遇到的问题
- 无

## 🤔 需要的决策
- 无

## 💡 下次恢复指令
```
继续实现 POST /auth/refresh 接口
参考 specs/001-auth/plan.md 第3节"认证流程"
文件：src/auth/api.py 第45行
```
```

---

### 使用方式

#### 标准流程（推荐）

所有项目默认支持断点续传，直接用即可：

```bash
# 1. 创建项目（自动创建 .task-context/）
~/.openclaw/skills/sdd-dev-workflow/scripts/init-project.sh my-app

# 2. 启动开发
cd ~/openclaw/workspace/projects/my-app
claude --permission-mode acceptEdits
```

#### 恢复中断的任务

**方式1：sessions_spawn 继续执行（推荐）**

```javascript
sessions_spawn({
  task: "继续开发 [项目名]，读取 .task-context/checkpoint.md 恢复上下文",
  agentId: "dev-agent",
  runTimeoutSeconds: 7200
})
```

**方式2：手动继续**

直接对话描述任务，我会自动读取 checkpoint.md 恢复上下文。

#### 手动初始化（已存在项目）

如果项目已存在，但缺少 `.task-context/`：

```bash
# 运行 init-project.sh 会自动创建
~/.openclaw/skills/sdd-dev-workflow/scripts/init-project.sh
```

---

### 自动化监控

#### Heartbeat 统一监控（推荐）

**机制**：Gateway 每30分钟触发 Heartbeat，统一检查所有任务

**检查逻辑**：
1. 扫描 `projects/*/.task-context/progress.json`
2. 对每个 `status="in_progress"` 的项目：
   - 检查 `lastUpdate` 是否超过10分钟
   - 超过 → 检查 tmux session 状态
   - 发送通知（不自动恢复）

**优势**：
- ✅ 单一入口，统一管理
- ✅ 无冲突（只读检查）
- ✅ 支持多任务并发
- ✅ 不干扰运行中任务

**配置**：详见 `HEARTBEAT.md`

**不推荐**：
- ❌ 独立 cron job（增加复杂度）
- ❌ 自动恢复脚本（可能误判干扰）

---

### 最佳实践

#### 1. 任务粒度控制

| 任务大小 | 建议 |
|---------|------|
| 太大（>1小时） | 拆分成更小任务 |
| 适中（30分钟-1小时） | ✅ 推荐 |
| 太小（<15分钟） | 合并成更大任务 |

#### 2. 检查点频率

| 情况 | 频率 |
|------|------|
| 关键任务 | 每个子任务完成 |
| 普通任务 | 每个任务完成 |
| 探索性开发 | 阶段性里程碑 |

#### 3. 上下文锚点

确保每次恢复时能快速回到工作状态：

| 锚点 | 内容 |
|------|------|
| **规范文档** | spec.md, plan.md, tasks.md |
| **进度文件** | progress.json |
| **检查点** | checkpoint.md（包含具体代码位置） |
| **会话日志** | session-log.md（可选） |

#### 4. 错误处理

遇到错误时的处理流程：

```
1. 记录错误到 checkpoint.md
2. 标记 status="blocked"
3. 发送通知给用户
4. 等待用户决策
5. 恢复后更新 status="in_progress"
```

---

### 与 Speckit 集成

长时间运行工作流与 Speckit 各阶段的关系：

| Speckit 阶段 | progress.json 状态 | 检查点内容 |
|-------------|-------------------|-----------|
| constitution | `"currentPhase": "constitution"` | 宪法创建完成 |
| specify | `"currentPhase": "specify"` | spec.md 路径 |
| clarify | `"currentPhase": "clarify"` | 澄清的问题和答案 |
| plan | `"currentPhase": "plan"` | plan.md 路径 |
| tasks | `"currentPhase": "tasks"` | tasks.md 路径 |
| analyze | `"currentPhase": "analyze"` | 分析结果 |
| implement | `"currentPhase": "implement"` | 当前任务索引 |

---

### 示例：完整流程

#### 项目：用户认证系统（预计4小时）

```bash
# ========== 首次启动（08:00）==========
cd ~/openclaw/workspace/projects
specify init auth-system
cd auth-system
mkdir -p .task-context

# 创建 progress.json
cat > .task-context/progress.json << 'EOF'
{
  "projectId": "auth-system",
  "projectName": "用户认证系统",
  "status": "pending",
  "currentPhase": "constitution"
}
EOF

# 启动 Claude Code
claude --permission-mode acceptEdits

# Claude Code 内执行：
/speckit.constitution 创建项目宪法
/speckit.specify 构建用户认证系统：邮箱登录、OAuth、JWT
/speckit.clarify
/speckit.plan Go 1.21 + PostgreSQL + Redis
/speckit.tasks
/speckit.analyze

# 更新进度（自动或手动）
# progress.json: currentPhase = "implement", currentTask.index = 1
# checkpoint.md: 记录任务1开始

/speckit.implement 严格遵循宪法规范

# ========== 中断（09:30，完成3/10任务）==========
# 网络断开，Claude Code 退出

# ========== 恢复（10:00）==========
cd ~/openclaw/workspace/projects/auth-system
claude --permission-mode acceptEdits

# 发送恢复指令：
"阅读 .task-context/progress.json 和 checkpoint.md，继续执行任务4"

# Claude Code 自动：
# 1. 读取 progress.json → 知道在 implement 阶段
# 2. 读取 checkpoint.md → 知道任务4是"JWT令牌生成"
# 3. 读取 tasks.md → 获取任务4的详细要求
# 4. 继续执行

# ========== 完成（12:00）==========
# 所有任务完成
# progress.json: status = "completed"
# checkpoint.md: 最终检查点
```

---


## 真正的 Autonomous Agent 方案（架构升级）

> **⚠️ 重要变更**：废弃 tmux 伪 agent → 使用 sessions_spawn 真正的 autonomous agent

### 之前方案的问题

**tmux + 遥控**（伪 agent）：
- ❌ 我需要主动检查 → 发现卡住 → 手动干预
- ❌ Claude Code 本身不是 autonomous（会暂停等批准）
- ❌ 依赖外部循环监控

### 新方案：sessions_spawn

**真正 autonomous**：
- ✅ 子 agent 自己决策执行
- ✅ 无需我主动监控
- ✅ 完成后自动通知

### 配置步骤（一次性）

**步骤1：配置 Gateway 支持子 Agent**

编辑 `~/.openclaw/openclaw.json`，在 `agents.list` 中添加 `main` agent 的子 agent 权限：

```json
{
  "agents": {
    "list": [{
      "id": "main",
      "subagents": {
        "allowAgents": ["dev-agent", "research-agent", "test-agent"]
      }
    }]
  }
}
```

或使用 Gateway tool：
```javascript
gateway({
  action: "config.patch",
  raw: {
    agents: {
      list: [{
        id: "main",
        subagents: {
          allowAgents: ["dev-agent", "research-agent", "test-agent"]
        }
      }]
    }
  }
})
```

**步骤2：验证配置**

```javascript
agents_list()
// 应该看到 allowAgents 中的 agent IDs

sessions_spawn({
  task: "测试任务",
  agentId: "dev-agent",
  runTimeoutSeconds: 60
})
// 返回 status: "accepted" 表示成功
```

### 使用方式

**创建开发任务**：

```javascript
sessions_spawn({
  task: `
    开发 AI-First 长租公寓系统，**目标：完成代码实现，不是写文档**

    ## 工具链协作方式

    1. **Specify CLI（仅初始化）**：
       - cd /path/to/workspace/projects/your-project
       - specify init .（如果项目未初始化）

    2. **Claude Code（执行开发）**：
       启动 Claude Code 并执行：
       - /speckit.constitution 定义项目宪法
       - /speckit.specify 创建功能规范
       - /speckit.clarify 需求澄清（至少2次）
       - /speckit.plan 实现计划
       - /speckit.tasks 任务拆分
       - /speckit.analyze 一致性分析（至少2次）
       - /speckit.implement **代码实现（最终目标）**

    ## 完成标准

    - ✅ 代码已实现（不是文档）
    - ✅ 测试已通过（至少 1 个核心测试）
    - ✅ 功能可运行（服务能启动）

    ## 🚨 强制验收检查（必须执行）

    \`\`\`bash
    # 1. 语法检查
    python3 -m py_compile backend/app/main.py

    # 2. 核心测试
    cd backend && poetry run pytest tests/test_api/ -v

    # 3. 服务启动验证
    cd backend && timeout 5 poetry run uvicorn app.main:app || true
    \`\`\`

    ## 核心原则

    **可运行 > 完整性**

    禁止：
    - ❌ 配置未使用的外部服务
    - ❌ 生成空测试文件
    - ❌ 只写代码不验证

    ## 工作目录

    /path/to/workspace/projects/your-project
  `,
  agentId: "dev-agent",
  runTimeoutSeconds: 7200,  // 2小时超时
  cleanup: "keep"  // 保留 session 供后续查看
})
```

**agentId 规范**：
- `dev-agent`：开发任务（SDD 工作流）
- `research-agent`：深度研究任务
- `test-agent`：测试任务

**优点**：
- ✅ 真正 autonomous（自己决策执行）
- ✅ 可移植（skill 包含配置说明）
- ✅ 其他 OpenClaw 实例安装 skill 后即可使用

### 错误处理

#### 常见错误

| 错误 | 原因 | 解决方法 |
|------|------|----------|
| `forbidden` | agent ID 未配置 | 添加到 `allowAgents` 列表 |
| `timeout` | 任务超时 | 增加 `runTimeoutSeconds` |
| `agent not found` | agent ID 不存在 | 检查 `agents_list()` |

#### 错误示例

```javascript
// 错误：agent 未配置
{
  "error": "forbidden",
  "message": "Agent 'dev-agent' not in allowAgents list"
}

// 解决：配置 Gateway
gateway({
  action: "config.patch",
  raw: {
    agents: {
      list: [{
        id: "main",
        subagents: {
          allowAgents: ["dev-agent", "research-agent", "test-agent"]
        }
      }]
    }
  }
})
```

### 监控子 Agent 进度

#### 方式1：查看 session 列表

```javascript
sessions_list({ kinds: ["isolated"] })
// 查找 agentId 对应的 session
```

#### 方式2：读取项目进度文件

```bash
# 查看进度
cat projects/your-project/.task-context/progress.json

# 查看检查点
cat projects/your-project/.task-context/checkpoint.md
```

#### 方式3：Heartbeat 自动监控

Heartbeat 会自动检查所有 in_progress 任务的进度，发现异常时通知。

---

---

### 一次性完整任务 Prompt 模板

#### ⚠️ 强制规则（CRITICAL）

**必须执行的阶段（不可跳过）**：
- ✅ **clarify 阶段**：必须至少执行 1 次 `/speckit.clarify`
  - 即使 spec 看起来完整，也必须由 AI 检查
  - 第一次无问题 → 执行第二次确认
  - 第二次仍无问题 → 才能进入 plan 阶段

- ✅ **analyze 阶段**：必须至少执行 1 次 `/speckit.analyze`
  - 即使实现看起来一致，也必须由 AI 检查
  - 第一次无问题 → 执行第二次确认
  - 第二次仍无问题 → 才能进入 implement 阶段

**原因**：AI 需要主动验证，而不是基于"看起来没问题"的假设跳过

#### 模板结构

```markdown
## 📋 任务目标

[简洁描述任务目标]

## 📦 交付物

- [ ] 交付物1：[描述]
- [ ] 交付物2：[描述]

## ⚠️ 强制步骤（SDD 流程）

- [ ] 执行 /speckit.clarify（至少 1 次）
- [ ] 执行 /speckit.analyze（至少 1 次）

## 🚫 不要做的事

- ❌ 询问可自动决策的问题
- ❌ 跳过 clarify 或 analyze 阶段

## 📢 通知策略

- ✅ 阶段转换时通知（clarify → plan → tasks → analyze → implement）
- ✅ Heartbeat 定期汇总进度（每30分钟）
- ✅ 遇到阻塞或需要决策时立即通知

## ✅ 完成标准

- [所有交付物已完成]
- [clarify 和 analyze 已各执行至少 1 次]
- [更新 progress.json 为 "completed"]
- [更新 checkpoint.md 最终状态]

## 🚀 执行

完成后发送通知：
- 状态：完成/阻塞
- 交付物：[列表]
- 位置：[项目路径]
```

#### 示例：SDD Plan 阶段

```markdown
## 📋 任务目标

完成 SDD plan 阶段，生成技术实现方案

## 📦 交付物

- [ ] specs/001-your-project-system/plan.md（技术方案）
  - 技术栈选型
  - 架构设计
  - 模块划分
  - 数据库设计
  - API 设计

## 📝 输入文件

- specs/001-your-project-system/spec.md（已完成）
- .specify/memory/constitution.md（已创建）

## ⚠️ 强制步骤（plan 阶段前）

1. 执行 `/speckit.clarify` 检查需求歧义
2. 如第一次无问题，执行第二次 `/speckit.clarify` 确认
3. 两次均无问题后，才能执行 `/speckit.plan`

## 🚫 不要做的事

- ❌ 询问可自主决策的技术选型
- ❌ 跳过 clarify 直接进入 plan

## ✅ 完成标准

- clarify 已执行至少 1 次（推荐 2 次）
- plan.md 已创建且内容完整
- progress.json 更新为：currentPhase="plan", phases.plan="completed", phases.clarify="completed"
- checkpoint.md 记录完成状态

## 🚀 执行

运行命令（按顺序）：
/speckit.clarify  # 第一次检查
/speckit.clarify  # 第二次确认（可选但推荐）
/speckit.plan     # 生成实现计划

完成后发送通知：
📊 SDD Plan 阶段完成

项目：AI-First 长租公寓系统
阶段：plan（2/8）
交付：specs/001-your-project-system/plan.md
澄清：已执行 2 次，无问题

下一步：运行 /speckit.tasks 生成任务清单
```

---

### 配置选项

在 `.task-context/config.json` 中配置：

```json
{
  "notificationPolicy": {
    "onComplete": true,          // 任务完成时通知
    "onBlocked": true,           // 遇到阻塞时通知
    "onDecision": true,          // 需要决策时通知
    "onPhaseChange": true,       // 阶段转换时通知 ✅
    "onProgress": true,          // 进度更新时通知 ✅（Heartbeat 触发）
    "quietHours": {              // 静默时段
      "start": "23:00",
      "end": "08:00"
    }
  }
}
```

### 进度反馈机制

**定期反馈**（通过 Heartbeat）：
- ⏰ 每 30 分钟（09:00-22:00）
- 📊 汇总所有 in_progress 任务进度
- 📝 内容：当前阶段、已耗时、已完成项

**阶段转换通知**：
- ✅ 进入新阶段时通知
- 📋 内容：阶段名称、交付物、下一步

**完成/阻塞/决策**：
- ✅ 立即通知

---

### 实施检查清单

在执行长时间任务前，确保：

- [ ] 使用"一次性完整任务 Prompt"模板
- [ ] **明确要求执行 clarify（至少 1 次）**
- [ ] **明确要求执行 analyze（至少 1 次）**
- [ ] 明确列出所有交付物
- [ ] 阶段转换时发送通知
- [ ] Heartbeat 定期汇总进度
- [ ] 更新 progress.json 和 checkpoint.md

---

## 🚨 任务卡住处理机制

> **原则**：主动解决 + 及时反馈，避免静默卡死

### 检测卡住的标准

| 情况 | 判断标准 | 超时阈值 |
|------|---------|---------|
| **API 无响应** | GLM-5/其他 API 超时 | 60秒 |
| **工具执行卡死** | 单个工具调用超时 | 120秒 |
| **进度停滞** | progress.json 未更新 | 10分钟 |
| **Claude Code 假死** | 无输出无响应 | 5分钟 |
| **循环错误** | 同一错误重复3次 | 立即 |

---

### 自动解决策略

#### 1. API 延迟
```
检测：API 调用 >60秒无响应
行动：
  - 重试1次（等待30秒）
  - 失败 → 降级方案（简化 prompt 或切换模型）
  - 失败 → 标记阻塞，通知用户
```

#### 2. 工具执行失败
```
检测：exec/read/write 返回错误
行动：
  - 分析错误类型
  - 可恢复 → 自动修复（如权限、路径问题）
  - 不可恢复 → 标记阻塞，通知用户
```

#### 3. 进度停滞
```
检测：10分钟内 progress.json 未更新
行动：
  - 检查 Claude Code 状态（tmux session）
  - 如假死 → kill + 重启 + 恢复任务
  - 如正常 → 发送提醒 prompt
```

#### 4. 循环错误
```
检测：同一错误重复3次
行动：
  - 记录错误详情
  - 标记 status="blocked"
  - 立即通知用户（附错误日志）
```

---

### 通知模板

#### 阻塞通知
```
🚨 任务阻塞

项目：{projectName}
阶段：{currentPhase}
任务：{task.index}/{task.total}

问题：
{错误描述}

尝试过的解决方案：
1. {方案1} - 失败
2. {方案2} - 失败

需要决策：
- [ ] 方案A：{描述}
- [ ] 方案B：{描述}
- [ ] 其他：{用户输入}

文件位置：{项目路径}
日志：.task-context/session-log.md
```

#### 恢复通知
```
✅ 任务已恢复

项目：{projectName}
问题：{原问题描述}
解决：{采取的行动}
当前：{新状态}

继续执行中...
```

---

### 超时监控脚本

创建 `.task-context/monitor.sh`：

```bash
#!/bin/bash
# 任务超时监控

PROJECT_DIR="$1"
TIMEOUT_MINUTES="${2:-10}"

progress_file="$PROJECT_DIR/.task-context/progress.json"
checkpoint_file="$PROJECT_DIR/.task-context/checkpoint.md"

# 检查最后更新时间
last_update=$(jq -r '.lastUpdate' "$progress_file")
last_epoch=$(date -d "$last_update" +%s)
now_epoch=$(date +%s)
diff_minutes=$(( (now_epoch - last_epoch) / 60 ))

if [ "$diff_minutes" -gt "$TIMEOUT_MINUTES" ]; then
  # 检查 tmux session 是否存活
  if tmux has-session -t "$(basename "$PROJECT_DIR")" 2>/dev/null; then
    # Session 存在，发送提醒
    tmux send-keys -t "$(basename "$PROJECT_DIR")" "继续执行任务" Enter
    echo "提醒已发送"
  else
    # Session 不存在，标记阻塞
    jq '.status = "blocked"' "$progress_file" > tmp.json && mv tmp.json "$progress_file"

    cat >> "$checkpoint_file" << EOF

## 🚨 阻塞（$(date '+%Y-%m-%d %H:%M:%S')）

**问题**：任务停滞 $diff_minutes 分钟
**原因**：tmux session 已终止
**状态**：等待用户恢复

**恢复指令**：
\`\`\`bash
cd $PROJECT_DIR
claude --permission-mode acceptEdits
# 发送："阅读 progress.json，继续执行任务"
\`\`\`
EOF

    # 发送通知
    curl -X POST "$GATEWAY_URL/api/message" \
      -H "Authorization: Bearer $GATEWAY_TOKEN" \
      -d "{\"channel\":\"feishu\",\"target\":\"<USER_OPEN_ID>\",\"message\":\"🚨 任务阻塞\\n\\n项目：$(jq -r '.projectName' \"$progress_file\")\\n问题：停滞 $diff_minutes 分钟\\n位置：$PROJECT_DIR\"}"
  fi
fi
```

---

### 最佳实践

#### 1. 定期检查进度
- Heartbeat 每30分钟检查一次 `progress.json`
- 如果 `lastUpdate` >10分钟 → 采取行动

#### 2. 错误自动记录
- 每次失败 → 记录到 `session-log.md`
- 包含：时间、错误、尝试的解决方案

#### 3. 降级方案
- API 超时 → 简化 prompt
- 工具失败 → 尝试替代方案
- 无法自动解决 → 立即通知用户

#### 4. 快速恢复
- 使用 `sessions_spawn` 继续任务
- checkpoint.md 包含恢复指令
- progress.json 保存完整状态

---

## 📚 参考资料

- [Speckit GitHub](https://github.com/github/spec-kit)
- [Claude Code 文档](https://docs.anthropic.com/claude-code)
- [SDD 规范驱动开发](https://github.com/github/spec-kit/blob/main/spec-driven.md)

---

## 🔗 相关 Skills

- `tmux` - 交互式 CLI 控制
- `github` - GitHub 操作
- `self-improving-agent` - 持续改进
