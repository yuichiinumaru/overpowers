import os
import json
import argparse
from datetime import datetime, timedelta
from pathlib import Path

def get_claude_projects_dir():
    return Path.home() / ".claude" / "projects"

def truncate_string(s, max_len=60):
    s = s.replace('\n', ' ')
    if len(s) <= max_len:
        return s
    return s[:max_len-3] + "..."

def extract_session_metadata(path):
    first_prompt = None
    git_branch = None
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            # Check first 50 lines for metadata
            for line in lines[:50]:
                if not line.strip():
                    continue
                try:
                    record = json.loads(line)
                    if not git_branch and 'gitBranch' in record:
                        git_branch = record['gitBranch']
                    
                    if not first_prompt and 'message' in record:
                        msg = record['message']
                        if msg.get('role') == 'user' and 'content' in msg:
                            content = msg['content']
                            if isinstance(content, str):
                                first_prompt = truncate_string(content)
                            elif isinstance(content, list):
                                text_blocks = [b.get('text', '') for b in content if b.get('type') == 'text']
                                if text_blocks:
                                    first_prompt = truncate_string(" ".join(text_blocks))
                    
                    if git_branch and first_prompt:
                        break
                except (json.JSONDecodeError, KeyError):
                    continue
    except Exception:
        pass
        
    return git_branch, first_prompt

def discover_sessions(target_date=None, project_filter=None):
    projects_dir = get_claude_projects_dir()
    if not projects_dir.exists():
        return []

    sessions = []
    
    # target_date is a datetime.date object
    
    for project_path in projects_dir.iterdir():
        if not project_path.is_dir():
            continue
            
        if project_filter and project_filter not in str(project_path):
            continue
            
        for session_path in project_path.glob("*.jsonl"):
            if session_path.name.startswith("agent-"):
                continue
                
            stat = session_path.stat()
            modified_at = datetime.fromtimestamp(stat.st_mtime)
            
            if target_date and modified_at.date() != target_date:
                continue
                
            git_branch, first_prompt = extract_session_metadata(session_path)
            
            sessions.append({
                "path": str(session_path),
                "project": project_path.name,
                "git_branch": git_branch,
                "summary": first_prompt or "No summary available",
                "modified_at": modified_at.isoformat()
            })
            
    # Sort by modification time, newest first
    sessions.sort(key=lambda x: x['modified_at'], reverse=True)
    return sessions

def main():
    parser = argparse.ArgumentParser(description="Digest Claude Code session history for daily updates.")
    parser.add_argument("--date", choices=["today", "yesterday"], default="yesterday", help="Target date for sessions (default: yesterday)")
    parser.add_argument("--format", choices=["json", "text"], default="text", help="Output format (default: text)")
    parser.add_argument("--project", help="Filter by project name (substring)")
    
    args = parser.parse_args()
    
    if args.date == "today":
        target_date = datetime.now().date()
    else:
        target_date = (datetime.now() - timedelta(days=1)).date()
        
    sessions = discover_sessions(target_date=target_date, project_filter=args.project)
    
    if args.format == "json":
        print(json.dumps(sessions, indent=2))
    else:
        if not sessions:
            print(f"No Claude Code sessions found for {args.date}.")
            return
            
        print(f"Claude Code Sessions for {args.date}:")
        for s in sessions:
            project_info = f" ({s['project']})" if s['project'] else ""
            branch_info = f" [branch: {s['git_branch']}]" if s['git_branch'] else ""
            print(f"- {s['summary']}{project_info}{branch_info}")

if __name__ == "__main__":
    main()
