#!/bin/bash

# AI Stack Recommender based on the Ecosystem Map.
# Usage: ./stack-recommender.sh "Project context"

CONTEXT=$1

if [ -z "$CONTEXT" ]; then
  echo "Usage: $0 \"Project context (e.g. enterprise RAG, local agent)\""
  exit 1
fi

echo "Stack Recommendation for: $CONTEXT"
echo "--------------------------------"

if [[ "$CONTEXT" =~ (RAG|search|knowledge) ]]; then
  echo "Group 1 (Brain): Claude 3.5 Sonnet / GPT-4o"
  echo "Group 2 (Connector): LlamaIndex"
  echo "Group 3 (Memory): Pinecone or pgvector"
  echo "Group 4 (Senses): OpenAI text-embedding-3"
elif [[ "$CONTEXT" =~ (Agent|autonomous|swarm) ]]; then
  echo "Group 1 (Brain): Claude 3.5 Sonnet / GPT-4o"
  echo "Group 2 (Connector): CrewAI or AutoGen"
  echo "Group 3 (Memory): ChromaDB or Weaviate"
  echo "Group 4 (Senses): BGE Embedding (Open Source)"
elif [[ "$CONTEXT" =~ (local|offline|private) ]]; then
  echo "Group 1 (Brain): Llama 3 8B / Mistral"
  echo "Group 2 (Connector): LangChain"
  echo "Group 3 (Memory): ChromaDB (Local)"
  echo "Group 4 (Senses): Hugging Face Sentence Transformers"
else
  echo "General AI Stack Recommendation:"
  echo "Brain: GPT-4o-mini (Cost-effective)"
  echo "Connector: LangChain (Versatile)"
  echo "Memory: pgvector (Simple start)"
fi
