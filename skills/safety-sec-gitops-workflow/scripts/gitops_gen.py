#!/usr/bin/env python3
import sys
import argparse

ARGOCD_APP_TEMPLATE = """apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: {name}
  namespace: argocd
spec:
  project: default
  source:
    repoURL: {repo_url}
    targetRevision: {branch}
    path: {path}
  destination:
    server: https://kubernetes.default.svc
    namespace: {target_namespace}
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
    - CreateNamespace=true
"""

FLUX_KUSTOMIZATION_TEMPLATE = """apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
  name: {name}
  namespace: flux-system
spec:
  interval: 5m
  path: {path}
  prune: true
  sourceRef:
    kind: GitRepository
    name: {name}
"""

def generate_manifest(type, name, repo_url, branch, path, target_namespace):
    if type == "argocd":
        manifest = ARGOCD_APP_TEMPLATE.format(
            name=name,
            repo_url=repo_url,
            branch=branch,
            path=path,
            target_namespace=target_namespace
        )
        filename = f"argocd-{name}.yaml"
    elif type == "flux":
        manifest = FLUX_KUSTOMIZATION_TEMPLATE.format(
            name=name,
            path=path
        )
        filename = f"flux-{name}.yaml"
    else:
        print(f"Error: Unknown type {type}")
        return

    with open(filename, 'w') as f:
        f.write(manifest)
    print(f"Successfully generated {type} manifest: {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate GitOps manifests")
    parser.add_argument("type", choices=["argocd", "flux"], help="Type of manifest to generate")
    parser.add_argument("--name", required=True, help="Application name")
    parser.add_argument("--repo-url", default="https://github.com/org/repo", help="Repository URL")
    parser.add_argument("--branch", default="main", help="Target revision/branch")
    parser.add_argument("--path", required=True, help="Path within repository")
    parser.add_argument("--namespace", default="production", help="Target namespace (ArgoCD only)")
    
    args = parser.parse_args()
    
    generate_manifest(args.type, args.name, args.repo_url, args.branch, args.path, args.namespace)
