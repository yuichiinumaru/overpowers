---
name: brand-namer
description: Generate creative brand and product names
tags:
  - business
  - branding
version: 1.0.0
---

# brand-namer

品牌命名和Slogan生成器。品牌名、广告语、域名建议。中英双语。

## Description

为产品/公司生成品牌名称、广告语、域名建议和品牌故事。支持中英双语输出，覆盖品牌建设全流程。

## Commands

| 命令 | 用法 | 说明 |
|------|------|------|
| `name` | `brand.sh name "行业" "调性关键词"` | 生成10个品牌名（中英双语） |
| `slogan` | `brand.sh slogan "品牌名" "行业"` | 生成5条广告语 |
| `domain` | `brand.sh domain "品牌名"` | 域名建议（含后缀推荐） |
| `story` | `brand.sh story "品牌名" "行业"` | 生成品牌故事 |
| `help` | `brand.sh help` | 显示帮助信息 |

## Usage

当用户需要品牌命名、广告语、域名或品牌故事时，运行对应脚本命令，将输出结果展示给用户。

```bash
# 生成品牌名
bash {{SKILL_DIR}}/scripts/brand.sh name "咖啡" "高端,简约"

# 生成广告语
bash {{SKILL_DIR}}/scripts/brand.sh slogan "星沐" "咖啡"

# 域名建议
bash {{SKILL_DIR}}/scripts/brand.sh domain "星沐"

# 品牌故事
bash {{SKILL_DIR}}/scripts/brand.sh story "星沐" "咖啡"
```

## Notes

- 纯本地生成，无需API
- Python 3.6+ 兼容
- 输出中英双语
