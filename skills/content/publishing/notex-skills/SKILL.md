---
name: notex-skills
description: "工作协同系统 CWork Key 授权入口，提供四套核心大模型能力。其一为 8 种内容创作技能（PPT、脑图等）的异步轮询生成；其二为 OPS 运营管理智能助手（ops-chat）的同步数据洞察接口；其三为 Notebook/Source 索引树与来源详情检索能力（支持本地索引缓存与全量定时刷新）；其四为 NoteX 链接带 Token 打开能力（支持返回前端可访问链接与可选自动打开浏览器）。"
metadata:
  openclaw:
    category: "social"
    tags: ['social', 'x', 'twitter']
    version: "1.0.0"
---

# NoteX Skills — 通用技能路由网关

**当前版本**: v1.4 | **接入渠道**: `CWork Key` 鉴权

本网关提供四套能力范式，分别对应**内容创作引擎**、**运营洞察助手**、**Notebook 来源检索**与**NoteX 链接带 Token 打开**。

---

## 1. 核心鉴权 (Authentication)

无论调用哪种技能，鉴权都必须先完成。**对用户只暴露 `CWork Key` 授权动作**，不暴露 Token 细节。

```http
GET https://cwork-web.mediportal.com.cn/user/login/appkey?appCode=cms_gpt&appKey={CWork Key}
```

### 1.1 统一前置鉴权规则（强约束）

所有接口调用（创作类 / OPS / 索引检索）都必须先做鉴权预检，且对外话术固定如下：

1. 若当前会话已有可用授权态：直接继续业务调用，不再向用户追问鉴权细节。
2. 若当前会话无可用授权态：只向用户索取/确认 `CWork Key` 授权。
3. 禁止在对话中向用户索取或解释 `access-token/x-user-id/personId/login` 等实现细节。
4. 禁止绕过鉴权直接调用业务 API。

### 1.2 内部执行规则（实现细节，不对用户暴露）

1. 若会话上下文已持有可用 `access-token + x-user-id`：直接复用。
2. 若无可用 Token 但有 `CWork Key`：调用换取接口获取 `xgToken/userId/personId` 后再请求业务接口。
3. 若两者都没有：停止调用，并在对话层仅提示“请先完成工作协同授权（CWork Key）”。
4. 后续业务请求 Header 继续携带：`x-user-id`、`access-token`，以及部分旧接口需要的 `personId`。

> 建议：将本次会话鉴权结果做短期本地缓存，避免同一会话重复换取。

### 1.3 环境约束（发布强约束）

1. `docs/skills/` 下所有文档、示例、脚本均仅使用生产域名。
2. NoteX 业务接口统一使用：`https://notex.aishuo.co/noteX`
3. CWork 授权接口统一使用：`https://cwork-web.mediportal.com.cn`
4. 严禁在发布内容中出现本地开发地址或非生产协议地址。

---

## 2. 内容创作类技能 (Asynchronous Creator)

覆盖从文本整理到视频渲染的 8 种高发算力场景，采用**队列投递 + 异步轮询**架构。

### 2.0 三要素（角色 / 能力 / 使用时机）

- 我是谁：NoteX 创作者智能生成助手，负责把输入素材转换成可交付的多媒体内容。
- 我能做什么：分发并执行 8 类创作任务（slide/infographic/video/audio/report/mindmap/quiz/flashcards），并返回可访问结果链接。
- 什么时候使用：当用户目标是“生成内容产物”（如 PPT、报告、音频、视频、脑图、测验、闪卡）时使用。
- 前置条件：调用前必须通过“1.1 统一前置鉴权规则”。

### 2.1 支持的创作技能 (`skill` 参数)
| 技能 ID | 产物形式 | 必填参数附加约束 | 预计渲染 |
|---|---|---|---|
| `slide` | PPT 演示文稿 | 需明确视觉风格 | 3~5 分钟 |
| `infographic` | 数据信息图 | 需明确配色风格 | 2~4 分钟 |
| `video` | 视频播客 | (无) | 5~10 分钟 |
| `audio` | 纯音频播客 | (无) | 3~6 分钟 |
| `report` | 深度分析报告 | (无) | 1~3 分钟 |
| `mindmap` | 结构化思维导图 | (无) | 1~2 分钟 |
| `quiz` | 测验练习题 | (无) | 1~2 分钟 |
| `flashcards` | 记忆闪卡 | (无) | 1~2 分钟 |

### 2.2 API 调用链路 (两步走)

**Step A: 投递异步任务**
```http
POST https://notex.aishuo.co/noteX/api/trilateral/autoTask
authorization: BP
x-user-id: {换取的userId}
access-token: {换取的xgToken}
personId: {换取的personId}
Content-Type: application/json

{
  "bizId": "skills_1709000000000",
  "bizType": "TRILATERA_SKILLS",
  "skills": ["slide"],
  "require": "商务简约风格，蓝白配色",
  "sources": [{"id": "src_001", "title": "标题", "content_text": "原文素材..."}]
}
```
*(响应返回 `taskId`)*

**Step B: 轮询结果直到完结**
```http
GET https://notex.aishuo.co/noteX/api/trilateral/taskStatus/{taskId}
```
*(每 60 秒轮询一次，最多 **20 次**，即最大超时时间 20 分钟；直到 `task_status` 为 `COMPLETED`，内部完成鉴权参数拼接后再把可访问链接提交给用户，不在话术中暴露 token 字段名)*

> 🌟 **大模型引导与越权拦截策略**：
> 关于如何向用户索要必要参数（针对不同形式索要时长或风格等），以及如何礼貌拒绝意图越权（例如：当用户要求“生成 Excel 或下载成 Word 文件”时，应明确拒绝并引导转化成支持的『分析报告』或『思维导图』），请务必参考系统内置的设定话术档案：👉 [`examples/notex-creator.md`](./examples/notex-creator.md)

---

## 3. OPS 运营数据洞察 (`ops-chat`)

专为内部系统后台打造的智能问答通道，对接 16 个底层观测本体工具（Function Calling），采用**短轮询 / 同步流式长连接**架构。

### 3.0 三要素（角色 / 能力 / 使用时机）

- 我是谁：OPS 运营智能助理，面向运营与管理场景提供数据问答服务。
- 我能做什么：调用运营数据工具链，输出用户、功能、告警、趋势等多维运营分析结果。
- 什么时候使用：当用户询问“运营数据、系统告警、用户活跃、功能使用、增长趋势”等问题时使用。
- 前置条件：调用前必须通过“1.1 统一前置鉴权规则”。

### 3.1 核心能力与权限
- 本技能强制校验用户的 `canViewOpsData` 内部查阅权限，无权限者统一拦截 403。
- 覆盖大盘看板统计、科室/项目组活跃排行、精准追踪某医生的流失节点、异常报错根因聚合分析等。
- 新增支持“注册队列 + 幻灯片闭环”分析：可直接回答“某日期后注册用户是否创建过幻灯片、创建次数、是否分享、分享是否被查看及查看次数”。

### 3.2 API 调用链路 (单发同步等待)

此接口内部将执行多达数十步的 ReAct 循环推理，网络超时上限需严格设定为 **300,000ms (5分钟)**。


```http
POST https://notex.aishuo.co/noteX/api/ops/ai-chat
authorization: BP
x-user-id: {换取的userId}
access-token: {换取的xgToken}
Content-Type: application/json

{
  "message": "帮我查一下最近一周的操作失误告警？"
}
```

**响应报文**：
```json
{
  "reply": "根据底盘数据，近期共发生了...",
  "historyCount": 3
}
```
*(注：服务端已自动记忆最近 6 轮对话上下文，客户端无需再次拼接历史)*

> 🌟 **大模型引导策略**：关于 16 个核心本体的逻辑链式拆解，以及遇到多名同姓氏用户时的追问确认协议，请查阅专属的管家设定指南： [`examples/ops-assistant.md`](./examples/ops-assistant.md)

---

## 4. Notebook 来源索引与详情检索 (Index + Details)

该能力用于回答“查看我名下所有 Notebook 的所有文件/来源”这类请求，核心是先拉**索引树**，再按需拉**最小详情**。

### 4.0 三要素（角色 / 能力 / 使用时机）

- 我是谁：Notebook 来源检索助手，负责管理“来源索引”和“最小上下文定位”。
- 我能做什么：构建并本地缓存索引树（仅 ID+名称），并按 notebook/source 返回最小详情（仅 ID+名称）。
- 什么时候使用：当用户要查看“我名下全部来源、某 notebook 下所有来源、某个 source 的定位信息”时使用。
- 前置条件：调用前必须通过“1.1 统一前置鉴权规则”。

### 4.1 接口一：全量索引树（推荐先调用）

```http
GET {NOTEX_BASE_URL}/api/notebooks/sources/index-tree?type=all
x-user-id: {userId}
access-token: {xgToken}
```

- 返回用户可访问范围内的 Notebook 树结构与每个 Notebook 的 Source 索引（仅 ID/名称）。
- `type` 支持：`all` | `owned` | `collaborated`，默认 `all`。

最小返回结构示例：
```json
{
  "generatedAt": "2026-03-10T09:00:00.000Z",
  "tree": [
    {
      "id": "nb_001",
      "name": "产品规划",
      "sources": [
        { "id": "src_101", "name": "需求评审纪要" }
      ],
      "children": []
    }
  ]
}
```

### 4.2 接口二：来源最小详情（按 notebookId 或 sourceId）

```http
GET {NOTEX_BASE_URL}/api/notebooks/sources/details?notebookId={notebookId}
GET {NOTEX_BASE_URL}/api/notebooks/sources/details?sourceId={sourceId}
x-user-id: {userId}
access-token: {xgToken}
```

- `notebookId` 模式：返回该 Notebook 下所有 Source 的最小详情（仅 `ID + 名称`）。
- `sourceId` 模式：返回单个 Source 的最小详情（仅 `ID + 名称`），并附带所属 Notebook 的 `ID + 名称`。

> 注：这里的 `context ID` 即 Source ID。该接口用于给 AI 定位上下文，不返回正文大字段。

最小返回结构示例：
```json
{
  "mode": "source",
  "notebook": { "id": "nb_001", "name": "产品规划" },
  "contexts": [
    { "id": "src_102", "name": "会议纪要" }
  ]
}
```

### 4.3 建议工作流（给 AI 的默认流程）

1. 先调用 `index-tree` 构建索引。
2. 将索引落盘到本地缓存（覆盖写，确保全量更新）。
3. AI 根据用户问题在索引中定位 `notebookId/sourceId`。
4. 调用 `details` 拉取最小上下文信息（`ID + 名称`）用于二次决策。

### 4.4 本地缓存目录建议

```text
docs/skills/cache/notebook-source-index/
  └── {userId}/
      ├── index-tree.json
      └── details/
          ├── notebook-{notebookId}.json
          └── source-{sourceId}.json
```

### 4.5 全量定时刷新（必须全量，不做增量）

推荐脚本（见 `/scripts/source-index-sync.js`）：

```bash
# 方式1（默认）：仅传 CWork Key，脚本内部自动完成授权并调用
node docs/skills/scripts/source-index-sync.js --mode index --base-url https://notex.aishuo.co/noteX --key <CWorkKey>

# 方式2：按 sourceId 拉取最小详情（仍只需 CWork Key）
node docs/skills/scripts/source-index-sync.js --mode detail --base-url https://notex.aishuo.co/noteX --key <CWorkKey> --source-id <sourceId>

# 每 60 分钟全量刷新一次索引（默认授权模式）
node docs/skills/scripts/source-index-sync.js --mode index --base-url https://notex.aishuo.co/noteX --key <CWorkKey> --interval-minutes 60

# 内部调试模式：可复用现有 token（不建议暴露给终端用户）
node docs/skills/scripts/source-index-sync.js --mode index --base-url https://notex.aishuo.co/noteX --user-id <uid> --access-token <token>
```

> 示例话术与调用流程参考：[`examples/notebook-source-index.md`](./examples/notebook-source-index.md)

---

## 5. NoteX 链接带 Token 打开 (Open NoteX URL)

该能力用于处理“帮我打开 NoteX”这类请求，目标是生成并返回**带 token 的可访问链接**，并在可行时自动拉起浏览器。

### 5.0 三要素（角色 / 能力 / 使用时机）

- 我是谁：NoteX 首页打开助手，负责把首页地址转换为可访问的授权链接。
- 我能做什么：生成 `https://notex.aishuo.co/?token=...` 最终链接，返回前端可直接使用，并可选自动打开浏览器。
- 什么时候使用：当用户说“帮我打开 NoteX / 打开这个 NoteX 链接”时使用。
- 前置条件：调用前必须通过“1.1 统一前置鉴权规则”。

### 5.1 输入输出约束

- 输入：默认不需要额外地址参数，固定打开 NoteX 首页路由。
- 输出：**必须**是 `https://notex.aishuo.co/?token=xxx` 形式的链接。
- 域名约束：仅允许 `https://notex.aishuo.co`。
- 对话约束：若当前会话无 token，不向用户索取 token；仅提示用户提供/确认 `CWork Key` 授权。
- 路由约束：该技能是“首页打开路由”，与创作任务返回的 `?skillsopen=task-...` 路由是两套不同入口。

### 5.2 默认执行流程

1. 固定使用首页路由 `https://notex.aishuo.co/`。
2. 读取会话授权态：有可用 token 则复用；没有则用 `CWork Key` 换取。
3. 生成 `https://notex.aishuo.co/?token=...` 最终链接。
4. 把最终链接返回前端用户。
5. 若运行环境支持且用户允许，可自动打开浏览器访问该链接。
6. 若自动打开失败，不影响主流程，仍返回最终链接供用户手动打开。

### 5.3 脚本调用示例

```bash
# 推荐：仅提供 CWork Key，内部自动换取 token 并生成首页链接
node docs/skills/scripts/notex-open-link.js --key <CWorkKey>

# 生成首页链接并自动打开浏览器（可选）
node docs/skills/scripts/notex-open-link.js --key <CWorkKey> --auto-open true

# 内部调试：复用已有 token
node docs/skills/scripts/notex-open-link.js --access-token <token> --user-id <uid>
```

> 示例话术参考：[`examples/notex-open-link.md`](./examples/notex-open-link.md)

---

## 6. 示例索引 (Examples Index)

本目录用于给 Agent 提供可复用的话术与流程模板。每个示例都包含三要素：
- 我是谁
- 我能做什么
- 什么时候使用

同时，所有示例都遵循同一前置鉴权约束：
- 对用户只暴露 `CWork Key` 授权动作
- 不向用户暴露 `token/x-user-id/personId/login` 等实现细节

并遵循统一环境约束：
- 仅允许生产域名：`https://notex.aishuo.co/noteX`
- 授权域名固定：`https://cwork-web.mediportal.com.cn`

### 6.1 示例与技能映射

| 能力 | 适用场景 | 对应示例 | 对应 SKILL 主文档 |
|---|---|---|---|
| 内容创作（Asynchronous Creator） | 生成 PPT、信息图、视频、音频、报告、脑图、测验、闪卡 | [`notex-creator.md`](./examples/notex-creator.md) | 第 2 节 |
| OPS 运营洞察（ops-chat） | 查询运营指标、告警、用户行为、组织分析 | [`ops-assistant.md`](./examples/ops-assistant.md) | 第 3 节 |
| Notebook 来源索引与详情 | 查询名下来源索引、按 notebook/source 拉最小详情 | [`notebook-source-index.md`](./examples/notebook-source-index.md) | 第 4 节 |
| NoteX 链接带 Token 打开 | 打开 NoteX 首页并确保带 token | [`notex-open-link.md`](./examples/notex-open-link.md) | 第 5 节 |

### 6.2 脚本映射

| 目标 | 推荐脚本 |
|---|---|
| 创作 + OPS 联调 | [`./scripts/skills-run.js`](./scripts/skills-run.js) |
| 来源索引落盘与定时全量刷新 | [`./scripts/source-index-sync.js`](./scripts/source-index-sync.js) |
| NoteX 链接补 token 并打开 | [`./scripts/notex-open-link.js`](./scripts/notex-open-link.js) |

### 6.3 推荐执行顺序

1. 先按第 1.1 节做鉴权预检。
2. 再根据任务类型选择对应示例。
3. 按示例中的调用顺序发起接口请求。

---

## 7. 相关依赖文件说明

| 文件/目录 | 用途描述 |
|---|---|
| [`/examples/`](./examples/) | **强烈建议阅读**。存放了三大能力（创作 / OPS / 来源索引）的系统示例。 |
| [`/examples/README.md`](./examples/README.md) | 示例目录索引。用于快速定位“我是谁 / 我能做什么 / 什么时候使用”及对应接口、脚本、调用顺序。 |
| [`/examples/notex-creator.md`](./examples/notex-creator.md) | 创作能力示例（skill: slide/infographic/video/audio/report/mindmap/quiz/flashcards）。 |
| [`/examples/ops-assistant.md`](./examples/ops-assistant.md) | OPS 能力示例（skill: ops-chat）。 |
| [`/examples/notebook-source-index.md`](./examples/notebook-source-index.md) | 第三块能力示例：如何先拉索引、落盘缓存、再按 notebookId/sourceId 拉最小详情。 |
| [`/examples/notex-open-link.md`](./examples/notex-open-link.md) | 第四块能力示例：如何生成 `https://notex.aishuo.co/?token=...` 并返回前端，必要时自动打开浏览器。 |
| [`/scripts/skills-run.js`](./scripts/skills-run.js) | Node.js 测试桩代码。开发者可通过此脚本直接在终端体验鉴权、发起任务与并发轮询的全套完整生命周期。 |
| [`/scripts/source-index-sync.js`](./scripts/source-index-sync.js) | Notebook 来源索引树/详情检索脚本，支持本地落盘与定时全量刷新（覆盖写）。 |
| [`/scripts/notex-open-link.js`](./scripts/notex-open-link.js) | NoteX 链接补 token 脚本，支持返回最终链接与可选自动打开浏览器。 |
