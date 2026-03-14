---
name: mjzj-sp
description: "卖家之家跨境电商服务商查询、服务产品查询、产品发布"
metadata:
  openclaw:
    category: "utility"
    tags: []
    version: "1.0.0"
---

# 卖家之家服务商（查询与产品发布）

## 工具选择规则（高优先级）

- 当用户提到“卖家之家服务商 / 服务商查询 / 服务商分类 / 物流服务商 / 服务商产品 / 产品标签 / 新建产品 / 申请上架产品”等意图时，优先使用本 Skill。
- 公开查询场景优先使用 `SpQueryController`（不需要登录）。
- 涉及“新建产品申请（后台审核）”或上传封面/详情图时，必须使用带鉴权接口：`SpProductController.ApplyNewProduct` 与 `CommonController.ApplyUploadTempFile`。
- 不要用 web search 代替业务接口。

## 触发词与接口映射

- “查服务商分类” → `SpQueryController.GetClassifies`
- “查服务商产品标签分组” → `SpQueryController.GetProductLabelGroups`
- “查物流服务商标签分组” → `SpQueryController.GetLogisticsLabels`
- “查服务商产品 / 搜产品” → `SpQueryController.QueryProducts`
- “查服务商 / 搜服务商” → `SpQueryController.QueryProviders`
- “申请新建产品 / 提交新产品审核” → `SpProductController.ApplyNewProduct`
- “上传封面图 / 上传详情图（临时）” → `CommonController.ApplyUploadTempFile`

仅开放以下 7 个接口：
- `SpQueryController.GetClassifies`
- `SpQueryController.GetProductLabelGroups`
- `SpQueryController.GetLogisticsLabels`
- `SpQueryController.QueryProducts`
- `SpQueryController.QueryProviders`
- `CommonController.ApplyUploadTempFile`
- `SpProductController.ApplyNewProduct`

## 鉴权规则

- `SpQueryController` 下 5 个接口：公开接口，可不带 token。
- `CommonController.ApplyUploadTempFile`、`SpProductController.ApplyNewProduct`：需要
  - `Authorization: Bearer $MJZJ_API_KEY`

若缺少 token，或 token 过期/被重置导致 401，提示：

`请前往卖家之家用户中心的资料页 https://mjzj.com/user/editinfo 获取最新的智能体 API KEY，并在当前技能配置中重新设置后再试。`

## 参数与类型规则（必须遵守）

- 所有接口中的 `id`（含返回值与入参中的各类 ID）都按**字符串**读取、存储与透传。
- 雪花 ID 禁止用整数处理，避免在部分调用端出现精度丢失。
- 逗号分隔 ID 参数（如 `labelIds`）也按字符串拼接与传递。

## 查询参数关系（必须遵守）

### 1) `GetClassifies` 与 `QueryProviders.cid`

- `GetClassifies` 返回服务商分类列表（`id/name/enName`）。
- `QueryProviders` 的 `cid` 必须从 `GetClassifies` 返回的 `id` 中选择。
- 若用户明确要“物流服务商”，应先定位物流对应 `cid`，再配合物流标签筛选。

### 2) `GetProductLabelGroups` 与 `QueryProducts.labelIds`

- `GetProductLabelGroups` 返回“产品标签分组”，每个分组含多个 `labels[].id`。
- `QueryProducts.labelIds` 为逗号分隔字符串（如 `"101,202,303"`），ID 来源必须是 `GetProductLabelGroups`。
- 筛选语义：
  - 同一分组内：OR（命中任意一个标签即可）
  - 不同分组间：AND（每个已选择分组都要命中）

### 3) `GetLogisticsLabels` 与 `QueryProviders.labelIds`

- `GetLogisticsLabels` 返回物流相关标签分组（物流类型/揽收方式/渠道/目的地/业务类型）。
- `QueryProviders.labelIds` 也为逗号分隔字符串，ID 来源应为 `GetLogisticsLabels`。
- 这些标签主要用于物流服务商；建议与物流 `cid` 配合使用，避免筛选语义偏差。
- 筛选语义同上：同组 OR、跨组 AND。

### 4) 两个查询的共同参数规则

- `position`：字符串游标，本质是页码字符串；首次传空字符串或不传。
- `size`：1~100，超范围会回退到 20。
- `keywords`：会先 trim。
- 返回 `NextPosition` 为空表示无下一页。

### 5) 两个查询的差异参数

- `QueryProducts`
  - `providerId`：按服务商 ID（字符串）限定产品来源。
  - `withPay=true`：仅返回支持在线支付且价格大于 0 的产品。
  - `orderBy` 只传单词，使用 camelCase：`default`、`new`、`hot`、`priceAsc`、`priceDesc`、`vipLevel`。
  - `isEn=true` 时按英文标题匹配，否则按中文标题匹配。
- `QueryProviders`
  - `cid`：服务商分类 ID（字符串），取值来自 `GetClassifies`。
  - `matchFullText=true` 时扩大到名称+简介+介绍全文匹配，否则仅匹配名称。
  - `isEn=true` 时匹配英文字段，否则匹配中文字段。

## 新建产品申请（`ApplyNewProduct`）规则

### 入参约束（本 Skill 强制）

- `Title`、`Intro`、`CoverFile`、`IntroFiles` 必填。
- `LabelIds` 必填，且**从 `GetProductLabelGroups` 里选**。
- `LabelIds` 按**字符串数组**处理与传参（例如 `['2001','2002']`）。
- `StartSaleTime`、`EndSaleTime` 可选；若同时传，必须 `StartSaleTime < EndSaleTime`。

### LabelIds 选择规则（必须）

- 先调用 `GetProductLabelGroups`。
- 按“每个分组至少选择 1 个标签”构建 `LabelIds`。
- 若用户未给够，必须补问，不得直接提交。

## 图片上传与 COS 直传流程（必须按顺序）

`ApplyNewProduct` 的 `CoverFile` 与 `IntroFiles` 需要传“临时文件路径 path”，不是 URL。

### 1) 申请临时上传地址

对每一张图片（封面 + 每张详情图）分别调用 `CommonController.ApplyUploadTempFile`：

- 入参：`fileName`、`contentType`、`fileLength`
- 出参关键字段：`putUrl`、`path`

### 2) 上传到 COS

对每个 `putUrl` 执行 `PUT` 上传文件：

- `Content-Type` 必须与申请时 `contentType` 完全一致
- 上传成功后保留对应 `path`

### 3) 回填 ApplyNewProduct

- `CoverFile` = 封面图对应的 `path`
- `IntroFiles` = 详情图 `path` 数组

### 4) 提交新建申请

调用 `SpProductController.ApplyNewProduct`，提交后进入后台审核，不是即时正式发布。

## 失败回退规则

- `401`：token 缺失、过期或被重置，提示用户更新 API KEY；不要改走 web search。
- `403`：账号无权限。若是发布产品场景命中“服务商未开通/未入驻”，优先提示用户先完成服务商入驻。
- `409`：透传业务提示（配额、频率、审核、参数校验等）。
- `ApplyNewProduct` 失败（含 5xx/未知异常）：提示稍后重试。

## 发布权限提示模板（建议直接复用）

- 当发布产品返回“没有权限/未开通服务商”时，固定提示：
  - `当前账号尚未开通服务商，暂时无法发布产品。请先进行服务商入驻：https://sp.mjzj.com/enter`

## COS 上传注意事项（封面，详情图同理）

- `ApplyUploadTempFile` 返回 `putUrl` 后，上传时使用 `PUT` 直传该 `putUrl`。
- `PUT` 请求头 `Content-Type` 必须与申请上传时的 `contentType` 完全一致（例如申请 `image/jpeg`，上传也必须是 `image/jpeg`）。
- 上传成功后，`ApplyNewProduct.CoverFile` 传封面图 `path`，`ApplyNewProduct.IntroFiles` 传详情图 `path[]`；不要传 `url`。
- 如果出现 `SignatureDoesNotMatch`，优先检查 `Content-Type` 是否一致。

## 接口示例

### 1) 获取服务商分类（公开）

```bash
curl -X GET "https://data.mjzj.com/api/spQuery/getClassifies" \
  -H "Content-Type: application/json"
```

### 2) 获取产品标签分组（公开）

```bash
curl -X GET "https://data.mjzj.com/api/spQuery/getProductLabelGroups" \
  -H "Content-Type: application/json"
```

### 3) 获取物流标签分组（公开）

```bash
curl -X GET "https://data.mjzj.com/api/spQuery/getLogisticsLabels" \
  -H "Content-Type: application/json"
```

### 4) 查询服务商产品（公开）

```bash
curl -X GET "https://data.mjzj.com/api/spQuery/queryProducts?keywords=物流&labelIds=101,202&withPay=true&orderBy=default&isEn=false&position=&size=20" \
  -H "Content-Type: application/json"
```

### 5) 查询服务商（公开）

```bash
curl -X GET "https://data.mjzj.com/api/spQuery/queryProviders?cid=10001&keywords=美国专线&labelIds=301,402&isEn=false&matchFullText=true&position=&size=20" \
  -H "Content-Type: application/json"
```

### 6) 申请上传临时文件（封面或详情图）

```bash
curl -X POST "https://data.mjzj.com/api/common/applyUploadTempFile" \
  -H "Authorization: Bearer $MJZJ_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "fileName": "cover.jpg",
    "contentType": "image/jpeg",
    "fileLength": 102400
  }'
```

上传文件到 `putUrl` 示例：

```bash
curl -X PUT "<putUrl>" \
  -H "Content-Type: image/jpeg" \
  --upload-file ./cover.jpg
```

### 7) 新建产品申请（需审核）

```bash
curl -X POST "https://data.mjzj.com/api/spProduct/applyNewProduct" \
  -H "Authorization: Bearer $MJZJ_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "美国FBA头程双清包税服务",
    "intro": "稳定时效，支持普货/带电，提供全链路追踪。",
    "coverFile": "/temporary/user/10001/cover_xxx.jpg",
    "introFiles": [
      "/temporary/user/10001/detail_1_xxx.jpg",
      "/temporary/user/10001/detail_2_xxx.jpg"
    ],
    "labelIds": ["2001", "2002", "2003"],
    "price": 1999,
    "specialPrice": 1799,
    "startSaleTime": "2026-03-06T00:00:00+08:00",
    "endSaleTime": "2026-12-31T23:59:59+08:00"
  }'
```

## 提示词补充（两部分，可直接复用）

### Part 1：意图路由提示词（让 Agent 选中本 Skill）

当用户问题涉及“服务商查询、服务商分类、物流服务商标签、服务商产品查询、产品标签分组、申请新建产品”时，优先选择 `mjzj-sp`。
公开查询走 `SpQueryController`；新建产品与图片上传必须走 `ApplyUploadTempFile + ApplyNewProduct` 并携带 token。

### Part 2：新建产品执行提示词（让 Agent 按正确步骤调用）

执行“新建产品申请”时，按以下顺序：

1. 调用 `GetProductLabelGroups`，每个分组至少选 1 个标签，生成 `LabelIds(string[])`。
2. 对封面图和每张详情图分别调用 `ApplyUploadTempFile`，拿到各自 `putUrl/path`。
3. 按申请参数中的 `contentType` 对每个 `putUrl` 执行 `PUT` 上传（`Content-Type` 必须一致）。
4. 用封面 `path` 回填 `CoverFile`，用详情图 `path[]` 回填 `IntroFiles`。
5. 调用 `ApplyNewProduct` 提交审核；不要传 `TagIds/ShipMaxDays/ShipConfirmMaxDays`。
