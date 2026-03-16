---
name: health-report-generator
description: 综合健康报告生成技能，生成专业的 HTML 格式健康报告，包含多种数据可视化图表，支持自定义章节和时间范围。
tags: [health, report, data-visualization, healthcare]
version: 1.0.0
category: healthcare
---

# 综合健康报告生成技能

生成专业的 HTML 格式健康报告，包含多种数据可视化图表。

## 核心流程

```
用户输入 -> 解析参数 -> 收集数据 -> 分析统计 -> 生成 HTML -> 保存文件 -> 确认输出
```

## 报告类型

| 类型 | 说明 |
|-----|------|
| comprehensive | 综合报告（默认） |
| biochemical | 生化趋势分析 |
| imaging | 影像检查汇总 |
| medication | 用药分析 |
| custom | 自定义报告 |

## 时间范围

| 参数 | 说明 |
|-----|------|
| all | 所有数据 |
| last_month | 上个月 |
| last_quarter | 上季度 |
| last_year | 去年 |
| YYYY-MM-DD,YYYY-MM-DD | 自定义范围 |

## 章节选择

| 代码 | 说明 |
|-----|------|
| profile | 患者概况 |
| biochemical | 生化检查 |
| imaging | 影像检查 |
| medication | 用药分析 |
| radiation | 辐射剂量 |
| allergies | 过敏摘要 |
| symptoms | 症状历史 |
| surgeries | 手术记录 |

## 图表类型

| 数据类型 | 图表 |
|---------|------|
| 生化指标趋势 | 折线图 |
| 异常指标分布 | 柱状图/饼图 |
| 检查类型统计 | 饼图 |
| 用药依从性 | 堆叠柱状图 |
| 辐射累积剂量 | 仪表图 |

## 使用示例
- "生成综合健康报告"
- "生成综合报告 上季度"
- "生成自定义报告 2025-01-01,2025-12-31 biochemical,medication"
