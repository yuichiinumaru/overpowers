import argparse
import os

def generate_manifests(model_name, namespace="llm-serving"):
    print(f"☸️ Generating K8s Manifests for LLM: {model_name}")
    
    deployment = f"""apiVersion: apps/v1
kind: Deployment
metadata:
  name: vllm-{model_name.lower().replace('/', '-')}
  namespace: {namespace}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: vllm
  template:
    metadata:
      labels:
        app: vllm
    spec:
      containers:
      - name: vllm-server
        image: vllm/vllm-openai:latest
        command: ["python3", "-m", "vllm.entrypoints.openai.api_server"]
        args: ["--model", "{model_name}"]
        ports:
        - containerPort: 8000
        env:
        - name: HUGGING_FACE_HUB_TOKEN
          valueFrom:
            secretKeyRef:
              name: hf-token
              key: token
        resources:
          limits:
            nvidia.com/gpu: 1
---
apiVersion: v1
kind: Service
metadata:
  name: vllm-service
  namespace: {namespace}
spec:
  selector:
    app: vllm
  ports:
  - port: 80
    targetPort: 8000
"""
    
    filename = f"vllm_deployment_{model_name.split('/')[-1].lower()}.yaml"
    with open(filename, 'w') as f:
        f.write(deployment)
    print(f"✅ Kubernetes manifests generated: {filename}")

def main():
    parser = argparse.ArgumentParser(description='Generate Kubernetes manifests for LLM serving')
    parser.add_argument('--model', required=True, help='HuggingFace model ID (e.g., meta-llama/Llama-3-8B)')
    parser.add_argument('--namespace', default='llm-serving', help='Kubernetes namespace')
    
    args = parser.parse_args()
    generate_manifests(args.model, args.namespace)

if __name__ == "__main__":
    main()
