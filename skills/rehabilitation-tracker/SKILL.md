---
name: rehabilitation-tracker
description: 康复训练管理技能，帮助记录康复进展、评估功能改善和达成康复目标，支持骨科康复、运动损伤、神经康复、心肺康复等多种类型。
tags: [rehabilitation, healthcare, fitness, training]
version: 1.0.0
category: healthcare
---

# 康复训练管理技能

全面的康复训练管理系统，帮助记录康复进展、评估功能改善和达成康复目标。

## 核心流程

```
用户输入 -> 识别操作类型 -> 提取参数信息 -> 检查完整性 -> [需补充] 询问用户
                                                      |
                                                   [信息完整]
                                                      |
                                              生成 JSON -> 保存数据 -> 输出确认
```

## 操作类型

| 输入关键词 | 操作类型 | 说明 |
|-----------|---------|------|
| start | start_rehab | 开始康复追踪 |
| exercise | exercise_log | 记录康复训练 |
| assess | functional_assessment | 功能评估 |
| progress | progress_report | 查看康复进展 |
| goals | goal_management | 康复目标管理 |
| plan | phase_management | 康复阶段管理 |

## 康复类型

### 骨科康复
- ACL 重建术后 (acl)
- 半月板手术 (meniscus)
- 骨折康复 (fracture)
- 关节置换 (replacement)
- 脊柱手术 (spine)

### 运动损伤
- 踝关节扭伤 (ankle)
- 膝关节损伤 (knee)
- 肩关节损伤 (shoulder)
- 网球肘 (tennis_elbow)

### 神经康复
- 脑卒中 (stroke)
- 脊髓损伤 (spinal)
- 帕金森 (parkinsons)

### 心肺康复
- 心脏手术 (cardiac)
- COPD (copd)

## 医学安全边界

### 不能做的事:
- 替代康复师的专业指导和治疗方案
- 给出具体的康复训练处方
- 诊断损伤程度或并发症

### 能做的事:
- 提供康复训练记录和进展追踪
- 提供功能评估记录和趋势分析
- 提供康复目标管理和达成追踪

## 紧急就医指征:
- 剧烈疼痛（>7/10）
- 关节明显肿胀或变形
- 完全无法负重或活动
- 出现麻木、无力等神经症状
