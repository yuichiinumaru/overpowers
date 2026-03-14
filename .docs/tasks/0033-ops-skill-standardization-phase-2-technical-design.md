# Technical Design: Skill Standardization Phase 2

## Architecture
The standardization effort will use Python-based transformation scripts that leverage the EvDD schemas for validation and the Serena symbolic tools for discovery.

### Component Details

#### 1. Audit Engine (`scripts/evdd_validate.py`)
- Already implemented.
- Used to identify target skills for repair.

#### 2. Metadata Inferrer/Updater (`scripts/skill_standardizer.py`)
- **Inputs**: Skill directory path.
- **Process**:
    1.  Parse `SKILL.md` frontmatter.
    2.  If `category` is missing, infer it from the parent directory name (e.g. `growth-biz` -> `business`).
    3.  If `tags` are missing, generate them based on the `name` and `description`.
    4.  If `version` is missing, default to `1.0.0`.
    5.  Rewrite `SKILL.md` with the updated frontmatter.
- **Tools**: `PyYAML` for frontmatter manipulation.

#### 3. Section Injector
- **Pattern**: Regex-based injection or Markdown AST manipulation.
- **Target**: Append or prepend `## Inputs`, `## Process`, `## Outputs` if they are not already identifiable by standard headers.

#### 4. Translation Workflow
- **Strategy**:
    1.  Identify Portuguese content (Grep for high-frequency PT words).
    2.  Use a specialized translation script that calls an LLM (e.g. Gemini 3 Flash) to translate while preserving Markdown formatting and YAML keys.
    3.  Save the translated content back to `SKILL.md`.

### Execution Plan (Phase 2)

#### Step 1: Baseline Audit
Run `scripts/evdd_validate.py` on the entire repo and save the results to `.agents/reports/baseline_audit.json`.

#### Step 2: Automated Metadata Sweep
Run the standardizer script on all skills to fill missing fields in the frontmatter.

#### Step 3: Targeted Repair
Manual or semi-automated repair of the 82+ invalid skills that failed basic schema validation.

#### Step 4: Linguistic Unification
Execute the translation sweep starting with the `growth-biz` and `content-media` categories.

## Implementation Details

### Dependency Management
- Reuse dependencies from Task 0025 (`jsonschema`, `PyYAML`).
- Add `pathlib` for clean path management.

### Error Handling
- The standardizer script must be non-destructive.
- It will create a backup of `SKILL.md` (or use Git state for safety) before overwriting.

## Security Considerations
- Ensure the scripts do not execute any code within the skills.
- All transformations are text-based.
