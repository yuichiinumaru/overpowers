---
name: business-ecommerce-price-comparison
version: 1.0.0
description: Price comparison skill for major Chinese e-commerce platforms (JD, Taobao, Tmall, Pinduoduo). Supports keyword search, link analysis, price history tracking, and purchase recommendations.
tags: [ecommerce, price-comparison, jd, taobao, shopping, analytical]
category: business
---

# 电商价格比较技能 (E-commerce Price Comparison)

本技能帮助用户在中国主流电商平台（京东、淘宝、天猫、拼多多）之间进行商品价格比较，找出最佳购买方案。

## 快速开始

### 基本使用方式

1. **提供商品信息**：可以给商品链接 or 商品名称
2. **执行价格比较**：技能会自动搜索各平台的价格
3. **查看分析结果**：获得价格对比 and 购买建议

### 示例命令

```
比较"iPhone 15"在各平台的价格
分析这个京东链接的价格：https://item.jd.com/123456.html
比较"小米手机" and "华为手机"的价格差异
```

## 核心功能

### 1. 价格抓取
- **京东**：支持自营 and 第三方商家
- **淘宝/天猫**：支持品牌官方店 and 普通店铺
- **拼多多**：支持百亿补贴 and 普通商品

### 2. 数据对比维度
- **价格**：售价、优惠价、券后价
- **服务**：运费、评价、店铺信誉

### 3. 分析算法
- **性价比计算**：结合价格、评价、店铺信誉
- **风险评估**：识别价格异常 or 可疑商品

## 技术实现

### 抓取策略
采用混合策略：浏览器自动化 (Playwright) + API 调用 + 数据缓存。

## 注意事项

1. **价格实时性**：电商价格变化频繁
2. **库存状态**：低价商品可能缺货
3. **账号差异**：不同账号可能看到不同价格

## 相关资源

- 比较逻辑: `references/comparison_logic.md`
- 抓取脚本: `scripts/`
