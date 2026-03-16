---
name: medical-report-saver
description: 医疗检查单保存技能，使用 AI 分析图片提取医疗检查报告数据，支持生化检查和影像检查两种类型，自动保存到个人医疗数据中心。
tags: [medical, report, OCR, healthcare, data-extraction]
version: 1.0.0
category: healthcare
---

# Save Medical Test Report Skill

Save user-provided medical test reports to the personal medical data center.

## 核心流程

```
用户输入图片 -> 读取并分析图片 -> 提取数据 -> 生成 JSON -> 保存图片和数据 -> 更新索引 -> 确认输出
```

## 参数说明

- **image_path（必填）**：检查单图片的本地路径
- **exam_date（可选）**：检查日期，格式 YYYY-MM-DD

## 日期确定规则（优先级顺序）

1. **用户提供的 exam_date**（最高优先级）
2. 图片中的采样时间
3. 图片中的送样时间
4. 图片中的检测时间/报告时间
5. 图片中的其他日期标识
6. 当前日期（仅作备选）

## 支持的报告类型

### 生化检查 (BiochemicalTestReport)
- 血液常规
- 尿液检查
- 生化全套
- 肝功能
- 肾功能
- 血脂血糖

### 影像检查 (ImagingTestReport)
- B 超/彩超检查
- X 光检查
- CT 检查
- MRI 检查
- 内窥镜检查
- 病理检查
- 心电图检查

## 文件路径格式

- 生化检查：`data/biochemical-tests/YYYY-MM/YYYY-MM-DD_test-type.json`
- 影像检查：`data/imaging-studies/YYYY-MM/YYYY-MM-DD_exam-type_body-part.json`

## 示例交互

### 自动提取日期
```
用户：@医疗报告/血液检查.jpg

输出:
✅ 检查单保存成功！
类型：生化检查（血液常规）
日期：2025-10-07（从图片提取）
提取到 15 项检查指标
```

### 手动指定日期
```
用户：@医疗报告/血液检查.jpg 2025-10-07

输出:
✅ 检查单保存成功！
类型：生化检查（血液常规）
日期：2025-10-07（使用用户指定日期）
```
