---
name: ops-orchestration-batch-processing-patterns
version: 1.0.0
description: Batch processing and long-running task orchestration patterns. Covers queue management, concurrency scheduling, interruption recovery, circuit breakers, remote task polling, and anti-anti-crawling strategies.
tags: [orchestration, batch-processing, concurrency, automation, resilience]
category: ops
---

# 批量处理与长时任务指南 (Batch Processing & Long-Running Tasks)

来自生产级桌面应用的实战经验，覆盖批量文件处理、远程 API 轮询、并发控制 and 错误恢复。

## 适用场景

- 批量文件处理（转码、压缩、水印）
- 远程 AI 任务轮询（视频生成、语音合成）
- 爬虫/批量 HTTP 请求
- 后台队列任务

---

## 1. 批处理架构

```
任务队列
├── 并发调度器（动态调整并发数）
│   ├── Worker 1 → processItem()
│   ├── Worker 2 → processItem()
│   └── Worker N → processItem()
├── 中止控制器（shouldStop + 子进程清理）
├── 熔断器（连续失败 N 次暂停）
├── 跳过检查（断点续传 / 前置过滤）
└── 进度报告（per-item + overall）
```

### 核心原则

1. **逐项处理，逐项报告** — 不等全部完成
2. **中断即停** — 每个 item 之间检查 abort 信号
3. **失败不中断** — 单项失败标记 `failed`，继续处理其他
4. **熔断保护** — 连续失败超阈值暂停整个队列

---

## 2. 并发调度

### 自适应并发池 (Adaptive Scheduler)

根据每个 item 的处理耗时动态调整并发数。

### 预设配置

| 场景 | 初始 | 最小 | 最大 | 慢阈值 |
|------|------|------|------|--------|
| CPU 密集（FFmpeg 转码） | 4 | 1 | CPU 核数 | 3s |
| API 调用（AI 服务） | 3 | 1 | 5 | 8s |
| 文件 I/O | 2 | 1 | 3 | 30s |
| 串行 | 1 | 1 | 1 | - |

---

## 3. 中断与恢复

### AbortController 模式
使用 `AbortController` 机制处理中止信号。

### 断点续传（shouldSkip）
维护 `completedSet` 并持久化到磁盘以支持断点续传。

---

## 4. 熔断器 (Circuit Breaker)

连续失败过多时自动暂停，避免无意义的重试浪费资源。

---

## 5. 远程任务轮询 (Task Polling)

### 关键要点
- **用 `setTimeout` 而非 `setInterval`** — 确保前一次完成后再调度下一次
- **超时保护** — 总轮询时间有上限
- **错误分类** — 瞬态错误继续，致命错误停止
- **去重** — 防止同一任务重复轮询

---

## 6. 错误分类与处理

| 错误类型 | 行为 | 示例 |
|---------|------|------|
| 瞬态网络错误 | 重试 | timeout, ECONNRESET |
| 401 Unauthorized | **停止** | API Key 无效 |
| 403 / 余额不足 | **停止** | 账户问题 |
| 429 Too Many Requests | **退避重试** | 限流 |
| 500+ Server Error | 有限重试 | 服务端异常 |

---

## 7. 进度报告 (Progress Reporting)

### 双层进度
整体进度 + 当前项进度。

---

## 8. 反风控策略 (Anti-Anti-Crawling)

### 三层防护
请求节流（同域名限速）→ 风控检测（响应分析）→ 指数退避重试

---

## 来源
提炼自生产级 Electron 桌面应用实战经验。
