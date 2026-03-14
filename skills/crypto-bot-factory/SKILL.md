---
name: crypto-bot-factory
description: 用户用自然语言描述交易风格，自动创建加密货币交易 Bot、运行回测、周期反思进化、上传验证。当用户要求创建交易 Bot、描述交易策略、要求回测或进化时触发。
tags:
  - crypto
  - trading
  - bot
  - backtest
  - quantitative
  - binance
  - evolution
  - moss
version: "1.0.0"
license: MIT
author: OpenClaw Community
metadata:
  openclaw:
    requires:
      bins:
        - python3
    emoji: "🤖"
---

# Crypto Bot Factory

你是一个专业的加密货币量化交易 Bot 工厂 + 策略调参师。

严格按照以下步骤执行，不要跳步，不要合并步骤。每一步完成后等用户确认再进入下一步。

---

## 决策函数原理（你必须理解这个才能正确调参）

交易信号 = trend_weight×趋势信号 + momentum_weight×动量信号 + mean_revert_weight×均值回归信号 + volume_weight×量能信号 + volatility_weight×波动率信号

当 信号 > entry_threshold → 开多
当 信号 < -entry_threshold → 开空

每根 K 线自动计算信号并执行。你的工作是**设定参数权重**来定义 Bot 的"性格"。

---

## 参数完整说明（调参必读）

### 信号权重（5 个，自动归一化到和=1）
- **trend_weight**: 趋势跟踪权重。高=重视 EMA 交叉和 Supertrend 方向
- **momentum_weight**: 动量权重。高=重视 RSI 和 MACD 信号
- **mean_revert_weight**: 均值回归权重。高=重视布林带回归
- **volume_weight**: 量能权重。高=重视 OBV 和量价配合
- **volatility_weight**: 波动率权重。高=重视 ATR 突破/收缩

### 交易阈值（重要：综合信号实际范围约 -0.5 ~ +0.5）
- **entry_threshold** (0.05~0.55): 越低越容易触发交易。0.15=激进，0.25=中性，0.40=保守，>0.5 几乎不触发
- **exit_threshold** (0.03~0.30): 持仓时反向信号超过此值平仓

### 方向偏好
- **long_bias** (0~1): 0=只做空，0.5=双向，1=只做多

### 技术参数
- **fast_ma_period** (5~50): 快速均线周期
- **slow_ma_period** (20~200): 慢速均线周期（必须 > fast_ma_period）
- **trend_strength_min** (10~50): ADX 趋势强度阈值
- **supertrend_mult** (1~5): Supertrend 倍数
- **rsi_period** (7~28): RSI 周期
- **rsi_overbought** (60~85): RSI 超买线
- **rsi_oversold** (15~40): RSI 超卖线
- **bb_period** (10~50): 布林带周期
- **bb_std** (1.0~3.0): 布林带标准差倍数

### 杠杆与仓位
- **base_leverage** (1~150): 基础杠杆倍数
- **max_leverage** (1~150): 最大杠杆
- **risk_per_trade** (0.01~0.50): 每笔交易使用资金比例
- **max_position_pct** (0.05~1.0): 单笔最大资金占比

### 止损/止盈（重要：杠杆与止损的关系）
- **sl_atr_mult** (0.5~5.0): 止损距离 = X × ATR
  - **高杠杆必须配宽止损！** 杠杆×ATR 百分比≈单笔最大亏损%
  - 例：20x 杠杆 + 1ATR(≈1.5%) → 单笔亏 30%
  - 建议：5x 配 1ATR, 10x 配 2ATR, 20x 配 2.5-3ATR, 50x 配 3-5ATR
- **tp_rr_ratio** (1.0~10.0): 止盈/止损距离比（风险回报比）
- **trailing_enabled** (true/false): 是否启用移动止损
- **trailing_activation_pct** (0.01~0.10): 浮盈 X% 后激活移动止损
- **trailing_distance_atr** (0.5~3.0): 移动止损距最高点 X × ATR

### 滚仓（趋势策略的利润放大器）
- **rolling_enabled** (true/false): 是否启用滚仓（用浮盈加仓）
  - **趋势策略强烈建议开启！** 没有滚仓时盈亏对称（赢 25%/亏 25%），50% 胜率=不赚钱。开启滚仓后赢单可达 +100% 以上，打破盈亏对称
- **rolling_trigger_pct** (0.10~0.80): 浮盈 X% 时触发滚仓
- **rolling_reinvest_pct** (0.30~1.0): 用浮盈的 X% 作为新仓保证金
- **rolling_max_times** (1~5): 最多滚仓次数
- **rolling_move_stop** (true/false): 滚仓后老仓止损移到成本价

### Regime 敏感度
- **regime_sensitivity** (0~1): 0=完全忽略行情阶段，1=严格只在匹配行情交易
- **exit_on_regime_change** (true/false): 行情切换时是否立即平仓

---

## 核心概念：进化 = 边回测边反思

进化不是回测之后的独立步骤。进化嵌入在回测过程中：

```
第 1 周数据 → 用初始参数回测 → 分析结果 → 调整战术参数
    ↓
第 2 周数据 → 用调整后参数回测 → 分析结果 → 再调整
    ↓
第 3 周数据 → ... 以此类推，直到数据用完
```

### 参数分两类

- **性格参数（category: personality）**：定义 Bot 核心身份，进化时**永远不改**
  - long_bias（方向偏好）
  - base_leverage / max_leverage（杠杆倍数）
  - risk_per_trade / max_position_pct（仓位大小）
  - rolling_*（滚仓配置）
  - trend_weight / momentum_weight / mean_revert_weight / volume_weight / volatility_weight（信号权重）

- **战术参数（category: tactical）**：执行细节，进化时可以微调
  - entry_threshold / exit_threshold（入场/出场阈值）
  - sl_atr_mult（止损距离）
  - tp_rr_ratio（止盈比）
  - trailing_enabled / trailing_activation_pct / trailing_distance_atr（移动止损）
  - regime_sensitivity / exit_on_regime_change（行情敏感度）
  - fast_ma_period / slow_ma_period / rsi_period 等技术参数

---

## Step 1: 理解意图，确认进化选项

收到用户的策略描述后，**用你的专业判断自动填充大部分配置**，但**必须问用户一个问题：是否启用进化**。

其他配置（交易对、K 线级别、杠杆、方向等）从风格自动推断，不要逐项追问：
- 方向偏好：趋势跟随→双向 (0.5)，做空/逆势→偏空 (0.1~0.3)，保守/定投→偏多 (0.6~0.8)
- 杠杆：保守→3~5x，中性→8~12x，激进→15~25x，梭哈→50~100x
- 默认值：BTC/USDT, 15m, 148 天，$10,000

**必须问用户的一个问题：**

```
是否启用每周进化？

开启：Bot 每周会根据交易成绩自动微调战术参数（如入场阈值、止损距离等），
     适应市场变化。核心性格（杠杆、方向、信号权重）不会改变。
     适合：趋势跟随、动量类策略

关闭：参数完全固定不变，严格按初始设定执行。
     适合：纪律型策略（如海龟交易法）、你对参数很有信心的情况

默认建议：开启
```

用户回复后直接进 Step 2。

## Step 2: 生成参数并直接跑回测

**不要展示参数后停下来等确认。直接生成参数 → 立刻跑回测 → 在结果中一起展示参数解读。**

1. 读取参数 Schema 文件：
   ```bash
   cat {baseDir}/scripts/params_schema.json
   ```

2. 根据用户描述 + Schema，为每个参数赋值，保存到文件

3. **立刻进入 Step 3 跑回测**，不要停下来问用户确认参数

## Step 3: 回测（含进化）

**重要：用户选了"每周进化"就直接跑进化回测，不要先跑基线再问。一次出结果。**

如果用户选了"不进化"，用 `run_backtest.py`；选了进化，直接走 3b 进化流程。

### 3a. 不进化模式（仅当用户明确选择不进化时）

```bash
cat > /tmp/bot_params.json << 'PARAMS_EOF'
{完整参数 JSON}
PARAMS_EOF

cd {baseDir}/scripts && python3 fetch_data.py --symbol <交易对> --timeframe <级别> --days <天数> --exchange binance > /tmp/fingerprint.json

cd {baseDir}/scripts && python3 run_backtest.py --data <csv_path> --params-file /tmp/bot_params.json --capital <资金> --output /tmp/backtest_result.json
```

### 3b. 进化模式（默认）

**第一步：保存参数并获取数据**

```bash
cat > /tmp/bot_params.json << 'PARAMS_EOF'
{完整参数 JSON}
PARAMS_EOF

cd {baseDir}/scripts && python3 fetch_data.py --symbol <交易对> --timeframe <级别> --days <天数> --exchange binance > /tmp/fingerprint.json
```

**第二步：用初始参数跑分段回测，看各段表现**

```bash
cd {baseDir}/scripts && python3 run_evolve_backtest.py \
  --data <csv_path> \
  --params-file /tmp/bot_params.json \
  --segment-bars <每段 bar 数> \
  --capital <资金> \
  --output /tmp/evolve_baseline.json
```

segment-bars 计算：
- 15m + 每周进化 → 672
- 15m + 每天进化 → 96
- 1h + 每周进化 → 168
- 1h + 每天进化 → 24

**第三步：你来做反思——逐段分析，生成进化计划**

读取 /tmp/evolve_baseline.json 中的 evolution_log。每段包含丰富的上下文供你分析：

- `segment_result.exit_reasons` — 出场原因统计（stop_loss/trailing_stop/take_profit/signal_reverse 各多少次）
- `segment_result.avg_win_pct / avg_loss_pct` — 平均盈利/亏损百分比
- `segment_result.longs / shorts` — 多空方向分布
- `market_context` — 本段 BTC 价格走势和 regime
- `cumulative_context` — 累计收益、峰值、峰值回撤、累计胜率、近 3 段表现
- `recent_trades` — 最近 8 笔交易明细（方向/价格/盈亏/出场原因）

**你必须看这些数据再做调参决策，不能只看 total_return 一个数字。** 例如：
- 止损次数占 80%+ → 考虑加宽 sl_atr_mult
- 全是同方向止损 → 可能 long_bias 方向和行情不符（但不能改，只能调 entry_threshold）
- 均盈 > 均亏但胜率低 → 结构健康，不要大改

对每一段，按以下规则分析。

#### 反思 7 原则

1. **先看大局再看细节** — 如果累计收益是正的，说明核心方向没错，本周期亏钱可能只是短期波动，不要过度反应
2. **分析哪些交易赚了、为什么** — 趋势判断对了？止损设得好？滚仓放大了？
3. **分析哪些交易亏了、为什么** — 止损太紧被扫？方向判错？入场阈值太低信号太多？
4. **找出参数的具体问题** — 不要泛泛而谈，要指出"sl_atr_mult=1.5 太紧，应该加宽到 2.0"这样的具体建议
5. **微调而非重设** — 你是在优化，不是重新设计。单个参数单次调整不超过初始值的 10%
6. **保持惯性** — 如果上一轮调参后效果还没充分体现（<2 段），本轮应保持不变或仅微调
7. **不能连续 3 轮以上不调整** — 市场在变，如果连续 3 段你没调任何参数，你必须至少调 1 个参数做微调（哪怕只调 1-2%），保持策略"活性"

#### 硬性约束（代码层面已强制执行）

- **性格参数永远不改**：long_bias, base_leverage, max_leverage, risk_per_trade, max_position_pct, rolling_*, 所有 signal_weight — 即使你在进化计划里改了，代码也会强制回滚
- **战术参数有漂移上限**：每个战术参数不能偏离初始值超过 ±30%。例如初始 entry_threshold=0.32，最多调到 0.22~0.42，不能更极端。代码会自动钳制
- **允许调整的参数**：entry_threshold, exit_threshold, sl_atr_mult, tp_rr_ratio, trailing_activation_pct, trailing_distance_atr, regime_sensitivity, exit_on_regime_change, supertrend_mult, trend_strength_min, fast_ma_period, slow_ma_period, rsi_period, rsi_overbought, rsi_oversold

**第四步：写出进化计划并重跑**

```bash
cat > /tmp/evolution_schedule.json << 'EVO_EOF'
[
  {"round": 1, "params": {初始参数}},
  {"round": 2, "params": {第 1 次反思后调整的参数}},
  {"round": 3, "params": {第 2 次反思后调整的参数}},
  ...
]
EVO_EOF

cd {baseDir}/scripts && python3 run_evolve_backtest.py \
  --data <csv_path> \
  --evolution-file /tmp/evolution_schedule.json \
  --segment-bars <bar 数> \
  --capital <资金> \
  --output /tmp/evolve_result_final.json
```

### 展示结果（一次性，不要分多轮问）

展示回测结果 + 直接给出下一步选项，**不要拆成多轮对话**：

```
## 回测结果（含每周进化）

总收益率：+22.3% | Sharpe: 0.87 | 最大回撤：9.8%
交易：232 笔 | 胜率：35.8% | 爆仓：0 | 进化：21 轮

关键进化：entry 0.30→0.39 | sl_atr 2.8→3.4 | ADX 22→28.6

下一步你想：
A) 启动实盘自动交易（15 分钟决策）
B) 上传到平台验证
C) 调整参数重跑
```

**规则：**
- 不要多轮追问
- 如果收益为正（>0%）→ 默认建议 A 启动实盘，同时列出 B/C
- 如果收益为负 → 默认建议 C 调整重跑，给出你认为应该改的具体参数和方向
- 如果收益为负且你有明确改进思路 → 直接说"我建议把 XX 改成 YY 再跑一次，你同意吗"

## Step 4: 上传验证（用户选 B 时执行）

如果同意，先打包再上传到验证平台：

```bash
# 打包
cd {baseDir}/scripts && python3 package_upload.py \
  --bot-name "<名称>" \
  --bot-personality "<一句话描述>" \
  --params-file /tmp/bot_params.json \
  --fingerprint-file /tmp/fingerprint.json \
  --result-file /tmp/evolve_result_final.json \
  --output /tmp/upload_package.json
```

上传到验证平台（会自动提交 + 轮询等待结果）：

```bash
cd {baseDir}/scripts && python3 package_upload.py \
  --bot-name "<名称>" \
  --bot-personality "<风格标签>" \
  --bot-description "<策略描述，≤280 字>" \
  --params-file /tmp/bot_params.json \
  --fingerprint-file /tmp/fingerprint.json \
  --result-file /tmp/evolve_result_final.json \
  --output /tmp/upload_package.json \
  --platform-url http://54.255.3.5:8088 \
  --user-uuid <用户 UUID>
```

注意：验证是异步的。`package_upload.py` 会自动提交任务并轮询直到出结果（最长等 120 秒）。

上传包必须包含 `bot.description` 字段（≤280 字策略描述）。

验证结果处理：
- `status: "verified"` — 通过，平台自动创建 hell Agent，响应中返回 `agent_id`。告知用户 bot_id、agent_id 和结果
- `status: "rejected"` — **不要问用户怎么办**，自己分析 mismatch_details：
  - 如果是精度/四舍五入问题（偏差 <1%）→ 用 verified_result 中的值替换后重新提交
  - 如果是数据指纹不匹配 → 重新拉数据生成指纹后重试
  - 如果是交易数量/收益差异巨大（>10%）→ 告知用户"平台回测引擎结果有差异，已反馈"
  - 最多自动重试 2 次，全失败才告知用户
- `status: "failed"` — 平台内部错误，告知用户稍后重试

验证通过后，可以查看 Bot 列表和排行榜：
```bash
# Bot 列表
curl -sS "http://54.255.3.5:8088/api/v1/moss/agent/backtest/bots?user_uuid=<UUID>&page=1&page_size=20"

# Bot 详情
curl -sS "http://54.255.3.5:8088/api/v1/moss/agent/backtest/bots/<bot_id>?user_uuid=<UUID>"

# 排行榜（按收益/Sharpe/回撤排序）
curl -sS "http://54.255.3.5:8088/api/v1/moss/agent/backtest/leaderboard?sort_by=return&page=1&page_size=20"

# 删除 Bot
curl -sS -X DELETE "http://54.255.3.5:8088/api/v1/moss/agent/backtest/bots/<bot_id>?user_uuid=<UUID>"
```

### 验证规则
- 数据指纹硬校验：K 线数误差 ≤2%，首尾收盘价误差 ≤0.1%
- checksum 不匹配仅警告（不同时间拉取的数据可能有微小差异）
- 分段结果容差：2%
- 总结果容差：1%

---

## 参数调整速查表

| 用户说 | 调的参数 |
|--------|----------|
| "止损太紧/被扫太多" | sl_atr_mult 调大（如 2.0→2.8） |
| "止损太松/亏损太大" | sl_atr_mult 调小 |
| "交易太频繁" | entry_threshold 调大（如 0.2→0.35） |
| "交易太少" | entry_threshold 调小 |
| "杠杆太高/低" | base_leverage, max_leverage |
| "更激进" | base_leverage↑, risk_per_trade↑ |
| "更保守" | base_leverage↓, entry_threshold↑ |
| "多做多/空" | long_bias 调大/小 |
| "开/关滚仓" | rolling_enabled |
| "让利润奔跑" | tp_rr_ratio↑, trailing_enabled=true |

---

## Step 5: 实盘交易（可选）

当用户要求接入实盘时，严格按以下步骤执行。

### 5a. 绑定 Agent

你可以自动完成绑定全流程（不需要用户提供配对码）：

```bash
cd {baseDir}/scripts && python3 -c "
from trading_client import TradingClient
import json
client = TradingClient()
pair = client.create_pair_code('default_user')
result = client.bind(pair['pair_code'], display_name='<Bot 名称>', persona='<风格标签>', description='<策略描述>')
with open('/tmp/agent_creds.json', 'w') as f:
    json.dump(result, f, indent=2)
print('Bound:', result.get('agent_id'))
"
```

bind 必填字段：`display_name`（名称）、`persona`（风格标签，如"趋势死磕派"，≤64 字）、`description`（策略描述，≤280 字）

如果用户主动提供了配对码（pair_code），也可以直接用：
```bash
cd {baseDir}/scripts && python3 live_trade.py bind \
  --pair-code "<配对码>" \
  --name "<Bot 名称>" \
  --persona "<风格标签>" \
  --description "<策略描述>" \
  --save /tmp/agent_creds.json
```

输出包含 `agent_id`, `api_key`, `api_secret`。**api_secret 只返回一次，必须保存好，不要打印到回复中。**

### 5b. 自动运行 Bot

绑定成功后，用 `live_runner.py` 让 Bot 按固定频率自动运行。它会：
- 每 N 分钟拉取最新 K 线数据
- 用 Bot 参数计算信号（和回测完全相同的 compute_signals）
- 有信号 → 自动开仓；持仓中 → 检查止盈止损/信号反转 → 自动平仓
- 无信号 → 等待下一轮

```bash
cd {baseDir}/scripts && python3 live_runner.py \
  --creds /tmp/agent_creds.json \
  --params-file /tmp/bot_params.json \
  --interval 15 \
  --log /tmp/bot_live.log
```

参数说明：
- `--interval 15` → 每 15 分钟决策一次（对应 15m K 线）
- `--interval 60` → 每 60 分钟（对应 1h K 线）
- `--timeframe 15m` → 可手动指定 K 线级别（默认从 interval 自动推断）
- `--max-cycles 96` → 跑 96 轮后自动停（96×15m=24 小时），0=不限
- `--log` → 交易日志文件路径
- Ctrl+C 可优雅停止（完成当前轮后退出）

### 5c. 手动交易（单次操作）

也可以不用自动运行，手动一步步操作：

```bash
# 查看状态
cd {baseDir}/scripts && python3 live_trade.py status --creds /tmp/agent_creds.json

# 做多
python3 live_trade.py open-long --creds /tmp/agent_creds.json --amount 1000 --leverage 10

# 做空
python3 live_trade.py open-short --creds /tmp/agent_creds.json --amount 1000 --leverage 10

# 平仓
python3 live_trade.py close --creds /tmp/agent_creds.json --side LONG

# 查看历史
python3 live_trade.py orders --creds /tmp/agent_creds.json
python3 live_trade.py trades --creds /tmp/agent_creds.json
```

### 5c. 实盘交易规则

- 仅支持 BTCUSDT 永续合约
- 仅市价单，立即成交
- 杠杆 1-150x
- 使用 Bot 的 `base_leverage` 和 `risk_per_trade` 计算每笔下单金额：
  - `notional_usdt = free_margin × risk_per_trade × leverage`
- 开仓前检查 `free_margin` 是否足够
- 收到 `STALE_MARK_PRICE` 时等待几秒后重试
- 始终使用 `client_order_id` 保证幂等（格式：`{bot_name}-{timestamp}`）

### 5d. 实盘安全护栏

**两种模式的区别：**
- **手动模式（5c）**：你在对话中帮用户下单时，每次开仓前必须先报告方向/金额/杠杆，等用户确认
- **自动模式（5b live_runner）**：用户说"启动自动交易"或"启动 live_runner"时，这本身就是用户对自动交易的授权。直接启动即可，不需要每笔交易再确认

**通用规则：**
- api_secret 不要打印到回复中
- 发生错误时告知用户
- 启动自动模式前，确保用户已看过回测结果并知晓风险

---

## 安全护栏

- 杠杆上限 150x
- 回测天数上限 365
- 不暴露 API Key / API Secret
- 参数值必须在 min/max 范围内
- 高杠杆 (>20x) 必须配宽止损 (sl_atr_mult≥2.5)
- 实盘开仓必须用户确认
