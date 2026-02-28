---
name: ai-model-selection-llm-slm-fm
description: Diretrizes arquiteturais para a seleção eficiente de Modelos de Inteligência Artificial. Diferencia Foundation Models (FMs), Large Language Models (LLMs) e Small Language Models (SLMs) com base em restrições de latência, complexidade de hardware (cloud vs. edge), precisão e custo, prevenindo alocações orçamentárias incorretas.
category: engineering
color: "#A52A2A"
tools:
  read: true
---

# AI Model Selection: LLMs vs. SLMs vs. FMs

## Description
This skill provides a decision-making framework for selecting the appropriate size and type of AI model for a given software engineering problem. A common pitfall in GenAI development is defaulting to the largest, most expensive model (like GPT-4 or Claude 3 Opus) for every task, leading to massive cloud inference bills and high latency. Understanding the spectrum between massive Foundation Models, specialized Large Language Models, and efficient Small Language Models is crucial for scalable architecture.

## Context
Extracted from: [IBM Technology - LLM vs. SLM vs. FM: Choosing the Right AI Model](https://www.youtube.com/watch?v=AVQzG2MY858)

## The Model Spectrum

1.  **Foundation Models (FMs):** The massive, general-purpose models trained on vast amounts of unlabeled data across multiple modalities (text, code, images). They serve as the "foundation" from which other models are built or fine-tuned. *Example:* Meta's Llama 3 base model, OpenAI's GPT-4 base.
2.  **Large Language Models (LLMs):** A subset of FMs specifically focused on text and reasoning, often instruction-tuned to be helpful and safe chatbots or complex reasoning engines. They typically have billions to trillions of parameters (e.g., 70B+). They require massive GPU clusters to run. *Example:* GPT-4o, Claude 3.5 Sonnet, Llama 3 70B Instruct.
3.  **Small Language Models (SLMs):** Also known as efficient or compact models. They have significantly fewer parameters (typically under 10B, often 1B-8B). They are trained on highly curated, high-quality data to punch above their weight class. They can run locally on laptops, smartphones, or edge devices. *Example:* Microsoft Phi-3, Llama 3 8B, Google Gemma 2B.

## Selection Matrix

| Primary Requirement | Ideal Choice | Why? |
| :--- | :--- | :--- |
| **Complex Reasoning & Planning** (e.g., Code Generation from scratch, Legal Contract Analysis, Autonomous Agent orchestration) | **Large Language Models (LLMs)** | High parameter count is necessary for deep logical deduction, extensive world knowledge, and managing complex instructions with many tools. |
| **Data Privacy & On-Premises Deployment** (e.g., Analyzing classified documents, Health records) | **Local LLMs / Fine-Tuned SLMs** | You cannot send the data to a public cloud API. A robust local model (like Llama 70B on a local server) or a fine-tuned SLM is required. |
| **Edge Computing & Offline Capability** (e.g., Smart home assistants, Mobile app features, IoT devices) | **Small Language Models (SLMs)** | SLMs fit into the limited VRAM of edge devices (phones/laptops). They run fast, locally, and without internet. |
| **High Throughput / Low Latency / Simple Tasks** (e.g., Sentiment analysis, Keyword extraction, Basic summarization of short text) | **Small Language Models (SLMs)** | Using GPT-4 to extract a keyword from 1,000,000 tweets is economically unviable and slow. An SLM or even a traditional NLP model does this faster and 100x cheaper. |

## Workflow for Optimization

1.  **Start Big (Prototyping):** Begin your project using the most capable LLM available (e.g., GPT-4o) via API. This proves if the task is even possible and establishes a baseline for maximum quality.
2.  **Build Evals:** Create a robust suite of automated evaluations (unit tests for your prompts) based on the outputs of the big model.
3.  **Scale Down (Optimization):** Swap the big LLM for a smaller, cheaper, or faster model (e.g., GPT-3.5, Haiku, or a local 8B model). Run your evals.
4.  **Fine-Tune if Necessary:** If the smaller model fails the evals but you *must* have lower costs/latency, collect the successful outputs from the big model and use them to fine-tune the smaller SLM on your specific task.
5.  **Deploy:** Deploy the smallest model that passes your quality threshold.
