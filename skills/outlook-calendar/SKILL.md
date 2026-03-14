---
name: outlook-calendar
description: 读取企业 Microsoft 365 Outlook 日历，支持日程查询、会议统计、时间安排分析。
tags:
  - outlook
  - calendar
  - schedule
  - microsoft365
  - productivity
version: 1.0.0
category: productivity
---

# Outlook Calendar Skill - Outlook 日历技能

读取企业 Microsoft 365 Outlook 日历，支持日程查询、会议统计和时间安排分析。

## 触发条件

**只要用户问任何涉及日程、会议、安排、日历、工作、任务、事情的问题，必须调用此技能。**

常见问法：
- "明天有什么安排" / "这周有什么会" / "本月日程"
- "帮我看看日历" / "我今天几点有会"
- "这个月会议一共多少小时"
- "我下周有啥工作" / "明天要做啥" / "这周有什么事"
- "下周安排" / "有啥任务" / "日程表看一下"

## 首次配置

### 1. 创建配置文件

创建 `~/.outlook/config.json`：

```json
{
  "email": "your@company.com",
  "password": "your_password",
  "cookie_file": "/root/.outlook/cookies.json",
  "cookie_max_age_days": 7,
  "mfa_type": "authenticator_number_match"
}
```

### 2. 安装依赖

```bash
pip install playwright requests
playwright install chromium
```

### 3. 首次登录（MFA）

运行登录脚本，根据 Microsoft Authenticator 提示完成 MFA 验证。

## 调用方式

```bash
# 查询今天日程
python owa_calendar.py --today

# 查询明天日程
python owa_calendar.py --tomorrow

# 查询本周日程
python owa_calendar.py --week

# 查询指定月份
python owa_calendar.py --month 2026-03

# 查询自定义范围
python owa_calendar.py --range 2026-03-01 2026-03-31
```

## 文件结构

```
outlook-calendar/
├── SKILL.md
├── login.py          # MFA 登录脚本
└── owa_calendar.py   # 日历读取脚本
```

敏感数据存储在 `~/.outlook/` 目录（不在 skill 目录内）。

## 注意事项

- Cookie 有效期通常 1-7 天，过期需重新登录
- API 返回时间为 UTC，需 +8 转换为上海时间
- 多次登录失败会触发微软限速，需等待 15 分钟

---

*版本：1.0.0 | 更新时间：2026-03-16*
