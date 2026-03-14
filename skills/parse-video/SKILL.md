name: parse-video
description: 解析视频分享链接，获取无水印视频下载地址。当用户想要下载视频、解析抖音/快手/小红书/B 站链接、获取无水印视频时使用此 skill。
tags: [视频下载，去水印，抖音，快手，小红书，B 站，免费]
version: "1.0.0"
---

解析各大平台的视频分享链接，获取无水印视频下载地址。**免费使用，无需认证**。

## 工作流程

1. **解析链接** - 调用 MCP `parse_video` 工具获取资源信息
2. **下载资源** - 执行 `scripts/download.py` 脚本下载到本地

## 支持平台

- 抖音 (Douyin)
- 快手 (Kuaishou)
- 小红书 (Xiaohongshu)
- 哔哩哔哩 (Bilibili)
- 微博 (Weibo)
- TikTok
- Instagram
- YouTube
- 其他主流平台

## 使用方法

调用 MCP 工具 `parse_video`：

```json
{
  "url": "视频分享链接"
}
```

### 参数说明

| 参数 | 类型 | 必填 | 说明 |
|-----|------|-----|------|
| url | string | **是** | 视频分享链接，支持带分享文案的文本（自动提取链接） |

### 返回字段

| 字段 | 类型 | 说明 |
|-----|------|------|
| success | boolean | 是否解析成功 |
| title | string | 视频标题 |
| thumbnail | string | 视频封面缩略图 |
| video_url | string | 首选视频下载链接 |
| video_urls | array | 所有视频链接列表 |
| audio_url | string | 音频下载链接 |
| audio_urls | array | 所有音频链接列表 |
| image_url | string | 首选图片链接（图集类型） |
| image_urls | array | 所有图片链接（图集类型） |
| parse_time | string | 解析时间 |

## 定价

**免费** - 无限制使用
