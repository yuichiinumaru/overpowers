---
name: visual-creative
description: 视觉创意生图提示词生成 skill。当用户需要为任何视觉物料生成 AI 生图提示词时使用，包括海报、banner、产品图、社交媒体配图、概念艺术、品牌物料等所有视觉场景。
tags: [视觉创意，AI 生图，提示词生成，创意设计，海报设计]
version: 1.0.0
category: creative
---

# 视觉创意生图 Skill

## 概述

本 skill 帮助 AI 将用户的视觉需求转化为富有创意的 AI 生图提示词。核心目标是突破平庸，解决三个常见问题：
1. **创意局限**：避免走最安全、最常见的视觉解法
2. **构图死板**：避免均匀分布和居中对称的惰性构图
3. **画面空洞**：主动填充丰富的视觉细节和层次

## 处理流程

分析需求 → 识别场景 → 调取创意方法 → 生成设计思路（用户可见）→ 输出提示词（传递下游）

## 场景子文件索引

识别用户需求后，读取对应场景子文件获取场景专属创意方向：

| 场景 | 子文件路径 |
|-----|----------|
| 电商主图与详情页 | scenes/ecommerce.md |
| 促销海报与活动 banner | scenes/promotion.md |
| 户外广告 OOH | scenes/ooh.md |
| 产品概念图与产品海报 | scenes/product.md |
| 品牌视觉与品牌故事图 | scenes/brand.md |
| 包装设计概念 | scenes/packaging.md |
| 通用海报设计 | scenes/general-poster.md |
| 小红书视觉 | scenes/xiaohongshu.md |
| 抖音视觉 | scenes/douyin.md |
| 微信公众号视觉 | scenes/wechat-oa.md |
| 微博视觉 | scenes/weibo.md |
| 短视频封面与缩略图 | scenes/video-cover.md |
| 信息图与数据可视化 | scenes/infographic.md |
| 电影与剧集海报 | scenes/film-poster.md |
| 游戏视觉与游戏海报 | scenes/game.md |
| 音乐封面与艺人宣传图 | scenes/music.md |
| 概念艺术与插画 | scenes/concept-art.md |
| 摄影风格图 | scenes/photography.md |
| 抽象艺术与实验性视觉 | scenes/abstract.md |
| 活动现场视觉与展览 | scenes/event.md |
| 室内空间概念图 | scenes/interior.md |
