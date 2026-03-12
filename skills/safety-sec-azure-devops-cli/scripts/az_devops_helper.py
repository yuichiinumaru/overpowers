#!/usr/bin/env python3
import argparse

COMMANDS = {
    "login": "az devops login --organization https://dev.azure.com/{org}",
    "project-list": "az devops project list --organization https://dev.azure.com/{org}",
    "repo-list": "az repos list --org https://dev.azure.com/{org} --project {project}",
    "pr-create": "az repos pr create --repository {repo} --source-branch {source} --target-branch {target} --title '{title}'",
    "pr-list": "az repos pr list --repository {repo}",
    "pipeline-run": "az pipelines run --name {pipeline_name} --branch main",
    "pipeline-list": "az pipelines list --output table"
}

def main():
    parser = argparse.ArgumentParser(description="Azure DevOps CLI Command Helper")
    parser.add_argument("task", choices=COMMANDS.keys(), help="Task to get command for")
    parser.add_argument("--org", default="ORG_NAME", help="Organization name")
    parser.add_argument("--project", default="PROJECT_NAME", help="Project name")
    parser.add_argument("--repo", default="REPO_NAME", help="Repository name")
    parser.add_argument("--source", default="feature-branch", help="Source branch")
    parser.add_argument("--target", default="main", help="Target branch")
    parser.add_argument("--title", default="PR Title", help="PR title")
    parser.add_argument("--pipeline_name", default="Pipeline_Name", help="Pipeline name")
    
    args = parser.parse_args()
    
    cmd_template = COMMANDS[args.task]
    cmd = cmd_template.format(
        org=args.org, 
        project=args.project, 
        repo=args.repo, 
        source=args.source,
        target=args.target,
        title=args.title,
        pipeline_name=args.pipeline_name
    )
    
    print(f"--- Command for {args.task} ---")
    print(cmd)

if __name__ == "__main__":
    main()
