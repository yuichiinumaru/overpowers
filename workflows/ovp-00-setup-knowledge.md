---
description: Initialize project knowledge parameters and memory slots in Memcord to adhere to Protocol Zero.
---

# /00-setup-knowledge (Memory & Continuity Setup)

**Goal**: Setup the memory slot in Memcord as directed by Protocol Zero for consistent context persistence.

## Actions

1. **Verify Memcord Slot**: Retrieve the list of active/existing Memcord slots using the `memcord_list` tool.
2. **Project Slot Creation**: Check if a slot matching the exact project's name exists.
    - If the exact slot doesn't exist, create a new slot with the name of the project using `memcord_name`.
3. **Validation**: Set the active Memcord slot to the project's slot using `memcord_use`.
4. Tell the user to use `00-setup-project-structure` next if they haven't already.
