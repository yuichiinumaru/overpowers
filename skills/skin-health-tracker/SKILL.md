---
name: skin-health-tracker
description: 皮肤健康管理技能，记录皮肤问题、监测痣的变化（ABCDE 法则）、管理护肤程序、跟踪皮肤健康状态、分析皮肤健康趋势。
tags: [skin, health, healthcare, mole-monitoring, skincare]
version: 1.0.0
category: healthcare
---

# 皮肤健康管理技能

记录皮肤问题、监测痣的变化、管理护肤程序、跟踪皮肤健康状态、分析皮肤健康趋势。

## 医学免责声明

本系统仅用于健康追踪和教育目的，不提供医学诊断或治疗建议。

**不能做到:**
- 所有皮肤问题应咨询专业皮肤科医生
- 痣的异常变化应立即就医检查
- 不能替代专业皮肤科检查和治疗

**能做到:**
- 记录和追踪皮肤健康数据
- 提供皮肤检查记录和提醒
- 提供 ABCDE 法则自查指导
- 提供一般性护肤建议

## 核心流程

```
用户输入 → 识别操作类型 → [concern] 解析皮肤问题 → 保存记录
                              ↓
                         [mole] 解析痣信息 → ABCDE 评估 → 保存
                              ↓
                         [routine] 解析护肤程序 → 保存
                              ↓
                         [exam] 记录检查结果 → 保存
                              ↓
                         [sun] 记录日晒信息 → 保存
                              ↓
                         [status/trend] 读取数据 → 显示报告
```

## 操作类型

| Input Keywords | Operation Type |
|---------------|----------------|
| concern | concern - Skin problem record |
| mole | mole - Mole monitoring |
| routine | routine - Skincare routine |
| exam | exam - Skin exam record |
| sun | sun - Sun exposure record |
| status | status - View status |
| trend | trend - Trend analysis |
| reminder | reminder - Exam reminder |
| screening | screening - Disease screening |

## ABCDE 法则详解

### A - Asymmetry（不对称性）
- 正常：痣从中间对折，两边基本对称
- 异常：痣的两半不对称，形状不规则

### B - Border（边缘）
- 正常：边缘清晰、平滑、规则
- 异常：边缘模糊、不规则、锯齿状、扇贝状

### C - Color（颜色）
- 正常：颜色均匀，通常是棕色、黑色或肤色
- 异常：颜色不均匀，包含多种颜色

### D - Diameter（直径）
- 正常：直径通常小于 6mm
- 异常：直径大于 6mm，或近期明显增大

### E - Evolution（变化/进展）
- 正常：长期稳定，无明显变化
- 异常：近期大小、形状、颜色、厚度、感觉发生变化

## 紧急情况指南

### 需要紧急处理（24 小时内）
- 痣突然出血、溃疡
- 痣快速增大或颜色改变
- 新出现的可疑痣
- 大面积皮疹伴发热

### 需要尽快就诊（1 周内）
- 痣出现 ABCDE 异常
- 伤口或溃疡超过 2 周未愈合
- 持续性瘙痒影响睡眠
