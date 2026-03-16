---
name: yoyoalphax-zentao
description: "禅道项目管理 API 集成技能。支持查询产品、项目、执行、需求、任务、缺陷等。触发词：禅道、zentao、禅道查询、禅道项目"
metadata:
  openclaw:
    category: "social"
    tags: ['social', 'x', 'twitter']
    version: "1.0.0"
---

# 禅道项目管理技能

## 快速开始

本技能整合禅道老 API 和 REST API，提供统一的项目管理查询接口。

### 凭证配置

禅道 API 凭证存储在 `TOOLS.md` 文件中：

```markdown
## 禅道 API

- **API 地址：** http://<your-zentao-host>/
- **用户名：** <your-username>
- **密码：** <your-password>
```

**⚠️ 安全提醒：** 不要将 API 凭证提交到版本控制或公开分享。

## 功能列表

### 查询类（无需确认）

#### 用户 User
- `GET /users` - 获取用户列表
- `GET /users/{id}` - 获取用户信息
- `GET /user` - 获取我的个人信息

#### 项目集 Program
- `GET /programs` - 获取项目集列表
- `GET /programs/{id}` - 获取项目集信息

#### 产品 Product
- `GET /products` - 获取产品列表
- `GET /products/{id}` - 获取产品信息
- `GET /products/{id}/teams` - 获取产品团队
- `GET /products/{id}/plans` - 获取产品计划列表
- `GET /products/{id}/stories` - 获取需求列表
- `GET /products/{id}/bugs` - 获取 Bug 列表
- `GET /products/{id}/releases` - 获取发布列表
- `GET /products/{id}/testcases` - 获取用例列表
- `GET /products/{id}/testtasks` - 获取测试单列表
- `GET /products/{id}/feedbacks` - 获取反馈列表
- `GET /products/{id}/tickets` - 获取工单列表

#### 项目 Project
- `GET /projects` - 获取项目列表
- `GET /projects/{id}` - 获取项目信息
- `GET /projects/{id}/stories` - 获取项目需求列表
- `GET /projects/{id}/executions` - 获取项目执行列表
- `GET /projects/{id}/builds` - 获取项目版本列表

#### 执行 Execution
- `GET /executions` - 获取执行列表
- `GET /executions/{id}` - 获取执行信息
- `GET /executions/{id}/tasks` - 获取执行任务列表
- `GET /executions/{id}/bugs` - 获取执行 Bug 列表
- `GET /executions/{id}/builds` - 获取执行版本列表

#### 任务 Task
- `GET /tasks` - 获取任务列表
- `GET /tasks/{id}` - 获取任务

#### 缺陷 Bug
- `GET /bugs/{id}` - 获取 Bug

#### 版本 Build
- `GET /builds/{id}` - 获取版本

#### 用例 TestCase
- `GET /testcases/{id}` - 获取用例

#### 测试单 TestTask
- `GET /testtasks/{id}` - 获取测试单

#### 反馈 Feedback
- `GET /feedbacks/{id}` - 获取反馈

#### 工单 Ticket
- `GET /tickets/{id}` - 获取工单

### 操作类（需要确认）
- ❌ POST /users - 创建用户
- ❌ PUT /users/{id} - 修改用户信息
- ❌ DELETE /users/{id} - 删除用户
- ❌ POST /programs - 创建项目集
- ❌ PUT /programs/{id} - 修改项目集
- ❌ DELETE /programs/{id} - 删除项目集
- ❌ POST /products - 创建产品
- ❌ PUT /products/{id} - 修改产品
- ❌ DELETE /products/{id} - 删除产品
- ❌ POST /products/{id}/plans - 创建产品计划
- ❌ PUT /products/{id}/plans/{planID} - 修改产品计划
- ❌ DELETE /products/{id}/plans/{planID} - 删除产品计划
- ❌ POST /products/{id}/stories - 创建需求
- ❌ PUT /products/{id}/stories/{storyID} - 修改需求
- ❌ DELETE /products/{id}/stories/{storyID} - 删除需求
- ❌ PUT /products/{id}/stories/{storyID}/activate - 激活需求
- ❌ PUT /products/{id}/stories/{storyID}/close - 关闭需求
- ❌ POST /projects - 创建项目
- ❌ PUT /projects/{id} - 修改项目
- ❌ DELETE /projects/{id} - 删除项目
- ❌ POST /projects/{id}/builds - 创建版本
- ❌ PUT /builds/{id} - 修改版本
- ❌ DELETE /builds/{id} - 删除版本
- ❌ POST /executions - 创建执行
- ❌ PUT /executions/{id} - 修改执行
- ❌ DELETE /executions/{id} - 删除执行
- ❌ POST /executions/{id}/tasks - 创建任务
- ❌ PUT /tasks/{id} - 修改任务
- ❌ DELETE /tasks/{id} - 删除任务
- ❌ POST /products/{id}/bugs - 创建 Bug
- ❌ PUT /bugs/{id} - 修改 Bug
- ❌ DELETE /bugs/{id} - 删除 Bug
- ❌ POST /products/{id}/testcases - 创建用例
- ❌ PUT /testcases/{id} - 修改用例
- ❌ DELETE /testcases/{id} - 删除用例
- ❌ POST /products/{id}/testtasks - 创建测试单
- ❌ POST /testtasks/{id}/testcases/{caseID}/run - 执行用例
- ❌ POST /products/{id}/feedbacks - 创建反馈
- ❌ PUT /feedbacks/{id} - 修改反馈
- ❌ DELETE /feedbacks/{id} - 删除反馈
- ❌ POST /products/{id}/tickets - 创建工单
- ❌ PUT /tickets/{id} - 修改工单
- ❌ DELETE /tickets/{id} - 删除工单

## 使用示例

### 查询产品列表
```
禅道产品列表
查询禅道所有产品
zentao products
```

### 查询项目列表
```
禅道项目列表
查询进行中的项目
zentao projects
```

### 查询需求列表
```
禅道需求列表 项目=IDS
查询禅道需求 产品=IDS_投资决策支持系统
```

### 查询任务列表
```
禅道任务列表 执行=176
查询禅道任务 项目=IDS
```

### 查询缺陷列表
```
禅道缺陷列表 产品=21
查询禅道 bug 产品=IDS
```

### 新建需求（需要确认）
```
禅道新建需求 产品=IDS 执行=176 标题=【新功能】测试需求 计划=2024-03-31 版本
```

### 新建任务（需要确认）
```
禅道新建任务 执行=176 需求=1234 标题=开发任务 指派=徐泽南
```

## 工作流程

1. **读取凭证** - 从 TOOLS.md 获取禅道 API 凭证
2. **解析命令** - 解析用户命令和参数
3. **认证登录** - 使用 REST API 获取 Token 或老 API 获取 Session
4. **执行操作** - 调用对应 API 接口
5. **输出结果** - 返回格式化的结果

## API 说明

### REST API (优先使用)
- 认证方式：Token
- 接口路径：`/api.php/v1/`
- 适用场景：用户、产品、项目、执行、版本等查询

### 老 API (兼容模式)
- 认证方式：Session/Cookie
- 接口路径：`/api-*.json`
- 适用场景：需求、任务、缺陷、发布计划等

## 输出格式

### 产品列表
```
✅ 禅道产品查询完成

共查询到 N 个产品：

| ID | 产品名称 |
|----|---------|
| 21 | IDS_投资决策支持系统 |
| ... | ... |
```

### 项目列表
```
✅ 禅道项目查询完成

共查询到 N 个项目：

| ID | 项目名称 | 状态 |
|----|---------|------|
| 176 | IDS_投资决策支持系统 | doing |
| ... | ... | ... |
```

## 错误处理

- **凭证缺失：** 提示用户在 TOOLS.md 中配置禅道 API 凭证
- **认证失败：** 检查用户名密码是否正确
- **API 连接失败：** 检查网络连接和 API 地址
- **无数据返回：** 可能是权限问题或时间范围内无数据

## 注意事项

1. 首次使用需在 TOOLS.md 中配置禅道 API 凭证
2. 所有新增、新建、删除操作都需要用户确认
3. 建议优先使用 REST API，老 API 作为兼容
4. 查询时间范围建议不超过 1 年（数据量较大）
