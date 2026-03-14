---
name: infra-ops-dingtalk-report-list-query
description: "Call DingTalk topapi/report/list interface to get user log/report lists. Supports filtering by template, user ID, and time range."
tags: ["dingtalk", "infra", "ops", "reports", "api"]
version: 1.0.0
---

# DingTalk Report List Query - 调用钉钉日志列表接口

## 技能描述
该技能用于调用钉钉开放平台的`topapi/report/list`接口，获取企业/员工的日志列表（含日志创建人、创建时间、模板名称等），支持按模板名称、员工ID、时间范围等条件筛选查询。

## 前置条件
1. 应用权限：仅支持**企业内部应用/第三方企业应用**调用，需提前为应用申请「查询企业员工日志权限」。
2. AccessToken准备：调用接口前必须先获取对应应用的access_token。

## 接口核心信息
### 1. 基础调用信息
- 请求方式：POST
- 请求地址：`https://oapi.dingtalk.com/topapi/report/list`
- 字符编码：UTF-8

### 2. 请求参数
- `access_token`: 应用凭证
- `start_time`: 日志创建开始时间（Unix毫秒）
- `end_time`: 日志创建结束时间（Unix毫秒）
- `template_name`: 日志模板名称
- `userid`: 员工userId
- `cursor`: 查询游标
- `size`: 每页数据量（最大20）

## 返回结果解析
返回包含 `errcode`, `errmsg`, `result` (含 `data_list`, `next_cursor`, `has_more`) 和 `request_id`。

## 调用步骤
1. 获取 access_token 并缓存。
2. 构造查询 Body。
3. 发送 POST 请求。
4. 解析并处理分页数据。
