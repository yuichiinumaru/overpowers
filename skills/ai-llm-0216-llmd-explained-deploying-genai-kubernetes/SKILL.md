---
name: llmd-explained-deploying-genai-kubernetes
description: Guia avançado de arquitetura DevOps e MLOps cobrindo o paradigma LLM-D (Deploying Large Language Models). Explora como transicionar de APIs SaaS (como OpenAI) para a hospedagem de modelos Open-Weights (como Llama 3) em clusters Kubernetes on-premises ou na nuvem corporativa (AWS EKS, GKE). Foco no uso de servidores de inferência como vLLM e implantação co-localizada de aplicações RAG e Vector Databases para minimizar latência, garantir total soberania dos dados e escalabilidade baseada no tráfego de usuários.
tags:
- ai
- llm
category: ops
color: null
tools:
  read: true
  write: true
  bash: true
---
# LLM-D Explained: Deploying GenAI on Kubernetes

## Description
This skill covers the **LLM-D** (Deploying Large Language Models) lifecycle. Moving beyond prototyping with managed SaaS APIs (like ChatGPT or Claude), enterprise architectures often require deploying open-source models (like Llama 3 or Mistral) internally. This shift is driven by strict data privacy compliance (GDPR/HIPAA), the need to eliminate vendor lock-in, and controlling the spiraling costs of API inference. To achieve production-grade reliability, high availability, and auto-scaling based on token throughput, the industry standard is to containerize these models and deploy them on **Kubernetes (K8s)** equipped with GPU node pools.

## Context
Extracted from: [IBM Technology - LLM‑D Explained: Building Next‑Gen AI with LLMs, RAG & Kubernetes](https://www.youtube.com/watch?v=CNKGgOphAPM)

## The Core Problem with Self-Hosting LLMs

If you try to run an LLM (e.g., Llama-3-70B) natively on a server using basic Python scripts, you will face catastrophic bottlenecks:
1.  **Memory Management:** The KV Cache (Key-Value Cache) used during token generation fragments memory rapidly.
2.  **Concurrency:** Handling hundreds of simultaneous users requires intelligent request batching, otherwise the GPU sits idle while waiting for inputs.

## The LLM-D Solution Stack on Kubernetes

### 1. The Inference Engine (e.g., vLLM or TGI)
Do not serve models with raw Hugging Face code in production. You must use a specialized inference server container:
-   **vLLM:** The current industry standard. It uses *PagedAttention*, which manages the KV cache like an operating system manages virtual memory, significantly increasing throughput (tokens/second) and allowing many more concurrent users.
-   **Text Generation Inference (TGI):** Hugging Face's robust, production-ready server.

### 2. The Kubernetes Cluster Architecture
Deploying on K8s involves several interconnected components:

*   **Node Pools:** You need specialized node pools with attached GPUs (e.g., NVIDIA A100s or H100s).
*   **The LLM Pod (vLLM Container):** You pull the vLLM Docker image and configure it to download your chosen model from Hugging Face (often requiring a secure secret for your `HF_TOKEN`).
*   **The Service / Ingress:** Exposes the vLLM container via a standard REST API (usually OpenAI-compatible), allowing your application to query it just as it would query GPT-4.
*   **The Vector Database Pod:** Deploy your vector store (e.g., Milvus, Qdrant, or a Postgres cluster with `pgvector`) in the same cluster.
*   **The RAG Application Pod:** Your backend (FastAPI, Express) running the LangChain or LlamaIndex logic.

## Why Co-locate RAG and the LLM on Kubernetes?

**Latency Reduction:** In a RAG application, the process is:
`User Query -> App -> Embedding Model -> Vector DB -> App -> LLM -> App -> User`
If you use cloud APIs for the Embedding Model, the Vector DB, and the LLM, you are introducing massive network latency (internet round-trips) at every step. By deploying the Embedding Engine, the Vector Database, the RAG Application, and the LLM within the *same* Kubernetes cluster (and often the same Virtual Private Cloud), the communication happens over ultra-fast internal cluster networks, drastically reducing Time-To-First-Token (TTFT).

## Scalability and Observability
-   **Auto-Scaling (HPA):** Configure the Kubernetes Horizontal Pod Autoscaler (HPA) to spin up new vLLM pods when GPU utilization or the request queue length hits a certain threshold.
-   **Monitoring:** Use Prometheus to scrape metrics from the vLLM server and Grafana to visualize token throughput, latency, and GPU memory usage.
