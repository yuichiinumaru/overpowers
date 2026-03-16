---
name: notion-sync-obsidian
description: Sync Notion pages to Obsidian
tags:
  - tool
  - sync
version: 1.0.0
---

# notion-sync-obsidian

A complete solution for automatically synchronizing Notion articles to your local Obsidian directory. Supports scheduled checks, full content export, intelligent title extraction, and mobile optimization notifications.

## ✨ Features

### ✅ Core Features
- **Automatic Synchronization**: Periodically checks for Notion updates and synchronizes them to your local Obsidian directory.
- **Full Export**: Exports article titles, metadata, and complete content.
- **Intelligent Title**: Automatically identifies the original article title (not summary content).
- **Mobile Notifications**: Optimized format for mobile, notifying only when there are updates.

### ✅ Advanced Features
- **Scheduled Checks**: Configurable check frequency (default 15 minutes).
- **Quiet Hours**: Supports configuring quiet hours (default 00:00-08:30).
- **Force Check**: Supports manual triggering of checks by the user, ignoring quiet hours.
- **Incremental Sync**: Avoids duplicate exports based on timestamps.
- **Error Handling**: Comprehensive error handling and logging.

### ✅ Technical Features
- **Python Support**: Uses the Python `requests` library for full API calls.
- **Environment Compatibility**: Automatically handles Python dependency installation.
- **Flexible Configuration**: Supports custom API keys, export directories, and check frequencies.
- **Cross-Platform**: Supports Linux/macOS/Windows (verified in container environments).

## 🚀 Quick Start

### 1. Prerequisites
- Notion API Key (obtain from https://notion.so/my-integrations)
- Obsidian directory path
- Python 3.6+ (optional, for full content export)

### 2. Basic Configuration
```bash
# 1. Navigate to the skill directory
cd ~/.openclaw/workspace/skills/notion-sync-obsidian

# 2. Edit the configuration file
nano config.json
```

Configuration file example (`config.json`):
```json
{
  "notion": {
    "api_key": "ntn_your_api_key_here",
    "api_version": "2022-06-28"
  },
  "obsidian": {
    "root_dir": "/path/to/your/obsidian/notion"
  },
  "sync": {
    "check_interval_minutes": 15,
    "quiet_hours_start": "00:00",
    "quiet_hours_end": "08:30",
    "enable_notifications": true
  }
}
```

### 3. Start the Sync System
```bash
# Start scheduled sync (checks every 15 minutes)
./scripts/start_timer.sh

# Manual check (ignores quiet hours)
FORCE_CHECK=1 ./scripts/simple_checker.sh

# View status
./scripts/status_timer.sh

# Stop sync
./scripts/stop_timer.sh
```

## 📁 Directory Structure

```
notion-sync-obsidian/
├── SKILL.md                    # Skill description document
├── config.json                 # Configuration file template
├── scripts/                    # Core scripts
│   ├── real_notion_checker.py  # Full Python checker
│   ├── simple_checker.sh       # Simplified Shell checker
│   ├── timer_checker.sh        # Scheduled checker
│   ├── start_timer.sh          # Start timer
│   ├── stop_timer.sh           # Stop timer
│   ├── status_timer.sh         # View status
│   ├── list_recent_articles.sh # List recent articles
│   └── debug_page_structure.py # Debug page structure
├── references/                 # Reference documents
│   └── NOTION_API_GUIDE.md     # Notion API usage guide
└── examples/                   # Example files
    └── exported_article.md     # Exported article example
```

## 🔧 Detailed Configuration

### Notion API Configuration
1. Visit https://notion.so/my-integrations to create an integration.
2. Copy the API key (starts with `ntn_`).
3. Share the integration with your Notion workspace.
4. Configure the API key in `config.json`.

### Export Directory Configuration
- **Default Path**: `/hellox/openclaw/obsidian/notion/`
- **Organizational Structure**: Subdirectories by year and month `YYYY-MM/`.
- **File Naming**: Uses the original article title, with special characters automatically filtered.

### Scheduled Check Configuration
- **Check Frequency**: Default 15 minutes, configurable.
- **Quiet Hours**: Default 00:00-08:30, to avoid nighttime disturbances.
- **Force Mode**: `FORCE_CHECK=1` environment variable bypasses all restrictions.

## 🛠️ Script Descriptions

### Core Scripts
- **`real_notion_checker.py`**: Full Python checker, exports complete content.
- **`simple_checker.sh`**: Simplified Shell checker, quickly checks for updates.
- **`timer_checker.sh`**: Scheduled checker, manages scheduled tasks.

### Management Scripts
- **`start_timer.sh`**: Starts the scheduled sync system.
- **`stop_timer.sh`**: Stops the scheduled sync system.
- **`status_timer.sh`**: Views system status and logs.
- **`list_recent_articles.sh`**: Lists recent Notion articles.

### Debugging Scripts
- **`debug_page_structure.py`**: Debugs Notion page structure.
- **`test_title_fix.py`**: Tests title extraction fixes.

## 📊 System Status

### View Status
```bash
./scripts/status_timer.sh
```

Example output:
```
📊 Notion Scheduled Sync Status Check
Check Time: 2026-02-24 15:44:53
Timezone: Asia/Shanghai
========================================
🟢 Status: Running
Process PID: 4538
Uptime:       10:29

📋 Log Information:
Log File: ./sync_timer.log
Log Lines: 1179

📁 Directory Status:
Articles Directory: /hellox/openclaw/obsidian/notion
Article Count: 78

⏰ Next Check Time:
   15:59 (in 15 minutes)
```

### View Logs
```bash
tail -f sync_timer.log
```

## 🔍 Troubleshooting

### Common Issues

**Q: Sync failed with API error**
A: Check if the API key is correct and ensure the integration has been shared with your workspace.

**Q: Filename uses summary instead of title**
A: This is a known issue that has been fixed. Ensure you are using the latest version of `real_notion_checker.py`.

**Q: Python dependency installation failed**
A: Container environments may require special handling; the script includes automatic installation logic.

**Q: Timer is not running**
A: Check the process status; you may need to restart the timer.

### Debugging Steps
1. Run `./scripts/debug_page_structure.py` to check API connectivity.
2. Run `FORCE_CHECK=1 ./scripts/simple_checker.sh` for manual testing.
3. Check the `sync_timer.log` log file.
4. Verify configuration file paths and permissions.

## 📈 Advanced Usage

### Custom Export Format
Modify the `export_page_to_markdown` function in `real_notion_checker.py` to customize the Markdown format.

### Integration with Other Systems
The script outputs in a standardized format, making it easy to integrate with:
- CI/CD pipelines
- Other automation tools
- Custom monitoring systems

### Extending Functionality
1. **Tag Sync**: Synchronize Notion tags to Obsidian tags.
2. **Image Download**: Automatically download images from articles.
3. **Bi-directional Sync**: Support syncing from Obsidian back to Notion.
4. **Multiple Databases**: Support syncing multiple Notion databases.

## 🤝 Contribution Guidelines

Contributions, bug reports, and suggestions are welcome!

### Development Environment
```bash
# Clone the repository
git clone https://github.com/your-username/notion-sync-obsidian.git

# Install dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/
```

### Code Standards
- Follow PEP 8 Python code standards.
- Add appropriate comments and documentation.
- Write unit tests.
- Update CHANGELOG.md.

## 📄 License

MIT License - See LICENSE file for details.

## 🙏 Acknowledgements

- Notion Official API Documentation
- OpenClaw Community
- All contributors and users

---

**Version**: 1.0.0  
**Last Updated**: 2026-02-24  
**Maintainer**: kk (Your Personal Assistant)  
**Status**: ✅ Production Ready
