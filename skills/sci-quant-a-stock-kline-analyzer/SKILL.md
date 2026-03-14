---
name: sci-quant-a-stock-kline-analyzer
description: "A-share K-line analysis tool providing real-time market data, technical indicator calculation (MA, MACD, RSI), pattern recognition, and automated technical reports."
tags:
  - finance
  - stock-market
  - k-line
  - analysis
  - china
version: 1.0.0
---

# A-Stock Kline Analyzer

A股K线分析工具 - 提供实时行情、技术指标计算、K线形态识别 e 技术分析报告。

## 功能

- **实时行情**：新浪财经API获取实时价格
- **K线数据**：Baostock获取历史K线数据
- **技术指标**：MA、MACD、RSI、布林带
- **形态识别**：锤子线、十字星、吞没形态
- **分析报告**：自动生成技术分析报告
- **可视化**：生成K线图（可选）

## 数据源

| 数据类型 | 来源 | 稳定性 |
|---------|------|--------|
| 实时价格 | 新浪财经 | ✅ 稳定 |
| K线历史 | Baostock | ✅ 稳定 |

## 使用方法

```bash
# 基础分析
python3 scripts/kline_analyzer.py --code 600409 --days 30 --realtime --report

# 生成图表
python3 scripts/kline_analyzer.py --code 600409 --days 60 --plot --output chart.png

# JSON输出
python3 scripts/kline_analyzer.py --code 600409 --json
```

## 参数说明

| 参数 | 说明 | 示例 |
|-----|------|------|
| `--code` | 股票代码 | 600409 |
| `--days` | 获取天数 | 30 |
| `--period` | 周期 | daily/weekly/monthly |
| `--realtime` | 获取实时价格 | - |
| `--report` | 生成分析报告 | - |
| `--plot` | 生成图表 | - |
| `--output` | 图表保存路径 | chart.png |
| `--json` | JSON格式输出 | - |

## 依赖

- Python 3.8+
- pandas
- matplotlib
- baostock

## 安装

```bash
pip3 install baostock pandas matplotlib --break-system-packages
```

## 示例输出

```
📊 600409 三友化工 技术分析报告
==================================================
【实时行情】
最新价: 8.42 元
涨跌幅: -3.11%

【技术指标】
MA5: 8.62 (股价在下方📉)
RSI(14): 67.60 (中性➖)
MACD: 0.413 (金叉📈)

【综合建议】
• MACD金叉，短期动能偏多
```

## 免责声明

本工具仅供学习研究使用，不构成投资建议。股市有风险，投资需谨慎。

## 版本

v1.0.0 - 2026-03-09

## 许可证

MIT License
