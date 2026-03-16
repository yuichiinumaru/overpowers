---
name: menews
description: "AIMPACT × ME News — 获取 AI 与加密行业实时热点与预测市场事件。通过实时快讯、聚合摘要与预测市场数据，帮助用户洞察 AI 与 Crypto 领域的趋势与市场共识。"
metadata:
  openclaw:
    category: "news"
    tags: ['news', 'media', 'content']
    version: "1.0.0"
---

# ME News Skill

获取加密货币行业快讯、聚合热点和 Polymarket 预测市场数据。

## 功能特性

- **📰 快讯列表** - 获取最新的加密货币行业快讯
- **🤖 聚合热点** - 智能聚合热点话题、热门代币和 X 平台热议内容
- **🎯 预测事件** - 查询 Polymarket 预测市场的活跃事件
- **🔄 实时更新** - 数据实时同步，保持最新
- **🌐 中英双语** - 支持中英文查询

## 快速开始

### 🎉 无需配置，立即使用！

本 Skill 使用**完全公开的 API**，无需任何认证或配置。

安装后直接使用触发词

## 使用示例

### 获取快讯列表

**用户提问**：
- "最近有什么加密货币新闻？"
- "Show me the latest crypto flash news"
- "今天的快讯"

**Skill 行为**：
1. 调用 ME News API 获取快讯列表
2. 解析并格式化数据
3. 返回清晰易读的快讯摘要

**返回示例**：
```
📰 最新加密货币快讯（前 5 条）

1. 【标题】比特币突破 $70,000
   时间：2026-03-10 23:00
   摘要：比特币价格突破 7 万美元关口...
   
2. 【标题】以太坊升级即将到来
   时间：2026-03-10 22:30
   摘要：以太坊将在下周进行重大升级...
   
...
```

### 获取聚合热点

**用户提问**：
- "最近有什么热点话题？"
- "Show me the aggregated digest"
- "热门代币有哪些？"
- "X 平台上在讨论什么？"

**Skill 行为**：
1. 调用聚合 API 获取智能摘要
2. 解析热点话题、热门代币和社交媒体热议
3. 返回结构化的聚合内容

**返回示例**：
```
🤖 聚合热点（过去 1 小时）

【当前热点】
1. 比特币 ETF 获批引发市场热议
   来源：OpenNews | 讨论数：1,234
   时间：2026-03-10 23:15
   
2. 以太坊 Layer 2 生态爆发
   来源：X Platform | 讨论数：856
   时间：2026-03-10 23:00

【热门代币】
1. $BTC - 看涨情绪
   原因：ETF 获批推动价格上涨
   讨论数：2,345
   
2. $ETH - 中性情绪
   原因：Layer 2 扩展方案进展
   讨论数：1,567

【X 平台热议】
1. Vitalik 发布以太坊路线图更新
   讨论数：3,456
   
...
```

### 查询预测事件

**用户提问**：
- "Polymarket 上有什么热门预测？"
- "Show me active prediction markets"
- "预测市场有什么新事件？"

**Skill 行为**：
1. 调用 Polymarket 事件 API
2. 筛选活跃事件
3. 展示事件详情和赔率

**返回示例**：
```
🎯 Polymarket 活跃预测事件

1. 【事件】2024 年美国总统大选
   市场：Politics
   流动性：$5.2M
   活跃度：高
   
2. 【事件】比特币年底价格预测
   市场：Crypto
   流动性：$2.1M
   活跃度：中
   
...
```

## API 端点

**API 基础地址**: `https://agent.me.news`

Skill 使用以下 API 端点（Skill 自动调用，无需手动配置）：

### 快讯列表
```
GET https://agent.me.news/skill/flash/list
```

**参数**：
- `page` (int): 页码，默认 1
- `size` (int): 每页数量，默认 20，最大 50

**示例**：
```bash
curl 'https://agent.me.news/skill/flash/list?page=1&size=20'
```

### 聚合热点内容
```
GET https://agent.me.news/skill/aggregation/list
```

**参数**：
- `type` (string): 聚合类型，默认 "digest"
- `window` (string): 时间窗口，默认 "1h"（可选：1h, 6h, 24h）
- `page` (int): 页码，默认 1
- `size` (int): 每页数量，默认 10，最大 50

**示例**：
```bash
curl 'https://agent.me.news/skill/aggregation/list?type=digest&window=1h&page=1&size=10'
```

**返回数据结构**：
- `x_hot`: X 平台热议话题列表
- `hot_tokens`: 热门代币及情绪分析
- `current_hot`: 当前热点事件列表
- `metadata`: 数据来源统计信息

### 预测事件
```
GET https://agent.me.news/skill/poly/events
```

**参数**：
- `page` (int): 页码，默认 1
- `size` (int): 每页数量，默认 20，最大 50
- `active_only` (bool): 仅显示活跃事件，默认 true

**示例**：
```bash
curl 'https://agent.me.news/skill/poly/events?page=1&size=20&active_only=true'
```

## 配置选项

本 Skill 无需任何配置，API 完全公开。

如需自定义 API 地址（高级用户）：

| 选项 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `NEWS_API_BASE_URL` | string | https://agent.me.news | API 基础地址（可选） |

## 触发词

Skill 会在以下情况下自动激活：

- 用户提到 "新闻"、"快讯"、"news"、"flash"
- 用户询问 "加密货币"、"crypto"、"bitcoin"、"ethereum"
- 用户提到 "Polymarket"、"预测市场"、"prediction"
- 用户询问 "市场动态"、"行业资讯"
- 用户提到 "热点"、"摘要"、"digest"、"aggregation"
- 用户询问 "热门代币"、"X 平台"、"社交媒体热议"

## 实现细节

### 数据处理

Skill 会自动：
- 清洗 HTML 标签，提取纯文本
- 格式化时间为易读格式
- 过滤无效或重复数据
- 按时间倒序排列
- 聚合多源数据（OpenNews、X Platform）
- 分析代币情绪（看涨、看跌、中性）
- 统计讨论热度和来源分布

### 错误处理

常见错误及解决方案：

**API 请求失败**
```json
{
  "detail": "CMS 请求失败"
}
```
**解决**：检查网络连接，稍后重试

**请求频率超限**
```json
{
  "detail": "Rate limit exceeded"
}
```
**解决**：等待一分钟后重试

## 限流说明

- 默认限流：每个 IP 地址 20 次/分钟
- 完全公开访问，无需认证
- 如遇限流，请稍后重试

## 注意事项

1. **数据时效性**
   - 快讯数据实时更新
   - 聚合内容每小时更新
   - 预测市场数据每 5 分钟刷新
   - 建议定期查询获取最新信息

2. **时间窗口选择**
   - `1h`: 适合追踪最新热点
   - `12h`: 适合了解半天趋势
   - `24h`: 适合查看全天概览

3. **使用建议**
   - 合理控制请求频率
   - 避免短时间内大量请求
   - 建议缓存结果以提升性能
   - 聚合内容包含多维度数据，建议完整解析

## 故障排查

### Skill 未激活

**问题**：OpenClaw 没有调用 ME News Skill

**解决**：
1. 确认 Skill 已安装：`clawhub list`
2. 检查环境变量是否配置
3. 尝试更明确的触发词，如 "使用 ME News 获取快讯"

### 返回数据为空

**问题**：API 返回成功但没有数据

**解决**：
1. 检查查询参数是否正确
2. 尝试调整 `page` 和 `size` 参数
3. 确认数据源是否有新内容

### 响应速度慢

**问题**：查询响应时间较长

**解决**：
1. 减少 `size` 参数值
2. 检查网络连接
3. 避免频繁查询，使用缓存结果

## 支持与反馈

- **问题反馈**：https://github.com/jamesmenews/menews/issues
- **功能建议**：https://github.com/jamesmenews/menews/discussions
- **邮件联系**：aimpact@me.news
- **官方网站**：https://me.news

## 许可证

MIT License

---

**提示**：首次使用建议先测试简单查询，熟悉 Skill 功能后再进行复杂操作。
