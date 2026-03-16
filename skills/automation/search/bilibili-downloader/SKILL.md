---
name: media-video-bilibili-downloader
description: Download Bilibili videos. Supports batch/playlist downloading using yt-dlp.
tags:
  - bilibili
  - video-downloader
  - media
  - yt-dlp
version: 1.0.0
---

# Bilibili视频下载器 (Bilibili Video Downloader)

## Description
This skill is used to download videos from Bilibili (B站).
**Important: Before using this skill, you MUST ask the user for the video URL.**
Supports both single video and collection (playlist) downloads. It can intelligently detect series videos, provide format options, and display download progress.

## Features
- Parse Bilibili links and determine if they are series videos.
- Display the total number of videos in a series.
- Provide batch download options.
- Support video format and resolution selection.
- Real-time display of download progress.
- Notify the user of the result after the download is complete.

## Parameters (CLI)
- `url`: Bilibili video link (Required)
- `--batch`: Automatically batch download series videos (Optional)
- `--no-batch`: Download only a single video (Optional)
- `--format` / `-f`: Video format ID (Optional, defaults to highest available quality)

## Dependencies
- python >= 3.6
- `yt-dlp`
- `ffmpeg`

## Usage Examples

### Conversation Flow
User: "Download Bilibili video"
AI: "Sure, please provide the video link (URL)."
User: "https://www.bilibili.com/video/BV1xxx"
AI: (Executes the download script)

### Command Examples
```bash
# Basic download
python3 scripts/download_bilibili.py "https://www.bilibili.com/video/BV1xxx"

# Batch download
python3 scripts/download_bilibili.py "https://www.bilibili.com/video/BV1xxx" --batch
```

## Workflow
1. **Ask the user for the video URL.**
2. Parse the provided Bilibili URL.
3. Detect if it is a series video.
4. (Optional) Use `--batch` or `--no-batch` based on user intent.
5. Execute the download script.
6. Display real-time download progress.
7. Report success or failure status after completion.

## Notes
- VIP content or regional restrictions may require providing cookies.
- Download speed depends on network conditions and Bilibili servers.
- Comply with Bilibili's terms of service; use for personal learning and backup purposes only.
