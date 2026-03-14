# Technical Design: Graph-based Continuity (Mindmodel Context)

## 1. Architecture Overview
Continuity records will be integrated into the existing `OverpowersGraph` schema. The `buildGraph` utility in `overpowers-graph-ext` will be extended to handle `.agents/` as a source directory, specifically filtering for `continuity-*.md` files.

## 2. API Signatures & Data Contracts

### Continuity Node Schema
Continuity nodes will follow the `GraphNode` interface:
- `id`: `continuity-[agent-name]`
- `type`: `continuity`
- `domain`: `Session`
- `description`: Summary of current focus or last actions.
- `requires`: List of skills or agents used in the session.
- `related_to`: List of files or tasks modified.

### Example Frontmatter for `continuity-omega.md`
```yaml
---
name: continuity-omega
type: continuity
domain: Session
description: Senior engineer session focusing on Advanced Hooks and Skill Decision Trees.
requires:
  - imagegen
  - speech
related_to:
  - .docs/tasks/0023-feature-advanced-hooks-implementation.md
  - .docs/tasks/0027-ops-skill-decision-trees.md
---
```

## 3. Implementation Details

### Script Modifications
In `extensions/overpowers-graph-ext/src/build-graph.ts`:
- Modify the `if (require.main === module)` block to include `dataDir/.agents` in the `sourceDirs` array.
- Update `getMarkdownFiles` or the processing loop to specifically handle `continuity-*.md` files in `.agents/`.

### Rebuild Command
```bash
npm run build:graph
```

## 4. System Dependencies
- `yaml` (npm package): For parsing frontmatter.
- `ts-node`: For executing the build script.

## 5. Security & Performance Considerations
- **Performance**: Scanning the root directory should be fast as we filter by filename pattern.
- **Security**: Continuity files should not contain secrets (standard Project Protocol).

## 6. Testing Strategy
- **Manual Verification**: Run `npm run build:graph` and inspect `overpowers-graph.json`.
- **Search Test**: Use the graph extension's `search` capability to find "omega" and verify it returns the continuity node.
