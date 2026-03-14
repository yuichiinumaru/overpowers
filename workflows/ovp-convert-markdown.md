---
description: Workflow for converting multiple documents to Markdown using MarkItDown.
---
# Workflow: Document Conversion to Markdown (MarkItDown)

This workflow describes the process of systematically converting various document formats into Markdown using the MarkItDown tool.

## Steps

### 1. Preparation
- Identify the source documents and their formats.
- Determine if OCR or audio transcription is required.
- Ensure Python 3.10+ is available.

### 2. Tool Installation
- Install MarkItDown with required extras:
  ```bash
  pip install 'markitdown[all]'
  ```

### 3. Conversion Execution
- **Single File**:
  ```bash
  markitdown input.pdf > output.md
  ```
- **Batch Directory**:
  ```bash
  markitdown ./source_dir/ --recursive -o ./output_dir/
  ```

### 4. Structure Verification
- Check if headings follow the correct hierarchy.
- Verify that tables are rendered properly.
- Ensure links and lists are preserved.

### 5. Final Integration
- Move converted files to the final knowledge base or documentation folder.
- Clean up any temporary processing files.
