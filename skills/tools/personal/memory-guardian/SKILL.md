---
name: ops-memory-memory-guardian
version: 1.0.0
description: Anti-loss memory system for OpenClaw. Automatically establishes, maintains, and restores AI agent memory to prevent work progress loss using real-time saving, version control, and crash recovery mechanisms.
tags: [memory, continuity, backup, recovery, productivity, agent-memory]
category: ops
---

# Claw Memory Guardian

## 🧠 Memory Guardian - Anti-Loss Memory System Skill

### Feature Description
An anti-loss memory system developed based on lessons learned. Automatically establishes, maintains, and restores the AI assistant's memory, preventing loss of work progress.

### 🎯 Core Problems Solved
1. **Session Amnesia** - Forgets previous work in each new session
2. **Task Interruption** - `exec` command is `KILL`ed, progress is lost
3. **Scattered Information** - Memory is dispersed, lacking unified management
4. **Lack of Backup** - No automatic backup mechanism
5. **Difficult Recovery** - Cannot quickly recover after accidental interruption

### 🏗️ System Architecture

#### **Memory File Structure**
```
memory/
├── MEMORY.md                    # Long-term core memory (manually maintained)
├── YYYY-MM-DD.md               # Daily work log (automatically created)
├── memory_index.json           # Memory index (automatically updated)
├── project_timeline.json       # Project timeline (automatically updated)
└── knowledge_base/             # Knowledge base
```

#### **Core Functional Modules**
1. **Real-time Memory Saving** - Saves immediately after each important step is completed
2. **Automatic Version Control** - Automatic `git` commits, supports rollback
3. **Semantic Search Index** - Quickly locates memory content
4. **Crash Recovery Mechanism** - Automatic recovery after accidental interruption
5. **Memory Maintenance Tools** - Cleaning, optimization, and backup tools

### 📦 Installation Method

```bash
# Install via ClawdHub
clawdhub install claw-memory-guardian

# Or manual installation
mkdir -p ~/.openclaw/skills/claw-memory-guardian
cp -r ./* ~/.openclaw/skills/claw-memory-guardian/
```

### 🚀 Quick Start

After installation, in an OpenClaw session:
```bash
# Initialize memory system
memory-guardian init

# Check memory status
memory-guardian status

# Search memory content
memory-guardian search "project progress"

# Backup memory
memory-guardian backup

# Restore memory
memory-guardian restore
```

### 🔧 Configuration Options

Add to `~/.openclaw/config.json`:
```json
{
  "memoryGuardian": {
    "autoSaveInterval": 300,      // Auto-save interval (seconds)
    "autoCommitInterval": 1800,   // Auto git commit interval (seconds)
    "backupRetention": 7,         // Backup retention days
    "enableSemanticSearch": true, // Enable semantic search
    "enableTimeline": true        // Enable project timeline
  }
}
```

### 💼 Use Cases

#### **1. Quick Onboarding for New Users**
- Automatically establish a complete memory system
- Avoid the confusion of "starting from scratch"
- Provide best practice templates

#### **2. Project Work Management**
- Automatically record project progress
- Prevent loss of progress due to task interruption
- Support collaborative memory for multiple users

#### **3. Knowledge Accumulation System**
- Automatically organize study notes
- Build a personal knowledge base
- Support fast retrieval

#### **4. Crash Recovery Assurance**
- Recovery after accidental power outage/reboot
- Protection against network interruptions
- Recovery from system failures

### 🛡️ Anti-Loss Strategy

#### **Real-time Protection**
- **At Session Start**: Automatically load today's memory file
- **During Important Decisions**: Automatically update `MEMORY.md`
- **Upon Task Completion**: Automatically update the project timeline
- **At Session End**: Automatically save a session summary

#### **Automatic Backup**
- **Every 30 minutes**: Automatic `git` commit
- **Daily**: Full backup to a separate directory
- **Weekly**: Clean up expired backups
- **During Crash**: Automatically restore to the latest state

#### **Recovery Mechanism**
1. **Automatic Detection** - Detect abnormal termination
2. **State Restoration** - Restore working state
3. **Progress Indication** - Display progress before interruption
4. **Continuation Suggestions** - Provide suggestions for continuing work

### 📊 Monitoring and Reporting

#### **Health Check**
```bash
# Check memory system health status
memory-guardian health

# Output:
✅ Memory files intact
✅ Backup system operational
✅ Search index up-to-date
✅ Version control active
📊 Last saved: 2 minutes ago
📊 Number of backups: 7
📊 Memory size: 15.2MB
```

#### **Usage Reports**
- Daily memory usage statistics
- Save frequency analysis
- Search hotspot analysis
- System performance report

### 🎨 Advanced Features

#### **1. Semantic Search**
```bash
# Search memory using natural language
memory-guardian search "project plan discussed last week"

# Search by date range
memory-guardian search --date "2026-02-01..2026-02-10" "client requirements"

# Search by tag
memory-guardian search --tag "important decision" "project"
```

#### **2. Memory Analysis**
```bash
# Analyze memory patterns
memory-guardian analyze

# Identify important decisions
memory-guardian analyze --decisions

# Extract learning experiences
memory-guardian analyze --learnings
```

#### **3. Collaboration Features**
```bash
# Share memory snippets
memory-guardian share "project plan" --to "colleague AI"

# Synchronize team memory
memory-guardian sync --team "project group"

# Resolve merge conflicts
memory-guardian merge --resolve
```

### 💰 Monetization Model

#### **Version Strategy**
1. **Free Version** - Basic memory saving and recovery
2. **Pro Version** ($9.99/month) - Semantic search, advanced analysis, team collaboration
3. **Enterprise Version** ($99/month) - Unlimited memory, API access, custom features

#### **Target Users**
- **Individual Users** - Prevent loss of personal work
- **Team Users** - Team knowledge management
- **Enterprise Users** - Enterprise AI assistant memory system
- **Developers** - OpenClaw skill developers

### 📈 Value Proposition

#### **Value to Users**
1. **Time Savings** - Avoid repetitive work, save 50%+ time
2. **Quality Improvement** - Complete memory leads to higher quality output
3. **Continuity Assurance** - Ensure work is not interrupted
4. **Knowledge Accumulation** - Build personal/team knowledge assets

#### **Value to OpenClaw Ecosystem**
1. **Lower Barrier to Entry** - Easier for new users to get started
2. **Increased User Stickiness** - Memory system locks in users
3. **Revenue Generation** - Paid features bring continuous income
4. **Ecosystem Completion** - Fills an important functional gap

### 🔄 Development Roadmap

#### **V1.0 (Current)**
- Basic memory saving and recovery
- Automatic `git` version control
- Simple search functionality

#### **V1.5 (1 Month Later)**
- Enhanced semantic search
- Memory analysis tools
- Team collaboration features

#### **V2.0 (3 Months Later)**
- AI memory optimization
- Cross-platform synchronization
- Advanced reporting system

### 🐛 Troubleshooting

#### **Common Issues**
1. **Corrupted Memory File**
   ```bash
   memory-guardian repair --file MEMORY.md
   ```

2. **Outdated Search Index**
   ```bash
   memory-guardian reindex
   ```

3. **Backup Restoration Failure**
   ```bash
   memory-guardian restore --force --backup 20260209
   ```

#### **Technical Support**
- Documentation: https://docs.claw-memory-guardian.com
- Community: Moltbook #memory-guardian
- Support: support@claw-memory-guardian.com

### 📝 License
MIT License - Free for personal and non-commercial use
Commercial use requires purchasing a license

---
**Development Team**: Claw & Boss
**Version**: 1.0.0
**Release Date**: 2026-02-10
**Official Website**: https://clawdhub.com/skills/claw-memory-guardian
