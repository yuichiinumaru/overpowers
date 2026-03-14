---
name: 12306-train-assistant
description: "12306 查询与订票辅助技能，支持余票查询、经停站查询、中转换乘、候补查询、登录状态检查及下单流程；当用户提到火车票、高铁票、经停站、中转、候补或 12306 查票时触发。"
metadata:
  openclaw:
    category: "ai"
    tags: ['ai', 'automation', 'generation']
    version: "1.0.0"
---

# 12306 CLI Skill 🚄

## 目标

用本仓库的 `client.py` 完成 12306 相关查询与下单辅助，优先覆盖：

- 余票查询：`left-ticket`
- 中转换乘：`transfer-ticket`
- 经停站：`route`（支持 `--train-code` 自动解析）
- 登录态检查：`status`
- 候补查询：`candidate-queue` / `candidate-orders`
- 需要登录的操作：`passengers` / `orders` / `book`

## 触发信号

用户提到下列需求时触发本技能：

- “查明天北京到上海余票”
- “G1033 经停站”
- “深圳到拉萨怎么中转”
- “候补排队状态怎么样”
- “12306 登录状态”

## 执行原则

1. 默认用 `text` 输出（便于用户阅读）；仅在用户明确要求结构化数据时加 `--json`。
2. 解析相对日期（今天/明天/后天）为 `YYYY-MM-DD` 后再执行命令。
3. 站名支持中文/拼音/三字码，直接传给命令即可。
4. `route` 优先用 `--train-code`，减少用户提供 `train_no` 的负担。
5. 失败时先给出可执行修复建议（缺参数、日期格式、站名不匹配、风控限制等）。

## 常用示例

### 示例 1：余票查询

```bash
python3 client.py left-ticket --date 2026-03-23 --from 北京南 --to 上海虹桥
python3 client.py left-ticket --date 2026-03-23 --from 北京 --to 上海 --limit 10 --json
```

### 示例 2：中转换乘

```bash
python3 client.py transfer-ticket --date 2026-03-23 --from 深圳 --to 拉萨 --limit 10
python3 client.py transfer-ticket --date 2026-03-23 --from 深圳 --to 拉萨 --middle 西安 --json
```

### 示例 3：经停站

```bash
# 推荐：直接用车次号，脚本自动解析 train_no
python3 client.py route --train-code C956 --date 2026-03-23 --from 南部 --to 南充北

# 已知 train_no 时可直查
python3 client.py route --train-no 760000C95604 --date 2026-03-23 --from NBE --to NCE
```

### 示例 4：登录与状态

```bash
python3 client.py status
python3 client.py login --username <账号> --password <密码>
python3 client.py login --username <账号> --id-last4 <证件后4位> --send-sms
python3 client.py login --username <账号> --id-last4 <证件后4位> --sms-code <6位验证码>
```

### 示例 5：乘车人与订单

```bash
python3 client.py passengers --limit 50
python3 client.py orders --where G --page-size 20
python3 client.py orders --where H --start-date 2026-02-01 --end-date 2026-03-01
```

### 示例 6：订票（预检与提交）

```bash
# 只校验，不最终提交
python3 client.py book --date 2026-03-23 --from 北京南 --to 上海虹桥 --train-code G101 --seat second_class --passengers 张三 --dry-run

# 正式提交
python3 client.py book --date 2026-03-23 --from 北京南 --to 上海虹桥 --train-code G101 --seat second_class --passengers 张三
```

### 示例 7：候补查询

```bash
# 候补排队状态
python3 client.py candidate-queue

# 候补订单（进行中）
python3 client.py candidate-orders

# 候补订单（已处理）
python3 client.py candidate-orders --processed --start-date 2026-03-11 --end-date 2026-04-09 --limit 20
```

## 每个命令参数说明

### 全局参数（所有命令可用）

| 参数 | 必填 | 默认值 | 说明 |
|---|---|---|---|
| `--base-url` | 否 | `https://kyfw.12306.cn` | 12306 服务地址 |
| `--timeout` | 否 | `15` | 请求超时时间（秒） |
| `--cookie-file` | 否 | `~/.kyfw_12306_cookies.json` | cookie 持久化文件 |
| `--json` | 否 | 关闭 | 以 JSON 输出结果 |

### `left-ticket` 余票查询

| 参数 | 必填 | 默认值 | 说明 |
|---|---|---|---|
| `--date` | 是 | 无 | 出发日期，`YYYY-MM-DD` |
| `--from` | 是 | 无 | 出发站（中文/拼音/三字码） |
| `--to` | 是 | 无 | 到达站（中文/拼音/三字码） |
| `--purpose` | 否 | `ADULT` | 乘客类型 |
| `--endpoint` | 否 | `queryG` | 余票接口类型，`queryG` 或 `queryZ` |
| `--limit` | 否 | `20` | 文本输出时最多展示行数 |

### `transfer-ticket` 中转换乘

| 参数 | 必填 | 默认值 | 说明 |
|---|---|---|---|
| `--date` | 是 | 无 | 出发日期，`YYYY-MM-DD` |
| `--from` | 是 | 无 | 出发站 |
| `--to` | 是 | 无 | 到达站 |
| `--middle` | 否 | 空 | 指定换乘站，不传则自动推荐 |
| `--result-index` | 否 | `0` | 分页游标 |
| `--can-query` | 否 | `Y` | 是否继续查询更多方案（`Y/N`） |
| `--show-wz` | 否 | 关闭 | 显示无座方案 |
| `--purpose` | 否 | `00` | 中转接口乘客类型参数 |
| `--channel` | 否 | `E` | 中转接口渠道参数 |
| `--endpoint` | 否 | `queryG` | 中转接口类型，`queryG` 或 `queryZ` |
| `--limit` | 否 | `20` | 文本输出时最多展示方案数 |

### `route` 经停站查询

| 参数 | 必填 | 默认值 | 说明 |
|---|---|---|---|
| `--train-code` | 二选一 | 无 | 车次号（如 `C956`、`G1033`），会自动解析 `train_no` |
| `--train-no` | 二选一 | 无 | 内部车次号（如 `760000C95604`） |
| `--date` | 是 | 无 | 查询日期，`YYYY-MM-DD` |
| `--from` | 是 | 无 | 区间出发站 |
| `--to` | 是 | 无 | 区间到达站 |
| `--endpoint` | 否 | `queryG` | 仅 `--train-code` 模式下用于解析 `train_no` |
| `--purpose` | 否 | `ADULT` | 仅 `--train-code` 模式下用于解析 `train_no` |
| `--limit` | 否 | `200` | 文本输出时最多展示站点数 |

### `login` 登录

| 参数 | 必填 | 默认值 | 说明 |
|---|---|---|---|
| `--username` | 是 | 无 | 12306 用户名/邮箱/手机号 |
| `--password` | 否 | 交互输入或 `KYFW_PASSWORD` | 登录密码 |
| `--id-last4` | 否 | 无 | 证件号后 4 位，短信验证场景需要 |
| `--sms-code` | 否 | 无 | 6 位短信验证码 |
| `--send-sms` | 否 | 关闭 | 仅发送短信验证码，不执行完整登录 |

### `status` 登录状态检查

无专属参数，仅使用全局参数。

### `passengers` 乘车人查询

| 参数 | 必填 | 默认值 | 说明 |
|---|---|---|---|
| `--limit` | 否 | `200` | 文本输出最多展示人数 |
| `--username` | 否 | 无 | cookie 失效时可用于自动补登录 |
| `--password` | 否 | 交互输入或 `KYFW_PASSWORD` | 自动补登录时使用 |
| `--id-last4` | 否 | 无 | 自动补登录短信场景 |
| `--sms-code` | 否 | 无 | 自动补登录短信场景 |

### `orders` 订单查询

| 参数 | 必填 | 默认值 | 说明 |
|---|---|---|---|
| `--where` | 否 | `G` | `G` 未出行/近期，`H` 历史订单 |
| `--start-date` | 否 | 自动计算 | 查询起始日期，`YYYY-MM-DD` |
| `--end-date` | 否 | 今天 | 查询结束日期，`YYYY-MM-DD` |
| `--page-index` | 否 | `0` | 页码 |
| `--page-size` | 否 | `8` | 每页条数 |
| `--query-type` | 否 | `1` | 订单查询类型 |
| `--train-name` | 否 | 空 | 可按车次过滤 |
| `--username` | 否 | 无 | cookie 失效时用于自动补登录 |
| `--password` | 否 | 交互输入或 `KYFW_PASSWORD` | 自动补登录时使用 |
| `--id-last4` | 否 | 无 | 自动补登录短信场景 |
| `--sms-code` | 否 | 无 | 自动补登录短信场景 |

### `candidate-queue` 候补排队状态

| 参数 | 必填 | 默认值 | 说明 |
|---|---|---|---|
| `--username` | 否 | 无 | cookie 失效时用于自动补登录 |
| `--password` | 否 | 交互输入或 `KYFW_PASSWORD` | 自动补登录时使用 |
| `--id-last4` | 否 | 无 | 自动补登录短信场景 |
| `--sms-code` | 否 | 无 | 自动补登录短信场景 |

### `candidate-orders` 候补订单查询

| 参数 | 必填 | 默认值 | 说明 |
|---|---|---|---|
| `--processed` | 否 | 关闭 | 查询已处理候补订单；默认查询进行中 |
| `--page-no` | 否 | `0` | 页码 |
| `--start-date` | 否 | 今天 | 查询起始日期，`YYYY-MM-DD` |
| `--end-date` | 否 | 起始日期+29天 | 查询结束日期，`YYYY-MM-DD` |
| `--limit` | 否 | `20` | 文本输出最多展示条数 |
| `--username` | 否 | 无 | cookie 失效时用于自动补登录 |
| `--password` | 否 | 交互输入或 `KYFW_PASSWORD` | 自动补登录时使用 |
| `--id-last4` | 否 | 无 | 自动补登录短信场景 |
| `--sms-code` | 否 | 无 | 自动补登录短信场景 |

### `book` 订票

| 参数 | 必填 | 默认值 | 说明 |
|---|---|---|---|
| `--date` | 是 | 无 | 出发日期，`YYYY-MM-DD` |
| `--from` | 是 | 无 | 出发站 |
| `--to` | 是 | 无 | 到达站 |
| `--train-code` | 是 | 无 | 目标车次（如 `G101`） |
| `--seat` | 是 | 无 | 席别（如 `second_class` / `O` / `一等座`） |
| `--passengers` | 是 | 无 | 乘客姓名，多个用逗号分隔 |
| `--purpose` | 否 | `ADULT` | 乘客类型 |
| `--endpoint` | 否 | `queryG` | 余票接口类型 |
| `--choose-seats` | 否 | 空 | 选座（如 `A1B1`） |
| `--max-wait-seconds` | 否 | `30` | 排队轮询最长等待秒数 |
| `--poll-interval` | 否 | `1.5` | 排队轮询间隔（秒） |
| `--dry-run` | 否 | 关闭 | 只检查不提交最终确认 |
| `--username` | 否 | 无 | cookie 失效时用于自动补登录 |
| `--password` | 否 | 交互输入或 `KYFW_PASSWORD` | 自动补登录时使用 |
| `--id-last4` | 否 | 无 | 自动补登录短信场景 |
| `--sms-code` | 否 | 无 | 自动补登录短信场景 |

## 参数提取规则

- 出发站：`--from`
- 到达站：`--to`
- 日期：`--date`（格式 `YYYY-MM-DD`）
- 经停场景：用户给车次号（如 `G1033`、`C956`）时用 `--train-code`
- 经停场景：用户给内部号（如 `760000C95604`）时用 `--train-no`
- 查询区间优先用用户提供的 `from/to`

## 输出策略

- 默认输出文本结果并概括关键信息。
- 若用户说“返回 JSON / 机器可读”，添加 `--json` 并返回结构化摘要。
- 当前 CLI 没有内置 `csv` 输出，不要承诺 CSV。

## 示例工作流

### 示例 A：余票

用户：“查明天北京到上海余票”

```bash
python3 client.py left-ticket --date <明天日期> --from 北京 --to 上海
```

### 示例 B：经停站

用户：“C956 经停哪些站”

如果用户未给日期或区间，先补齐最小参数（日期、from、to）；拿到后执行：

```bash
python3 client.py route --train-code C956 --date <日期> --from <出发站> --to <到达站>
```

### 示例 C：中转

用户：“深圳到拉萨怎么中转”

```bash
python3 client.py transfer-ticket --date <日期> --from 深圳 --to 拉萨 --limit 10
```

### 示例 D：候补

用户：“帮我看看候补订单有没有兑现”

```bash
python3 client.py candidate-orders --processed --start-date <起始日期> --end-date <结束日期> --limit 20
```

## 限制与注意

1. 中转结果来自 12306 推荐，不保证覆盖所有可行组合。
2. 可能触发风控（如 `error.html`），需提示用户稍后重试或降低频率。
3. 订票链路依赖登录态与乘车人信息，建议先 `status`/`passengers`。
4. 站点解析依赖 12306 站名字典，极少数别名可能无法直接命中。
5. 相对日期必须换算成绝对日期再执行命令。
