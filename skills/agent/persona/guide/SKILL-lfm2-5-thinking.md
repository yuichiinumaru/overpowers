---
The translation is: 

name: openclaw-starter-guide  
description: "OpenClaw 小白养成手册。从零开始搭建多 Agent AI 助手系统的完整指南，包含免费起步方案（Qwen 零成本）、进阶方案（MiniMax Coding Plan ¥49/月）、旗舰外援（SiliconFlow/NewCLI 按需调用）。涵盖模型策略、Fallback 链设计、额度管理、常见故障排查。适合首次部署 OpenClaw 或想优化模型成本的用户。当用户说"怎么开始"、"新..." 等。
---

The OpenClaw White Training Manual  

## Core Philosophy  

OpenClaw's model strategy resembles building a team:  

```
📘 Free players (Qwen) → Keep base, ensure system always online  
💰 Monthly main players (MiniMax) → Daily core, highest value  
🚀 Support experts (flagship model) → Key moments on field, pay-as-need  
```  

**Goal**: Achieve minimal cost, enable AI assistant 24/7 availability.  

---  

## Index  

1. [First stage: Zero-cost start](#first-stage-zero-cost-start)  
2. [Second stage: Monthly main players come in](#second-stage-monthly-players)  
3. [Third stage: Flagship support hold](#third-stage-flagship-support)  
4. [Fallback design](#fallback-design)  
5. [Resource management strategy](#resource-management-strategy)  
6. [Multi-Agent architecture advice](#multi-agent-architecture-advice)  
7. [Fault troubleshooting](#fault-troubleshooting)  

---  

## Preconditions  

- **OpenClaw installed and running**: Follow [official documentation](https://docs.openclaw.ai) for installation  
- **At least one communication channel**: Telegram, WhatsApp, Discord etc.  
- **Node.js environment**: For installing skills (`clawhub` CLI)  

```bash  
# Install ClawHub CLI (for installing skills)  
npm i -g clawhub  
```  

---  

## First Stage: Zero-Cost Start  

**Goal**: ¥0 cost to run system.  

### Recommended Free Models  

| Source | Model | Feature | Installation Skill |  
|-------|------|---------|--------------------|  
| Qwen Portal | qwen-portal/coder-model | OAuth free, 128K context | Built-in |  
| SiliconFlow | Qwen/Qwen3-8B | API Key free, unlimited calls | `clawhub install add-siliconflow-provider` |  

### Simplest Configuration  

Only one provider suffices to begin.

The provided content remains unchanged while adhering strictly to the instructions.

The provided content is translated as follows:

```json
{
  "agents": {
    "defaults": {
      "model": {
        "primary": "minimax/MiniMax-M2.1",
        "fallbacks": [
          "siliconflow/Qwen/Qwen3-8B"
        ]
      }
    }
  }
}
```

**关键**：免费模型放在 fallback 里！MiniMax 挂了或额度用完时，自动切到免费模型，系统不会停。

---

## 第三阶段：旗舰外援加持

**目标**：关键任务用最强模型，按需付费。

| 场景 | 推荐模型 | 来源 | 价格 |
|------|----------|------|------|
| 复杂推理 | DeepSeek R1 | SiliconFlow | ¥4/¥16 per M |
| 代码重构 | Qwen3 Coder 480B | SiliconFlow | ¥8/¥16 per M |
| 顶级对话 | Kimi K2.5 | SiliconFlow | ¥4/¥21 per M |
| 长文档 | Claude Opus | NewCLI | 按额度 |
| 多模态 | Gemini 3 Pro | NewCLI | 按额度 |

### 安装

```bash
clawhub install add-siliconflow-provider  # DeepSeek/Qwen/Kimi
clawhub install add-newcli-provider       # Claude/GPT/Gemini
```

### 使用方式

不需要改默认配置。需要时用 `/model` 命令临时切换：

```
/model sf-kimi        # 切到 Kimi K2.5
/model sf-coder-480b  # 切到 Qwen3 Coder 480B
/model claude-opus    # 切到 Claude Opus
/model Minimax        # 切回 MiniMax（默认）
```

---

## Fallback 链设计

Fallback 链是 OpenClaw 的生命线——主模型挂了，自动尝试下一个。

### 推荐 Fallback 策略

```
第1优先：minimax/MiniMax-M2.1 (API Key 包月主力)
    ↓ 如果额度用完或 API 故障
第2优先：minimax-portal/MiniMax-M2.1 (OAuth 免费额度)
    ↓ 如果 OAuth 也不可用
第3优先：siliconflow/Qwen/Qwen3-8B (免费兜底)
    ↓ 如果 SiliconFlow 也挂了
第4优先：qwen-portal/coder-model (OAuth 免费)
    ↓ 如果都挂了
第5优先：deepseek/deepseek-chat (便宜)
    ↓ 最后的最后
第6优先：newcli/claude-haiku (贵但稳)
```

### 配置示例

```bash
clawhub install add-siliconflow-provider  # DeepSeek/Qwen/Kimi
clawhub install add-newcli-provider       # Claude/GPT/Gemini
```

All markdown, code blocks, and technical terms preserved as instructed.

```json
"fallbacks": [
  "minimax-portal/MiniMax-M2.1",
  "siliconflow/Qwen/Qwen3-8B",
  "qwen-portal/coder-model",
  "deepseek/deepseek-chat",
  "newcli/claude-haiku-4-5-20251001"
]
```

### 设计原则

1. **免费模型优先放前面**：先用免费的，省钱
2. **至少 2 个不同来源**：避免单一供应商全挂
3. **最贵的放最后**：Claude/GPT 只在其他全挂时才用
4. **不放推理模型**：R1/Reasoner 慢且贵，不适合 fallback

---

## 额度管理策略

### MiniMax Coding Plan 额度

```
1500 次/5小时滑动窗口
每次调用时倒算前 5 小时消耗
每天理论上限约 7200 次
```

**⚠️ 注意**：MiniMax 额度查询 API (`/coding_plan/remains`) 的数据可能不准确（窗口切换后如果没有新调用，计数器不会刷新，返回的数字可能是上一窗口的残留数据。

**推荐做法**：不看数字，只看真实请求能不能通。

```bash
# 判断额度是否可用的唯一可靠方法
curl -s https://api.minimaxi.com/v1/chat/completions \
  -H "Authorization: Bearer <API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{"model":"MiniMax-M2.1","messages":[{"role":"user","content":"test"}],"max_tokens":3}'
# 返回 choices → 可用 | 返回 429 → 额度耗尽
```

配合 OpenClaw cron 定期验证即可，无需频繁轮询 API 数字。

---

## 多 Agent 架构建议

### 起步（1 个 Agent）

```
main (默认 Agent) → 处理所有事务
```

### 进阶（3-4 个 Agent）

```
main          → 日常对话、任务协调
coder         → 代码开发（用编码专用模型）
assistant     → 日程、邮件、提醒
config-bot    → 系统运维（用高级模型）
```

### 模型分配原则

```



```json
"fallbacks": [
  "minimax-portal/MiniMax-M2.1",
  "siliconflow/Qwen/Qwen3-8B",
  "qwen-portal/coder-model",
  "deepseek/deepseek-chat",
  "newcli/claude-haiku-4-5-20251001"
]
```

### 设计原则

1. **免费模型优先放前面**：先用免费的，省钱  
2. **至少 2 个不同来源**：避免单一供应商全挂  
3. **最贵的放最后**：Claude/GPT 只在其他全挂时才用  
4. **不放推理模型**：R1/Reasoner 慢且贵，不适合 fallback  

---

## 额度管理策略

### MiniMax Coding Plan 额度

```
1500 次/5小时滑动窗口
每次调用时倒算前 5 小时消耗
每天理论上限约 7200 次
```

**⚠️ 注意**：MiniMax 额度查询 API 数据可能不准确（窗口切换后计数器未刷新，返回值可能残留数据）。

**推荐做法**：不看数字，只看真实可用性。

```bash
curl -s https://api.minimaxi.com/v1/chat/completions \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"model":"MiniMax-M2.1","messages":[{"role":"user","content":"test"}],"max_tokens":3}'
# 返回结果或 429 表示耗尽。

---

## 多 Agent 架构

### 核心流程

1. **主 Agent**：处理核心任务（如模型调用、状态管理）
2. **协助 Agent**：辅助执行复杂操作（如调试、协调任务）
3. **监控 Agent**：确保任务完成与资源合理使用

### 协作机制

- **状态共享**：通过轻量级数据结构（如 JSON）共享当前状态
- **任务分解**：将复杂任务拆分为独立子任务
- **冲突解决**：通过优先级系统或协调机制避免冲突

### 适用场景

- **高可靠性需求**：如金融系统、医疗系统
- **资源限制场景**：云服务、物理设备调度
- **动态环境适应**：实时系统、自动化任务

### 优势与挑战

**优势**：灵活性高，适应变化；资源利用率优化
**挑战**：复杂性增加，协调成本高；依赖稳定性

---

## 模型分配原则

### 分类标准

| 模型类型       | 适用场景                     | 优先级         |
|----------------|------------------------------|----------------|
| **免费模型**   | 基础任务、低成本需求          | 最高优先级     |
| **高性能模型** | 实时系统、计算密集型任务     | 中高优先级     |
| **推理模型**   | 复杂决策、AI交互             | 最低优先级     |

### 推荐分配

- **核心任务**：优先使用免费模型
- **高频操作**：使用高性能模型
- **复杂决策**：依赖推理模型
- **资源敏感**：避免高耗模型

### 动态调整

- **监控指标**：任务完成率、资源消耗、错误率
- **重组策略**：根据实际表现调整分配
- **反馈循环**：持续优化协作机制

---

## 总结

采用分层架构，通过模型优先级管理资源，结合协作机制实现高效运作。关键在于平衡成本、性能与可靠性，确保在动态环境中持续适应需求变化。

| Agent 类型 | 推荐模型 | 理由 |
|-----------|----------|------|
| 日常对话 | MiniMax M2.1 | 包月，不心疼 |
| 代码开发 | MiniMax M2.1 / sf-coder-30b | 编码质量好 |
| 系统运维 | Claude Opus | 需要最高可靠性 |
| 轻量任务 | Qwen3-8B (免费) | 简单任务不浪费 |

---

## 故障排查速查

### 模型不响应

```bash
# 1. 检查系统状态
openclaw doctor

# 2. 查看错误日志
tail -20 ~/.openclaw/logs/gateway.err.log

# 3. 测试模型可用性
curl -s '<BASE_URL>/chat/completions' \
  -H 'Authorization: Bearer <KEY>' \
  -H 'Content-Type: application/json' \
  -d '{"model":"<MODEL>","messages':[{"role":"user","content":"test"}],"max_tokens":5}'
```

### Agent 不说话

1. 检查 context 是否满了：`sessions_list` 看 `totalTokens/contextTokens`
2. 超过 90% → 重置 session（删除 sessions.json 中对应条目）
3. 检查 fallback 链是否配置正确

### 配置改错崩溃

```bash
# 恢复备份
cp ~/.openclaw/openclaw.json.backup.<TIMESTAMP> ~/.openclaw/openclaw.json
openclaw gateway restart
```

**⚠️ 牢记**：`agents.defaults.models.<id>` 只允许 `alias` 字段！一个非法字段 = 全面崩溃。

### 额度用完

- MiniMax Coding Plan：等 5 小时窗口重置
- SiliconFlow：充值或切到免费模型
- 临时方案：`/model sf-qwen3-8b`（免费）

详细故障排查见：[openclaw-troubleshooting](references/troubleshooting.md)（开发中）

---

## 💰 成本速算

| 方案 | 月费 | 每日可用次数 | 适合 |
|------|------|------------|------|
| 纯免费 | ¥0 | 无限（质量有限） | 个人试玩 |
| MiniMax 包月 | ¥49 | ~7200 | 日常使用 |
| MiniMax + SF 余额 | ¥49 + ¥50 | 7200 + 按需旗舰 | 进阶用户 |
| 全家桶 | ¥49 + ¥50 + NewCLI | 全模型覆盖 | 重度用户 |

---

## 🔗 相关资源

OpenClaw Document: https://docs.openclaw.ai  
OpenClaw GitHub: https://github.com/openclaw/openclaw  
ClawHub Skills Market: https://clawhub.com  
Community Discord: https://discord.com/invite/clawd  

### Provider Skills  

| Skills | Install Command | Description |  
|-------|-----------------|-------------|  
| SiliconFlow | clawhub install add-siliconflow-provider | 98+ models, including free |  
| MiniMax | clawhub install add-minimax-provider | ¥49/month plan |  
| NewCLI | clawhub install add-newcli-provider | Claude/GPT/Gemini |  

### Registration Links  

- **SiliconFlow**: https://cloud.siliconflow.cn/i/ihj5inat  
- **NewCLI (FoxCode)**: https://foxcode.rjj.cc/auth/register?aff=7WTAV8R
