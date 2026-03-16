---
name: zettelkasten-cn
description: "Luhmann's Zettelkasten (Slip-box) full lifecycle management system, supporting classification across nine life domains, undo operations, and interactive creation processes. Handles CRUD operations for fleeting notes, literature notes, permanent notes, and project notes, as well as bidirectional association with Agent memory systems."
metadata:
  openclaw:
    category: "utility"
    tags: ['chinese', 'china']
    version: "1.0.0"
---

# Luhmann Card Learning Method (Zettelkasten)

A personal knowledge management system based on Luhmann's slip-box note-taking method, deeply integrating four levels of notes with nine life domains, supporting undo operations and streamlined card creation.

## Storage Location

Card data is stored in: `~/Desktop/cardsdata/`

```
cardsdata/
├── inbox/              # Fleeting notes (temporary, needs regular cleanup)
├── lit/                # Literature notes (reading notes)
├── zettel/             # Permanent notes (core knowledge assets)
│   ├── Health & Mind/            # Health, psychology, exercise
│   ├── Learning/            # Learning methods, skill improvement
│   ├── Investment/            # Financial management, asset allocation
│   ├── Family/            # Intimate relationships, parenting
│   ├── Career/            # Career development, work
│   ├── Social/            # Interpersonal relationships, communication
│   ├── Possessions/            # Item management, consumption
│   ├── Hobbies/            # Interests and hobbies
│   └── Experiences/            # Travel, food, cultural activities
├── project/            # Project notes
├── map/                # Index/Map (MOC)
│   └── index.md        # Main index (organized by the nine domains)
├── attach/             # Attachments
├── template/           # Local templates
└── .system/            # System files
    ├── trash/          # Recycle bin
    └── operation_history.json  # Operation history (for undo)
```

## Four Levels of Notes + Nine Domains

| Type | Directory | Lifecycle | Purpose |
|------|------|---------|------|
| **Fleeting Notes** | `inbox/` | 1-2 days | Quick capture of ideas |
| **Literature Notes** | `lit/` | Long-term | Reading notes |
| **Permanent Notes** | `zettel/category/` | Permanent | Core knowledge organized by the nine domains |
| **Project Notes** | `project/` | Project duration | Specific project-related |

### Nine Life Domains

1. **Health & Mind** - Health, psychology, exercise, sleep
2. **Learning** - Learning methods, skill improvement, knowledge management
3. **Investment** - Financial management, asset allocation, risk management
4. **Family** - Intimate relationships, parenting, household chores
5. **Career** - Career development, work skills, entrepreneurship
6. **Social** - Interpersonal relationships, communication skills, networking
7. **Possessions** - Item management, purchasing decisions, minimalism
8. **Hobbies** - Interests and hobbies, leisure activities
9. **Experiences** - Travel, food, cultural activities

## Core Scripts

### 1. Basic Management Script

**card_manager.py** - Card CRUD (Create, Read, Update, Delete)

```bash
cd /path/to/zettelkasten

# Create notes
python3 scripts/card_manager.py create fleeting "Fleeting Note Title" --content "Content"
python3 scripts/card_manager.py create permanent "Permanent Note Title" --category Learning

# Query
python3 scripts/card_manager.py list --type permanent
python3 scripts/card_manager.py search "keyword"
python3 scripts/card_manager.py read 20260301-0001

# Update and Delete
python3 scripts/card_manager.py update 20260301-0001 --content "New Content"
python3 scripts/card_manager.py delete 20260301-0001

# Link notes
python3 scripts/card_manager.py link 20260301-0001 20260301-0002 --type related

# Memory association
python3 scripts/card_manager.py memory add 20260301-0001 2026-03-01
python3 scripts/card_manager.py memory find 2026-03-01

# Convert fleeting to permanent
python3 scripts/card_manager.py convert 20260301-0001 --category Learning
```

### 2. Undo Management Script

**undo_manager.py** - Operation Undo

```bash
# Undo the last operation
python3 scripts/undo_manager.py undo

# List recent operations
python3 scripts/undo_manager.py list --limit 10

# Clear operation history
python3 scripts/undo_manager.py clear
```

**Supported Undo Operations**:
- ✅ Undo create (delete newly created card)
- ✅ Undo delete (restore from recycle bin)
- ✅ Undo batch delete (batch restore)
- ✅ Undo update (restore content before update)

**Operation History Storage**: `~/.zettelkasten/memory/history.json`

### 3. Interactive Creation Script

**card_creator.py** - Streamlined Card Creation

```bash
# Interactive creation (wizard mode)
python3 scripts/card_creator.py

# Quick creation (non-interactive)
python3 scripts/card_creator.py --quick \
  --title "Note Title" \
  --content "Note Content" \
  --type permanent \
  --category Learning \
  --memory 2026-03-01
```

**Interactive Process**:
1. **Input Phase** - Select type, enter title and content, choose category, add tags, associate memory
2. **Processing Phase** - Validate input, generate ID, render template, write file, record history
3. **Output Phase** - Display creation result, suggest next actions

## Integration with Memory System

### Card → Memory
```bash
# Associate memory during creation
python3 scripts/card_manager.py create permanent "Note Title" --category Learning --memory 2026-03-01

# Add memory reference afterwards
python3 scripts/card_manager.py memory add 20260301-0001 2026-03-01 --context "Generated during discussion"
```

### Memory → Card
```bash
# Find all cards associated with a specific day
python3 scripts/card_manager.py memory find 2026-03-01
```

## Workflow

### Daily Capture
```bash
# Method 1: Using the basic script
python3 scripts/card_manager.py create fleeting "Inspiration" --content "Detailed content"

# Method 2: Using the interactive script (recommended)
python3 scripts/card_creator.py
```

### Regular Organization
```bash
# View unprocessed fleeting notes
python3 scripts/card_manager.py list --type fleeting

# Convert valuable ones to permanent notes
python3 scripts/card_manager.py convert 20260301-0001 --category Learning

# If conversion was incorrect, undo
python3 scripts/undo_manager.py undo
```

### Browse by Category
Open `~/Desktop/cardsdata/map/index.md` to browse the knowledge structure by the nine domains.

## Note ID Format

```
YYYYMMDD-NNNN
```

Example: `20260301-0001`

- Automatically generated, no manual specification needed
- Globally unique, never changes
- Sorted by time, facilitating traceability

## Advanced Features

See [references/advanced.md](references/advanced.md) for details:
- Batch import/export
- Knowledge graph generation
- Tag cloud statistics
- Automatic archiving policies

## Script Architecture

```
scripts/
├── card_manager.py     # Basic CRUD (automatically records operation history)
├── undo_manager.py     # Undo management (independent history record)
├── card_creator.py     # Interactive creation process
└── search_index.py     # Search index (optional)
```

### Operation History Mechanism

1. **Automatic Recording**: `create`/`delete`/`update` operations in `card_manager.py` are automatically recorded.
2. **Independent Storage**: History is stored in a JSON file, not polluting card data.
3. **Limited Retention**: Only the last 100 operation records are kept.
4. **Undo Marking**: Undone operations are marked to prevent repeated undoing.

## Best Practices

1. **Use Interactive Creation**: `card_creator.py` provides a more user-friendly experience.
2. **Regular Undo Check**: Immediately use `undo_manager.py undo` after an accidental operation.
3. **Associate Memories**: When creating cards, try to associate memory dates for easier traceability.
4. **Clear Categorization**: Permanent notes must be assigned to one of the nine life domains.

---

*Skill Version: 2.0 | Updated: 2026-03-02*
