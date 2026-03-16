---
name: agent-memory-patterns
description: Implement persistent memory patterns for AI agents using AgentDB
tags:
  - agent
  - memory
version: 1.0.0
---

# Agent Memory Pattern

An efficient memory management system for persistent AI agents. A guide to implementing daily files, long-term memory, search optimization, and staged processing of external content.

## Architecture Overview

### Memory Hierarchy

```
workspace/
├── MEMORY.md              # Long-term memory (manually curated)
├── memory/
│   ├── YYYY-MM-DD.md     # Daily logs
│   ├── pending-memories.md  # Staged processing of external content
│   ├── heartbeat-state.json  # Heartbeat state
│   └── queued-messages.json # Message queue
└── skills/
    └── memory-tools/     # Memory management tool suite
```

## Daily File Management

### Automatic Daily File Creation

```bash
#!/bin/bash
# daily-memory-init.sh

create_daily_memory() {
    local date="$(date -I)"
    local memory_dir="/home/bot/.openclaw/workspace/memory"
    local daily_file="$memory_dir/$date.md"
    
    mkdir -p "$memory_dir"
    
    if [[ ! -f "$daily_file" ]]; then
        cat > "$daily_file" << EOF
# Daily Memory: $date

## Session Start
$(date): Memory system initialized

## Key Events

## Learnings

## Carry-over for Next Time

## External Links & References

EOF
        echo "Created daily memory file: $daily_file"
    fi
}

create_daily_memory
```

### Structuring Daily Logs

```bash
#!/bin/bash
# memory-logger.sh

log_memory() {
    local event_type="$1"
    local description="$2"
    local importance="${3:-normal}"
    
    local date="$(date -I)"
    local time="$(date '+%H:%M')"
    local memory_file="/home/bot/.openclaw/workspace/memory/$date.md"
    
    # Check and create file if it doesn't exist
    if [[ ! -f "$memory_file" ]]; then
        create_daily_memory
    fi
    
    # Importance marker
    local marker=""
    case "$importance" in
        "high") marker="🔴 " ;;
        "medium") marker="🟡 " ;;
        "low") marker="⚪ " ;;
        *) marker="📝 " ;;
    esac
    
    # Add log entry
    echo "" >> "$memory_file"
    echo "### $time - $event_type" >> "$memory_file"
    echo "$marker$description" >> "$memory_file"
    
    echo "Memory log added: $event_type [$importance]"
}

# Usage example
log_memory "User Interaction" "Confirmed new project requirements" "high"
log_memory "System Update" "Created 5 skill packages" "medium"
```

## Long-Term Memory Management (MEMORY.md)

### Curation Strategy

```bash
#!/bin/bash
# memory-curation.sh

curate_weekly_memories() {
    local workspace="/home/bot/.openclaw/workspace"
    local memory_file="$workspace/MEMORY.md"
    local week_start="$(date -d '7 days ago' -I)"
    local today="$(date -I)"
    
    echo "## Weekly Memory Curation ($week_start to $today)" >> "$memory_file"
    
    # Extract important events from the past 7 days
    for i in {0..6}; do
        local check_date="$(date -d "$i days ago" -I)"
        local daily_file="$workspace/memory/$check_date.md"
        
        if [[ -f "$daily_file" ]]; then
            # Extract high-importance events
            grep -E "🔴|high importance|important" "$daily_file" >> /tmp/important-events.txt
        fi
    done
    
    # Consolidate important events into MEMORY.md
    if [[ -s /tmp/important-events.txt ]]; then
        echo "### Important Events" >> "$memory_file"
        cat /tmp/important-events.txt >> "$memory_file"
        echo "" >> "$memory_file"
    fi
    
    # Record learned patterns
    echo "### Learned Patterns" >> "$memory_file"
    grep -h "Learned" "$workspace/memory"/*.md | tail -10 >> "$memory_file"
    
    # Cleanup
    rm -f /tmp/important-events.txt
    
    echo "Weekly curation complete"
}
```

## grep-based Smart Search

### Memory Search System

```bash
#!/bin/bash
# memory-search.sh

smart_memory_search() {
    local query="$1"
    local context_lines="${2:-3}"
    local workspace="/home/bot/.openclaw/workspace"
    
    echo "=== Memory Search Results: '$query' ==="
    
    # Search MEMORY.md (long-term memory)
    echo "## Long-Term Memory (MEMORY.md)"
    if [[ -f "$workspace/MEMORY.md" ]]; then
        grep -n -i -C "$context_lines" "$query" "$workspace/MEMORY.md" | head -20
    fi
    
    echo ""
    echo "## Recent Memories (Last 7 Days)"
    # Search daily files from the past 7 days
    for i in {0..6}; do
        local check_date="$(date -d "$i days ago" -I)"
        local daily_file="$workspace/memory/$check_date.md"
        
        if [[ -f "$daily_file" ]]; then
            local matches="$(grep -l -i "$query" "$daily_file" 2>/dev/null)"
            if [[ -n "$matches" ]]; then
                echo "### $check_date"
                grep -n -i -C 2 "$query" "$daily_file" | head -10
                echo ""
            fi
        fi
    done
    
    # Suggest related keywords
    echo "## Related Keyword Suggestions"
    grep -h -i "$query" "$workspace/MEMORY.md" "$workspace/memory"/*.md 2>/dev/null \
        | tr ' ' '\n' | grep -v '^$' | sort | uniq -c | sort -nr | head -5
}

# Keyword expansion search
contextual_search() {
    local keywords=("$@")
    local workspace="/home/bot/.openclaw/workspace"
    
    echo "=== Contextual Search: ${keywords[*]} ==="
    
    # Build OR pattern
    local pattern="$(IFS='|'; echo "${keywords[*]}")"
    
    # Search all memory files with relevance scores
    find "$workspace/memory" -name "*.md" -exec grep -l -i -E "$pattern" {} \; \
        | while read file; do
            local score="$(grep -c -i -E "$pattern" "$file")"
            echo "$score:$file"
        done \
        | sort -nr | head -5 | while IFS=':' read score file; do
            echo "Relevance $score: $(basename "$file")"
            grep -n -i -E "$pattern" "$file" | head -3
            echo ""
        done
}

# Usage examples
smart_memory_search "project"
contextual_search "Hugo" "blog" "configuration"
```

## Staged Processing of External Content

### pending-memories.md System

```bash
#!/bin/bash
# external-content-queue.sh

queue_external_memory() {
    local source="$1"
    local content="$2"
    local reason="$3"
    local workspace="/home/bot/.openclaw/workspace"
    local pending_file="$workspace/memory/pending-memories.md"
    
    # Initialize pending-memories.md
    if [[ ! -f "$pending_file" ]]; then
        cat > "$pending_file" << 'EOF'
# Pending Memories - Staged Processing of External Content

## Items Awaiting Processing

<!-- Information from external sources will be recorded here in stages -->
EOF
    fi
    
    # Add entry
    cat >> "$pending_file" << EOF

### $(date -I) $(date '+%H:%M') - $source
**Reason**: $reason
**Source**: $source
**Status**: pending

\`\`\`
$content
\`\`\`

**Verification Items**:
- [ ] Reliability check
- [ ] Consistency with existing memories
- [ ] Value assessment
- [ ] Classification decision

EOF
    
    echo "Added to external content staging queue: $source"
}

# Review pending memories
review_pending_memories() {
    local workspace="/home/bot/.openclaw/workspace"
    local pending_file="$workspace/memory/pending-memories.md"
    
    if [[ ! -f "$pending_file" ]]; then
        echo "Pending queue is empty"
        return
    fi
    
    echo "=== Pending Queue Review ==="
    
    # Count pending items
    local pending_count="$(grep -c "Status.*pending" "$pending_file")"
    echo "Items awaiting processing: $pending_count"
    
    # Identify old items (older than 7 days)
    local week_ago="$(date -d '7 days ago' -I)"
    grep -B 5 -A 10 "$week_ago" "$pending_file" | head -20
    
    echo ""
    echo "If there are old items, please perform manual review."
}
```

## Memory Maintenance Schedule

### cron Configuration

```bash
# memory-maintenance-cron.txt
# Regular maintenance for the memory system

# Daily at 1:00 AM: Initialize daily files
0 1 * * * /home/bot/.openclaw/workspace/skills/memory-tools/daily-memory-init.sh

# Weekly on Sunday at 2:00 AM: Weekly curation
0 2 * * 0 /home/bot/.openclaw/workspace/skills/memory-tools/curate-weekly-memories.sh

# Monthly on the 1st at 3:00 AM: Monthly archive
0 3 1 * * /home/bot/.openclaw/workspace/skills/memory-tools/monthly-archive.sh

# Daily at 6:00 AM: Staged processing review
0 6 * * * /home/bot/.openclaw/workspace/skills/memory-tools/review-pending-memories.sh
```

### Automatic Archiving

```bash
#!/bin/bash
# monthly-archive.sh

monthly_archive() {
    local workspace="/home/bot/.openclaw/workspace"
    local archive_dir="$workspace/memory/archive"
    local current_month="$(date '+%Y-%m')"
    local last_month="$(date -d 'last month' '+%Y-%m')"
    
    mkdir -p "$archive_dir"
    
    echo "Starting monthly archive: $last_month"
    
    # Archive files from the previous month
    find "$workspace/memory" -name "$last_month-*.md" -exec mv {} "$archive_dir/" \;
    
    # Create monthly summary
    cat > "$archive_dir/$last_month-summary.md" << EOF
# Monthly Summary: $last_month

## Statistics
- Daily files count: $(ls "$archive_dir/$last_month"-*.md 2>/dev/null | wc -l)
- Total events: $(grep -c "###" "$archive_dir/$last_month"-*.md 2>/dev/null || echo 0)

## Key Topics
$(grep -h "^### " "$archive_dir/$last_month"-*.md 2>/dev/null | sort | uniq -c | sort -nr | head -10)

## Archive Date
$(date)
EOF
    
    echo "Monthly archive complete: $archive_dir"
}
```

## Heartbeat Integration

### Memory State Monitoring

```json
// heartbeat-state.json - Heartbeat state management
{
    "lastMemoryCheck": 1703275200,
    "pendingMemoryCount": 3,
    "lastCuration": 1703260800,
    "memoryHealth": {
        "dailyFilesCount": 7,
        "longTermMemorySize": 15420,
        "lastSuccessfulBackup": 1703268000
    },
    "alerts": [
        {
            "type": "pending_queue_full",
            "threshold": 10,
            "current": 3
        }
    ]
}
```

### Heartbeat Check Items

```bash
#!/bin/bash
# heartbeat-memory-check.sh

heartbeat_memory_check() {
    local workspace="/home/bot/.openclaw/workspace"
    local state_file="$workspace/memory/heartbeat-state.json"
    
    # Check pending processing queue
    local pending_count="$(grep -c "Status.*pending" "$workspace/memory/pending-memories.md" 2>/dev/null || echo 0)"
    
    if [[ $pending_count -gt 10 ]]; then
        echo "⚠️ Pending processing queue is full ($pending_count items)"
    elif [[ $pending_count -gt 5 ]]; then
        echo "📋 Pending processing queue requires review ($pending_count items)"
    fi
    
    # Check MEMORY.md size
    local memory_size="$(wc -c < "$workspace/MEMORY.md" 2>/dev/null || echo 0)"
    if [[ $memory_size -gt 100000 ]]; then
        echo "📚 MEMORY.md is growing large. Consider organizing."
    fi
    
    # Check daily files
    local today="$(date -I)"
    if [[ ! -f "$workspace/memory/$today.md" ]]; then
        echo "📝 Creating today's daily file."
        create_daily_memory
    fi
}
```

## Example Usage Patterns

### 1. At Session Start
```bash
# Load recent context
smart_memory_search "project" 2
grep -n "important" memory/$(date -I).md memory/$(date -d yesterday -I).md
```

### 2. Recording New Information
```bash
# Safely record via staged processing
queue_external_memory "web_search" "New library information" "Consider for project use"
```

### 3. Regular Curation
```bash
# Automatic execution during heartbeat
curate_weekly_memories
review_pending_memories
```

Tarosho Library trades knowledge regarding agent state backup strategies.
