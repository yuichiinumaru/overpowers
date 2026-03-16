---
name: alimail
description: "快速查询企业内部员工邮箱、工号及部门信息。"
metadata:
  openclaw:
    category: "ai"
    tags: ['ai', 'automation', 'generation']
    version: "1.0.0"
---

# 阿里邮箱企业助手 (AliMail Assistant)

本技能通过调用 `search_alimail_user` 接口获取员工信息。

## 核心功能
* **精准查询**：输入姓名即可获取完整邮箱地址。
* **模糊搜索**：支持姓名片段搜索，自动处理 `(name=*xxx)` 逻辑。
* **信息详情**：返回工号 (`employeeNo`)、邮箱(`email`)及姓名(`name`)。

## 使用指南
AI 会自动识别用户提及的名字并进行检索。例如：
- "查一下张三的邮箱"

## 隐私说明
本技能仅调用查询接口，不具备读取、删除或发送邮件的权限，确保企业数据安全。