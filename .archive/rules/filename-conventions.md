# Filename & Naming Conventions

Strict adherence to filename conventions is required across the Overpowers repository to maintain organization and ensure files are easily sortable and discoverable by both humans and agents.

## 1. General Rule
For most files, especially agent thoughts, drafts, or general documents, use the following format:
**Format:** `type-nnnn-names.md`
- **`type`**: The category or type of the file (e.g., `analysis`, `draft`, `report`).
- **`nnnn`**: A 4-digit zero-padded sequential number or related identifier.
- **`names`**: A brief, kebab-case description of the file's content.
*Example:* `analysis-0042-memory-systems-audit.md`

## 2. Tasks (`docs/tasks/`)
For all task files residing inside `docs/tasks/` (including planning and completed subdirectories), the number must come first for chronological and priority sorting.
**Format:** `nnnn-type-names.md`
- **`nnnn`**: A 4-digit zero-padded sequential sequence or ticket number.
- **`type`**: The type of task (e.g., `feature`, `bugfix`, `plan`, `scavenge`).
- **`names`**: A brief, kebab-case description of the task.
*Example:* `024-plan-research-librarian-nlm.md`

## 3. Scavenge Tasks (Jules / Code Ingestion)
When creating tasks specifically for Jules to analyze an external repository and extract ideas or code ("scavenge"), the repository name must prefix the file.
**Format:** `reponame-nnnn-names.md`
- **`reponame`**: The name of the target repository being scavenged.
- **`nnnn`**: A 4-digit zero-padded sequence number.
- **`names`**: Additional descriptive terms, such as the specific module or type of code being extracted.
*Example:* `langchain-0012-memory-extraction.md`

## 4. General Guidelines
*   **Case:** Always use lowercase.
*   **Separators:** Use hyphens (`-`) to separate words. NEVER use spaces, underscores, or camelCase.
*   **Extensions:** Append the appropriate file extension (e.g., `.md`, `.json`, `.ts`).
*   **Clarity:** Make names descriptive but concise. Avoid overly long filenames.
