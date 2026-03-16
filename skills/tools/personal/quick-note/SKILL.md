---
name: quick-note
description: "Quickly record ideas and notes to local files. Use cases: (1) Quickly record inspirations and ideas (2) Save temporary notes (3) Organize thoughts. Supports adding, viewing, and searching notes."
metadata:
  openclaw:
    category: "utility"
    tags: []
    version: "1.0.0"
---

# Quick Notes

A simple and efficient note-taking tool to help you quickly capture ideas.

## Usage

### Add a Note

```
note today: Learned something new today
```

Or

```
note add Learned something new today
```

### View Notes

```
view all notes
```

Or

```
note list
```

### Search Notes

```
search notes keyword
```

Or

```
note search keyword
```

## Note Storage

Notes are stored by default in the `~/.quick-notes/` directory, with files organized by date.

## Command Reference

- `note add <content>` - Add a new note
- `note list` - List all notes
- `note search <keyword>` - Search notes
- `note today` - View today's notes
- `note clear` - Clear all notes
