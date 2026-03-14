---
name: character-creator
version: 1.0.0
description: AI character creation workflow. Generates detailed character descriptions, portraits, and multi-angle reference images using the Seedream 4.5 model. Outputs HTML gallery pages for visual presentation.
tags: [character-design, image-generation, seedream, creative, asset-creation]
category: creative
---

# 角色创建器 (Character Creator)

使用即梦4.5 (Seedream) 模型创建完整的角色资产，包括详细描述、主肖像图 and 10个不同角度的参考图。每个阶段生成HTML展示页面。

## 创建流程 (Workflow)

### 第一步：生成详细角色描述
根据用户简短描述，扩展为详细角色描述（含年龄、性别、特征、服装、气质、画画风等）。

### 第二步：生成主肖像图
使用 `user-sora2-mcp / create_image_task` 生成角色主图。

### 第三步：生成肖像图HTML展示页面
读取模板并保存为 `character-portrait.html` 供展示。

### 第四步：生成多角度参考图
使用主肖像图作为参考，批量生成10个角度（正面特写、侧面、背面、俯视、仰视等）。

### 第五步：生成多角度HTML画廊页面
生成 `character-gallery.html` 集中展示所有角度参考图。

## 输出文件 (Outputs)

| 文件名 | 说明 |
|--------|------|
| `character-portrait.html` | 肖像图展示页面 |
| `character-gallery.html` | 多角度画廊页面 |

## 注意事项

1. 肖像图完成后立即生成HTML展示，不等角度图
2. 生成多角度时必须传入 `image_url` 参数
3. 轮询间隔5-10秒
