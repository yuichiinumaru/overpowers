---
name: fitness-plan
description: Generate personalized fitness and workout plans
tags:
  - health
  - fitness
version: 1.0.0
---

# fitness-plan

健身计划生成器。增肌、减脂、塑形。每日训练计划+饮食建议。

## Commands

| 命令 | 说明 |
|------|------|
| `fitness.sh workout "目标" [--level 新手\|中级\|高级]` | 生成训练计划（目标：增肌/减脂/塑形） |
| `fitness.sh diet "目标" "体重kg"` | 饮食方案（含热量和宏量素） |
| `fitness.sh cardio "时长分钟"` | 有氧训练方案 |
| `fitness.sh stretch` | 拉伸动作推荐 |
| `fitness.sh help` | 显示帮助信息 |

## Usage

当用户询问健身、训练计划、饮食方案、有氧或拉伸等话题时，使用对应命令。

**示例：**
```bash
# 新手增肌训练计划
bash scripts/fitness.sh workout "增肌" --level 新手

# 70kg减脂饮食方案
bash scripts/fitness.sh diet "减脂" "70"

# 30分钟有氧训练
bash scripts/fitness.sh cardio "30"

# 拉伸动作
bash scripts/fitness.sh stretch
```

将脚本输出作为回复内容的基础，根据用户体质和目标进行个性化调整。
