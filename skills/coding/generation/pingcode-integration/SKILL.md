---
name: dev-ops-pingcode-integration
description: PingCode 研发管理平台 API 集成。支持查询工作项、生成周报、管理项目进度等。使用场景：研发管理自动化、团队协作、数据分析。
tags: [pingcode, devops, agile, api-integration]
version: 1.0.0
---

# PingCode Skill

通过 PingCode Open API 操作研发管理平台数据。

## 前置条件

1. 在 PingCode 企业后台创建应用，获取 `Client ID` 和 `Client Secret`
2. 配置应用的数据访问范围
3. 将凭证填入脚本中的 `CLIENT_ID` 和 `CLIENT_SECRET`

## 功能脚本

### 获取我的工作项

```bash
python3 scripts/get_my_tasks.py
```

输出示例：
```
📋 你的工作项列表 (共 15 条，显示前 20 条)

⬜ [5e05d844] 优化登录页面性能
   项目: Web端重构 | 状态: 待处理 | 优先级: 高
   负责人: 张三

🔄 [5e05d845] API 接口文档更新
   项目: 开放平台 | 状态: 进行中 | 优先级: 中
   负责人: 李四
```

### 生成项目周报

```bash
# 生成周报并输出到控制台
python3 scripts/generate_weekly_report.py

# 指定项目和名称
python3 scripts/generate_weekly_report.py --project_id xxx --project_name "PingCode 重构"

# 输出到文件
python3 scripts/generate_weekly_report.py --output /tmp/weekly_report.md
```

输出示例：
```markdown
# 📊 项目周报
生成时间：2024-03-01 14:30

## 📈 数据概览
- 工作项总数：45
- 本周完成：12 (26.7%)
- 进行中：15
- 待处理：18
- 延期风险：3

## ⚠️ 延期风险
发现 3 个工作项已延期，建议优先处理：
- 优化登录性能 (截止：2024-02-28)
```

### 创建工作项（待实现）

```bash
python3 scripts/create_workitem.py --title "修复登录bug" --type bug --priority high
```

## API 参考

详见 `references/api_docs.md` 或访问 https://open.pingcode.com/

## 常用 API 端点

| 功能 | 端点 |
|------|------|
| 获取令牌 | `GET /v1/auth/token` |
| 获取工作项 | `GET /v1/project/work_items` |
| 创建工作项 | `POST /v1/project/work_items` |
| 获取项目 | `GET /v1/agile/projects` |
| 获取迭代 | `GET /v1/agile/iterations` |

## 注意事项

1. **频率限制**：每分钟最多 200 次请求
2. **Token 有效期**：30 天
3. **分页**：默认每页 30 条，最大 100 条
