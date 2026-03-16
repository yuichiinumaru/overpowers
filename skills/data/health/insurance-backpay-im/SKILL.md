---
name: finance-social-insurance-backpay-im
version: 1.0.0
description: Social insurance backpay calculation tool for Inner Mongolia. Computes backpay amounts for pension insurance including principal, interest (compounded monthly), and late fees based on historical average wages and policy rules.
tags: [finance, social-insurance, backpay, calculation, inner-mongolia, pension]
category: finance
---

# 内蒙古养老保险补缴计算 (Social Insurance Backpay Calculation - IM)

## 功能概述

本工具用于计算内蒙古地区养老保险补缴金额，支持：

- 按历年社平工资计算缴费基数
- 按月复利计算利息（从缴费当月开始计息）
- 按日万分之五计算滞纳金
- 支持60%/80%/100%/150%/200%/300%六档缴费比例
- 分别汇总有滞纳金 and 无滞纳金金额

## 计算规则

### 1. 缴费基数

按当年内蒙古社平工资 × 缴费档次比例（60%/80%/100%/150%/200%/300%）

### 2. 缴费比例

- **个人缴费**（进入个人账户，逐步提高）：
  - 1996–1997 年：3%
  - 1998–1999 年：4%
  - 2000 年：5%
  - 2001–2002 年：6%
  - 2003–2004 年：7%
  - 2005 年至今：8%
- **单位缴费**（随政策调整）：
  - 1996–1997 年：20%
  - 1998–1999 年：26%
  - 2000 年：25%
  - 2001–2002 年：24%
  - 2003–2004 年：23%
  - 2005–2017 年：20%
  - 2018 年 5–12 月：19%
  - 2019 年 1–4 月：19%
  - 2019 年 5 月起：16%
  - 2021 年至今：16%

### 3. 利息计算

- 每月缴费从当月开始按月复利计息
- 利率按历年社保记账利率
- 计算公式：`终值 = 本金 × (1 + 月利率)^月数`

### 4. 滞纳金计算

- 费率：按日万分之五（0.05%）
- 起算：欠缴次月1日
- 截止：补缴时间

## 使用方法

### 命令行调用

```bash
# 单档次计算
python scripts/calculate_backpay.py 2004 4 2011 3 --rate 0.6 --target 2026 3

# 多档次对比
python scripts/calculate_backpay.py 2004 4 2011 3 --all --target 2026 3
```

**可选参数**：
- `--rate`：缴费档次比例（默认 0.6）
- `--all`：计算全部六档对比
- `--target YEAR MONTH`：补缴时间
- `--monthly-base`：自定义月缴费基数

## 参考数据

- 历年社平工资: `references/social_avg_wages.md`
- 历年记账利率: `references/interest_rates.md`
- 政策规则: `references/policy_rules.md`

## 注意事项

1. **数据准确性**：以官方公布为准
2. **滞纳金减免**：根据当地政策可能存在减免
3. **单位欠缴**：滞纳金应由单位承担
4. **计算精度**：保留两位小数
