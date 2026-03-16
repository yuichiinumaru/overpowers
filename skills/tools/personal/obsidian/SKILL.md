---
name: flomo-to-obsidian
description: "Parse and sync flomo exported HTML data to Obsidian vault with attachment support. Supports one-time manual export conversion and automatic sync. Use when users want to import flomo notes, convert ..."
metadata:
  openclaw:
    category: "productivity"
    tags: ['productivity', 'obsidian', 'knowledge']
    version: "1.0.0"
---

**📁 SKILL DIRECTORY PATH**

`<skill-directory>`

All relative file paths mentioned in this skill are relative to the above directory.

---

# Flomo to Obsidian Synchronization Tool

Synchronize flomo notes to Obsidian, supporting full features such as attachments, tags, and voice transcription.

## 🎯 Use Cases

### Scenario 1: Initial Import (Manual Conversion)
The user has exported data from the flomo web version and needs to convert it to Obsidian.

**Trigger phrases**:
- "Help me convert flomo data to Obsidian"
- "Convert flomo export file"
- "Import flomo notes"

### Scenario 2: Automatic Synchronization (Recommended)
The user wants to automatically synchronize the latest notes from flomo to Obsidian periodically.

**Two modes are provided**:
- 🔐 **Secure Mode**: No password saved, uses browser login status (recommended for personal use)
- 🤖 **Password Mode**: Saves password, fully automated (suitable for servers/scheduled tasks)

**Trigger phrases**:
- "Set up automatic flomo synchronization"
- "Periodically sync flomo to Obsidian"
- "Create flomo sync task"
- "flomo secure mode sync"

---

## 🚀 Scenario 1: Manual Conversion (Initial Import)

### Step 1: Obtain Flomo Export File

Guide the user:
1. Log in to the flomo web version (https://flomoapp.com)
2. Go to **Settings → Account Details**
3. Click the **"Export Data"** button
4. Download the ZIP file and extract it

### Step 2: Ask for Necessary Information

Confirm with the user:
- **Flomo HTML file path** (e.g., `~/Downloads/flomo@username/username's notes.html`)
- **Obsidian vault directory** (e.g., `~/Documents/Obsidian/Flomo`)
- **Whether to use a tag prefix** (recommended: `flomo/`)

### Step 3: Execute Conversion

```bash
cd {skillDir}

python scripts/convert_v2.py \
  --input "{flomo_html_path}" \
  --output "{obsidian_vault_path}" \
  --mode by-date \
  --tag-prefix "flomo/"
```

### Step 4: Report Results

After conversion, inform the user:
- ✅ Number of notes converted
- ✅ Number of attachments copied
- ✅ Output directory location
- ✅ How to view in Obsidian

---

## ⚡ Scenario 2: Automatic Synchronization Setup

### ⚠️ Important: Ask the user to choose a mode first

**You must first explain the differences between the two modes and let the user choose**:

```
I can help you set up automatic flomo synchronization! There are two modes available:

🔐 Secure Mode (Recommended)
  ✅ Does not save passwords to the configuration file
  ✅ Uses the login status saved in the browser
  ✅ Requires manual login once initially (within 5 minutes)
  ✅ Subsequent automatic synchronization
  ✅ Suitable for daily use on personal computers

🤖 Password Mode
  ✅ Fully automated
  ✅ Suitable for servers and scheduled tasks
  ⚠️ Requires saving the password in the configuration file

Which mode would you like to use?
1. Secure Mode (Recommended)
2. Password Mode
```

---

### Mode A: 🔐 Secure Mode (Recommended)

#### Workflow

```
User selects Secure Mode
    ↓
Ask for Obsidian vault path
    ↓
Run synchronization script (opens browser)
    ↓
Wait for user to log in manually
    ↓
Complete initial synchronization automatically
    ↓
Ask if a scheduled task should be created
    ↓
Done!
```

#### Example Conversation Flow

**AI**: Okay! Setting up with Secure Mode.

Please tell me:
- Obsidian vault path: (e.g., /Users/username/Documents/Obsidian/flomo)
- Tag prefix: (Recommended: `flomo/`, just press Enter to use the default)

---

**User**: [Provides path]

---

**AI**: Received! Starting the initial synchronization now.

⚠️ Important Note:
- The script will open a browser window.
- Please log in to flomo manually in the browser.
- After logging in, the browser will remember your login status.
- It will automatically synchronize next time.

Press Enter to continue...

[Execute synchronization script]

```bash
cd {skillDir}
./sync_safe.sh
```

Wait for the user to complete login and synchronization...

✅ Synchronization successful!
- New notes: 120
- Attachments: 15
- Output location: /Users/username/Documents/Obsidian/flomo

Running `./sync_safe.sh` next time will automatically synchronize without requiring login again!

Would you like to create a scheduled task for automatic synchronization?
[Same options as Password Mode for scheduled tasks]

---

### Mode B: 🤖 Password Mode

#### Workflow

```
User selects Password Mode
    ↓
Ask for flomo account email and password
    ↓
Ask for Obsidian vault path
    ↓
Create configuration file (.env)
    ↓
Test synchronization once
    ↓
Ask if a scheduled task should be created
    ↓
Done!
```

#### Example Conversation Flow

**AI**: Okay! Setting up with Password Mode.

First, I need your flomo account information:
- Login email/phone number:
- Login password:

---

**User**: [Provides email and password]

---

**AI**: Received! Next:
- Obsidian vault path: (e.g., /Users/username/Documents/Obsidian/flomo)
- Tag prefix: (Recommended: `flomo/`, just press Enter to use the default)

---

**User**: [Provides path]

---

**AI**: Configuration complete! Now performing the initial synchronization test...

[Execute synchronization]

✅ Synchronization successful!
- New notes: 120
- Attachments: 15
- Output location: /Users/username/Documents/Obsidian/flomo

Would you like to create a scheduled task for automatic synchronization?
1. Every night at 10:00 PM
2. Every night at 11:00 PM
3. Once every 6 hours
4. Do not set up for now

---

### Implementation Steps

#### Secure Mode Implementation

##### Step 1: Collect Information

```python
vault_path = "Obsidian vault path"
tag_prefix = "flomo/"  # Default value
```

##### Step 2: Run Secure Mode Script

```bash
cd {skillDir}

# First run (will open a browser for the user to log in)
python3 scripts/auto_sync_safe.py \
  --output "{vault_path}" \
  --tag-prefix "{tag_prefix}" \
  --no-headless \
  --verbose
```

**⚠️ Important**:
- The script will open a browser window.
- Wait for the user to log in manually (up to 5 minutes).
- Synchronization will continue automatically after successful login.
- Login status will be saved in the `flomo_browser_data` directory.

##### Step 3: Verify Results

Check the output to confirm:
- ✅ Login successful
- ✅ Export successful
- ✅ Conversion successful
- ✅ Status saved

---

#### Password Mode Implementation

##### Step 1: Collect Information

```python
email = "User's flomo email"
password = "User's flomo password"
vault_path = "Obsidian vault path"
tag_prefix = "flomo/"  # Default value
```

##### Step 2: Create Configuration File

```bash
cd {skillDir}

cat > .env << EOF
FLOMO_EMAIL={email}
FLOMO_PASSWORD={password}
OBSIDIAN_VAULT={vault_path}
TAG_PREFIX={tag_prefix}
EOF

chmod 600 .env
```

##### Step 3: Test Synchronization

```bash
cd {skillDir}

python scripts/auto_sync.py \
  --email "{email}" \
  --password "{password}" \
  --output "{vault_path}" \
  --tag-prefix "{tag_prefix}" \
  --no-headless
```

**Note**: For the first test, it is recommended to use `--no-headless` to display the browser window and allow the user to observe the process.

#### Step 4: Create Scheduled Task

Use OpenClaw's `scheduled_task_create` function:

```python
# Create scheduled task via MCP call
task_config = {
    "name": "Flomo Automatic Synchronization",
    "command": f"cd {skillDir} && ./sync.sh",
    "schedule": "0 22 * * *",  # 10:00 PM every day
    "description": "Automatically sync notes from flomo to Obsidian"
}
```

Or manually add cron:
```bash
crontab -l > /tmp/crontab_backup
echo "0 22 * * * cd {skillDir} && ./sync.sh >> /tmp/flomo_sync.log 2>&1" >> /tmp/crontab_backup
crontab /tmp/crontab_backup
```

---

## 📝 Conversation Templates

### Template 1: Manual Conversion

```
User: Help me convert flomo data to Obsidian

AI: Okay! I'll help you convert your flomo data.

Please provide the following information:
1. Path to your exported Flomo HTML file: (If you haven't exported yet, I can guide you on how to do it)
2. Destination directory for your Obsidian vault:

User: [Provides paths]

AI: Received! Starting the conversion...

[Execute conversion]

✅ Conversion complete!
- Notes: 513
- Attachments: 54
- Output location: /Users/username/Documents/Obsidian/flomo

You can now open this directory in Obsidian to view your notes.

Would you like to set up automatic synchronization to import new notes automatically in the future?
```

### Template 2: Automatic Synchronization

```
User: Set up automatic flomo synchronization

AI: Okay! I'll help you set up automatic flomo synchronization.

To log in to flomo and export data automatically, I need your account information:
- Flomo login email:
- Flomo login password:

(This information will be encrypted and stored locally, not uploaded)

User: [Provides account details]

AI: Received! One more confirmation:
- Obsidian vault path: (e.g., /Users/username/mynote/flomo)

User: /Users/ryanbzhou/mynote/flomo

AI: Okay! Configuration complete, testing synchronization now...

⏳ Attempting to log in to flomo automatically...
⏳ Exporting data...
⏳ Converting notes...

✅ Synchronization successful!
- New notes: 120
- Attachments: 15

Would you like to create a scheduled task?
1. Sync automatically every night at 10:00 PM
2. Sync automatically every night at 11:00 PM
3. Sync every 6 hours
4. Do not set up for now (run manually when needed)

User: 1

AI: Okay! Scheduled task created:
- Task name: Flomo Automatic Synchronization
- Execution time: 10:00 PM daily
- Task command: cd /path/to/skill && ./sync.sh

Starting tomorrow, new notes from flomo will be automatically synchronized to Obsidian!

You can also synchronize manually at any time:
cd /path/to/skill && ./sync.sh
```

---

## 🔧 Script Descriptions

### convert_v2.py - Manual Conversion Script

Converts exported flomo HTML to Obsidian markdown.

**Arguments**:
- `--input` (Required): Flomo HTML file path
- `--output` (Required): Obsidian vault output directory
- `--mode`: Organization mode (`by-date` | `individual` | `single`), default `by-date`
- `--tag-prefix`: Tag prefix, default empty
- `--no-attachments`: Do not copy attachments
- `--verbose`: Display detailed logs

### auto_sync.py - Automatic Synchronization Script

Uses browser automation to export from flomo and sync to Obsidian.

**Arguments**:
- `--email` (Required): Flomo login email
- `--password` (Required): Flomo login password
- `--output` (Required): Obsidian vault output directory
- `--tag-prefix`: Tag prefix, default empty
- `--no-headless`: Display browser window (for testing)
- `--force-full`: Force full synchronization (ignore incremental)
- `--verbose`: Display detailed logs

### sync.sh - Synchronization Shortcut Script

Reads the `.env` configuration file and executes synchronization.

**Usage**:
```bash
./sync.sh                 # Run in background
./sync.sh --no-headless   # Display browser
./sync.sh --force-full    # Full synchronization
```

---

## ⚙️ Configuration File

### .env File Format

```bash
FLOMO_EMAIL=your-email@example.com
FLOMO_PASSWORD=your-password
OBSIDIAN_VAULT=/path/to/obsidian/vault/flomo
TAG_PREFIX=flomo/
```

**Security Notice**:
- ✅ Automatically added to `.gitignore`
- ✅ File permissions set to `600` (readable and writable only by the owner)
- ✅ Will not be committed to Git

---

## 📊 Output Format

### Note Format (by-date mode)

```markdown
---
date: 2024-03-11
source: flomo
tags: [flomo/flomo, flomo/work]
note_count: 5
---

# Flomo Notes - 2024-03-11

## 2024-03-11 09:30:15

This is the note content #work

### Attachments

![[attachments/image_123.jpg]]

![[attachments/audio_456.m4a]]

**Voice Transcription:**

> This is the transcribed text content...

---

## 2024-03-11 14:20:00

Another note...

---
```

### Attachment Organization

```
vault/flomo/
├── 2024-03-11.md
├── 2024-03-12.md
└── attachments/
    ├── image_123.jpg
    ├── audio_456.m4a
    └── ...
```

---

## 🐛 Troubleshooting

### Problem 1: Browser Automation Failure

**Symptom**: Cannot log in or export automatically.

**Solution**:
1. Use `--no-headless` to observe browser operations.
2. Check if the email and password are correct.
3. View error screenshot: `flomo_downloads/error_screenshot.png`
4. Check logs: `auto_sync.log`

### Problem 2: Missing Attachments

**Symptom**: Images or audio were not copied.

**Solution**:
1. Confirm that the flomo export ZIP includes the `file/` directory.
2. Check the directory structure after extraction.
3. Manually inspect attachment paths in the HTML file.

### Problem 3: Incremental Synchronization Not Working

**Symptom**: Full synchronization occurs every time.

**Solution**:
1. Check if `.flomo_sync_state.json` exists.
2. Do not delete the state file.
3. Use `--force-full` to force a complete synchronization.

---

## 📈 Performance Notes

- **Initial Synchronization**: Approximately 30-60 seconds for 500 notes.
- **Incremental Synchronization**: Approximately 20-30 seconds for 10 new notes.
- **Browser Startup**: Approximately 5-10 seconds.
- **Attachment Copying**: Depends on file size.

---

## 🔄 Version History

### V3.0.0 (2024-03-11)
- ✅ Simplified workflow suitable for Agent conversations
- ✅ Optimized user interaction flow
- ✅ Integrated scheduled task creation

### V2.0.0 (2024-03-11)
- ✅ Added browser automation synchronization
- ✅ Added incremental synchronization mechanism
- ✅ Added automatic attachment copying

### V1.0.0 (2024-03-10)
- ✅ Basic HTML to Markdown conversion
- ✅ Preserved tags and metadata

---

## 📚 Related Documents

- **AUTO_SYNC.md** - Technical documentation for automatic synchronization
- **SETUP_GUIDE.md** - Guide for setting up environment variables
- **README.md** - Project overview

---

## 💡 Agent Usage Recommendations

### First-time Use

1. **Probe Needs**: Ask the user if they need manual conversion or automatic synchronization.
2. **Guide Operation**: Provide clear steps based on the scenario.
3. **Collect Information**: Gradually ask for necessary parameters.
4. **Execute Operation**: Run the corresponding script.
5. **Confirm Results**: Display conversion statistics and ask about follow-up needs.

### Continuous Use

1. **Check Status**: See if `.env` exists to determine if it's configured.
2. **Quick Execution**: Directly run `./sync.sh`.
3. **Report Results**: Display incremental synchronization statistics.

### Error Handling

1. **Friendly Explanation**: Explain errors in simple terms.
2. **Provide Solutions**: Offer 2-3 suggested solutions.
3. **Proactive Assistance**: Offer commands to view logs and screenshots.

---

## ✅ Feature Checklist

When assisting users with this skill, ensure:

- [ ] Necessary parameters (paths, account details, etc.) were requested.
- [ ] Data security (local storage, no uploading) was explained.
- [ ] Parameters were confirmed before execution.
- [ ] Result statistics were displayed after execution.
- [ ] Suggestions for future use (automatic sync, scheduled tasks, etc.) were provided.
- [ ] Instructions on how to view converted notes were given.

---

**Remember**: This is a skill for general users. Conversations should be friendly, clear, and progressive!
