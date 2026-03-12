---
name: docling-document-parsing-for-rag
description: Utiliza a biblioteca open-source Docling da IBM para realizar o parsing de documentos corporativos complexos (PDFs, PPTXs, DOCX, Imagens) em formato Markdown ou JSON estruturado. Essencial para aumentar a precisão de pipelines RAG, preservando a hierarquia de títulos e a estrutura de tabelas que parsers tradicionais destroem.
tags:
- ai
- llm
category: data
color: null
tools:
  read: true
  write: true
  bash: true
---
# Unlock Better RAG & AI Agents with Docling

## Description
This skill introduces **Docling**, an open-source library created by IBM Research, designed to solve the most persistent problem in Enterprise RAG (Retrieval-Augmented Generation): terrible document parsing. When traditional parsers extract text from PDFs or PowerPoints, they destroy tables, ignore headers, and lose the visual hierarchy. Docling uses specialized AI models to extract documents intelligently, converting them into clean, structured Markdown or JSON, which exponentially improves the quality of chunks stored in a Vector Database.

## Context
Extracted from: [IBM Technology - Unlock Better RAG & AI Agents with Docling](https://www.youtube.com/watch?v=rrQHnibpXX8)

## The RAG Document Parsing Problem
1.  **Garbage In, Garbage Out:** If your PDF parser reads a complex financial table as a single, unformatted string of numbers, the LLM will hallucinate when asked to query that table.
2.  **Loss of Hierarchy:** Traditional tools don't differentiate between an `<h1>` Title and a paragraph. This ruins semantic chunking strategies.

## The Docling Solution

Docling seamlessly parses complex formats (PDF, DOCX, PPTX, HTML, Images) and outputs them as structured Markdown.

### Key Features:
-   **Table Recognition:** It accurately reconstructs tables from PDFs and converts them into Markdown tables.
-   **Equation & Image Understanding:** It can process equations and use built-in Vision Language Models (VLMs) to describe charts or figures found inside the document.
-   **LangChain / LlamaIndex Integration:** It provides native loaders for popular GenAI frameworks.

## Implementation Guide (Python)

### 1. Installation
```bash
pip install docling
```

### 2. Basic Extraction
```python
from docling.document_converter import DocumentConverter

converter = DocumentConverter()
# Can process local files or URLs
result = converter.convert("https://example.com/complex-financial-report.pdf")

# Export to Markdown (perfect for LLMs)
markdown_text = result.document.export_to_markdown()
print(markdown_text)

# Export to JSON
json_dict = result.document.export_to_dict()
```

### 3. Integrating with LlamaIndex (RAG Pipeline)
```python
from docling.document_converter import DocumentConverter
from llama_index.core import VectorStoreIndex

# Docling provides a native reader for LlamaIndex
from docling.utils.llama_index import DoclingReader 

reader = DoclingReader()
documents = reader.load_data("report.pdf")

# The documents are now perfectly formatted with metadata
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("Summarize the Q3 revenue table.")
print(response)
```

## Best Practices
-   **Always use Docling for PDFs:** If your RAG pipeline touches PDFs, replace PyPDF or simple OCR tools with Docling immediately to see a massive boost in retrieval accuracy.
-   **Chunking Strategy:** Because Docling preserves Markdown headers (`#`, `##`), use a `MarkdownHeaderTextSplitter` (in LangChain or LlamaIndex) to chunk your documents logically by sections, rather than arbitrarily by character count.
